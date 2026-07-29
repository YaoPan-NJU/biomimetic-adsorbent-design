# PFHxS R2_A01 — 隔离角色循环（设计-攻击-裁决 × 2 轮）

> 趋液（chaotropic/Hofmeister）水合识别 × OAT4 型 ≥C6 链长窗口。角色隔离持久化。

---

## 设计者 r1

**有界输入**：`rounds/fresh_1000/pfhxs/BRIEF.md`、`angle_maps/pfhxs_ANGLES.yaml`（R2_A01）、`GLOBAL_SPEC.md`、`INNOVATION_CHECKLIST.md`、`R1_OCCUPIED_SPACE.yaml`、PROTO_R2_002。

**科学问题**：PFHxS（C6 磺酸根，单项 MCL 10 ng/L，斯德哥尔摩附件 A）在 mM 硫酸根背景下的选择捕获。R1 A01（中性氢键头基）水相弱、A07（盲腔深度窗口）单轴天花板。能否以 **趋液水合轴（排斥硫酸根）× OAT4 型 ≥C6 链长窗口（优先 PFHxS 于短链 PFBS）** 双正交实现？

**工程难题**：构建阴离子友好端口（竹环，非葫芦脲羰基端口）的高能水释放受限腔，趋液优先纳弱水化 PFHxS、排斥强水化二价硫酸根，且腔深以 OAT4 型 ≥C6 阈值优先 PFHxS 于 PFBS。

**生物原型（诚实转译距离）**：(1) 生物阴离子通道 Hofmeister 序选择性（PROTO_R2_002，趋液水合轴）；(2) OAT4 转运 PFHxS 而排除 PFBS（Louisse 2023，≥C6 链长窗口轴）——**PFBS 恰被 OAT4 排除，故该 ≥C6 支撑为 PFHxS 独有**（PFBS R2 无此支撑）。转译距离：通道功能为通透调制、OAT4 为肾重吸收转运，非水相选择捕获；C 维诚实类比级。

**双正交机制**：轴 1 趋液水合门（高能水释放竹环腔优先纳弱水化 PFHxS、内禀排斥强水化 SO₄²⁻，正面解决陷阱 4）；轴 2 OAT4 型 ≥C6 链长窗口（腔深/端口优先 PFHxS 于短链 PFBS）。两轴正交（水合 vs 几何/链长）。C6 绝对亲和力显著优于 PFBS 的 C4（趋液性/疏水面积随链长增）。

**材料**：竹环（bambusuril，脲基/硫代端口阴离子友好）型高能水释放腔，腔深匹配 ≥C6，接枝多孔载体。

**因果对照**：Hofmeister 序滴定（选择性随趋液性单调、随电荷密度反相关）；C4/C6/C8 链长系列（证 ≥C6 窗口：PFBS 低、PFHxS/PFOS 高）；SO₄²⁻/PO₄³⁻/Cl⁻ 竞争；ITC 焓-熵分解（高能水释放熵驱动）。

**创新自评**：A 通过（趋液水合 × OAT4 窗口双识别超越普通疏水/静电/尺寸）；B 条件性（竹环平台已存）；C 不通过（诚实，原型功能非吸附）；D 通过（趋液 × 链长窗口 2 正交维，各有生物原型）；E 条件性（大环腔 R1 明确推迟为未占据，竹环阴离子端口 + OAT4 窗口为增量，但 CD/CB PFAS 平台拥挤）。

**弱点自报**：(1) C6 绝对 Ka 虽优于 C4 但仍须量热确认达 ng/L 占位阈值；(2) 趋液偏好更长 PFOS（co-capture，两者均管制可接受，非致命）；(3) 原创性受 CD/CB PFAS 平台拥挤 + 趋液为 R2 第二次用（PFBS）压制。

---

## 攻击者 r1

**C1（critical，降 high 待回应）——C6 ng/L 绝对亲和力未经证实**。趋液 host-guest 对 C6 PFAS 的 Ka 虽高于 C4，但文献 CD/CB 对 PFAS 的 Ka 多在 10³–10⁵ M⁻¹（mg/L–µg/L 尺度测定）；ng/L（约 25 pM）占位需材料侧有效分布系数极高（多价/聚合物放大）。绝对亲和力充分性未证，须量热(ITC)确认。

**H1（high）——原创性受平台拥挤 + R2 内趋液重复压制**。CD/CB 主客体 PFAS 已密集（Kancharla 2022、Wei 2024、Verma 2022 PFBS）；趋液原理为 R2 第二次使用（PFBS R2_A01）。增量须以竹环阴离子端口 + OAT4 ≥C6 窗口 + Hofmeister 因果对照的 PFHxS 特异组合精确界定，否则原创性维受限。

**H2（high，降 medium）——PFOS co-capture 削弱类内选择性主张**。趋液偏好更长 PFOS，材料对 PFOS 结合强于 PFHxS，无法在 PFHxS/PFOS 间分离。降 medium：PFHxS/PFOS 均受管制（附件 A、单项 MCL），co-capture 于工程可接受，主张为"≥C6 PFAS vs 无机 + vs 短链 PFBS"成立。

**M**：C 维原型类比（通道/OAT4 功能非吸附）；竹环水相合成/可及性；ng/L 传质。

**攻击结论**：1 critical（C6 绝对亲和力未证）+ 1 high（原创性）。较 PFBS 显著改善（PFBS 有 2 critical：C4 亲和力 + 逆向窗口；PFHxS 的 C6 亲和力上移且 OAT4 窗口方向正确无逆向问题）。须量热 go/no-go 消解 C1。

---

## 裁决者 r1

| 攻击项 | 裁决 |
|---|---|
| C1 C6 绝对亲和力 | critical。C6 优于 C4 但 ng/L 充分性未证，须量热确认。 |
| H1 原创性 | high。平台拥挤 + 趋液 R2 重复，增量须精确界定。 |
| H2 PFOS co-capture | medium（两者均管制，co-capture 可接受）。 |

**评分 r1**：因果闭环 15 / 选择性机制 16 / 转译 15 / 原创 9 / 可证伪 9 / 证据 8 = **72/100**。**verdict：revise，1 critical + 1 high。**

诚实预判：较 PFBS（r1 62，2 critical）显著改善——C6 亲和力上移 + OAT4 ≥C6 窗口方向正确（PFBS 缺此且被 OAT4 排除）。r2 转量热 go/no-go 消解 C1 后，天花板 80-84；通过 85 仍受原创性（平台拥挤）与 ng/L 绝对亲和力先验压制。

---

## 设计者 r2（回应台账）

**C1（→ 前置量热 go/no-go）**：不主张 C6 绝对亲和力充分为通过前置，改为量热(ITC)决定性检验：测竹环腔对 PFHxS 的绝对 Ka 与焓-熵分解（验高能水释放熵驱动）+ α(PFHxS/SO₄²⁻)。GO：Ka(C6) 达 ng/L 占位阈值（多价材料格式）且 α(PFHxS/SO₄²⁻)≥10²。诚实：C6 先验优于 C4（趋液性随链长增），GO 概率高于 PFBS 但仍须实测。NO-GO 交付清洁负结果（界定趋液路线链长阈值在 C6 附近）。

**H1（→ 原创性增量精确界定）**：增量三点——(a) 竹环脲基/硫代阴离子友好端口（规避葫芦脲羰基排阴离子，R1 明确推迟大环方向的具体化解决）；(b) OAT4 型 ≥C6 链长窗口的材料转译（PFBS 恰被 OAT4 排除，此支撑 PFHxS 独有）；(c) Hofmeister 序滴定因果对照分离趋液分量。三点可实验量化，非载体替换。

**H2（→ 主张定位）**：主张定位为"≥C6 PFAS（PFHxS/PFOS）vs 无机含氧阴离子 + vs 短链 PFBS"；PFHxS/PFOS 类内分离不作主张（co-capture 工程可接受，两者均管制）。

**四结果框架**：M1 竹环腔对 C6 达 ng/L 选择捕获（vs 硫酸根 α≥10²、vs PFBS ≥C6 窗口成立）/ M2 温和 / F1 C6 亲和力不足如期证伪（界定趋液链长阈值）/ F3 选择性存在但源自疏水非趋液（Hofmeister 序错向）。

---

## 裁决者 r2

| 项 | r2 裁决 |
|---|---|
| C1 C6 绝对亲和力 | critical→解除（转前置量热 go/no-go + 清洁负结果，同 Endosulfan/OC/TCDD 范式；C6 GO 先验高于 PFBS） |
| H1 原创性 | 部分闭合，留 1 high（增量三点精确界定，但 CD/CB PFAS 平台拥挤 + 趋液 R2 第二次用，原创性封顶，角度内禀） |
| H2 PFOS co-capture | medium 闭合（主张定位 ≥C6 vs 无机 + vs PFBS） |

**评分 r2**：因果闭环 16 / 选择性机制 17（趋液排硫酸根 + OAT4 ≥C6 窗口双正交，方向全正确，co-capture 可接受）/ 转译 15 / 原创 10（大环腔 R1 推迟为未占据 + 竹环阴离子端口 + OAT4 窗口增量，但平台拥挤 + 趋液重复封顶）/ 可证伪 9 / 证据 8 = **~82/100（区间 80-84）**。

**verdict：revise_with_phase0_prerequisite；~82（区间 80-84）；0 critical / 1 high（原创性受 CD/CB PFAS 平台拥挤 + 趋液 R2 重复封顶，角度内禀）。未达 85。**

- 天花板诚实评估 82-84：较 PFBS（~72）显著上移（C6 亲和力 + OAT4 ≥C6 窗口独有支撑 + 无逆向窗口问题 + 无主张收窄）；但 ng/L 绝对亲和力量热未证 + 原创性受平台拥挤封顶为角度内禀，非文本可闭合至 85。
- 外部前置：量热(ITC) go/no-go（C6 绝对 Ka + α(PFHxS/SO₄²⁻)），C6 GO 先验高于 PFBS。
- 残余价值：**趋液路线链长适用性系列 C4(PFBS ~72)→C6(PFHxS ~82) 的定量进阶**（可传递正知识：趋液路线在 ≥C6 显著改善，链长阈值约在 C6 附近；OAT4 ≥C6 窗口为 ≥C6 PFAS 的独有第二正交维）；对 PFOS（C8）预期更优，但 PFOS 不在本轮 20 污染物清单。
