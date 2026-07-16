#!/usr/bin/env python3
"""Export the minimal BMDL analysis snapshot under enforced read-only settings.

This script intentionally contains no data-changing SQL. It exports canonical
tables plus a de-duplicated performance view whose surrogate ``id`` is removed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras
from dotenv import dotenv_values
from psycopg2 import sql


TABLES = (
    "biological_prototypes",
    "pollutant_profiles",
    "match_weights",
    "pollutant_aliases",
)
SCHEMA_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("data/bmdl_snapshot"))
    parser.add_argument("--schema", default=None)
    parser.add_argument("--source-commit", default="unknown")
    return parser.parse_args()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)


def write_json(path: Path, value: Any) -> dict[str, Any]:
    text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n"
    path.write_text(text, encoding="utf-8")
    return {
        "path": path.as_posix(),
        "bytes": len(text.encode("utf-8")),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def require_env(values: dict[str, str | None], key: str) -> str:
    value = values.get(key)
    if value is None or str(value).strip() == "":
        raise RuntimeError(f"Missing required environment key: {key}")
    return str(value)


def main() -> None:
    args = parse_args()
    values = dict(dotenv_values(args.env_file))
    schema = args.schema or values.get("BMDL_SCHEMA") or "bmdl"
    if not SCHEMA_PATTERN.fullmatch(schema):
        raise RuntimeError("Unsafe BMDL schema identifier")

    params = {
        "host": require_env(values, "POSTGRES_HOST"),
        "port": int(values.get("POSTGRES_PORT") or 5432),
        "dbname": require_env(values, "POSTGRES_DB"),
        "user": require_env(values, "POSTGRES_USER"),
        "password": require_env(values, "POSTGRES_PASSWORD"),
        "connect_timeout": 15,
        "options": "-c default_transaction_read_only=on",
    }

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    conn = psycopg2.connect(**params)
    conn.set_session(readonly=True, autocommit=False)
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SHOW default_transaction_read_only")
        default_read_only = cur.fetchone()["default_transaction_read_only"]
        cur.execute("SHOW transaction_read_only")
        transaction_read_only = cur.fetchone()["transaction_read_only"]
        if default_read_only != "on" or transaction_read_only != "on":
            raise RuntimeError("Database session is not strictly read-only")

        manifest: dict[str, Any] = {
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "schema": schema,
            "source_bmdl_commit": args.source_commit,
            "safety": {
                "default_transaction_read_only": default_read_only,
                "transaction_read_only": transaction_read_only,
                "allowed_operations": ["SHOW", "SELECT"],
            },
            "files": {},
            "counts": {},
            "notes": [],
        }

        for table in TABLES:
            cur.execute(
                sql.SQL("SELECT to_jsonb(t) AS row FROM {}.{} AS t").format(
                    sql.Identifier(schema), sql.Identifier(table)
                )
            )
            rows = [record["row"] for record in cur.fetchall()]
            rows.sort(key=canonical_json)
            filename = f"{table}.json"
            manifest["files"][table] = write_json(output / filename, rows)
            manifest["counts"][table] = len(rows)

        cur.execute(
            sql.SQL("SELECT to_jsonb(t) AS row FROM {}.{} AS t").format(
                sql.Identifier(schema), sql.Identifier("performance_data")
            )
        )
        raw_performance = [record["row"] for record in cur.fetchall()]
        normalized: dict[str, Any] = {}
        for row in raw_performance:
            row = dict(row)
            row.pop("id", None)
            normalized[canonical_json(row)] = row
        performance_rows = [normalized[key] for key in sorted(normalized)]
        manifest["files"]["performance_data_deduplicated"] = write_json(
            output / "performance_data_deduplicated.json", performance_rows
        )
        manifest["counts"]["performance_data_raw"] = len(raw_performance)
        manifest["counts"]["performance_data_deduplicated"] = len(performance_rows)
        duplicates = len(raw_performance) - len(performance_rows)
        manifest["counts"]["performance_data_duplicate_rows"] = duplicates
        if duplicates:
            manifest["notes"].append(
                "performance_data contained repeated rows after surrogate id removal; "
                "only the de-duplicated view is included in the analysis snapshot"
            )

        conn.rollback()
        manifest["files"]["manifest"] = {"path": "data/bmdl_snapshot/manifest.json"}
        manifest_path = output / "manifest.json"
        write_json(manifest_path, manifest)
        print(
            json.dumps(
                {
                    "safety": manifest["safety"],
                    "counts": manifest["counts"],
                    "output": str(output),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    finally:
        conn.close()


if __name__ == "__main__":
    main()

