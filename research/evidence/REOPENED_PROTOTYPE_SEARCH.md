# 无 finalist 后的库外生物原型重开审查

## 审查目的

Top-five Round 2 与 S1 Round 3 均未产生达到 `85/100`、零 critical/high 且同时具备静态和动态硬对应的方案。本文件按项目合同重新开放库外生物原型。BMDL 未参与候选发现、证据检索或方案排序。

检索优先回答两个问题：目标污染物是否直接出现在结构或动力学证据中；观察到的构象变化是否能转译为比“材料会动”更具体的材料坐标和因果对照。

## 结论摘要

| 路线 | 直接目标证据 | 动态证据 | 当前裁决 |
|---|---|---|---|
| PFOA–FABP4 | PFOA 共晶 `9MIW`，主/次两个结合位点 | PFOA 结合态 Phe57 为 open，apo `9OB7` 为 closed；第二个 PFOA 的容纳需要该 open 构象 | **重开为 S11**；动态主张限于 Phe57 局部侧链门，不扩写为全蛋白开闭 |
| PFOA–PPARγ | PFOA–PPARγ LBD 共晶，三个 PFOA 位点 | 论文结论为 Helix 12-independent partial agonism | 静态参考；不作为动态门原型 |
| PFOS–FadL | PFOS 异构体与 FadL 的 MD，另有细胞摄取/异构体分析 | hatch 变化来自模拟；FadL 被作者用作人脂肪酸转运蛋白的 proxy | 保留为低等级线索；不足以形成动态硬对应 |
| 罗红霉素–核糖体 | 罗红霉素属于大环内酯且抑制 50S | A2062 转动和停滞证据来自红霉素、阿奇霉素、泰利霉素、solithromycin 等相关药物 | 不重开；不能把同类药物动态转移给罗红霉素 |

## 1. PFOA–FABP4：允许重开

### 直接来源

- Birchfield AS et al. *Broad PFAS Binding with Fatty Acid Binding Protein 4 Is Enabled by Variable Binding Modes*. JACS Au. 2025;5(6):2469–2474. DOI: `10.1021/jacsau.5c00504`; PMCID: `PMC12188406`.
- 已检查全文及结构条目：PFOA-bound FABP4 `9MIW`，apo delipidated FABP4 `9OB7`，PFDA-bound `9MIZ`，PFHxDA-bound `9MP2`。

### 已核实事实

1. FABP4 对多种 PFAS 有可测结合，亲和力随碳链、头基和氟化方式变化。因此该原型支持的是 PFAS/PFCA 识别窗口，不能预设 PFOA 单分子特异性。
2. `9MIW` 中观察到两个 PFOA：主位点羧酸头基涉及 Arg126、Tyr128 和水介导的 Arg106；次位点羧酸头基涉及 Thr29。
3. 与 apo `9OB7` 相比，PFOA-bound `9MIW` 的 Phe57 取 open 构象并扩大疏水腔。作者明确指出该 open 构象为容纳第二个 PFOA 所需，并说明 PFOA 情形的相似变化由第二个配体引起。
4. PFDA 也使 Phe57 取 open；PFHxDA 则使其更接近 apo 的 inward/closed 状态。Phe57 因而是链长/占位相关的局部构象坐标，不是 PFOA 独占开关。

### 可用主张边界

- **可用：** FABP4 的头基锚定、受限疏水腔、双位点 PFOA 占位和 Phe57 局部门可形成同一生物原型内的静态—动态对应。
- **不可用：** “PFOA 特异触发全蛋白闭合”“Phe57 open 必然提高吸附选择性”“双位点必然在痕量二级出水中同时占据”。后两项必须由浓度依赖、突变体和竞争平衡实验判定。
- **设计后果：** 优先使用实际 FABP4 或保持完整口袋的确定构建体；Phe57 因果对照必须与静态锚定位点突变分开。仅用普通柔性肽模拟 Phe57 不足以继承直接证据。

## 2. PFOA–PPARγ：不作为动态原型

### 直接来源

- Pederick JL et al. *A structural basis for the activation of peroxisome proliferator-activated receptor gamma (PPARγ) by perfluorooctanoic acid (PFOA)*. Chemosphere. 2024;354:141723. DOI: `10.1016/j.chemosphere.2024.141723`.

### 核实结果

论文用 X-ray 共晶解析 PFOA–PPARγ LBD，观察到三个 PFOA 位点，并以荧光偏振检验 coactivator peptide recruitment。作者把 PFOA 定义为微摩尔条件下的弱 partial agonist，同时明确其机制为 Helix 12-independent。该来源加强 PFOA 多位点静态识别，但不能支持把 Helix 12 设计成 PFOA 触发的动态硬对应。

## 3. PFOS–FadL：保留线索，不晋级

### 直接来源

- James D et al. *Bioaccumulation of PFOS Isomers in Transporter Proteins*. Chem Res Toxicol. 2026;39(1):168–177. DOI: `10.1021/acs.chemrestox.5c00432`; PMCID: `PMC12820963`.

### 核实结果

研究包含 HEK293T 细胞 PFOS 暴露与异构体分析，但 FadL 的 PFOS 结合、LAS/HAS 位点和 hatch 氢键网络变化来自 docking/MD。作者把大肠杆菌 FadL 用作人长链脂肪酸转运的模型，研究目标是 PFOS 异构体生物累积差异。该工作可以提出“分级位点加局部 hatch”线索，却不能把模拟中的变化当作已实验确认的 PFOS 目标动态，也不能直接推出污水中 PFOS 选择性吸附。

## 4. 罗红霉素–核糖体：维持终止

大环内酯可诱导 23S rRNA A2062 约 160° 转动，并与 m2A2503 等局部结构关联；相关结构主要来自 erythromycin、azithromycin、telithromycin、solithromycin 或其他组合。现有允许证据没有给出 roxithromycin-bound 核糖体的同等直接构象链。结构相似和同类药理不足以建立罗红霉素的动态硬对应，S6 不因本次重开恢复。

## 重开决定

只重开一个新候选：`S11 FABP4 双位点/Phe57 局部门生物杂化吸附体`。S11 必须经过新的 Designer、Attacker、Reviewer 隔离链；旧 S1 分数和 finalist 身份不继承。若实际 FABP4 的广谱脂质结合、双占位浓度条件、容量、固定化失活或真实基质竞争使选择性主张无法成立，则终止 S11，不再把同一证据改写为合成柔性门方案。
