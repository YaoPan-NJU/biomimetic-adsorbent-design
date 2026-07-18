# Biomimetic Selective Adsorbent Design

面向市政二级出水选择性吸附的独立研究仓库。`main` 分支由 Codex 维护并同步 `origin/main`，`GLM` 分支由 Claude Code 维护并同步 `origin/GLM`；两条分支独立演进，互不交叉推送。Pan Yao 负责科学决策，实验交接对象为 Zhou Jiaqi。本项目与 ADRMATS 无关。

## 当前结论

当前没有通过的主方案或备选方案，`primary_design` 与 `backup_design` 均为 `null`。BPA、PFBS、罗红霉素和 2,6-二氯苯酚的 20 方案扩展与统一排名已经完成；原始前五经攻击后均未达到终审门槛，见 [`rounds/portfolio_20_reopen/REVIEW.md`](rounds/portfolio_20_reopen/REVIEW.md)。

Pan Yao 已纠正此前的路线偏移：生物组织分布和蛋白结合证据用于发现、解释并约束人工材料机制，不能自动把蛋白、表达构建体或折叠肽带入最终材料。主方案必须具有至少一个落实到人工材料的硬功能对应；动态对应改为可选，不再是通过门槛。

此前的 **S1-SYN** PFOA 路线暂停但未终止。当前组合首位为 **BPA-1**：ERRγ 静态化学功能启发、非模板化、非蛋白的选择性吸附路线。它在组合攻击后为 84/100，尚不是主方案。Pan Yao 已授权继续深化 BPA-1；首轮从 `2E2R` 坐标得到 BPA 两酚氧间距约 9.27 Å，并曾冻结 1,2-di(pyridin-4-yl)ethyne（`R1-BPE`）作为可溶机制探针，见 [`GEOMETRY_AND_RECEPTOR_TRIAGE.md`](rounds/bpa1_deep_design_1/GEOMETRY_AND_RECEPTOR_TRIAGE.md)。随后的化学攻击发现 R1 两端吡啶氮向外发散，原子间距接近并不等于氢键方向会聚，因此 R1 已被降为负面对照，BPA-1 新评分为 68/100、`revise`，见 [`R1_CHEMISTRY_ATTACK.md`](rounds/bpa1_deep_design_1/R1_CHEMISTRY_ATTACK.md)。

对 ERRγ 功能证据的复核进一步表明，对称双端夹并非原型强制要求：关键证据更支持“一个酚羟基的互补极性主锚 + 疏水芳香包围”，单羟基类似物仍可强结合。当前已提出确切的可聚合小分子探针 `P1-MAPy`（2-methacrylamidopyridine，162.19 g/mol），并冻结供体删除、受体删除、邻位破坏和疏水空白四级对照及水相停止门，见 [`P1_MAPY_CONTROL_AND_GATE.md`](rounds/bpa1_deep_design_1/P1_MAPY_CONTROL_AND_GATE.md)。随后攻击发现，acylaminopyridine 的成熟两点识别对象是具有两个氧的羧酸，而不是 BPA 的单个酚氧；直接水凝胶先例也表现为一般酚吸附且体积增大时容量下降。故 P1 只保留为实验探针，BPA-1 当前 `70/100, experiment-gated`，不进入材料化，见 [`P1_MAPY_ATTACK.md`](rounds/bpa1_deep_design_1/P1_MAPY_ATTACK.md)。

BPA-2 的纸面攻击已完成。β-CD 对 BPA 的 `1:1` 水相包合有直接 NMR 支持，`Ka` 约 `3.62–4.10×10^3 M^-1`；但“β-CD 与随机双氢键单体共聚”不能证明同一个 BPA 同时接触两个位点。路线因此拆为 `BPA-2E` 工程基线（72/100，只主张高 β-CD 位点密度与工程化）和 `BPA-2R` 研究变体（63/100，必须先冻结同一 β-CD 次级宽口上的确切共价极性站）。纯 β-CD 的 `1:1` 理论上限仅 `201.14 mg BPA/g β-CD`，最终材料上限为 `201.14 × w_betaCD mg/g`，所以交联剂与骨架质量必须严格计入。完整记录见 [`BPA2_BASELINE_AND_COLOCALIZATION_ATTACK.md`](rounds/bpa2_deep_design_1/BPA2_BASELINE_AND_COLOCALIZATION_ATTACK.md)。架构比较又确认，已有自支撑高 β-CD 网络同时覆盖快速吸附、再生、腐殖酸/离子耐受和实际废水场景，再做交联剂优化不足以形成新的选择性贡献；故 `BPA-2E` 已降为工程阳性对照，见 [`BPA2E_ARCHITECTURE_COMPARISON.md`](rounds/bpa2_deep_design_1/BPA2E_ARCHITECTURE_COMPARISON.md)。

PFBS-1 的攻击也已完成。2022 年已有工作几乎原样实现了“七位苯乙烯化 β-CD + 阳离子甲基丙烯酸共聚单体 + 永久多孔网络”，因此该路线不存在足够的材料原创空间；更关键的是，`1 mM Na2SO4` 使 PFBS 去除率从约 `94%` 降至 `38%`，而 PFOS 仍约为 `79%`，说明它在盐竞争下并不优先保留短链 PFBS。PFBS-1 新增处置为 `58/100, control-only`，历史 82/74 分保留，见 [`PFBS1_PRIOR_ART_AND_SALT_ATTACK.md`](rounds/pfbs1_deep_design_1/PFBS1_PRIOR_ART_AND_SALT_ATTACK.md)。PFBS-2 的可溶受体攻击随后未找到确切、轻质、非氟化且在盐水中 C4 优先的受体；胍基/脲反而有优先捕获硫酸根和磷酸根的直接风险，故为 `52/100, exact-receptor-not-found`，不进入材料化，见 [`PFBS2_SOLUBLE_RECEPTOR_ATTACK.md`](rounds/pfbs2_deep_design_1/PFBS2_SOLUBLE_RECEPTOR_ATTACK.md)。PFBS-3/4/5 分别受含氟材料生命周期、模板泄漏和普通离子交换原创性限制，不继续消耗深设轮次；下一纸面路线转向 ROX-2。当前仍无主方案或备选方案，不订购、不合成、不开展实验。

## 阅读入口

新会话入口：`GLM` 分支从 [`CLAUDE.md`](CLAUDE.md) 起，`main` 分支从 [`AGENTS.md`](AGENTS.md) 起；两者规则一致。随后按以下顺序阅读：

1. [`AGENTS.md`](AGENTS.md)
2. [`SOUL.md`](SOUL.md)
3. [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml)
4. [`HANDOFF.md`](HANDOFF.md)
5. [`research_contract.yaml`](research_contract.yaml)
6. [`S1_SYNTHETIC_RECOVERY_BRIEF.md`](rounds/synthetic_recovery_1/S1_SYNTHETIC_RECOVERY_BRIEF.md)

`PROJECT_STATE.yaml` 是机器可读状态，`HANDOFF.md` 保存完整跨设备交接和历史解释。

## 设计边界

- 主水体为市政/生活污水处理二级出水，超纯水只用于机制控制。
- 选择性是主性能；容量、再生、浸出和稳定性是工程约束。
- 载体不预设为硅、树脂或碳；容量按整个干燥复合材料和装填床体积报告，不能用大量不参与吸附的载体隐藏质量惩罚。
- 组织富集是候选原型发现信号，不是某一蛋白负责富集的因果证明。
- 可选的“体内组织/器官选择性富集 → 机制确认 → 暴露前人工截留”思路见 [`ORGAN_ENRICHMENT_BIOMIMETIC_HEURISTIC.md`](research/evidence/ORGAN_ENRICHMENT_BIOMIMETIC_HEURISTIC.md)；它不参与评分，也不改变当前路线。
- 默认材料为可制造的非蛋白人工吸附剂。
- 蛋白、折叠肽和生物杂化路线只有在 Pan Yao明确重开范围后才能进入。
- BMDL 不进入创意设计，只允许在设计冻结后做负面审计。
- 所有历史轮次均保留，不以新结论覆盖旧文件。

## 完整历史轨迹

### 第一阶段：旧污染物漏斗与磷酸盐周期

1. **BMDL 审计与基线。** 模型-only 基线、BMDL 快照和盲评均已完成。第一次配对比较因证据账本变化而作废；第二次受控比较未达到增益门槛，形成“设计阶段排除、冻结后负面审计”的政策。入口见 [`BMDL_PAIRED_EVALUATION.md`](research/bmdl/BMDL_PAIRED_EVALUATION.md)。
2. **旧 Round 1。** D1–D5 完成设计、攻击和复核，均未通过；D1 磷酸盐为最强修订候选。见 [`rounds/round_1/REVIEW.md`](rounds/round_1/REVIEW.md)。
3. **旧 Round 2。** D1 提升至 83，D2 克拉霉素因动态证据不足被排除，D3–D5 终止。见 [`rounds/round_2/REVIEW.md`](rounds/round_2/REVIEW.md)。
4. **旧 Round 3。** D1-A 合成双臂磷酸盐肽夹以 93/100 通过设计审查；D1-B 固定化 PBP 痕量抛光床以 89/100 通过设计审查。见 [`REVIEW_D1A.md`](rounds/round_3/REVIEW_D1A.md) 和 [`REVIEW_D1B.md`](rounds/round_3/REVIEW_D1B.md)。
5. **旧交付。** 中文报告与附件保存在 [`deliverables/`](deliverables/README.md)。这些是设计通过记录，不是实验结果；在有机新污染物范围重开后成为历史方案。

### 第二阶段：有机/新污染物范围重开

1. **污染物范围重开。** 主漏斗改为有机污染物并优先考虑新污染物；环境相关性和健康/环境关注度改为入场硬门。见 [`REOPENED_SCOPE.md`](research/pollutants/REOPENED_SCOPE.md)。
2. **十方案组合。** 产生 S1–S10，并推荐 S1 PFOA、S5 BPA、S3 GenX、S4 PFBS/PFHxS/PFOS、S6 罗红霉素进入深度设计。见 [`DEEP_RESEARCH_BIOMIMETIC_SCHEME_PORTFOLIO.md`](DEEP_RESEARCH_BIOMIMETIC_SCHEME_PORTFOLIO.md)。
3. **Top-5 Round 1。** 五个方案均未通过；保存了设计、攻击、审查和独立角色执行偏差。见 [`rounds/top5_round_1/REVIEW.md`](rounds/top5_round_1/REVIEW.md)。
4. **Top-5 Round 2。** S3、S6 终止，S4、S5 降为对照；S1 以 82/100 成为唯一进入第三轮的候选。见 [`rounds/top5_round_2/REVIEW.md`](rounds/top5_round_2/REVIEW.md)。
5. **Top-5 Round 3。** S1 被改写为 hL-FABP 静态原型＋iLBP portal 动态原型的折叠肽方案，终审为 56/100、3 Critical、4 High，正式终止。见 [`rounds/top5_round_3/REVIEW.md`](rounds/top5_round_3/REVIEW.md)。

### 第三阶段：外部原型重开与 S11

1. 外部原型搜索只接纳了 FABP4–PFOA 直接结构路线，形成 S11 FABP4 生物杂化候选。见 [`REOPENED_PROTOTYPE_SEARCH.md`](research/evidence/REOPENED_PROTOTYPE_SEARCH.md)。
2. S11 初始设计得分 60/100；后续修正序列、编号、表面偶联、占位测量、NMR、T30A 因果对照和统计规则。
3. S11 Gate 1a 在设计层达到 0 Critical、0 High，但 Gate 1b 采购制造未完成，Gate 2 实验未开始。见 [`GATE1_REVIEW_2.md`](rounds/prototype_reopen_1/GATE1_REVIEW_2.md)。
4. S11 从未成为主方案或备选，也从未授权订购或实验。

### 第四阶段：人工材料方向恢复

Pan Yao 复核后确认，强制“静态＋动态硬对应”使项目从机制转译偏移到复制蛋白结构。当前规则已改为：

- 至少一个人工材料中的硬功能对应；
- 动态可选；
- 蛋白和组织信息只作为机制证据；
- S1、S11 及全部旧轮次作为历史审计保留；
- 重新从第二轮提出的人工材料方向发展 S1-SYN。

恢复设计入口为 [`rounds/synthetic_recovery_1/S1_SYNTHETIC_RECOVERY_BRIEF.md`](rounds/synthetic_recovery_1/S1_SYNTHETIC_RECOVERY_BRIEF.md)。

### 第五阶段：四污染物 20 方案与 BPA-1 深化

1. 针对 BPA、PFBS、罗红霉素和 2,6-二氯苯酚冻结 20 个非蛋白人工材料方案，并保留原始排名、证据审计和前五攻击。见 [`rounds/portfolio_20_reopen/`](rounds/portfolio_20_reopen/REVIEW.md)。
2. 攻击后 BPA-1 为 84/100、`revise`；其余前五均不高于 74，当前仍无主方案或备选方案。
3. Pan Yao 授权只继续深化 BPA-1。首个检查点把蛋白结构压缩为静态几何：`2E2R` 中 BPA 两酚氧约相距 9.27 Å、芳环接近正交；不转译蛋白序列、折叠或动态。
4. 首轮曾冻结 `R1-BPE` 及删除/错配系列；下一次化学攻击发现其受体方向发散且控制组同时改变多项性质，故 R1 终止为完整受体，只保留为负面对照。该修订追加记录，没有覆盖首轮文件。
5. 再复核 ERRγ 的突变与单羟基类似物证据后，撤销“必须跨两个羟基对称夹持”的错误约束，转为单端互补主锚与疏水包围。`P1-MAPy` 已作为确切、轻质、可聚合的机制探针候选记录，但尚未通过水相 BPA 结合门。
6. 已冻结 `P1/C1-NHoff/C2-Noff/C3-meta/C4-H` 对照组和可溶门：P1–BPA 至少达到 `100 M-1`、高于三个结构对照中最强者 3 倍，且两种正交方法的 `Ka` 相差不超过 3 倍；这些是待攻击的预注册设计，不是实验结果。
7. 对抗审查确认 P1 的经典两点证据属于羧酸受体化学，不能直接转给单酚氧；水相酚吸附先例的体积趋势也不利。P1 保留为高信息量实验探针，BPA-1 暂停材料化，纸面深化转向 BPA-2 保险路线。
8. BPA-2 攻击确认 β-CD 是可靠的水相 BPA 工程受体，却否定随机极性共聚单体的“同腔协同”主张；新增 `BPA-2E` 工程基线与 `BPA-2R` 精确次级口研究变体，两者均未成为最终方案。
9. 架构比较确认高 β-CD 自支撑网络已有拥挤先例，且低密度接枝会受载体质量惩罚；`BPA-2E` 固定为阳性对照，下一纸面攻击转向 PFBS-1。
10. PFBS-1 与 2022 年阳离子 β-CD 多孔平台直接重合，且 PFBS 在硫酸盐中显著失效；该路线固定为阳性对照，下一纸面攻击转向 PFBS-2。
11. PFBS-2 未找到能在水和无机阴离子竞争下产生 C4 非单调选择性的确切受体，停止于可溶受体门；动态资源转向 ROX-2。
