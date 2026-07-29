# beta-HCH 执行 Spec：六氯环己烷仿生选择性吸附设计

> 版本：v1.0 | 日期：2026-07-29 | 状态：待执行

---

## 1. 简报锁定

> 继承 `betahch/BRIEF.md`，以下为核心参数摘要。

### 1.1 分子身份

| 参数 | 值 |
|------|-----|
| 名称 | β-六氯环己烷（β-HCH） |
| CAS | 319-85-7 |
| 分子式 | C₆H₆Cl₆ |
| MW | 290.83 g/mol |
| logKow | ~5（异构体实验值须回溯 Willett 1998 ES&T） |
| 构型 | 全平伏 eeeeee，D3d 对称，无手性 |
| 电荷 | 恒中性（pH 0–14），无可电离基团、无氢键供受体 |
| 监管 | Stockholm 公约附件 A（COP-4 SC-4/11，2009），无豁免 |

### 1.2 环境存在

- **来源**：全部来自工业 HCH/林丹生产副产物（每吨林丹产 6–10 吨其他异构体废物），水相赋存为遗留废物淋溶与老化残留
- **持久性**：四异构体中最稳定（全平伏氯锁死脱氯化氢与碱性消除），老化后成为环境主导异构体
- **去除序**：α = γ = δ > β = ε（β-HCH 最难去除，Černík 2024）

### 1.3 难去除机制（四维度）

1. **几何稳定性与消除路径锁死**：全平伏六氯构型不含反式双直立 H-Cl 对，锁死 LinA 脱氯化氢（需 1,2-双直立 HCl）与碱性消除（被迫 syn 消除，反应性四异构体最低）
2. **识别把手全面缺失**：静电/酸碱/氢键三把手全部不可用；四异构体同分子式/同分子量/logKow 3.6–4.1，唯一差异为氯原子轴向/平伏排布
3. **微量驱动力与传质**：水溶度 mg/L 级、环境浓度 ng/L–µg/L，传质驱动力极小
4. **无电荷把手的再生困境**：恒中性分子无 pH 摆动再生把手，热处置有 PCDD/F 与氯苯二次污染风险

### 1.4 水质场景与浓度区间

| 场景 | 浓度范围 | 典型值 | 来源 | 是否主目标 |
|------|---------|--------|------|-----------|
| 点源高浓度（林丹填埋渗滤液） | mg/L 级 | — | De Carluccio 2024 | 否（工程修复对象） |
| 历史场地影响区地下水 | µg/L–低 mg/L | 数十 µg/L | Černík 2024; Xu 2023 | **主目标** |
| 一般地下水（中国全国尺度） | >1 µg/L 占 7.14% | — | Li 2026 | **主目标** |
| 地表水一般流域/饮用水源 | ng/L–低 µg/L | β-HCH 为优势 HCH 异构体 | Zhang 2026; Jin 2019 | **主目标** |
| 饮用水（产粮市镇） | ~2 µg/L | 超美国 MCL 一个数量级 | Panis 2022 | 验证场景 |
| 市政二级出水 | 中低频率、近检测限 | — | Katsoyiannis 2004 | 可选验证 |
| 背景海水 | pg/L 级 | — | Wong 2011 | 可选外部验证 |

**建议实验浓度三点**：低点 5–50 ng/L；中点 100–500 ng/L；高点 2–5 µg/L。ng/L 级需 Kd ~10⁴ L/kg。

---

## 2. 角度地图锁定

> 继承 `betahch/DESIGN_SPACE.md`，21 个角度完整列表。

| 角度 | 原型家族 | 识别机制轴 | 材料架构轴 | 先例风险 |
|------|---------|-----------|-----------|---------|
| A01 | PF1 环糊精主客体 | M5 主客体包合形状选择 | AR1 交联 CD 聚合物 | medium |
| A02 | PF1 环糊精主客体 | M5 主客体包合形状选择 | AR9 CD 接枝介孔硅 | medium |
| A03 | PF1 环糊精主客体 | M5 主客体包合形状选择 | AR10 CD 复合膜 | medium |
| A04 | PF1+PF3 CD+钴啉 | M5+M6 包合+还原脱氯 | AR1 双功能交联聚合物 | low |
| A05 | PF2 LinB 腔 | M1 范德华形状互补 | AR2 MIP（非功能单体） | medium |
| A06 | PF2 LinB+σ-hole | M1+M3 形状+卤键 | AR2 MIP（N-杂环功能单体） | medium |
| A07 | PF2 LinB/DhlA | M1+M4 形状+NH···Cl 弱氢键 | AR2 MIP（脲/硫脲功能单体） | medium |
| A08 | PF2 LinB 腔 | M1+M2 形状+偶极读出 | AR3 COF（极性节点） | low |
| A09 | σ-hole 原理 | M3 C-Cl σ 孔卤键 | AR3 COF（三嗪节点） | low |
| A10 | PF6 LinA 负参照 | M8 尺寸/形状排阻（负选择） | AR4 超交联聚合物 HCP | low |
| A11 | PF2 LinB 腔 | M1 范德华形状互补 | AR4 HCP（本征微孔） | low |
| A12 | PF2 LinB/DhlA | M1+M4 形状+NH···Cl 预组织 | AR6 离散分子笼 | low |
| A13 | PF2 LinB 水解腔 | M7 水解 SN2 置换 | AR6 分子笼（羧酸根/广义碱） | low |
| A14 | PF3 Dehalobacter | M6 还原脱氯（电化学） | AR8 电化学活性电极 | medium |
| A15 | PF3 Dehalobacter | M6 还原脱氯（化学还原） | AR7 碳载钴啉+ZVI | medium |
| A16 | PF3 Dehalobacter | M6 还原脱氯（结构钴节点） | AR5 水稳定 Co-MOF | low |
| A17 | PF4 颗粒污泥互养 | M9+M6 疏水预捕获+还原 | AR11 核壳结构 | low |
| A18 | PF5 MLP 疏水口袋 | M9 非特异疏水分配 | AR7 生物炭/木质素 | high |
| A19 | PF1+PF8 CD+表面活性素 | M5+M10 包合+界面增溶 | AR9 CD 接枝+生物表面活性素 | low |
| A20 | PF2 LinB 腔 | M2 偶极/四极静电读出 | AR3/AR6 极性 COF/分子笼 | low |
| A21 | PF2 LinB 腔 | M1+M4 形状+Zr-OH···Cl | AR5 水稳定 Zr-MOF | low |

---

## 3. 角度预分类（S/A/B/X）

对每个角度执行 TFG/PADS/ODC 三道快速预筛。

### 3.1 预筛详情

#### A01 γ-CD 交联聚合物包合树脂

```yaml
angle_id: A01
tfg:
  conclusion: fail
  note: "CD 包合对 β-HCH 水相 Ka 不确定（1–10³ M⁻¹ 假设域），Kd 上限约 0.2–600 L/kg，低于 ng/L 工况需求 ~10⁴ L/kg 达 1.2–4.7 个数量级。S29 已实证终止（r4=67），热力学标尺确认。"
pads:
  score: 35
  direct: 0
  directional: 2
  platform: 5
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["主客体包合形状选择"]
  monotonic_risk: high
verdict: X
override_reason: "S29 已实证终止（4 轮 65–67 分 plateau），热力学上限结构性不可逾越。保留为角度耗尽记录。"
```

#### A02 CD 接枝介孔硅表面包合

```yaml
angle_id: A02
tfg:
  conclusion: fail
  note: "与 A01 同机制（M5 包合），Ka 上限相同。传质体制改善（表面可及 vs 体相扩散）不改变热力学上限。"
pads:
  score: 35
  direct: 0
  directional: 2
  platform: 5
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["主客体包合形状选择"]
  monotonic_risk: high
verdict: X
override_reason: "同 A01 热力学上限。架构变体（接枝 vs 交联）不构成机制可区分角度。"
```

#### A03 CD 选择性层复合膜

```yaml
angle_id: A03
tfg:
  conclusion: fail
  note: "同 A01 机制，膜工艺耦合包合不改变包合热力学上限。"
pads:
  score: 38
  direct: 0
  directional: 2
  platform: 6
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["主客体包合形状选择"]
  monotonic_risk: high
verdict: X
override_reason: "同 A01。CD 膜工艺为架构变体，不独立开槽。"
```

#### A04 CD-钴啉双功能包合-还原

```yaml
angle_id: A04
tfg:
  conclusion: borderline
  note: "CD 包合捕获（弱）+ 钴啉还原破坏。CD 维 Ka 上限同 A01；还原维对 β-HCH 速率极慢（T6）。双功能组合的首次性提供 novelty，但热力学可行性受 CD 弱包合与还原慢速率双重限制。"
pads:
  score: 20
  direct: 0
  directional: 0
  platform: 2
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["包合形状选择", "还原脱氯"]
  monotonic_risk: low
verdict: B
override_reason: "CD 包合维热力学上限同 A01（fail 级），但还原破坏维提供不可逆驱动，整体架构为捕获-破坏一体化（非平衡选择性）。风险极高但机制新颖，保留为 S/A 失败后的探索候选。"
```

#### A05 β-HCH 形状 MIP（非功能单体）

```yaml
angle_id: A05
tfg:
  conclusion: pass
  note: "范德华形状互补在水相中可行，去溶剂化代价对中性疏水分子相对较低。MIP 空腔对 β-HCH 盘状轮廓的再结合可测。"
pads:
  score: 30
  direct: 0
  directional: 1
  platform: 2
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["范德华形状互补"]
  monotonic_risk: high
verdict: B
override_reason: "单维度（形状）落入 GC3 双维度正交硬约束不通过。MIP 形状排阻为非特异机制（CT3）。须与 A06/A07 配对解耦。"
```

#### A06 形状+卤键双维 MIP（N-杂环功能单体）

```yaml
angle_id: A06
tfg:
  conclusion: borderline
  note: "卤键维：脂肪族 C-Cl σ 穴弱于芳基氯（T3），多价弱卤键在水相中的净焓增益为核心科学问题。形状维可行。组合净效应不确定但可测。"
pads:
  score: 15
  direct: 0
  directional: 1
  platform: 1
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["形状互补", "C-Cl σ 孔卤键"]
  monotonic_risk: low
verdict: A
override_reason: "卤键水相削弱为真实风险（T3），但双维度正交性成立，先例密度低（G8 卤键/σ-hole 从未作为水相 HCH 吸附设计原理），与 A05 配对可解耦两维贡献。"
```

#### A07 形状+弱氢键双维 MIP（脲/硫脲功能单体）

```yaml
angle_id: A07
tfg:
  conclusion: borderline
  note: "NH···Cl 弱氢键在水相中竞争力存疑（Schneider 2009 水相氢键净收益常仅数 kJ/mol）。但 β-HCH 六平伏 Cl 提供 6 个潜在作用位点，多价加和或可产生可测焓增益。"
pads:
  score: 15
  direct: 0
  directional: 0
  platform: 1
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["形状互补", "N-H···Cl 弱氢键"]
  monotonic_risk: low
verdict: A
override_reason: "与 A06 机制正交（A06 中 Cl 为亲电端 σ 穴，A07 中 Cl 为亲核端孤对电子），DhlA 卤化物稳定穴为生物先例。水相弱氢键竞争力为核心风险，但双维度成立、先例密度低。"
```

#### A08 β-HCH 形状预组织 COF 腔（形状+偶极读出）

```yaml
angle_id: A08
tfg:
  conclusion: borderline
  note: "形状维可行。偶极维：β-HCH D3d 近零偶极 vs α/γ-HCH 有限偶极为真实物理差异，但水相中高介电常数强烈屏蔽静电贡献，量级极小。"
pads:
  score: 10
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["形状互补", "偶极/四极矩读出"]
  monotonic_risk: low
verdict: S
override_reason: "MOF/COF 水相 HCH 捕集零先例（G6），先例密度极低。双维度正交（几何+静电），COF 有序孔道可设计性高。偶极维水相贡献量级为核心科学问题，但可行性风险不阻塞。"
```

#### A09 三嗪节点 COF σ 孔读出

```yaml
angle_id: A09
tfg:
  conclusion: borderline
  note: "脂肪族 C-Cl σ 穴极弱（T3），三嗪 N 阵列作为 σ 穴受体的多价弱卤键在水相中的净焓增益高度不确定。"
pads:
  score: 10
  direct: 0
  directional: 1
  platform: 2
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["C-Cl σ 孔卤键"]
  monotonic_risk: high
verdict: B
override_reason: "单维度（卤键）不满足 GC3 双维度要求。脂肪族 C-Cl σ 穴极弱，水相中可能无法产生可测选择性。但先例密度极低（G8），保留为机制探索候选。"
```

#### A10 孔径筛分超交联聚合物（负选择）

```yaml
angle_id: A10
tfg:
  conclusion: pass
  note: "尺寸排阻为熵驱动机制，水相中可行。β-HCH 全平伏盘状截面最小（~7 Å），含轴向氯异构体截面更大。"
pads:
  score: 10
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["尺寸/形状排阻"]
  monotonic_risk: high
verdict: B
override_reason: "单维度（尺寸排阻）不满足 GC3。β-HCH 与 α-HCH 有效截面差异可能 <1 Å，分子筛效应是否可测为核心风险。负选择概念（排除竞争物而非捕获目标物）为独特策略。"
```

#### A11 形状互补超交联聚合物（正选择）

```yaml
angle_id: A11
tfg:
  conclusion: pass
  note: "范德华形状互补在水相中可行，HCP 本征微孔腔体与 β-HCH 盘状轮廓最大接触。"
pads:
  score: 10
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["范德华形状互补"]
  monotonic_risk: high
verdict: B
override_reason: "单维度不满足 GC3。HCP 孔径分布宽、腔体形状可控性低于 MIP。先例密度极低（HCP/HCH 零先例）。"
```

#### A12 卤化物稳定穴分子笼（形状+NH···Cl 预组织氢键）

```yaml
angle_id: A12
tfg:
  conclusion: borderline
  note: "形状维可行。NH···Cl 弱氢键维同 A07 风险（水相竞争力），但分子笼预组织可提供多点协同，加和效应或可克服。笼腔去溶剂化能为核心变量。"
pads:
  score: 10
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["形状互补", "预组织 N-H···Cl 弱氢键"]
  monotonic_risk: low
verdict: A
override_reason: "DhlA 卤化物稳定穴为强生物先例（Franken 1991 EMBO J），双维度正交，先例密度极低（分子笼水相 HCH 零先例）。分子笼水溶性/聚集与笼腔去溶剂化能为工程风险。"
```

#### A13 亲核水解分子笼（LinB 反应性转译）

```yaml
angle_id: A13
tfg:
  conclusion: fail
  note: "非蛋白体系中 SN2 对饱和 C-Cl 的速率极慢，无酶预组织与过渡态稳定化。可行性本身即科学问题，且水解产物五氯环己醇毒性须评估。"
pads:
  score: 5
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["SN2 反应性"]
  monotonic_risk: none
verdict: X
override_reason: "TFG 不通过：非蛋白 SN2 对饱和脂肪族 C-Cl 在水相中本质不可行。"
```

#### A14 电化学钴啉还原捕获电极

```yaml
angle_id: A14
tfg:
  conclusion: borderline
  note: "还原脱氯热力学可行（钴啉递送电子至 C-Cl σ*），但 β-HCH 为四异构体中还原最慢者（T6）。电位门控可提供选择性窗口，但先验不确定。"
pads:
  score: 25
  direct: 0
  directional: 2
  platform: 3
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["还原电位"]
  monotonic_risk: low
verdict: B
override_reason: "还原脱氯对 β-HCH 速率极慢（T6），D. mccartyi 对 β-HCH 转化不显著（Bashir 2018 负证据）。单维度（还原电位）选择性轴单薄。电极传质与氯苯中间体闭合（T6）为附加风险。"
```

#### A15 碳载钴啉-ZVI 化学还原

```yaml
angle_id: A15
tfg:
  conclusion: borderline
  note: "同 A14 还原维风险。碳载预浓缩同时浓缩竞争物（T8），ZVI 非生物还原对 β-HCH 选择性未知。"
pads:
  score: 30
  direct: 1
  directional: 3
  platform: 5
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["还原脱氯"]
  monotonic_risk: high
verdict: X
override_reason: "PADS 偏高（ZVI/还原脱氯先例密集，CT2），单维度，β-HCH 还原最慢。碳载预浓缩对竞争物无区分（T8）。"
```

#### A16 水稳定钴-MOF 还原捕获

```yaml
angle_id: A16
tfg:
  conclusion: borderline
  note: "Co-MOF 结构钴节点还原电位是否匹配 β-HCH C-Cl σ* 不确定。多数 MOF 水稳定性不足。"
pads:
  score: 15
  direct: 0
  directional: 1
  platform: 3
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["MOF 孔道形状预浓缩", "结构钴节点还原"]
  monotonic_risk: low
verdict: B
override_reason: "MOF 水相 HCH 零先例（G6），先例密度低。但 MOF 水稳定性、钴节点还原活性、水分子配位竞争三重风险。按 G6 材料复杂度约束，MOF 为'避免'级体系。"
```

#### A17 核壳分级捕获-还原复合体

```yaml
angle_id: A17
tfg:
  conclusion: borderline
  note: "壳层非特异疏水预浓缩对竞争物无区分（T8），核层还原对 β-HCH 选择性须独立验证（T6）。分级架构概念合理但两核心组件均有选择性风险。"
pads:
  score: 10
  direct: 0
  directional: 0
  platform: 1
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["空间分级（非正交）"]
  monotonic_risk: high
verdict: B
override_reason: "壳层预浓缩非选择性（T8），核层还原选择性独立不成立（T6）。空间分级不构成正交选择性维度。"
```

#### A18 MLP 启发式疏水生物炭（非选择对照）

```yaml
angle_id: A18
tfg:
  conclusion: pass
  note: "非特异疏水分配热力学可行，但无选择性维度。"
pads:
  score: 60
  direct: 2
  directional: 5
  platform: 10
  saturation: true
odc:
  dimensions: 0
  dimension_list: []
  monotonic_risk: high
verdict: X
override_reason: "PADS > 50 先例饱和（β-HCH AC 两篇专一研究 + 碳质吸附大量先例），零正交维度，纯疏水分配单调（CT1）。仅作为非选择对照基线，不独立开槽。"
```

#### A19 CD-生物表面活性素协同传质增强

```yaml
angle_id: A19
tfg:
  conclusion: borderline
  note: "CD 包合维同 A01 热力学上限。表面活性素增溶同时增溶竞争物，选择性损失风险。"
pads:
  score: 20
  direct: 0
  directional: 1
  platform: 2
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["包合+传质增强（非正交）"]
  monotonic_risk: high
verdict: B
override_reason: "传质增强不构成独立选择性维度。CD 包合热力学上限同 A01。表面活性素 CMC 与 CD 包合竞争。"
```

#### A20 四极矩读出极性腔体

```yaml
angle_id: A20
tfg:
  conclusion: fail
  note: "β-HCH 与 α/γ-HCH 的偶极/四极矩差异为真实物理量（D3d vs C3v/C1），但量级极小。水相中高介电常数（ε=78.4）强烈屏蔽静电贡献，净效应远低于可测下限。"
pads:
  score: 5
  direct: 0
  directional: 0
  platform: 0
  saturation: false
odc:
  dimensions: 1
  dimension_list: ["四极矩静电"]
  monotonic_risk: high
verdict: X
override_reason: "TFG 不通过：水相静电贡献被高介电屏蔽至不可测。可行性风险极高，保留为机制探索性候选但通过概率近零。"
```

#### A21 水稳定 Zr-MOF 形状孔道+Zr-OH···Cl

```yaml
angle_id: A21
tfg:
  conclusion: borderline
  note: "形状维可行（β-HCH ~7 Å vs UiO-66 孔径 ~6–8 Å，匹配度须精确核验）。Zr-OH···Cl 弱相互作用在水相中极弱，水分子在 Zr 簇上竞争配位。"
pads:
  score: 15
  direct: 0
  directional: 0
  platform: 2
  saturation: false
odc:
  dimensions: 2
  dimension_list: ["形状互补", "Zr-OH···Cl 弱氢键"]
  monotonic_risk: low
verdict: B
override_reason: "双维度正交但第二维（Zr-OH···Cl）水相中极弱。MOF 按 G6 为'避免'级体系。β-HCH 与 UiO-66 孔径匹配度为先决验证项。"
```

### 3.2 预分类汇总

| 等级 | 角度 | 数量 | 核心特征 |
|------|------|------|---------|
| **S 级** | A08 | **1** | 形状+偶极双维 COF，零先例，GC3 通过 |
| **A 级** | A06, A07, A12 | **3** | 双维度正交，先例密度低，水相弱相互作用竞争力为核心风险 |
| **B 级** | A04, A05, A09, A10, A11, A14, A16, A17, A19, A21 | **10** | 热力学可行但单维度或选择性轴单薄 |
| **X 级** | A01, A02, A03, A13, A15, A18, A20 | **7** | TFG 不通过/实证终止/PADS 饱和/结构性不可行 |

> **注意**：A01/A02/A03 为同一 CD 包合机制的三种架构变体，已因热力学上限被 S29 实证终止（§0.1 热力学标尺），归入 X 级。若将三者视为架构变体而非独立角度，机制可区分上限从 21 收缩至 19（与 DESIGN_SPACE.md 上限评估一致）。

---

## 4. 历史教训注入

### 4.1 C 组分类 Spec 陷阱库（继承）

| 编号 | 陷阱 | 对 β-HCH 的具体威胁 | 规避策略 |
|------|------|---------------------|---------|
| **CT1** | 疏水分配单调性 | β-HCH logKow ~5，DDT 6.5–6.9、狄氏剂 5.4、HCB 5.5——纯疏水设计对更高 logKow 共存 OCP 必然竞争落败 | 任何"脂质样腔"须以有限体积（Langmuir 可饱和）+ 尺寸窗口 + 脂质归一化对照区别于无限脂质分配 |
| **CT2** | 破坏性平台先例饱和 | ZVI/Fe-Pd/B12 等还原脱氯全非选择，β-HCH 为最慢反应者 | 增量须落 ng/L 工况、异构体选择性、真实竞争谱，不以容量或总降解率替代 |
| **CT3** | MIP 机制空洞 | 形状排阻为非特异机制，HCH MIP 唯一先例为 lindane 传感（无分离因子） | 轮廓识别角度须以机制驱动空腔设计（非模板印迹）自辩，报告结构近似物分离因子 |
| **CT4** | 第三相分配竞争 | β-HCH 比其他异构体更易吸附悬浮颗粒物（Li 2020），溶解相与总浓度口径须区分 | 报告脂质/有机质归一化对照，证明有限体积腔相对无限脂质分配的热力学优势 |
| **CT5** | 再生-二噁英窗口 | 含氯笼状分子热处置在特定温区生成 PCDD/F | 再生路径采用低温溶剂/超临界 CO₂/电化学，避开二噁英生成温区 |
| **CT7** | CD DFT ≠ 水相选择性 | γ-CD/β-HCH DFT 包合最稳定但无实验水相吸附数据（T1） | 阶段 0 模型化合物水相滴定 go/no-go 门控 |

### 4.2 Dieldrin S27 成功方案启示

Dieldrin A01（S27，89 分 pass）为 C 组唯一通过方案，其成功模式对 β-HCH 有以下可迁移教训：

1. **"刚性疏水腔 + 唯一极性把手几何读出"策略**：Dieldrin 用方酰胺双 NH 读出 exo-环氧几何。β-HCH 无环氧桥，但全平伏氯阵列的盘状轮廓 + C-Cl σ 孔图案可作为几何读出目标。关键差异：β-HCH 的极性把手更弱（C-Cl vs 环氧氧），需更强的预组织补偿
2. **阶段 0 模型化合物水相滴定**：Dieldrin 方案设 go/no-go 门（K ≥ 10 M⁻¹），该做法应成为 β-HCH 所有涉及弱相互作用角度的标准前置步骤
3. **诚实标注仿生强度与方向性限定**：Dieldrin 方案诚实承认 A302S 极性插入削弱结合（抗性），原型仅提供架构原理不含增强方向。β-HCH 方案同样须诚实标注：LinA 模板方向相反（T2）、LinB 为真正 β-HCH 底物但无晶体结构
4. **热力学图像修正**：Dieldrin r1 的"疏水层近简并"错误在 r2 修正为实测 logKow 排序。β-HCH 方案须前置锁定异构体物化参数差异（logKow 3.6–4.1 区间，差异 <0.5 单位），诚实评估识别增量需求
5. **迭代轨迹**：Dieldrin r1=70→r2=89，每轮有实质议题闭合。β-HCH 方案应预期 2–4 轮迭代，首轮重点为热力学标尺与阶段 0 go/no-go

### 4.3 β-HCH S29 终止方案教训

S29_A01（γ-CD 交联聚合物，r4=67 终止）提供以下核心教训：

1. **热力学标尺前置**：先锁定 Kd 上限再定工况，避免 ng/L 头条主张超出自身上限 1.2–4.7 个数量级
2. **方向先验诚实评估**：H2（β 优于 γ）为低先验几何外推，两条 CD-HCH 实验先例方向均为 γ 优先——方向问题应由 Stage 0a 预筛裁定
3. **占腔竞争 KaC 预算**：氯苯类（Hajek 排水氯苯 640 µg/L）对 CD 空腔的竞争风险须定量核算
4. **架构变体 ≠ 机制变体**：A01/A02/A03 为同一 CD 包合机制的三种架构，不应独立开槽

### 4.4 β-HCH 特殊性教训

1. **全平伏氯构型的几何识别特殊性**：β-HCH 为 HCH 四异构体中唯一全平伏构型（0 轴向氯），α/γ/δ 分别含 3/3/2 轴向氯。识别策略须利用"0 轴向氯 vs N 轴向氯"的轮廓差异，而非"有 vs 无"的二值区分
2. **LinA 模板方向相反**：自然界唯一 HCH 立体识别机制（LinA）针对含轴向氯异构体，识别几何与 β-HCH 全平伏形状互补性相反。可转译线索在 LinB 水解腔（β-HCH 真底物）与 Dehalobacter 还原，不在 LinA
3. **脂肪族 C-Cl 卤键弱于芳基氯**：TTR-T4 型卤键原理不宜直接转译，卤键不应作为单独识别维度，须与形状维协同
4. **疏水分配天花板**：纯疏水设计在真实混合基质中对 β-HCH 无选择性收益（T8），所有角度须明确超越 logKow 单调

---

## 5. 竞争物谱锁定

### 5.1 三层竞争物架构

| 层级 | 竞争物类别 | 具体物质 | 威胁等级 | 说明 |
|------|-----------|---------|---------|------|
| **第一层：立体异构体** | α/β/γ/δ/ε-HCH | α-HCH（3 轴向氯）、γ-HCH/林丹（3 轴向氯）、δ-HCH（2 轴向氯）、ε-HCH | **极高** | 同分子式/同 MW/logKow 3.6–4.1，唯一差异为氯取向。β-HCH 0 轴向氯 vs 其他含轴向氯 |
| **第二层：同流程副产物** | 氯苯类 | PeCB、HCB、1,2,4-TCB、苯 | **高** | Hajek 排水氯苯 640 µg/L 对总 HCH 约 5:1；Sardas 场地 HCH+氯苯+苯混合污染 |
| **第二层** | 氯酚 | 2,4-DCP 等 | 中 | Sardas 场地检出，Hajek 排水 16 µg/L |
| **第三层：环境共残留 OCPs** | 不同类 OCPs | DDT (logKow 6.5–6.9)、DDE (~6.5)、Dieldrin (5.4)、Endosulfan (3.6–3.8)、HCB (5.5) | **高** | 更高或相当疏水度，纯疏水设计必然竞争落败 |
| **第三层：基质竞争** | 天然有机物 | 腐殖酸/富里酸、DOC、脂质相、有机碳 | **高** | 疏水位点抢占；β-HCH 比其他异构体更易吸附悬浮颗粒物（Li 2020） |

### 5.2 竞争物使用规则

1. **先证第一层**：必须证明 β-HCH 对 α/γ/δ-HCH 的分离因子 α > 1，且该选择性不可由 logKow 微小差异（<0.5 单位）单调解释
2. **脂质归一化对照**：所有选择性声称须以脂质/有机质归一化对照排除普通疏水吸附（GC1）
3. **氯苯占腔预算**：对涉及有限体积腔的角度，须按 KaC 框架定量核算氯苯占腔风险（参照 S29 §0.2 方法）
4. **结构近似物为必须**：仅报告 NOM 等不同类物质的选择性不构成证据（GC2）

---

## 6. 诚实上限预估

### 6.1 预估方法

基于 21 个角度的预分类结果、历史终止率（fresh_1000 整体 ~73%）与 C 组特殊性，按等级估算可通过方案数。

### 6.2 分等级预估

| 等级 | 角度数 | 预期开槽数 | 单角度通过概率 | 预期通过数 |
|------|--------|-----------|-------------|-----------|
| **S 级** | 1 (A08) | 1 | 20–30% | 0–1 |
| **A 级** | 3 (A06, A07, A12) | 3 | 10–20% | 0–1 |
| **B 级** | 10 | 5–8（S/A 失败后尝试） | 5–10% | 0–1 |
| **X 级** | 7 | 0 | 0% | 0 |

### 6.3 诚实上限

- **乐观估计**：3–4 个通过方案（S 级 1 个 + A 级 1–2 个 + B 级 0–1 个）
- **中位估计**：1–2 个通过方案
- **悲观但现实估计**：0–1 个通过方案
- **结构性约束**：β-HCH 识别维度空间极窄（恒中性、无官能团、四异构体物化参数极近），诚实通过数可能 < 50 槽上限。按 G8 耗尽条款，"诚实的 N < 50 优于凑数的 50"

### 6.4 关键不确定性

1. **水相弱相互作用的可测性**：A06/A07/A12 的卤键/弱氢键在水相中能否产生 >1 kJ/mol 净识别增量，是决定 A 级角度通过概率的核心变量
2. **偶极/四极矩水相贡献**：A08 的偶极维在水相中被高介电屏蔽，实际贡献量级高度不确定
3. **阶段 0 go/no-go 结果**：所有涉及弱相互作用的角度须先通过阶段 0 模型化合物水相滴定，go/no-go 结果将大幅调整实际可行角度数

---

## 7. 执行建议

### 7.1 推荐首先执行的角度（S 级 + A 级）

| 优先级 | 角度 | 核心策略 | 推荐材料平台 | 预期迭代轮次 | 关键 go/no-go 门 |
|--------|------|---------|-------------|-------------|-----------------|
| **1** | A08 | 形状+偶极双维 COF 腔 | 极性节点 COF（如三嗪-苯二醛骨架，有序孔道 ~7–8 Å） | 2–3 轮 | 阶段 0：β-HCH vs γ-HCH 在极性 COF 微孔中的吸附焓差 ΔΔH > 1 kJ/mol（ITC 或 van't Hoff） |
| **2** | A06 | 形状+卤键双维 MIP | β-HCH 模板 MIP + 吡啶/三嗪功能单体 | 2–4 轮 | 阶段 0：功能单体 MIP vs 非功能单体 MIP（A05）的 β-HCH 吸附焓差 ΔΔH > 0.5 kJ/mol |
| **3** | A07 | 形状+弱氢键双维 MIP | β-HCH 模板 MIP + 脲/硫脲功能单体 | 2–4 轮 | 阶段 0：脲/硫脲 MIP vs 非功能单体 MIP 的吸附焓差，供体强弱序列（脲 < 硫脲）α 响应 |
| **4** | A12 | 卤化物稳定穴分子笼 | 离散共价笼（内壁 NH 供体阵列，腔径 ~7 Å） | 3–5 轮 | 阶段 0：笼化合物水相滴定 β-HCH 包合常数 K > 10 M⁻¹ |

### 7.2 执行策略

1. **A08 先行**：COF 平台可设计性最高、先例密度最低（G6），且形状+偶极双维正交性最清晰。建议首先合成 2–3 种极性节点 COF，验证 β-HCH 吸附基线与异构体区分度
2. **A06/A07 并行**：两者均为 MIP 平台但功能单体不同（N-杂环 vs 脲/硫脲），可共享模板制备流程与非功能单体对照（A05），实验效率高。A06 与 A07 的配对实验可解耦卤键与弱氢键贡献
3. **A12 后行**：分子笼合成复杂度最高，但 DhlA 卤化物稳定穴提供最强生物先例支撑。建议在 A06/A07 MIP 结果基础上确定 NH 供体最优构型后，再设计分子笼

### 7.3 B 级角度触发条件

B 级角度仅在以下条件满足后开启：
- S 级 + A 级全部角度已执行（通过或终止）
- 通过数 < 1（即 S/A 级均未产出通过方案）
- 具体 B 级角度有明确的增量区分策略（非简单参数调优）

B 级中优先候选：
- **A05**（形状 MIP，作为 A06/A07 的对照基线，可与 A06/A07 同步制备）
- **A10**（负选择 HCP，独特策略——排除轴向氯异构体而非捕获 β-HCH）
- **A11**（正选择 HCP，与 A10 配对解耦正/负选择贡献）

### 7.4 终止条件

| 终止条件 | 触发规则 |
|---------|---------|
| 单槽终止 | 3 次重建仍 < 85 分，或阶段 0 go/no-go 未通过 |
| 角度终止 | TFG 不通过（X 级）或 PADS > 50 |
| 污染物终止 | S/A/B 级角度全部用尽且重建仍无法通过，按 G8 耗尽条款记录 |
| 全局终止 | 至少 1 个通过方案后即推进到下一污染物，回溯补充在 20 污染物全部访问一轮后执行 |

### 7.5 阶段 0 标准前置实验

所有 A 级及以上角度在开启方案槽前，须完成以下阶段 0 门控实验（参照 Dieldrin S27 成功模式与 GC6 硬约束）：

1. **模型化合物水相滴定**：合成识别单元简化模型（如方酰胺/脲/硫脲小分子或功能单体），在超纯水中与 β-HCH 执行 ITC 或 van't Hoff 分析，测定表观结合常数 K。Go 线：K ≥ 10 M⁻¹
2. **异构体方向预筛**：在模型体系中同时测定 γ-HCH（林丹）的结合常数，确认 β/γ 方向与假设一致（β 优于 γ）。若方向证伪（γ 优于 β），角度终止
3. **氯苯占腔应力测试**：在模型体系中引入 1,2,4-TCB（10 mg/L 应力点），测定 β-HCH 摄取保留率。保留率 < 50% 则标记占腔风险为高

---

## 附录：角度预分类快速索引

| 角度 | 等级 | TFG | PADS | ODC 维度 | 核心风险 | 推荐材料平台 |
|------|------|-----|------|---------|---------|-------------|
| A01 | X | fail | 35 | 1 | CD 包合热力学上限（S29 实证终止） | — |
| A02 | X | fail | 35 | 1 | 同 A01 | — |
| A03 | X | fail | 38 | 1 | 同 A01 | — |
| A04 | B | borderline | 20 | 2 | CD 弱包合 + 还原慢速率 | 双功能交联聚合物 |
| A05 | B | pass | 30 | 1 | 单维度（GC3 不通过） | MIP 非功能单体 |
| **A06** | **A** | borderline | 15 | 2 | 脂肪族 C-Cl 卤键水相弱 | MIP + 吡啶/三嗪 |
| **A07** | **A** | borderline | 15 | 2 | NH···Cl 水相竞争力 | MIP + 脲/硫脲 |
| **A08** | **S** | borderline | 10 | 2 | 偶极维水相屏蔽 | 极性节点 COF |
| A09 | B | borderline | 10 | 1 | 单维度 + σ 穴极弱 | 三嗪 COF |
| A10 | B | pass | 10 | 1 | 截面差异 <1 Å | 超交联 HCP |
| A11 | B | pass | 10 | 1 | 单维度 + HCP 孔径分布宽 | HCP 本征微孔 |
| **A12** | **A** | borderline | 10 | 2 | 笼腔去溶剂化能 | 离散分子笼 |
| A13 | X | fail | 5 | 1 | SN2 非蛋白不可行 | — |
| A14 | B | borderline | 25 | 1 | β-HCH 还原最慢 | 电化学电极 |
| A15 | X | borderline | 30 | 1 | PADS 高 + 单维度 | — |
| A16 | B | borderline | 15 | 2 | MOF 水稳定性（G6 避免级） | Co-MOF |
| A17 | B | borderline | 10 | 1 | 壳层非选择 + 核层选择性不成立 | 核壳复合体 |
| A18 | X | pass | 60 | 0 | PADS 饱和，纯非选择对照 | — |
| A19 | B | borderline | 20 | 1 | 传质增强非选择性维度 | CD + 表面活性素 |
| A20 | X | fail | 5 | 1 | 水相静电屏蔽至不可测 | — |
| A21 | B | borderline | 15 | 2 | MOF 避免级 + Zr-OH 竞争 | Zr-MOF |
