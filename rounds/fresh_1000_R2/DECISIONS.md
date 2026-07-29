# fresh_1000 Round 2 决策日志

> 本文件记录 R2 执行过程中的关键决策，确保决策不丢失于会话上下文。

---

## 2026-07-29 R2 启动

### 一、范围决策

1. **R2 独立于 R1**：R2 的 1000 个方案槽不继承 R1 方案编号，不继承 R1 分数
2. **正交性硬约束**：每个 R2 方案须通过 R1-DEDUP 预筛，与 R1 已占据机制空间正交
3. **中间产物持久化**：每个方案完成 r1 设计后即提取原型卡片/机制映射/角度地图
4. **仿生原型库扩充**：从 83 条扩充至 150+ 条，作为 R2 的核心中间产物

### 二、基线确认

- R1 最终状态：20/20 污染物全覆盖，9 正式通过 / 17 终止 / 5 自评通过
- R1 已占据机制空间：9 个通过方案 + 5 个自评通过方案的核心机制/材料/原型已记录于 `R1_OCCUPIED_SPACE.yaml`
- R1 终止方案：17 个终止方案的失败模式已分类（FM1-FM4），作为 R2 已知陷阱注入

### 三、执行策略

- 五梯队执行顺序（继承 R1 化学分组）
- 广度优先：每污染物至少 1 个 R2 方案后推进
- Phase A 复用 R1 文件 + R2 角度扩展
- Phase A+ 预筛对 R2 新角度重新执行（含 R1-DEDUP）

### 四、质量门控

- 继承 R1 全部质量规则（GLOBAL_SPEC.md G1-G10）
- 新增 R1-DEDUP 预筛
- 通过线不变：85/100 + 零未决 critical/high + 创新性清单通过

---

## 2026-07-29 PFOA R2 广度优先 slot 1 执行

### 一、角度地图与预筛（`angle_maps/pfoa_ANGLES.yaml`）

1. 锁定 R1 已占据角度：A02（通过，脲氧阴离子洞中性氢键）+ A01/A03-A10（终止）+ A11-A26（枚举未开启）。
2. R2 新增 4 个正交候选并执行 Phase A+ 预筛（TFG/PADS/ODC/R1-DEDUP）：
   - **R2_A01 anion-π 缺电子 π 面识别**：A 级（条件性）——识别轴正交、正交维度 2、PADS 45（平台拥挤/机制空白）、TFG borderline（硫酸根反转风险）。
   - R2_A02 大环穿套动力学识别：X 级（TFG fail，ng/L 穿套动力学 + 无独立热力学锚）。
   - R2_A03 σ-空穴卤键受体：X 级（TFG fail + 生物原型门 fail）。
   - R2_A04 全氟螺旋横截面形状腔：X 级（生物原型门 fail，无自然进化刚性杆识别器，逼近 AT1 氟特异边界）。
3. **决策**：执行唯一 A 级候选 R2_A01 为 slot 1，定位机制确证型研究（E 组 S5 模式）+ Phase 0 前置门。

### 二、slot R2_S01_A01 裁决

- 轨迹：r1 62（1c/3h）→ r2 ~74（0c/1h）。
- critical（C1 anion-π 对二价硫酸根方向反转，创新层即负债层）经 r2 重构为**前置 Phase 0 决定性检验 + 清洁负结果交付**消解（同 Endosulfan/OC A04/TCDD 范式）。
- 残 1 个**角度内禀 high**（C2：NO-GO 分支剩余选择性落入 A02 已占据空间 + 正向选择性先验低），天花板诚实评估 76-80，**未达 85**。
- **verdict：revise_with_phase0_prerequisite**；Phase 0 计算门（DFT-SAPT+SMD）挂起为仓库外计算动作。

### 三、中间产物提取（每方案完成即提取）

- 原型卡片：`prototype_cards/PROTO_R2_001_flavoprotein-anion-pi.yaml`（黄素蛋白 anion-π，仿生原型库 83→84）。
- 机制映射：`mechanism_maps/pfoa_anion-pi.yaml`（MECH_pfoa_001）。
- 角度地图：`angle_maps/pfoa_ANGLES.yaml`（R2_A01 状态更新为 revise_with_phase0_prerequisite）。
- 知识图谱：`knowledge_graph.yaml` 追加 1 原型 + 1 机制 + 1 材料 + 3 边。

### 四、去向决策

- PFOA R2 正交空间接近诚实耗尽（4 候选 3 个 X 级、1 个 revise_with_phase0），与 R1 记录的机制空间本征狭窄（诚实上限 26）一致。
- Phase 0 计算门挂起（外部计算动作，同 OC A04/TCDD A01 模式）；建议轮转下一污染物 PFBS（A 组，头基/几何正交空间较宽）。
- 可传递负知识：anion-π 对单价全氟羧酸根在硫酸根背景下为潜在选择性负债——若证实，收窄全 PFAS 组 anion-π 分支设计空间。

---

## 2026-07-29 PFBS R2 广度优先 slot 1 执行

### 一、角度地图与预筛（`angle_maps/pfbs_ANGLES.yaml`）

1. 锁定 R1 已占据角度：A17（通过，头基几何反差）+ A01/A04/A05（终止）+ 19 角度枚举空间。
2. R2 新增 4 候选 Phase A+ 预筛：**R2_A01 趋液（chaotropic/Hofmeister）水合识别 × C4 尺寸窗口** 判 A 级（第六类机制轴=水合热力学）；anion-π（继承 PFOA 槽可传递负知识，硫酸根反转）/卤键/穿套均 X 级。
3. **决策**：执行唯一 A 级 R2_A01。选择趋液的关键理由：与 anion-π 方向相反，趋液效应内禀排斥 kosmotrope 硫酸根，**正面解决 PFBS 头号竞争陷阱（陷阱 4）**。

### 二、slot R2_S02_A01 裁决

- 轨迹：r1 62（2c/2h）→ r2 ~72（0c/1h）。
- 2 critical（C1 C4 短链趋液绝对亲和力不足 ng/L；C2 逆向尺寸窗口排 PFOS 不成立）经 r2：C1 转前置量热(ITC)/Phase 0 go/no-go + 清洁负结果；C2 转**适用范围声明**（主张收窄为 PFBS vs 无机含氧阴离子，放弃 PFAS 类内分离）消解。
- 残 1 角度内禀 high（C4 绝对亲和力先验低 + 主张收窄致链长维承重削弱），天花板 78-82，**未达 85**。
- **verdict：revise_with_phase0_prerequisite**；量热/Phase 0 计算门挂起。

### 三、中间产物提取

- 原型卡片 `prototype_cards/PROTO_R2_002_hofmeister-chaotropic-channel.yaml`（库 84→85）；机制映射 `mechanism_maps/pfbs_chaotropic.yaml`（MECH_pfbs_001）；角度地图更新；知识图谱 +1 原型/+1 机制/+1 材料/+3 边。

### 四、跨槽知识沉淀（PFOA↔PFBS 互补）

- **PFAS 组头基-水合识别方向一对互补知识**：anion-π（PFOA R2）偏好高电荷密度硫酸根=**选择性负债**；趋液效应（PFBS R2）偏好弱水化 PFAS、排斥硫酸根=**选择性资产**。该方向知识对后续 PFHxS/GenX 有传递价值。
- PFBS R2 正交空间同 PFOA 接近诚实耗尽；建议量热/Phase 0 挂起后轮转 PFHxS（C6 链长趋液性强于 C4，趋液路线对 PFHxS 绝对亲和力优于 PFBS，可作趋液路线链长适用性检验）。

---

## 2026-07-29 PFHxS R2 广度优先 slot 1 执行

### 一、角度地图与预筛（`angle_maps/pfhxs_ANGLES.yaml`）

1. 锁定 R1：A01（中性氢键头基，终止 70）/A07（盲腔深度窗口，终止 78）+ 13 角度枚举。**关键：R1 明确将大环腔（cucurbituril 葫芦脲/环糊精）方向列为未枚举推迟方向（未占据）**。
2. R2_A01 趋液水合 × OAT4 型 ≥C6 链长窗口双正交判 A 级；R2_A02 anion-π/R2_A03 卤键 X 级。
3. **决策**：执行 R2_A01。关键设计：用阴离子友好端口的竹环（bambusuril）规避 R1 记录的cucurbituril 端口 C=O 基对阴离子静电排斥问题；第二正交维用 OAT4 ≥C6 窗口（PFBS 恰被 OAT4 排除，此支撑 PFHxS 独有）。

### 二、slot R2_S03_A01 裁决

- 轨迹：r1 72（1c/1h）→ r2 ~82（0c/1h）。**较 PFBS（~72）显著上移**。
- 1 critical（C6 ng/L 绝对亲和力未证）经 r2 转前置量热(ITC) go/no-go 消解（C6 GO 先验高于 PFBS）。
- 残 1 角度内禀 high（原创性受 CD/CB PFAS 平台拥挤 + 趋液为 R2 第二次用封顶），天花板 82-84，**未达 85**。
- **verdict：revise_with_phase0_prerequisite**；量热(ITC) 门挂起。

### 三、中间产物提取

- 新原型卡片 `PROTO_R2_003_oat4-c6-chain-length-window.yaml`（OAT4 ≥C6 窗口，库 85→86）；机制映射 `mechanism_maps/pfhxs_chaotropic-oat4.yaml`（MECH_pfhxs_001）；角度地图；知识图谱 +1 原型/+1 机制/+4 边。

### 四、A 组诚实轨迹小结

- A 组 PFAS 三槽：PFOA ~74 / PFBS ~72 / PFHxS ~82，均 revise_with_phase0（无通过）。与 R1 一致（A 组全轮仅 PFOA A02/PFBS A17 通过，机制空间近耗尽）。趋液路线随链长上移为清晰可发表规律。
- 下一步：轮转 GenX（A 组末位，六氟环氧丙烷二聚酸（短链离域羧酸头），趋液性弱，预期趋液路线弱于磺酸）完成 A 组覆盖，随后转 D 组（BPA/NP，通过更可期）。

---

## 2026-07-30 GenX R2 广度优先 slot 1 执行（诚实角度耗尽 + 代表性终止）

### 一、角度地图与预筛（`angle_maps/genx_ANGLES.yaml`）

1. 锁定 R1：A01=36（中性氢键氧阴离子洞，全项目最低分）/A03=61（ether-O 双锚）终止 + 22 角度枚举。
2. R2 新增 3 候选**全 X 级**：趋液（TFG fail，GenX 强亲水）/anion-π（硫酸根反转 + 离域羧酸更弱）/支链形状识别（无进化原型）。
3. **决策**：GenX 为项目最难 PFAS，无可行正交角度（诚实角度耗尽）。以趋液路线为代表开 1 槽并 r1 即诚实终止（完成广度优先“≥ 1 槽尝试”）。

### 二、slot R2_S04_A01 裁决

- r1 **41 terminate**（1 critical 结构性）：趋液效应要求客体弱水化，GenX 强亲水（logKow~0.5-1.5）位于 Hofmeister kosmotrope 侧，脱水增益小、净结合弱——客体本征水化性质与识别机制根本不匹配，不可重建。GenX 不在 OAT4 底物谱（无 ≥C6 窗口第二维）。

### 三、中间产物与 A 组小结

- 机制映射 `mechanism_maps/genx_chaotropic-boundary.yaml`（MECH_genx_001，负知识）；角度地图；知识图谱 +1 机制/+1 边。无新原型（复用 PROTO_R2_002 作负结果测试）。
- **趋液路线完整适用性映射（可传递负知识）**：PFHxS(C6 疏水磺酸)~82 > PFBS(C4 磺酸)~72 > GenX(亲水酸)fail。趋液路线适用阈值约在“中等疏水性”以上。
- **A 组覆盖完成**：PFOA ~74 / PFBS ~72 / PFHxS ~82 均 revise_with_phase0；GenX 41 terminate/耗尽。与 R1 一致（A 组全轮仅 2 通过，机制空间近耗尽）。无凑数。
- **下一步：转 D 组 BPA**（R1 DmpR 锁定路线通过 86，D 组正交空间较宽，通过更可期）。
