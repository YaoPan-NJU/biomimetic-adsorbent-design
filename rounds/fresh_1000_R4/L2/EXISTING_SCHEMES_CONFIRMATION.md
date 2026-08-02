# L2 已有方案引用确认（5 个已有完整设计的方案）

**日期：** 2026-08-02
**说明：** 以下 5 个方案在 fresh_1000 R1 中已完成完整的设计-攻击-裁决闭环（多轮迭代），本文件确认其 L2 状态并链接源文件。

---

## 1. NP A01 — Bayram ipso α-四级碳深腔笼（92 分，全项目最高）

- **源文件：** `rounds/fresh_1000/np/SCHEMES/S26_A01_ipso-alpha-quaternary-topology-cavity_passed.md`
- **迭代轨迹：** r1=82 → r2=92 pass（0c/0h）
- **L2 状态：** ✅ 已完成（R1 即为 L2 深度）
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **关键弱点：** 无酶-底物复合物结构（几何统计对应）；水相形状区分可能 <2 倍；heroic 合成

## 2. BPA A01 — DmpR 酚锚门控 COF（86 分）

- **源文件：** `rounds/fresh_1000/bpa/SCHEMES/S14_A01_DmpR-anchor-gate-COF_passed.md`
- **迭代轨迹：** r1=71 → r2=82 → r3=83 → r4=84 → r5=86 pass（0c/0h）
- **L2 状态：** ✅ 已完成（5 轮迭代）
- **同源 main 版本：** `rounds/bpa_dcp_20x2_deep_design_20260725/DEEP_DESIGN_AND_SCORECARD.md`（BPA20-01，86 分 E1_ready）
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-concept_valid
- **关键弱点：** 水相酚-吡啶 H 键可能趋零；同晶格精度制造难；P(S2)≈20-30% 低先验

## 3. Dieldrin A01 — Rdl 刚性疏水腔+方酰胺环氧读出（89 分原始 / 83 分 L2 校准）

- **源文件：** `rounds/fresh_1000/dieldrin/SCHEMES/S27_A01_exo-epoxide-dual-Hbond-cavity_passed.md`
- **迭代轨迹：** r1=70 → r2=89 pass（0c/0h）
- **L2 状态：** ✅ 已完成（但 L2 校准降分至 83，因毒性靶标降级+水相弱 H 键）
- **谱系状态：** SP-retained / BP-conditional（毒性靶标）/ TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **关键弱点：** Rdl 是毒性靶标（改称理性受体设计）；水相环氧 H 键 <2-3 kJ/mol

## 4. ROX A01 — 23S rRNA NPET 核苷酸碱基裂缝半笼（85 分原始 / 79 分 L2 校准）

- **源文件：** `rounds/fresh_1000/rox/SCHEMES/S32_A01_ribosome-NPET-nucleobase-cleft-cage_passed.md`
- **迭代轨迹：** r1=66 → r2=78 → r3=82 → r4=85 pass（0c/0h）
- **L2 状态：** ✅ 已完成（但 L2 校准降分至 79，因材料完全悬空未实例化）
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **关键弱点：** 材料处于"参数化而非实例化阶段"；亲和力要求 10⁸-10⁹ L/mol 不现实

## 5. DDT A01 — 脱氯化氢酶 β-消除双基序（86 分原始 / 76 分 L2 校准）

- **源文件：** `rounds/fresh_1000/ddt/SCHEMES/S51_A01_dehydrochlorinase-dual-motif_passed.md`
- **迭代轨迹：** r1=73 → r2=86 pass（0c/0h）
- **L2 状态：** ✅ 已完成（但 L2 校准降分至 76，因工程化缺失+证据完整性 6/10+跨分支审查 D 级）
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-embodiment_rejected（离散笼无法装柱）/ SR-route_rejected / ER-lead_only
- **关键弱点：** 离散笼是溶液相分子非材料；Born 方程计算未复核；跨分支审查列 D 级
- **再平台化建议：** 保留 BP（脱氯化氢酶）和 TR（Born 方程低介电去稳定），将 ME 替换为介孔 PMO 碱位-疏水口袋双区（见 L1 A05/A09）

---

## L2 已有方案总结

| 方案 | R1 分数 | L2 校准分 | 状态 | 主要问题 |
|---|---|---|---|---|
| NP A01 | 92 | 92 | pass（维持） | 合成 heroic |
| BPA A01 | 86 | 86 | pass（维持） | 水相锚弱 |
| Dieldrin A01 | 89 | 83 | pass（降分） | 毒性靶标 |
| ROX A01 | 85 | 79 | pass（降分） | 材料悬空 |
| DDT A01 | 86 | 76 | pass（降分） | 工程化缺失 |

**L2 累计进度：** 10/150（5 新方案 + 5 已有方案确认）
