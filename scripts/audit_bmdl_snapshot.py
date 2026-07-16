#!/usr/bin/env python3
"""Produce a reproducible structural audit of the committed BMDL snapshot."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
from typing import Any, Iterable


ORGANIC_TARGETS = ("PFOA", "PFOS", "BPA", "SMX", "CIP", "Roxithromycin")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, default=Path("data/bmdl_snapshot"))
    parser.add_argument("--json-output", type=Path, default=Path("research/bmdl/audit_metrics.json"))
    parser.add_argument("--report-output", type=Path, default=Path("research/bmdl/BMDL_AUDIT.md"))
    return parser.parse_args()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk_dicts(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def counter_dict(counter: collections.Counter) -> dict[str, int]:
    return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))


def pct(numerator: int, denominator: int) -> str:
    return f"{100 * numerator / denominator:.1f}%" if denominator else "0.0%"


def main() -> None:
    args = parse_args()
    manifest = load(args.snapshot / "manifest.json")
    prototypes = load(args.snapshot / "biological_prototypes.json")
    profiles = load(args.snapshot / "pollutant_profiles.json")
    matches = load(args.snapshot / "match_weights.json")

    source_categories = collections.Counter(str(p.get("source_category") or "missing") for p in prototypes)
    dimensions = collections.Counter(str(p.get("biomimetic_dimension") or "missing") for p in prototypes)
    statuses = collections.Counter(str(p.get("status") or "missing") for p in prototypes)
    mechanism_basis = collections.Counter()
    mechanism_verification = collections.Counter()
    design_tiers = collections.Counter()
    prototype_quality = collections.Counter()
    total_mechanisms = 0
    total_design_translations = 0

    for prototype in prototypes:
        mechanisms = prototype.get("mechanisms") or []
        if isinstance(mechanisms, dict):
            mechanisms = [mechanisms]
        if not isinstance(mechanisms, list):
            mechanisms = []
        total_mechanisms += len(mechanisms)
        for mechanism in mechanisms:
            for node in walk_dicts(mechanism):
                if node.get("basis"):
                    mechanism_basis[str(node["basis"])] += 1
                if node.get("verification"):
                    mechanism_verification[str(node["verification"])] += 1

        translations = prototype.get("design_translation") or []
        if isinstance(translations, dict):
            translations = [translations]
        if not isinstance(translations, list):
            translations = []
        total_design_translations += len(translations)
        for translation in translations:
            if isinstance(translation, dict):
                design_tiers[str(translation.get("source_tier") or "missing")] += 1

        if prototype.get("honesty_ledger"):
            prototype_quality["with_honesty_ledger"] += 1
        if mechanisms:
            prototype_quality["with_mechanisms"] += 1
        if translations:
            prototype_quality["with_design_translation"] += 1
        if prototype.get("performance_data"):
            prototype_quality["with_performance_data"] += 1

    lane_counts = collections.Counter(str(row.get("lane") or "missing") for row in matches)
    direct_counts = collections.Counter(str(bool(row.get("direct_evidence"))).lower() for row in matches)
    honesty_counts = collections.Counter(str(row.get("candidate_honesty") or "missing") for row in matches)
    prototype_frequency = collections.Counter(str(row.get("prototype_id") or "missing") for row in matches)
    pollutant_rows: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in matches:
        pollutant_rows[str(row.get("pollutant_id"))].append(row)

    organic_queries = {}
    all_organic_prototypes: list[str] = []
    for pollutant in ORGANIC_TARGETS:
        rows = pollutant_rows.get(pollutant, [])
        ids = [str(row.get("prototype_id")) for row in rows]
        all_organic_prototypes.extend(ids)
        organic_queries[pollutant] = {
            "rows": len(rows),
            "lanes": counter_dict(collections.Counter(str(row.get("lane")) for row in rows)),
            "direct_evidence": sum(bool(row.get("direct_evidence")) for row in rows),
            "prototypes": ids,
        }
    organic_frequency = collections.Counter(all_organic_prototypes)

    metrics = {
        "snapshot_counts": manifest["counts"],
        "source_categories": counter_dict(source_categories),
        "statuses": counter_dict(statuses),
        "biomimetic_dimensions": counter_dict(dimensions),
        "prototype_field_coverage": counter_dict(prototype_quality),
        "total_mechanisms": total_mechanisms,
        "mechanism_basis_occurrences": counter_dict(mechanism_basis),
        "mechanism_verification_occurrences": counter_dict(mechanism_verification),
        "total_design_translations": total_design_translations,
        "design_translation_source_tiers": counter_dict(design_tiers),
        "match_lanes": counter_dict(lane_counts),
        "match_direct_evidence": counter_dict(direct_counts),
        "candidate_honesty": counter_dict(honesty_counts),
        "top_retrieved_prototypes": prototype_frequency.most_common(12),
        "organic_target_queries": organic_queries,
        "organic_prototype_frequency": organic_frequency.most_common(),
        "profile_classes": counter_dict(collections.Counter(str(p.get("pollutant_class") or "missing") for p in profiles)),
    }

    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    raw = manifest["counts"]["performance_data_raw"]
    unique = manifest["counts"]["performance_data_deduplicated"]
    design_literature = design_tiers.get("literature", 0)
    design_inferred = design_tiers.get("llm_inference", 0)
    direct_true = direct_counts.get("true", 0)
    total_matches = len(matches)
    report = f"""# BMDL客观结构审计

> 数据来源：只读 PostgreSQL 快照  
> BMDL来源提交：`{manifest.get('source_bmdl_commit')}`  
> 导出安全状态：default transaction read only = `{manifest['safety']['default_transaction_read_only']}`，transaction read only = `{manifest['safety']['transaction_read_only']}`

## 结论

BMDL适合作为结构化原型线索和证据诚实性检查工具，但当前数据不足以直接决定新污染物选择性吸附材料。主要原因是有机微污染物匹配多处于探索通道，设计转译中推断内容占比高，并且多个目标会反复返回少数常见原型。正式设计必须先冻结模型独立方案，再根据配对盲评决定BMDL是进入设计辅助、仅做证据核验，还是完全退出设计阶段。

## 快照事实

| 指标 | 数值 | 解释 |
|---|---:|---|
| biological_prototypes | {len(prototypes)} | 包含primary、reference和quarantined等类别 |
| pollutant_profiles | {len(profiles)} | 污染物画像数量 |
| match_weights | {total_matches} | 原型与污染物的匹配记录 |
| performance_data原始行 | {raw} | 含重复导入，不可作为证据量 |
| 去除代理ID后的唯一性能行 | {unique} | 用于后续证据审查的最大候选集合 |
| 重复性能行 | {raw - unique} | 占原始行的{pct(raw - unique, raw)} |
| 直接证据匹配 | {direct_true} | 占匹配记录的{pct(direct_true, total_matches)} |
| literature设计转译 | {design_literature} | 总设计转译{total_design_translations}条 |
| llm_inference设计转译 | {design_inferred} | 不得直接支持硬对应 |

## 匹配质量

- Lane分布：{json.dumps(counter_dict(lane_counts), ensure_ascii=False)}。
- 候选诚实性：{json.dumps(counter_dict(honesty_counts), ensure_ascii=False)}。
- 高频原型：{', '.join(f'{name}({count})' for name, count in prototype_frequency.most_common(8))}。
- PFOA、PFOS、BPA、SMX、CIP和Roxithromycin的候选主要集中于：{', '.join(f'{name}({count})' for name, count in organic_frequency.most_common(8))}。

上述重复说明BMDL会把芳香性、疏水性、带电或含氢键位点的有机污染物压缩到相似原型族。该结果可提供起始线索，但不足以证明原型具备目标污染物选择性，更不能替代从生物识别、跨膜运输、门控结合或可逆释放机制出发的库外探索。

## 使用约束

1. BMDL结果不得在model-only方案冻结前进入设计者上下文。
2. `weight`仅表示规则或特征匹配，不解释为性能、选择性或真实可信度。
3. `exploratory`和`llm_inference`只能形成待核验线索。
4. 每项进入硬对应的机制必须回到原始文献核实生物功能、适用条件和可移植边界。
5. `performance_data`必须按自然字段去重，并逐条核实指标类型、材料归属和实验条件后才能引用。

## 待完成的正式判定

在十种候选污染物的问题陈述冻结后，对每种污染物分别生成model-only和bmdl-assisted方案，由隔离Reviewer盲评。最终按`research_contract.yaml`中的6/10胜出、平均提升5分、原创性下降不超过2分等门槛决定BMDL的角色。
"""
    args.report_output.parent.mkdir(parents=True, exist_ok=True)
    args.report_output.write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()

