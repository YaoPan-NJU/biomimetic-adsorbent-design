# Biomimetic Selective Adsorbent Design

面向市政二级出水选择性吸附的独立研究仓库。Codex 负责证据整理、材料设计和对抗审查，Pan Yao负责科学决策，实验交接对象为 Zhou Jiaqi。本项目与 ADRMATS 无关。

## 当前结论

当前没有通过的主方案或备选方案，`primary_design` 与 `backup_design` 均为 `null`。BPA、PFBS、罗红霉素和 2,6-二氯苯酚的 20 方案扩展与统一排名已经完成；原始前五经攻击后均未达到终审门槛，见 [`rounds/portfolio_20_reopen/REVIEW.md`](rounds/portfolio_20_reopen/REVIEW.md)。

Pan Yao 已纠正此前的路线偏移：生物组织分布和蛋白结合证据用于发现、解释并约束人工材料机制，不能自动把蛋白、表达构建体或折叠肽带入最终材料。主方案必须具有至少一个落实到人工材料的硬功能对应；动态对应改为可选，不再是通过门槛。

此前的 **S1-SYN** PFOA 路线暂停但未终止。当前组合首位为 **BPA-1**：ERRγ 静态几何启发、非模板化、非蛋白的刚性双端夹持超交联多孔聚合物。它在攻击后为 84/100，尚缺确切受体结构和水相几何验证，因此不是主方案。PFBS-1、PFBS-2、BPA-2 为并行修订路线，ROX-1 仅作为工程基准。

当前下一动作是 Pan Yao 审阅 20 方案和攻击后排名。若批准继续，只深化 BPA-1 的确切非模板化受体、可溶删除/错配系列和总材料容量上限；在该设计通过前，不订购、不合成、不开展实验，也不继续 S11 Gate 1b/Gate 2。

## 阅读入口

新会话按以下顺序阅读：

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
