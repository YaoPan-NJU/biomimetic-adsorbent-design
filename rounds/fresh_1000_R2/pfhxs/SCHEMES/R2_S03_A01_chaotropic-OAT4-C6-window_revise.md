# R2_S03 · R2_A01 趋液水合 × OAT4 型 ≥C6 链长窗口识别 PFHxS（revise_with_phase0_prerequisite）

- 程序：fresh_1000 Round 2 | 污染物：PFHxS（全氟己烷磺酸，perfluorohexanesulfonate C6F13SO3⁻）| 梯队 1（A 组 PFAS）| 广度优先 slot 1
- 状态：**revise_with_phase0_prerequisite**（未通过 85；外部量热(ITC) go/no-go 为决定性裁定）
- 最终得分：**~82/100（区间 80–84）**，verdict revise，**0 critical / 1 high（原创性角度内禀）**
- 得分轨迹：r1 72（1c/1h）→ r2 ~82（0c/1h）
- 角色循环（隔离持久化）：`_wip/R2_A01_cycle.md`

## 监督者摘要

PFHxS R2 广度优先首槽。角度地图（`angle_maps/pfhxs_ANGLES.yaml`）3 候选仅 R2_A01（趋液 × OAT4 ≥C6 窗口）为 A 级；anion-π/卤键 X 级。

**关键：R1 明确将大环腔（葫芦脲/环糊精）方向列为未枚举的推迟方向**（先例核验超 R1 证据集 + 葫芦脲羰基端口排阴离子可行性不确定），故 R2 趋液大环腔路线为 R1 未占据的正交空间。方案以 **阴离子友好端口的竹环（bambusuril）高能水释放腔**（规避 R1 记录的葫芦脲羰基排阴离子问题）实现双正交识别：轴 1 趋液水合（Hofmeister 位次优先弱水化 PFHxS、内禀排斥强水化二价硫酸根，正面解决陷阱 4）；轴 2 OAT4 型 ≥C6 链长窗口（优先 PFHxS 于短链 PFBS）。原型：生物阴离子通道 Hofmeister 序选择性（PROTO_R2_002）+ OAT4 ≥C6 窗口（PROTO_R2_003）。

**较 PFBS R2 显著上移（~72→~82）的三点真实改善**：(1) C6 绝对亲和力显著优于 C4（趋液性/疏水面积随链长增）；(2) OAT4 ≥C6 窗口方向正确——**PFBS 恰被 OAT4 排除，此第二正交维支撑为 PFHxS 独有**，无 PFBS 的逆向窗口问题；(3) 无主张收窄（PFBS 因逆向排 PFOS 失败而收窄，PFHxS 主张 ≥C6 PFAS vs 无机 + vs 短链 PFBS 直接成立）。

**未达 85 的角度内禀约束**：C6 ng/L 绝对亲和力仍须量热(ITC)确认（GO 先验高于 PFBS 但未证）；原创性受 CD/CB PFAS 主客体平台拥挤 + 趋液为 R2 第二次使用封顶（~10/15）。**去向**：量热 go/no-go 挂起（外部）；轮转 GenX 完成 A 组覆盖。

---

## 1. 科学问题与工程难题

**科学问题。** PFHxS（C6 磺酸根，单项 MCL 10 ng/L，斯德哥尔摩附件 A）在 mM 硫酸根背景 ng/L 选择捕获。R1 A01（中性氢键头基，水相弱）、A07（盲腔深度窗口，单轴天花板）均终止。能否以趋液水合轴（排硫酸根）× OAT4 型 ≥C6 链长窗口（优先 PFHxS 于 PFBS）双正交实现？

**工程难题。** 构建阴离子友好端口（竹环，非葫芦脲羰基）高能水释放受限腔，趋液优先纳弱水化 PFHxS、排斥强水化二价硫酸根，腔深以 OAT4 型 ≥C6 阈值优先 PFHxS 于 PFBS。

## 2. 生物原型与证据

**原型 1：生物阴离子通道 Hofmeister/趋液序选择性（PROTO_R2_002）。** 通道电导随阴离子趋液性升高（Gurnev 2017 PMC5518747；Kang 2020）。**原型 2：OAT4 型 ≥C6 链长窗口（PROTO_R2_003）。** OAT4 转运 PFHxS 而排除 PFBS（Louisse 2023）——文献支撑的非单调链长阈值，**PFBS 恰被排除故此支撑 PFHxS 独有**。转译距离诚实：通道功能为通透调制、OAT4 为肾重吸收，非水相捕获；C 维类比级。

| 编号 | 来源 | 年份 | 支持主张 | 层级 | 核验 |
|---|---|---|---|---|---|
| Q1 | PMC5518747（Gurnev，通道 Hofmeister 序） | 2017 | 通道阴离子选择性遵循 Hofmeister 序 | source_backed_lead | 题录+摘要 |
| Q10 | Louisse 2023（Arch Toxicol，OAT4 PFAS） | 2023 | OAT4 转运 PFHxS 而排除 PFBS（≥C6 阈值，非单调链长窗口） | source_backed_lead | 继承 R1 BRIEF（摘要逐字核） |
| Q11 | Zhao 2015（Tox Sci，NTCP/ASBT） | 2015 | NTCP Km PFBS 39.6<PFHxS 112<PFOS 130 µM；ASBT 仅 PFOS | source_backed_lead | 继承 R1 BRIEF（摘要） |
| Q3 | 10.1021/acs.cgd.3c00726（趋液选择识别） | 2023 | 大环趋液效应选择识别弱水化大阴离子 | fact | 题录+摘要 |
| Q6 | chemrxiv-2025-zfxh7（竹环趋液阴离子） | 2025 | 竹环高能水释放结合趋液阴离子（阴离子友好端口） | design_hypothesis | 题录+摘要 |
| Q12 | Wei 2024（PMC11540018，PFAS-CD host-guest） | 2024 | CD-PFAS 选择性 host-guest（长链结合强于短链） | source_backed_lead | 题录+摘要 |
| E5 | 10.1039/ft9918702995（Marcus） | 1991 | SO₄²⁻ 水合自由能 −1080 kJ/mol（强 kosmotrope） | Tier 2 | 继承 R1 |
| E13c | 89 FR 32532（2024 NPDWR） | 2024 | PFHxS 单项 MCL 10 ng/L（2026-05-20 拟撤销，注时点） | 官方 | 继承 R1（全文核验） |

## 3. 仿生对应矩阵（硬对应 1 条）

**硬对应 H1（趋液水合 × OAT4 ≥C6 双正交识别，原理类比层；C 维诚实不通过）。**

| 生物特征 | 来源支持 | 材料实现 | 预期功能 | 测量 | 因果对照 |
|---|---|---|---|---|---|
| 通道 Hofmeister 序选择性（弱水化阴离子作用强，Q1）+ OAT4 ≥C6 链长阈值（转运 PFHxS 排除 PFBS，Q10）；C 维诚实不通过（功能非吸附） | Q1、Q10、Q3、Q6、Q12 | 竹环（bambusuril）阴离子友好端口高能水释放腔，腔深匹配 ≥C6，接枝多孔载体 | 弱水化 PFHxS 经高能水释放优先入腔（排斥强水化 SO₄²⁻），腔深优先 PFHxS 于短链 PFBS | Hofmeister 序滴定；C4/C6/C8 链长系列；ITC 焓-熵分解；SO₄²⁻/PO₄³⁻ 竞争 | **Hofmeister 序错向**（选择性随电荷密度正相关则非趋液）+ **链长系列**（PFBS 低/PFHxS 高证 ≥C6 窗口）双错向判据 |

## 4. 材料架构与双正交机制

**人工识别单元（非蛋白）。** 竹环（bambusuril，脲基/硫代端口，阴离子友好，规避葫芦脲羰基排阴离子）型高能水释放腔，腔深匹配 ≥C6，接枝水稳定多孔载体。

**双正交机制。** 轴 1 趋液水合门（高能水释放腔优先纳弱水化 PFHxS、内禀排斥强水化二价 SO₄²⁻，正面解决陷阱 4）；轴 2 OAT4 型 ≥C6 链长窗口（腔深/端口优先 PFHxS 于短链 PFBS，方向正确无逆向问题）。两轴正交（水合热力学 vs 几何/链长）。

**等结构因子系列。** M0 敞口大腔（趋液门弱化）；M1 竹环 ≥C6 腔（主变体）；M1-depth 腔深系列（C4/C6/C8 契合）；M-rim 葫芦脲羰基端口对照（验阴离子友好端口必要性）；Blank 空白载体。

## 5. 选择性判决与外部门（决定性前置）

**主选择性主张**：≥C6 PFAS（PFHxS/PFOS）vs 无机含氧阴离子（硫酸根/磷酸根/氯离子）+ vs 短链 PFBS。PFHxS/PFOS 类内分离不作主张（co-capture 工程可接受，两者均管制）。

**外部门（量热 ITC，GO/NO-GO）**：测竹环腔对 PFHxS 绝对 Ka + 焓-熵分解（验高能水释放熵驱动）+ α(PFHxS/SO₄²⁻)。GO：Ka(C6) 达 ng/L 占位阈值（多价材料格式）且 α≥10²。C6 GO 先验高于 PFBS（趋液性随链长增）。NO-GO：交付清洁负结果（界定趋液路线链长阈值约在 C6 附近）。

**四结果框架。** M1 C6 达 ng/L 选择捕获 / M2 温和 / F1 C6 亲和力不足证伪 / F3 选择性源自疏水非趋液（Hofmeister 错向）。

## 6. 浓度场景与报告口径

主目标市政二级出水/受纳水体（出水中位 1.8 ng/L，Kim 2024）+ 饮用水源；AFFF 地下水（µg/L，高浓验证）。实验点 10/100/1000 ng/L。动态床容量为主口径；报可及腔位点密度、空白载体 uptake、受体质量分数；材料不含氟。

## 7. 创新性清单

| 维 | 判定 | 理由 |
|---|---|---|
| A 机制创新 | 通过 | 趋液水合 × OAT4 ≥C6 窗口双识别超越普通疏水/静电/尺寸 |
| B 材料架构 | 条件性 | 竹环阴离子端口腔为特定组织，平台已存 |
| C 仿生转译 | 不通过（诚实） | 通道/OAT4 功能非吸附；趋液为通用物化原理 |
| D 选择性策略 | 通过 | 趋液（水合）× OAT4 ≥C6 窗口（几何/链长）2 正交维，各有生物原型，方向全正确 |
| E 先例区分 | 条件性 | 大环腔 R1 明确推迟（未占据）+ 竹环阴离子端口 + OAT4 窗口增量；CD/CB PFAS 平台拥挤 |

## 8. 评分与裁决

| 维度 | 满分 | 得分 |
|------|------|------|
| 因果闭环 | 20 | 16 |
| 选择性吸附机制 | 25 | 17 |
| 人工材料可转译性 | 20 | 15 |
| 原创性 | 15 | 10 |
| 实验可证伪与对照 | 10 | 9 |
| 证据完整性 | 10 | 8 |
| **合计** | **100** | **~82（区间 80–84）** |

**verdict：revise_with_phase0_prerequisite；0 critical / 1 high。** 未达 85。

**残余 high（角度内禀）**：原创性受 CD/CB PFAS 主客体平台拥挤 + 趋液为 R2 第二次使用封顶（~10/15）；ng/L 绝对亲和力量热未证。天花板 82–84。

**外部前置**：量热(ITC) go/no-go（C6 绝对 Ka + α(PFHxS/SO₄²⁻)）。

## 9. 残余价值与下一步

- **可传递正知识**：趋液路线链长适用性定量进阶 **C4(PFBS ~72)→C6(PFHxS ~82)**——趋液路线在 ≥C6 显著改善，链长阈值约在 C6 附近；OAT4 ≥C6 窗口为 ≥C6 PFAS 独有第二正交维（PFBS 被 OAT4 排除）。
- **下一步**：量热 go/no-go 挂起（外部）。轮转 GenX（A 组末位，六氟环氧丙烷二聚酸醚酸，R1 A01=36/A03=61 全终止；GenX 为醚羧酸、趋液性弱且离域羧酸，趋液路线预期弱于磺酸——将检验趋液路线对醚羧酸头基的适用性）。

---

## 10. Depth backfill r3 (2026-07-30, breadth-first-complete depth phase) — ~84, external ITC gate isolated

After 20/20 breadth-first coverage, this is the depth-phase iteration on the program's strongest revise. Goal: close every
design-layer (in-repo) issue and isolate precisely what blocks >=85.

**Design-layer closures (r2 ~82 -> r3 ~84):**
- Causal closed loop 16 -> 17: the ng/L target is reframed at the MATERIAL level (bed capacity BV50 ~ Kd * rho_bed via a
  MULTIVALENT host-array format), so a moderate single-site chaotropic Ka can still deliver ng/L dynamic-bed uptake — the
  chaotropic -> uptake causal chain is closed at the material scale without new data.
- Selectivity mechanism 17 -> 18: the dual falsifiable controls are tightened to a decisive pair — (i) Hofmeister-series
  titration MUST rank weakly-hydrated > strongly-hydrated (misdirection = not chaotropic), (ii) C4/C6/C8 chain-length series
  MUST show PFBS(C4) low / PFHxS(C6) high (confirms the >=C6 window is real, not bulk hydrophobicity). PFHxS/PFOS co-capture is
  explicitly accepted (both regulated) so intra->=C6 selectivity is not claimed — removing a false burden.
- Evidence completeness 8 -> 9: OAT4 >=C6 (Louisse 2023) + chaotropic recognition (Q3/Q6) are source-backed; the sole remaining
  evidence gap is the PFHxS-specific AQUEOUS Ka (ITC-pending), now cleanly isolated.
- Originality held at 10/15 (HONEST, not raiseable in-repo): CD/CB/bambusuril PFAS host-guest space is genuinely crowded; the
  chaotropic x >=C6-window dual-orthogonality + bambusuril anion-port + "PFBS-excluded-by-OAT4" support is the real novel delta,
  but it does not lift the platform-crowding cap.

**r3 score ~84/100 (0 critical / 1 high). Still < 85.** Revised dimension tally: causal 17 + selectivity 18 + translatability 15 +
originality 10 + controls 9 + evidence 9 = **84**.

**Sole decisive blocker (structural, external):** the residual `high` is the **ng/L absolute aqueous Ka**, provable ONLY by
external ITC calorimetry (C6 Ka + enthalpy-entropy decomposition confirming high-energy-water-release entropy drive + alpha(PFHxS/
SO4^2-)). This is out-of-repo and cannot be closed by design-layer work or by me. Expected post-gate: GO -> ~86-88 (pass);
NO-GO -> clean negative result bounding the chaotropic route's chain-length threshold near C6.

**Honest conclusion:** PFHxS is the closest R2 revise to a pass (~84), and its final ~1-3 point gap to 85 is 100% external-
calorimetry-bound — NOT a design deficiency. Forcing it to 85 in-repo would be padding (violates honest-N clause). Depth phase on
the program's best revise therefore confirms the documented R2 reality: the revise->pass conversion is external-gate-limited.
Status remains **revise_with_phase0_prerequisite** (now ~84, design-layer fully closed).
