# Ultimate 轮 · BPA×100 + PFBS×100 组合（阅读索引）

- 分支：`Ultimate`（自 `Qwen` af5c419 派生，独立深化）
- 产出日期：见 git 提交
- 状态：文书设计，未授权采购/合成/实验；无主方案/备选方案

## ⚠️ 与 fresh_1000 前沿的关系（务必先读）

**本轮存在重大范围偏差，如实记录。** 本轮以旧的 `rounds/portfolio_100`（各污染物 20 方案、结论"无方案达 85"）为基线构建，**未交叉参照仓库真正的前沿轮次 `rounds/fresh_1000`**（`STATUS.yaml` last_updated 2026-07-22）。核对后发现前沿已推进得多：

1. **前沿已有 6 个通过方案（≥85）**，其中 **BPA A01 = DmpR 锚-门 COF = 86（passed）**、**PFBS A17 = 孔口双位点头基类型反差 = 85（passed）**。因此本 README/各排序文件中"无方案达 85"的表述**仅对 portfolio_100 成立，对全仓库不成立**。
2. **本轮 BPA 最高分 U13（非对称单酚锚 + 异丙叉桥基判别 COF，80）实为前沿已终止的死路**：等同 `fresh_1000/bpa` A03 `isopropylidene-geometric-ruler-COF`，r3=64 terminate，理由为 BPA/BPF 桥差内禀过微、α(BPA/BPF) 被纯疏水 ΔlogKow 覆盖（命中陷阱 T1）、C 维仿生硬对应缺如。**本轮对 U13 评 80 分是相对 portfolio_100 的高估，前沿证据判其不可达 85。**
3. **本轮 BPA 承重 U01（漆酶 Cu 配位）被前沿 BPA Phase A 质疑**：其判"降解酶系属催化转化非识别、生物处理单元启发式不够格"。U01 以"取配位识别步而非催化"辩护尚可，但与前沿采用的 **DmpR 酚感应蛋白**（真实识别原型，已通过 86）相比，承重原型选择偏弱。
4. **本轮 PFBS 承重 α（脱水选择性弱配位孔）与前沿终止项重叠**：`fresh_1000` 中 KcsA-脱水路线（PFOA A06）平台期 69 terminate；前沿 PFBS 的通过方案 A17 走的是**头基类型反差（四面体磺酸根 vs 平面羧酸根，T/P 双位点）**，与本轮 α 机制不同。

**如何看待本轮**：宜视为**在旧基线上的一次系统性广度铺覆（100+100，角度地图 + 10 家族）**，用于补充前沿"广度优先、每污染物仅试 2–3 槽"未触及的角度；**不构成前沿推进**，顶部选条（U13/U01/α）须按上述前沿证据重新裁决或降级。`PROJECT_STATE.yaml` 保持前沿（fresh_1000）状态未改动。**下一步建议**：以 `fresh_1000/bpa/S14_A01_DmpR-anchor-gate-COF_passed.md` 与 `fresh_1000/pfbs/S17_A17_pore-mouth-dual-site-headgroup_passed.md` 为起点，将本轮广度角度中与前沿不重复、未被终止理由覆盖者并入 fresh_1000 回溯补角。

## 这是什么

按项目框架（`docs/BIOMIMETIC_DESIGN_FRAMEWORK.md`、`SOUL.md`、`research_contract.yaml`）对 **BPA** 与 **PFBS** 各系统性冻结 **100 个机制可区分的非蛋白人工吸附材料方案**（共 200），随后按 6 维评分漏斗淘汰、排序，并对各污染物存活的高质量候选做实验级深化。价值在**系统覆盖 + 硬漏斗 + 深化赢家**，非方案计数。

## 阅读顺序

1. [`00_DESIGN_BRIEF.md`](00_DESIGN_BRIEF.md) — 任务、框架约束、评分、继承死路、增量入口
2. [`BPA_ANGLE_MAP.md`](BPA_ANGLE_MAP.md) / [`PFBS_ANGLE_MAP.md`](PFBS_ANGLE_MAP.md) — 设计空间与 100 方案生成矩阵
3. 组合目录：`BPA_PORTFOLIO_01-50.md`、`BPA_PORTFOLIO_51-100.md`；`PFBS_PORTFOLIO_01-50.md`、`PFBS_PORTFOLIO_51-100.md`
4. 内部排序：[`BPA_RANKING.md`](BPA_RANKING.md) / [`PFBS_RANKING.md`](PFBS_RANKING.md)
5. 隔离攻击淘汰：[`BPA_CULL.md`](BPA_CULL.md) / [`PFBS_CULL.md`](PFBS_CULL.md)
6. [`GLOBAL_RANKING.md`](GLOBAL_RANKING.md) — 跨污染物全局排序与诚实总评
7. `deep_design/` — 顶部赢家实验级深化

## 顶部赢家（深化文档）

| 污染物 | 编号 | 简称 | 分 | 深化 |
|:--:|---|---|---:|---|
| BPA | U01 | 漆酶 Cu 配位识别活性炭 | 79 | [`deep_design/BPA_U01_LACCASE_CU.md`](deep_design/BPA_U01_LACCASE_CU.md) |
| BPA | U13 | 非对称单酚锚 + 桥基判别 COF | 80 | [`deep_design/BPA_U13_ASYM_BRIDGE_COF.md`](deep_design/BPA_U13_ASYM_BRIDGE_COF.md) |
| PFBS | α (U13/U21/U01/U11) | 脱水选择性弱配位门闩孔口 | 74 | [`deep_design/PFBS_ALPHA_DEHYDRATION_LATCH.md`](deep_design/PFBS_ALPHA_DEHYDRATION_LATCH.md) |

## 编号与既有工作的关系

- 本轮用 `BPA-U01…U100`、`PFBS-U01…U100`（`U`=Ultimate），避免与既有 `BPA-1…19`、`PFBS-1…20`（`portfolio_100`、`portfolio_20_reopen`）冲突。
- 继承并硬性规避既有死路（对称夹持、酰氨吡啶=羧酸受体、β-CD 天花板、电荷=盐敏感、含氟 lifecycle、思路三），见 `00_DESIGN_BRIEF.md` §4。

## 一句话结论（含前沿更正）

本轮在 portfolio_100 基线上封顶 BPA 80 / PFBS 74，且顶部 U13 实为前沿已终止死路、U01 承重原型偏弱、α 与前沿终止项重叠——**故本轮不构成前沿推进**。仓库前沿（fresh_1000）已有 BPA 86、PFBS 85 通过方案（DmpR 锚-门 COF / 孔口头基反差）。本轮价值在旧基线上的系统性广度铺覆与诚实的方向级否定记录，须与前沿 reconcile 后方可采信顶部选条。
