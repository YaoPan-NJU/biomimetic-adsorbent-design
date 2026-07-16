#!/usr/bin/env python3
"""Create identity-neutral concept bodies for the BMDL paired review."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAIRED = ROOT / "research" / "bmdl" / "paired"
BLIND = PAIRED / "blind_inputs"


def section(text: str, start: str, stop: str) -> str:
    begin = text.index(start)
    end = text.index(stop, begin)
    body = text[begin:end].strip()
    for forbidden in ("BMDL", "model-only", "Model-only", "库辅助", "纯模型基线"):
        if forbidden in body:
            raise ValueError(f"identity token {forbidden!r} leaked into blind body")
    return body + "\n"


def write_variant(filename: str, label: str, body: str) -> None:
    BLIND.mkdir(parents=True, exist_ok=True)
    header = (
        f"# 匿名方案 {label}\n\n"
        "本文件只含待评分的概念正文。不得从写作风格推断生成方法；"
        "请仅按统一量表和证据台账评分。\n\n"
    )
    (BLIND / filename).write_text(header + body, encoding="utf-8")


def main() -> None:
    model_a = (PAIRED / "model_only_batch_a.md").read_text(encoding="utf-8")
    model_b = (PAIRED / "model_only_batch_b.md").read_text(encoding="utf-8")
    assisted_a = (PAIRED / "bmdl_assisted_batch_a.md").read_text(encoding="utf-8")
    assisted_b = (PAIRED / "bmdl_assisted_batch_b.md").read_text(encoding="utf-8")

    # Counterbalanced labels. The reviewer is instructed not to inspect this script.
    write_variant(
        "batch_a_variant_q.md",
        "A-Q",
        section(assisted_a, "## 1. PFOA", "## 6. 横向判断"),
    )
    write_variant(
        "batch_a_variant_r.md",
        "A-R",
        section(model_a, "## A1. PFOA", "## 批次内比较"),
    )
    write_variant(
        "batch_b_variant_m.md",
        "B-M",
        section(model_b, "## 1. 磺胺甲噁唑", "## 6. 批次横向判断"),
    )
    write_variant(
        "batch_b_variant_n.md",
        "B-N",
        section(assisted_b, "## B1. SMX", "## 批次内判断"),
    )


if __name__ == "__main__":
    main()
