#!/usr/bin/env python3
"""Build counterbalanced blind inputs for controlled BMDL attempt 2."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RERUN = ROOT / "research" / "bmdl" / "rerun"
OUT = RERUN / "blind_inputs"


def body(filename: str, first: str, appendix: str) -> str:
    text = (RERUN / filename).read_text(encoding="utf-8")
    selected = text[text.index(first) : text.index(appendix)].strip() + "\n"
    selected = selected.replace("拥挤基线", "拥挤对照路线")
    for token in ("BMDL", "库辅助", "model-only", "Model-only", "基线", "weight"):
        if token in selected:
            raise ValueError(f"identity token {token!r} in {filename}")
    return selected


def write(name: str, label: str, selected: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    header = (
        f"# 匿名方案 {label}\n\n"
        "两种变体使用同一冻结证据。只按正文与统一量表评分，"
        "不得从格式或措辞推断生成方法。\n\n"
    )
    (OUT / name).write_text(header + selected, encoding="utf-8")


def main() -> None:
    # Counterbalanced identity labels; reviewer must not inspect this script.
    write(
        "batch_a_variant_u.md",
        "A-U",
        body("model_only_attempt2_batch_a.md", "## PFOA", "## Appendix"),
    )
    write(
        "batch_a_variant_v.md",
        "A-V",
        body("assisted_attempt2_batch_a.md", "## PFOA", "## Appendix A"),
    )
    write(
        "batch_b_variant_w.md",
        "B-W",
        body("assisted_attempt2_batch_b.md", "## 磺胺甲噁唑", "## Appendix"),
    )
    write(
        "batch_b_variant_x.md",
        "B-X",
        body("model_only_attempt2_batch_b.md", "## SMX", "## Appendix"),
    )


if __name__ == "__main__":
    main()
