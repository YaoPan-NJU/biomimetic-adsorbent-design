# S39 · dieldrin · A03 · 笼状轮廓形状互补离散主体腔

- 污染物：狄氏剂 dieldrin（CAS 60-57-1，C12H8Cl6O）
- 角度：A03 笼状轮廓形状互补的离散主体腔（cage-shaped contour shape-complementary discrete host cavity）
- 状态：**terminated**（r1 即终止；热力学不可能三角——基础性结构天花板）
- r1 工作流：设计 73→攻击 3c/6h→裁决 51/terminate
- 创新性清单：A 部分通过（机制轴独立于 A01）、B 通过（离散有机笼/葫芦脲材料架构新颖）、C 不通过（原型基础薄弱，水相结合纯推理）、D 不通过（endrin 选择性低于可测下限，有效维度仅剩尺寸排除）、E 不通过（Koc 参数引用错误）

## 角色交付
- 设计者（r1）：自评 73/100，诚实标注水相离散主体腔对中性极疏水笼状客体的结合常数无先例可循；14 条引用零杜撰（10 metadata_verified, 1 abstract_read, 2 BRIEF 继承 verified, 1 继承）；主要离散主体候选为 SC6 有机笼（~7.6 Å 腔径）与 CB[8] 葫芦脲。
- 攻击者（r1）：3 critical / 6 high。独立发现 Koc 参数引用错误（设计使用 10⁴-10⁵ 估算，ATSDR 2022 verified 级实测 Koc ≈ 4.7×10⁶ L/kg，差 ~2 个数量级）；离散主体腔对中性客体的 Ka 天花板 ~10⁴ M⁻¹ → Kd_eff 上限 ~5,000 L/kg；构成热力学不可能三角。
- 裁决者（r1）：独立重算 51/100。三条 critical 全部确认且形成互证链。

## Critical 发现（3 条，基础性不可修复）

### C1 · Koc 基线参数引用错误
设计声称狄氏剂 Koc 约 10⁴-10⁵ L/kg（继承自 DESIGN_SPACE），但 ATSDR 2022 第 5 章（verified 级来源）实测 Koc = 10^6.67 ≈ 4.7×10⁶ L/kg。该参数为 logKow 5.40 的超高疏水分子的物理必然，Koc 基线比设计声称高约 2 个数量级。

### C2 · Ka 天花板（主体化学固有物理约束）
离散分子主体腔（葫芦脲/杯芳烃/有机笼）对中性疏水客体的水相结合常数 Ka 上限约 10⁴ M⁻¹（Schneider 2009 Angew Chem，Murray 2017 Chem Soc Rev 综述级证据）。换算有效 Kd_eff ≈ Ka × V_water/M_site ≈ 5,000 L/kg（按典型位点密度估算）。相对 Koc ≈ 4.7×10⁶ L/kg 差约 3 个数量级。

### C3 · 热力学不可能三角
C1 + C2 构成不可闭合三角：(1) 材料须在脂质/有机质竞争下显著超越 Koc 基线；(2) 离散主体腔 Ka 天花板使 Kd_eff 远低于 Koc；(3) 任何功能化/载体工程均无法闭合 ~3 数量级差距。结论：对 logKow > 5 的中性笼状客体，离散分子主体腔路线实质耗尽。

## 裁决六维评分

| 维度 | 得分 | 说明 |
|---|---|---|
| 因果闭环 | 9/20 | 核心 SC6-狄氏剂结合为纯推理，Koc 勘误后热力学不可行 |
| 选择性吸附机制 | 11/25 | endrin 选择性低于可测下限，有效维度仅剩尺寸排除 |
| 人工材料可转译性 | 11/20 | 磺酸基固载遮挡杯口，CB[8] 物理包埋将浸出 |
| 原创性 | 8/15 | 零先例实为不可行暗示，与 A01 材料实现层有重叠 |
| 实验可证伪与对照 | 7/10 | 四阶段实验设计优秀，但 T4 基准失锚 |
| 证据完整性 | 5/10 | Koc 参数引用错误，核心声称零支撑 |
| **合计** | **51/100** | **terminated** |

## 证据引用
- Barrow 2015 Chem Rev, DOI 10.1021/acs.chemrev.5b00341（葫芦脲主客体化学综述，metadata_verified）
- Assaf & Nau 2015 Chem Soc Rev, DOI 10.1039/C4CS00273A（葫芦脲化学综述，metadata_verified，PMID 25408290）
- Moghaddam 2011 JACS, DOI 10.1021/ja109904u（CB[7] 超高亲和热力学，metadata_verified）
- Murray 2017 Chem Soc Rev, DOI 10.1039/c6cs00768d（有机笼综述，metadata_verified，PMC 全文）
- Yang 2023 Chem Rev, DOI 10.1021/acs.chemrev.2c00667（多孔有机笼综述，metadata_verified）
- Tozawa 2009 Nat Mater, DOI 10.1038/nmat2545（有机笼合成，metadata_verified）
- Hasell 2016 Nat Rev Mater, DOI 10.1038/natrevmats.2016.53（多孔有机分子综述，metadata_verified）
- Schneider 2009 Angew Chem, DOI 10.1002/anie.200802947（水相主客体结合常数基准，metadata_verified）
- ATSDR 2022（狄氏剂 Koc 实测 verified 级来源）

## 穷尽评估
A03 对 logKow > 5 的中性笼状客体实质耗尽（热力学不可能三角为基础性物理约束）。Dieldrin A03 形状互补路线不可行。剩余有潜力的狄氏剂加深角度：A02（环氧开环反应性捕获，medium 先例）、A08（刺激响应温和再生，low 先例）、A17（捕获腔-微氧 FeS 串联耦合，low 先例）；其中 A02 与 A17 为反应性/转化方向，不受 Koc 基线约束；A08 为再生架构轴。下一候选首选 A02（环氧开环，独立于 A01 氢键锚定机制，且不受热力学不可能三角约束）。
