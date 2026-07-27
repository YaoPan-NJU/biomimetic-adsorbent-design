# DDT A01 方案：脱氯化氢酶 β-消除读出启发的桥双基序反应性识别腔

角度编号：A01（脱氯化氢酶 β-消除读出启发的桥双基序反应性识别腔）。对应科学问题 SP1（无极性把手的桥取代基几何识别）。本方案为非蛋白人工识别材料方案，蛋白、折叠肽、表达构建体与蛋白杂化不进入材料实现（陷阱 T8）；DDT-脱氯化氢酶（本质为 GST）仅作原理级仿生原型，提供双基序反应性读出原理的结构约束。

## 1. 科学问题与工程难题（方案层面具体化）

### 1.1 方案层面科学问题

能否在刚性疏水受限腔内预组织一对空间定位的弱碱位与三氯甲基互补亚腔，使材料在水相中凭借 C1 桥 -CH(CCl3) 的双基序几何（桥氢供体 + 三氯甲基四面体轮廓）对 DDT 产生超越疏水分配的额外结合贡献，且该结合在操作条件下不触发 β-消除（捕获而不转化），从而对 DDE（无桥氢）与 DDD（无 -CCl3）实现双拒绝式结构判别。

该问题拆为四个可证伪子问题。

**子问题一：双基序识别的热力学贡献。** DDT 桥碳叔氢（-CH(CCl3)-）因邻接三氯甲基与双芳基而贫电子，可与弱碱形成弱 C-H···B 氢键（估计 2-6 kJ/mol，推断，须 DFT 与变温 ITC 核验）。-CCl3 四面体轮廓与互补亚腔的范德华接触提供额外形状读出（估计 1-3 kJ/mol，推断）。二者须同时满足几何匹配方产生结合增益（协同非加和），单独任一基序不足以产生可测选择性。可证伪判据：消融对照（无碱位腔、无 -CCl3 亚腔的宽松腔）的选择性因子 α(DDT/DDE) 与 α(DDT/DDD) 均回落至疏水基线（≤1.5），而完整双基序腔的 α 显著高于加和预测。

**子问题二：捕获而不转化的化学可行性。** 核心设计约束：碱位须识别（结合于）桥氢附近而不攫取之。能量地貌分析如下：DDT 桥 C-H 的 pKa 估计约 35-40（DMSO 标度，推断，基于 McLennan 1972 速率-酸性相关与 E2 消除文献），水相有效 pKa 更高。设计碱位为位阻胺（如 2,2,6,6-四甲基哌啶衍生物，共轭酸 pKa 约 10-11 水相）或弱 π 碱（如六甲基苯，共轭酸 pKa 约 -2），与桥 C-H 的 pKa 差 ΔpKa > 25 个单位。热力学上，质子转移平衡常数 K_PT = 10^(-ΔpKa) < 10^(-25)，完全不可逆。动力学上，E2 消除过渡态要求碱-氢-碳-氯四中心反式共面排列，活化能约 80-120 kJ/mol（典型 E2 弱碱条件，推断），而结合态仅提供 2-6 kJ/mol 的弱氢键稳定化。在 25°C（kT ≈ 2.5 kJ/mol）下，E2 能垒为 32-48 kT，反应速率可忽略。可证伪判据：材料在 25°C、pH 7 水相中接触 DDT 7 天后，DDE 生成量低于检出限（GC-MS SIM，LOD < 0.1 ng/L）；若检出 DDE 生成 > 1% 转化，则"捕获不转化"设计失败。

**子问题三：双拒绝选择性的真实性。** DDE（=CCl2，无桥氢）：碱位无氢键供体可识别，双基序中第一基序缺失，结合能损失 ΔΔG_H-bond（估计 2-6 kJ/mol）。DDD（-CHCl2，无 -CCl3）：三氯甲基亚腔几何失配（-CHCl2 四面体轮廓小于 -CCl3，范德华接触减少），第二基序缺失，结合能损失 ΔΔG_shape（估计 1-3 kJ/mol）。Dicofol（Ar2C(OH)CCl3，保留 -CCl3 但桥氢被 -OH 取代）：桥位为羟基而非 C-H，碱位无法形成 C-H···B 氢键（-OH 为强氢键供体但几何与 pKa 完全不同），第一基序以不同机制失配。三竞争物各以不同方式被拒读，构成因果三角验证。可证伪判据：α(DDT/DDE) ≥ 3 且 α(DDT/DDD) ≥ 2 且 α(DDT/dicofol) ≥ 2（超纯水，等摩尔竞争，1 µg/L 档）；若任一 α < 1.5，则对应基序的识别贡献不显著。

**子问题四：ng/L 工况亲和力。** 目标溶解相浓度 0.5-5 ng/L（一般流域，E2 verified）。疏水受限腔对 DDT 的基础亲和力由去溶剂化自由能驱动：DDT logKow 6.9 对应水→疏水相转移 ΔG ≈ -39 kJ/mol（ΔG = -2.303RT·logKow），受限腔去润湿协同可额外贡献 5-15 kJ/mol（推断，须以 A03 类腔体实验标定）。预计 Kd 达 10^5-10^7 L/kg 量级（远超 10^4 门槛），但此高亲和力主要来自疏水效应，对 DDE/DDD 同样有效（logKow 6.5/6.0）。选择性增量（双基序贡献）叠加于此高基线之上，其可测性取决于 ΔΔG_motif 相对于实验误差的显著性。

### 1.2 方案层面工程难题

**EN1 碱位在刚性腔内的精确定位。** 位阻胺碱须以固定取向嵌入腔壁，使氮孤对电子方向指向桥氢结合位，同时位阻基团（如四甲基）阻止碱与桥碳的紧密接触（防止 E2 过渡态几何达成）。合成挑战：在 COF/HCP 骨架中后合成引入定位碱位，或以功能化单体直接构筑。

**EN2 -CCl3 亚腔的几何精度。** 三氯甲基四面体轮廓（Cl 范德华半径 1.75 Å × 3 + C 骨架）须与亚腔壁形成紧密范德华接触（间隙 < 0.5 Å），过松则无形状读出，过紧则 DDT 无法进入。DDT 分子长轴约 13 Å、双氯苯环横截面约 9-10 Å（推断，须 DFT 几何优化复核），腔体尺寸须匹配。

**EN3 水相竞争与第三相。** DDT 在天然水中主要赋存于颗粒/胶体/DOC 相（简报 3.2），吸附剂须与 foc·Koc 非特异分配竞争。腐殖酸可能污堵腔口。须以二级出水加标与脂质/有机质归一化对照核定（陷阱 T1/T7）。

**EN4 再生与位点保持。** 高疏水结合使温和洗脱困难。候选再生路径：(a) 低比例共溶剂（甲醇/水 ≤ 20%）破坏疏水作用，(b) 升温至 60°C 加速脱附，(c) 超临界 CO2。须验证再生后碱位不降解、腔形不塌陷、选择性不衰减。

## 2. 生物原型与证据

原型家族：DDT-脱氯化氢酶（本质为谷胱甘肽 S-转移酶 GST），催化 DDT → DDE + HCl 的 β-消除反应。该酶的底物特异性严格依赖 C1 桥双基序：(i) 桥 β-氢（被碱攫取），(ii) -CCl3 三氯甲基（作为离去基团）。缺少任一基序的底物（DDE 无桥氢、DDD 无 -CCl3）均不被催化。本方案提取该双基序读出的几何原理，转译为人工识别腔的"结合而不催化"设计。

### E1 Clark AG, Shamaan NA. Pesticide Biochemistry and Physiology, 1984, 22(3): 350-361.
- DOI: 10.1016/0048-3575(84)90018-x
- 标题: "Evidence that DDT-dehydrochlorinase from the house fly is a glutathione S-transferase"
- 支持主张: DDT-脱氯化氢酶的本质为谷胱甘肽 S-转移酶（GST），确立该酶的蛋白身份与催化机制框架（GSH 依赖性碱催化 β-消除）。
- 层级: 一手文献（酶学鉴定）
- 核验状态: metadata_verified（Crossref 题录自核：作者、期刊、年、DOI 一致；被引 310 次）
- 定位: 题名、作者、期刊卷年

### E2 Sternburg J, Wedemeyer G, Kearns CW. Journal of Agricultural and Food Chemistry, 1954, 2(22): 1125-1126.
- DOI: 10.1021/jf60042a008
- 标题: "Resistance to DDT, DDT-Dehydrochlorinase, an Enzyme"
- 支持主张: DDT-脱氯化氢酶的原始发现，确立昆虫 DDT 抗性经酶促脱氯化氢（DDT→DDE）实现。
- 层级: 一手文献（原始发现）
- 核验状态: metadata_verified（Crossref 题录自核：作者、期刊、年、DOI 一致；被引 135 次）
- 定位: 题名、作者

### E3 Ranson H, Hemingway J 等. Insect Biochemistry and Molecular Biology, 2005, 35(5): 471-481.
- DOI: 10.1016/j.ibmb.2005.03.008
- 标题: "Elevated activity of an Epsilon class glutathione transferase confers DDT resistance in the dengue vector, Aedes aegypti"
- 支持主张: 伊蚊 Epsilon 类 GST（GSTe2）过表达赋予 DDT 抗性，确认 GST 介导的 DDT 脱氯化氢在双翅目昆虫中的普遍性与底物特异性（DDT 特异，DDE/DDD 非底物）。
- 层级: 一手文献（功能鉴定）
- 核验状态: metadata_verified（Crossref 题录自核：期刊、年、DOI 一致）
- 定位: 题名

### E4 Lipke H, Kearns CW. Journal of Biological Chemistry, 1959, 234(8): 2129-2132.
- DOI: 10.1016/S0021-9258(18)69878-3
- 标题: "DDT dehydrochlorinase. II. Substrate and cofactor specificity"
- 支持主张: DDT-脱氯化氢酶的底物特异性系统研究：严格依赖三氯乙基桥构型（-CH(CCl3)-），DDE（无桥氢）与 DDD（无 -CCl3）均非有效底物。确立双基序（桥 β-氢 + -CCl3 离去基）同时要求的实验证据。
- 层级: 一手文献（酶学动力学）
- 核验状态: metadata_verified（Crossref/PubMed 题录自核：作者、期刊、卷页、年一致；被引 179 次）
- 定位: 题名、PubMed PMID 13673024 关联

### E5 McLennan DJ. Journal of the Chemical Society, Perkin Transactions 2, 1972.
- 标题: "Rate-acidity correlation for the base-promoted dehydrochlorination of DDT in methanol"
- 支持主张: DDT 碱促进脱氯化氢遵循 E2 消除机制，速率与碱强度（共轭酸 pKa）呈 Brønsted 相关；弱碱条件下速率极低，确立"碱强度阈值"概念——低于阈值的碱不能有效攫取桥氢。
- 层级: 一手文献（物理有机化学）
- 核验状态: metadata_verified（EPA HERO 题录自核：作者、年、题名一致）
- 定位: 题名、EPA HERO reference 2147592
- 注: 全文未读，Brønsted 相关的具体斜率（β 值）与 pKa 阈值须全文核验，标注推断。

### E6 Wang Y 等. Journal of Molecular Biology, 2008, 384(1): 165-177.
- DOI: 10.1016/j.jmb.2008.09.010
- 标题: "Structure of an insect epsilon class glutathione S-transferase (GSTe2) from the malaria vector Anopheles gambiae"
- 支持主张: GSTe2 晶体结构揭示 DDT 结合活性位点的几何约束：疏水腔容纳双氯苯环，GSH 硫醇盐定位于桥 β-氢攫取距离（约 3-4 Å），-CCl3 朝向离去基团口袋。提供双基序空间排布的原子级结构模板。
- 层级: 一手文献（结构生物学）
- 核验状态: metadata_verified（Crossref 题录自核：作者、期刊、年一致；被引 97 次）
- 定位: 题名
- 注: 全文未读，活性位点几何数值为基于摘要与同源结构的推断，须全文核验。

### E7 Kallman BJ, Andrews AK. Science, 1963, 141(3585): 1050-1051.
- DOI: 10.1126/science.141.3585.1050
- 标题: "Reductive Dechlorination of DDT to DDD by Yeast"
- 支持主张: 酵母还原脱氯 DDT→DDD 且 DDE 不反应（简报 R4-1 摘要直读），从还原路径反向确认 C1 桥取代差异的化学反应性区分：-CCl3 可还原而 =CCl2 不可。
- 层级: 一手文献
- 核验状态: abstract_read（简报 R4-1 摘要直读；Crossref 题录自核一致）
- 定位: 简报 R4-1

### E8 Hale SE 等. Water Research, 2009, 43(17): 4263-4272.
- DOI: 10.1016/j.watres.2009.06.031
- 标题: "Sorption of dichlorodiphenyltrichloroethane (DDT) and its metabolites by activated carbon in clean water and sediment slurries"
- 支持主张: AC-水分配系数 logKAC 8.47-9.26（DDT 及代谢物），示疏水腔亲和力有裕度；代谢物与母体同处高吸附区间，示疏水分配对桥三元组无区分力（印证 T1）。
- 层级: 一手文献
- 核验状态: abstract_read（简报 R2-1）
- 定位: 简报 R2-1

### E9 Montuori P 等. Environmental Sciences Europe, 2020, 32: 132.
- DOI: 10.1186/s12302-020-00408-4
- 标题: "Polychlorinated biphenyls and organochlorine pesticides in water and sediment from Volturno River, Southern Italy"
- 支持主张: 溶解相 ΣDDT ND-1.34 ng/L（均值 0.38），(DDD+DDE)/DDT 13.8-16.8，示一般流域 ng/L 级且代谢物主导。
- 层级: 一手监测文献
- 核验状态: verified（简报 E2 全文已读）
- 定位: 简报 E2

### E10 Makgoba A 等. Heliyon, 2024, 10(7): e28054.
- DOI: 10.1016/j.heliyon.2024.e28054
- 标题: "DDT contamination in water resources of some African countries"
- 支持主张: 非洲地表水 DDT 浓度综合；WHO 准则值 1 µg/L 经全文引文核实。
- 层级: 综述
- 核验状态: verified（简报 E1 全文已读）
- 定位: 简报 E1

### E11 PPDB (Pesticide Properties DataBase), Hertfordshire 大学, DDT 条目 id 3140.
- URL: https://sitem.herts.ac.uk/aeru/ppdb/en/Reports/3140.htm
- 支持主张: DDT 理化常数（CAS 50-29-3、MW 354.49、logKow 6.5-6.9）；DDT/DDE/DDD logKow 序列约 6.9/6.5/6.0。
- 层级: 权威数据库
- 核验状态: verified（简报 E16 页面已读）
- 定位: 简报 E16

### E12 Cram DJ. Angewandte Chemie International Edition, 1986, 25(12): 1039-1057.
- DOI: 10.1002/anie.198610391
- 标题: "Preorganization — from solvents to spherands"
- 支持主张: 预组织是主客体化学中结合亲和力与选择性的核心设计原则；宿主结合前构象预组织程度越高，结合时构象熵罚越小，选择性越强。本方案刚性腔预组织碱位与 -CCl3 亚腔即该原理转译。
- 层级: 权威综述（诺贝尔演讲级文献）
- 核验状态: metadata_verified（S20 终止档案裁决者订正：正确预组织原理文献为 Cram 1986 Angew. Chem. Int. Ed. 25:1039-1057，非 Reinhoudt PAC 1988）
- 定位: S20 终止档案裁决者订正记录

### E13 Politzer P, Murray JS, Clark T. Physical Chemistry Chemical Physics, 2010, 12: 7748-7757.
- DOI: 10.1039/c004189k
- 标题: "Halogen bonding: an electrostatically-driven highly directional noncovalent interaction"
- 支持主张: 卤键 σ-hole 模型；为 -CCl3 亚腔内可选卤键受体叠加维度提供原理依据。
- 层级: 权威综述
- 核验状态: metadata_verified（S20 已引同条目）
- 定位: 题名

### E14 Varadwaj PR 等. Crystals, 2020, 10(3): 146.
- DOI: 10.3390/cryst10030146
- 标题: "Does Chlorine in CH3Cl Behave as a Genuine Halogen Bond Donor?"
- 支持主张: CH3Cl 中氯表面为弱负电性、非固有卤键供体。据此诚实标注：DDT -CCl3 的 C-Cl 氯为弱至可疑的卤键供体，卤键叠加维度贡献预计弱。
- 层级: 一手文献（计算级）
- 核验状态: abstract_read（S20 已读摘要）
- 定位: 摘要

先例检索说明：简报既有检索确认 DDT 反应性识别吸附剂零先例（空白区 G2）。本轮追加 Crossref 检索 "DDT selective recognition adsorbent"、"dehydrochlorinase biomimetic material"、"bridge hydrogen recognition cavity"、"hindered base C-H binding without abstraction"、"reactive recognition adsorbent organochlorine"，未见"双基序反应性识别腔水相选择性吸附 DDT"的直接先例。最近邻为 Fe-SBA-15 低温吸附-降解 DDx（Wang 2012，10.1016/s1001-0742(11)60800-0，metadata_verified），属破坏性非选择路线，与本方案"捕获不转化"方向相反。

## 3. 仿生对应矩阵

### HC1（硬对应，主干）：DDT-脱氯化氢酶双基序读出原理的"结合而不催化"转译

- **生物特征**: DDT-脱氯化氢酶（GST）活性位点以 GSH 硫醇盐（碱）定位于桥 β-氢攫取距离（约 3-4 Å），同时疏水腔壁与 -CCl3 四面体轮廓互补（离去基团口袋）。双基序同时就位方催化 β-消除；DDE（无桥氢）与 DDD（无 -CCl3）均非有效底物（E4 Lipke & Kearns 1959；E6 Wang 2008 GSTe2 结构）。
- **来源支持**: E1（Clark 1984 酶鉴定）、E2（Sternburg 1954 原始发现）、E3（GSTe2 2005 功能）、E4（Lipke 1959 底物特异性）、E6（Wang 2008 结构）。
- **材料实现**: 刚性疏水 COF/HCP 受限腔内预组织：(i) 位阻弱碱位（2,2,6,6-四甲基哌啶基或 1,8-双(二甲氨基)萘基）以共价键固定于腔壁，氮孤对电子方向指向桥氢结合位，位阻基团阻止 E2 过渡态几何达成；(ii) -CCl3 互补亚腔（三氯甲基形状的范德华口袋）与碱位呈固定空间关系（距离约 3-5 Å，角度约束模拟酶活性位点几何）。
- **预期功能**: DDT 进入腔体后，桥 C-H 与碱位形成弱氢键（C-H···N，2-6 kJ/mol），-CCl3 嵌入互补亚腔（范德华 1-3 kJ/mol），双基序协同产生超越疏水基线的额外结合（ΔΔG_motif 约 3-8 kJ/mol）。DDE 无桥氢→碱位无识别对象→ΔΔG 损失；DDD 无 -CCl3→亚腔失配→ΔΔG 损失。操作条件下（25°C、pH 7、弱碱）不触发 E2 消除。
- **测量**: 等摩尔 DDT/DDE/DDD/dicofol 四元竞争（超纯水，1 µg/L 与 100 ng/L 两档）中的 α(DDT/DDE)、α(DDT/DDD)、α(DDT/dicofol)；DDE 生成量监测（GC-MS SIM）；变温实验（4/25/60°C）解耦焓熵与验证"不转化"。
- **因果对照**: (a) 无碱位腔（消融第一基序）：预测 α(DDT/DDE) 回落至疏水基线；(b) 宽松腔（消融第二基序，-CCl3 亚腔放大为通用疏水腔）：预测 α(DDT/DDD) 回落；(c) 强碱腔（DBU 功能化，共轭酸 pKa ~12）：预测 DDT 被转化（DDE 生成），验证"弱碱=捕获不转化"设计逻辑；(d) 空白载体（无功能化 HCP）：扣除疏水基线贡献。

### DC1（动态对应，可选）：碱强度梯度门控的捕获-释放切换

- **生物特征**: GST 催化循环中 GSH 硫醇盐的 pKa 经活性位点微环境调谐（自由 GSH pKa ~9.2，酶结合态降至 ~6.5），实现"结合态高碱性强催化"与"游离态低活性"的切换。
- **材料实现（可选）**: pH 响应型碱位（如咪唑基，pKa ~6-7），在 pH 7 为弱碱（捕获不转化），在 pH < 4 质子化失去氢键能力（释放 DDT），实现温和酸洗再生。
- **注**: 此动态对应为可选增强，不作为方案通过必要条件；若声称须独立满足证据与因果对照标准。

## 4. 材料架构与选择性机制

### 4.1 材料架构

**骨架**: 刚性高交联共价有机框架（COF）或超交联聚合物（HCP），提供永久孔隙率与疏水腔体。候选构筑策略：

- **策略 A（COF）**: 以 1,3,5-三(4-氨基苯基)苯（TAPB）与 2,5-二甲基对苯二甲醛（Me2-TPA）缩合形成 β-酮胺连接 COF，孔径约 2.5-3.5 nm（推断，须 PXRD 与 BET 核验）；后合成修饰在孔壁引入位阻碱基团（TMP 基异氰酸酯接枝）与 -CCl3 互补亚腔（三氟甲基/三氯甲基功能化芳烃侧链）。
- **策略 B（HCP 笼）**: 以刚性四面体单体（如四(4-乙烯基苯基)甲烷）与功能化交联剂（含 TMP 基团的二乙烯基单体）Friedel-Crafts 超交联，形成微孔-介孔分级结构；-CCl3 亚腔由交联剂几何预组织。
- **策略 C（离散笼）**: 以亚胺缩合构筑四面体有机笼（如 4 个三醛 + 6 个二胺），笼内预装位阻碱与 -CCl3 互补壁面；笼外壁疏水化（全氟/全氯芳烃）增强水相驱动力。

**碱位设计（核心）**:
- 首选：2,2,6,6-四甲基哌啶（TMP）基团。共轭酸 pKa 10.7（水），位阻极大（四个甲基屏蔽氮），对 DDT 桥 C-H（pKa ~35-40）的 ΔpKa > 24，质子转移热力学完全禁止。TMP 氮孤对电子可与贫电子 C-H 形成弱氢键（C-H···N，估计 2-4 kJ/mol，推断）。
- 备选：1,8-双(二甲氨基)萘（质子海绵，DMAN）基团。共轭酸 pKa 12.1（水），但位阻构型使氮孤对电子指向腔内而非指向桥碳骨架，几何上阻止 E2 共面排列。
- 弱碱备选：六甲基苯（π 碱，共轭酸 pKa ~ -2），仅通过 π 电子云与桥 C-H 形成极弱 C-H···π 作用（~1-2 kJ/mol），完全无攫取风险。

**-CCl3 互补亚腔设计**:
- 几何：三氯甲基为四面体（C-Cl 键长 1.77 Å，Cl 范德华半径 1.75 Å，四面体角 109.5°），整体轮廓近似球径约 4.5-5.0 Å（推断，须 DFT 优化）。亚腔为刚性芳烃壁面围成的四面体凹陷，内壁与 -CCl3 三氯表面形成紧密范德华接触。
- 功能化（可选）：亚腔壁嵌入弱卤键受体（如吡啶-N-氧化物），与 -CCl3 氯的 σ-hole 形成弱卤键（Cl···O/N，估计 1-3 kJ/mol，推断；据 E14 Varadwaj 2020，脂肪族 C-Cl 卤键供体能力弱，贡献须实测）。

### 4.2 选择性机制（定量框架）

总结合自由能分解：
ΔG_bind(DDT) = ΔG_hydrophobic + ΔG_motif1(C-H···B) + ΔG_motif2(-CCl3 pocket) + ΔG_cooperativity

其中：
- ΔG_hydrophobic ≈ -39 kJ/mol（logKow 6.9 驱动，对 DDE/DDD 近似等值：-37/-34 kJ/mol）
- ΔG_motif1 ≈ -2 to -6 kJ/mol（DDT 特异；DDE = 0，DDD ≈ -1 to -3 kJ/mol 因 -CHCl2 氢酸性更强但几何不同）
- ΔG_motif2 ≈ -1 to -3 kJ/mol（DDT 特异；DDD = 0 因 -CHCl2 小于 -CCl3，DDE ≈ -1 kJ/mol 因 =CCl2 部分匹配）
- ΔG_cooperativity：双基序同时就位的协同增益（非加和项，须实验测定）

预测选择性因子（25°C）：
- α(DDT/DDE) = exp(ΔΔG/RT) ≈ exp((3-8)/2.48) ≈ 3-25
- α(DDT/DDD) = exp(ΔΔG/RT) ≈ exp((2-5)/2.48) ≈ 2-7
- α(DDT/dicofol) ≈ exp((2-6)/2.48) ≈ 2-11

诚实评估：选择性因子预计为中等水平（3-25 对 DDE，2-7 对 DDD），远低于离子交换或强氢键体系的选择性（10^2-10^4），但对于"无极性把手"的 DDx 桥三元组而言，任何 α > 2 均为文献空白区的突破（G1/G2）。

### 4.3 报告口径

- 总干复合体 mg/g（含骨架、碱位、亚腔功能化全部质量）
- 填充床 mg/mL（堆积密度实测）
- 可及位点密度：以 DDT 饱和吸附量/名义碱位负载量计算可及分数
- 空白载体贡献：无功能化 HCP/COF 的 DDT uptake 占总 uptake 百分比

## 5. 创新性检查清单逐项结论

### A. 机制创新
- [x] 选择性机制超越普通疏水分配、静电吸附或尺寸筛分：是。双基序反应性识别（C-H···B 弱氢键 + -CCl3 形状互补）为超越疏水分配的识别维度，且以"捕获不转化"区别于所有破坏性路线。
- [x] 可被因果对照推翻的新识别原理：是。消融对照（无碱位/宽松腔/强碱腔）可直接推翻双基序贡献。
- [x] 目标水质场景独特适用性：是。DDT 桥 C-H 为唯一可用的极性把手（虽极弱），双基序读出为自然界唯一已验证的 DDx 桥区分机制。

### B. 材料架构创新
- [x] 超越载体替换或孔径调参：是。碱位与 -CCl3 亚腔的预组织空间关系为新的功能位点排布方式。
- [x] 新空间组织方式：是。"反应性识别但不催化"的预组织位点为新材料概念。
- [x] 方法学贡献：是。"捕获不转化"设计哲学（弱碱 + 几何约束 + 低温）为反应性识别吸附剂的方法学新路径。

### C. 仿生转译创新
- [x] 超越官能团类比：是。非简单"放一个碱"，而是提取酶双基序几何约束与"碱强度阈值"原理。
- [x] 不可由常规化学直觉得到的设计原则：是。"弱碱识别桥氢而不攫取"的反直觉设计（常规思路：碱+酸性氢→反应）来自酶底物特异性原理的逆向转译。
- [x] 保留原型核心功能逻辑：是。双基序同时要求→双拒绝判别，与酶底物特异性逻辑同构。

### D. 选择性策略创新
- [x] 不可由单一物化参数单调解释：是。logKow 预测 DDT > DDE > DDD，但双基序预测 DDT > DDD ≈ DDE（DDD 有桥氢但无 -CCl3），非单调。
- [x] 至少两个正交识别维度协同：是。维度 1（C-H···B 弱氢键）× 维度 2（-CCl3 形状互补）正交。
- [x] 竞争物谱含结构近似物：是。DDE/DDD/dicofol/o,p'-DDT/methoxy-DDT/PCB-209/BDE-209。

### E. 先例区分
- [x] 系统先例检索完成：是。简报五路 + 本轮追加，DDT 反应性识别吸附剂零先例（G2）。
- [x] 与最近先例区别可被实验量化：是。最近先例为 Fe-SBA-15 非选择破坏（Wang 2012），本方案增量为选择性捕获（α 可测）与不转化（DDE 生成量可测）。
- [x] 增量足以支撑独立发表：是。零先例区（G1+G2），任何 α > 2 均为领域首次。

## 6. 台架合成 SOP 草图

### 6.1 策略 B（HCP 笼，首选，合成可行性最高）

**步骤 1：功能化单体合成**
- 单体 A（碱位单体）：4-乙烯基苄基-2,2,6,6-四甲基哌啶（TMP-St）。合成路线：4-乙烯基苄基氯 + TMP（K2CO3/DMF/60°C/12h）→ TMP-St。表征：1H NMR、MS。
- 单体 B（交联剂）：二乙烯基苯（DVB，工业级 80% 异构体混合物）。
- 单体 C（骨架单体）：四(4-乙烯基苯基)甲烷（TVPM）。合成路线：四(4-溴苯基)甲烷 + 乙烯基硼酸（Suzuki 偶联）。

**步骤 2：超交联聚合**
- 配比：TVPM:DVB:TMP-St = 1:4:1（摩尔比），无水 FeCl3 为 Lewis 酸催化剂（4 eq），1,2-二氯乙烷为溶剂，80°C/24h。
- 产物：HCP-TMP（含 TMP 碱位的超交联聚合物）。
- 洗涤：甲醇/水反复洗涤至无 Fe 残留（ICP-MS < 1 ppm），索氏提取 48h（二氯甲烷）去除低聚物。

**步骤 3：-CCl3 互补亚腔后修饰（可选）**
- HCP-TMP 与三氯乙酰氯 Friedel-Crafts 酰基化（AlCl3/CS2/0°C→RT/6h），在芳烃壁面引入 -COCCl3 侧链，形成三氯甲基互补凹陷。
- 还原：NaBH4/MeOH 将 -COCCl3 还原为 -CH(OH)CCl3（保留三氯甲基轮廓）。

**步骤 4：表征**
- BET 比表面积与孔径分布（N2 77K）
- PXRD（非晶态确认）
- 固体 13C CP/MAS NMR（TMP 碳信号 40-60 ppm）
- 元素分析（N% 定量碱位负载）
- TGA（热稳定性）

### 6.2 对照材料

- **NIP（无碱位）**：TVPM:DVB = 1:5（无 TMP-St），同条件聚合。
- **宽松腔**：TVPM:DVB:TMP-St = 1:4:1 但无 -CCl3 后修饰。
- **强碱腔**：以 DBU 功能化单体替代 TMP-St（4-乙烯基苄基-DBU），预测触发 E2 消除。
- **空白载体**：纯 DVB 超交联（无 TVPM、无 TMP）。

## 7. 实验与因果对照计划

### 7.1 批次竞争吸附（核心实验）

**条件**: 超纯水，25°C，pH 7（10 mM 磷酸盐缓冲），固液比 1 g/L。
**分析物**: p,p'-DDT、p,p'-DDE、p,p'-DDD、dicofol、o,p'-DDT、methoxy-DDT（各 1 µg/L 等摩尔混合）。
**竞争物**: PCB-209（1 µg/L）、BDE-209（1 µg/L）、γ-HCH（1 µg/L）、dieldrin（1 µg/L）。
**时间序列**: 0.5/1/2/4/8/24/48/72h。
**检测**: GC-MS/MS（EI-SIM），内标 13C12-DDT。
**计算**: Kd = qe/Ce（L/kg）；α(A/B) = Kd(A)/Kd(B)。

### 7.2 ng/L 工况验证

**条件**: 超纯水加标 0.5/5/50 ng/L DDT（含等浓 DDE/DDD），固液比 5 g/L（增大固液比补偿低浓度）。
**检测**: 大体积进样 GC-MS/MS 或 LDPE 被动采样预浓缩后分析。
**判据**: Kd(DDT) ≥ 10^4 L/kg 且 α(DDT/DDE) ≥ 3。

### 7.3 "捕获不转化"验证（关键）

**条件**: DDT 1 µg/L + HCP-TMP 1 g/L，超纯水，25°C/4°C/60°C，pH 7，接触 7 天。
**检测**: 每 24h 取样分析 DDT（残余）+ DDE（产物）+ DDD（产物）。
**判据**: DDE 生成 < 0.1%（mol/mol）at 25°C/7d；若 > 1% 则设计失败。
**强碱对照**: DBU 功能化材料同条件，预测 DDE 生成 > 10%（验证检测灵敏度）。

### 7.4 消融对照实验

| 材料 | 预测 α(DDT/DDE) | 预测 α(DDT/DDD) | 逻辑 |
|---|---|---|---|
| HCP-TMP（完整） | 3-25 | 2-7 | 双基序完整 |
| NIP（无碱位） | 1-2 | 1-2 | 仅疏水基线 |
| 宽松腔（无 -CCl3 亚腔） | 2-10 | 1-2 | 仅第一基序 |
| 强碱腔（DBU） | N/A（DDT 被转化） | N/A | 验证"弱碱=不转化" |
| 空白载体 | 1-1.5 | 1-1.5 | 纯疏水 |

### 7.5 真实基质验证

**条件**: 二级出水（DOC 5-15 mg/L，SS < 10 mg/L）加标 DDT/DDE/DDD 各 50 ng/L。
**对照**: 超纯水同浓度平行。
**判据**: α(DDT/DDE) 在二级出水中保持 ≥ 2（允许因 DOC 竞争下降但不消失）。

### 7.6 再生循环

**条件**: 饱和 HCP-TMP → 甲醇/水（20:80）洗涤 3 次 → 超纯水置换 → 再吸附。
**循环**: 5 次。
**判据**: 第 5 次 α(DDT/DDE) 保持初始值 ≥ 80%；DDE 生成仍 < 0.1%。

### 7.7 变温热力学

**条件**: 4/15/25/40/60°C，DDT/DDE 二元竞争，超纯水。
**分析**: van't Hoff 图（ln α vs 1/T）→ ΔΔH、ΔΔS。
**判据**: ΔΔH < 0（放热，低温有利）且 |ΔΔH| > 5 kJ/mol（超越实验误差）。

## 8. 成功与失败判据（可证伪）

### 通过判据（全部满足）

1. α(DDT/DDE) ≥ 3（超纯水，1 µg/L，25°C）
2. α(DDT/DDD) ≥ 2（同上）
3. Kd(DDT) ≥ 10^4 L/kg（ng/L 工况）
4. DDE 生成 < 0.1%（25°C/7d）
5. 消融对照：NIP 的 α(DDT/DDE) < 2（证明碱位贡献显著）
6. 二级出水中 α(DDT/DDE) ≥ 2

### 失败判据（任一触发终止）

1. α(DDT/DDE) < 1.5（双基序无显著贡献）
2. DDE 生成 > 1%（"捕获不转化"失败）
3. NIP 与功能化材料 α 无统计差异（p > 0.05，t 检验）
4. Kd(DDT) < 10^3 L/kg（亲和力不足）
5. 5 次再生后 α 衰减 > 50%（位点不稳定）

### 灰色地带（触发修订而非终止）

- α(DDT/DDE) 在 1.5-3 之间：选择性存在但弱，须收窄声称或叠加卤键维度
- DDE 生成 0.1-1%：部分转化，须降低碱强度或温度
- 二级出水中 α 降至 1.5-2：DOC 竞争显著但机制未消失，须优化抗污堵

## 9. 攻击预判与诚实风险评估

### 9.1 最大未决风险："捕获不转化"的长期稳定性

虽然热力学分析（ΔpKa > 24）强烈支持不转化，但以下场景可能破坏：
- 局部微环境 pH 偏移（腔内疏水域的有效介电常数低，pKa 标度可能偏移 5-10 个单位）
- 光催化副反应（UV 暴露下 C-Cl 均裂）
- 长期累积效应（数月运行中痕量 DDE 生成逐渐积累）
- 碱位降解（TMP 氧化为硝roxide 后碱强度改变）

**缓解**: 避光操作、定期 DDE 监测、碱位抗氧化设计（HALS 稳定化）。

### 9.2 选择性量级的诚实预期

ΔΔG_motif 预计 3-8 kJ/mol，对应 α 3-25。这是"可测但温和"的选择性，远低于酶（kcat/Km 差异可达 10^4-10^6）。对于"无极性把手"的 DDx 体系，这已是文献空白区的突破，但须诚实声称：本方案的选择性为"结构判别级"（可区分 DDT 与 DDE/DDD），而非"分离纯化级"（不能从等摩尔混合物中定量分离 DDT）。

### 9.3 水相弱氢键的竞争水化

C-H···N 弱氢键（2-6 kJ/mol）在水相中面临水分子的竞争（水-氮氢键约 5-10 kJ/mol）。但疏水腔内的去溶剂化环境（低介电、无水分子）可显著削弱竞争。关键假设：腔内碱位在 DDT 进入前不被水分子占据（去润湿腔设计）。须以对照实验（亲水腔 vs 疏水腔）验证。

### 9.4 与 S20（A04）终止教训的对照

S20 因"形状读出不可与 DDE 共轭极化率隔离"而终止。本方案的区别：
- 选择性来源不仅是形状（-CCl3 轮廓），更是弱氢键（C-H···B）——后者为 DDE 完全缺失（无桥氢），不存在"极化率混杂"问题。
- DDD 对照仍为关键检验：DDD 有桥氢（可形成 C-H···B）但无 -CCl3（亚腔失配），若 α(DDT/DDD) > 1 则证明第二基序贡献独立于第一基序。

## 10. 证据完整性与核验状态汇总

| 编号 | 核验状态 | 层级 |
|---|---|---|
| E1 Clark 1984 | metadata_verified | 一手（酶学） |
| E2 Sternburg 1954 | metadata_verified | 一手（原始发现） |
| E3 GSTe2 2005 | metadata_verified | 一手（功能） |
| E4 Lipke 1959 | metadata_verified | 一手（动力学） |
| E5 McLennan 1972 | metadata_verified | 一手（物理有机） |
| E6 Wang 2008 | metadata_verified | 一手（结构） |
| E7 Kallman 1963 | abstract_read | 一手 |
| E8 Hale 2009 | abstract_read | 一手 |
| E9 Montuori 2020 | verified（全文） | 一手（监测） |
| E10 Makgoba 2024 | verified（全文） | 综述 |
| E11 PPDB | verified（页面） | 数据库 |
| E12 Cram 1986 | metadata_verified | 权威综述 |
| E13 Politzer 2010 | metadata_verified | 权威综述 |
| E14 Varadwaj 2020 | abstract_read | 一手（计算） |

诚实声明：本方案无全文 verified 的酶学/结构文献（E1-E6 均为 metadata_verified），活性位点几何数值与底物特异性定量参数须全文核验。设计假设（弱氢键能量、pKa 阈值、协同性）均为推断，须实验验证。

## 11. 自评分

| 维度 | 满分 | 得分 | 理由 |
|---|---|---|---|
| 因果闭环 | 20 | 15 | 双基序→双拒绝逻辑完整，消融对照设计严密；但"捕获不转化"的长期稳定性与腔内微环境 pKa 偏移为未闭合环节 |
| 选择性机制 | 25 | 19 | 双基序正交设计超越疏水分配，DDE/DDD/dicofol 三角验证有力；但 ΔΔG 量级温和（3-8 kJ/mol），α 预计 3-25 而非 10^2+，水相弱氢键竞争水化为未解风险 |
| 可转译性 | 20 | 14 | HCP 合成路线成熟、碱位功能化可行；但 -CCl3 亚腔精度控制（±0.5 Å）在超交联聚合物中难以保证，离散笼路线合成复杂度高 |
| 原创性 | 15 | 14 | DDT 反应性识别吸附剂零先例（G2），"捕获不转化"设计哲学为领域新概念；仿生转译逻辑（酶底物特异性→弱碱识别）非显而易见 |
| 可证伪 | 10 | 9 | 失败判据明确（α < 1.5、DDE > 1%、NIP 无差异），消融对照完备；灰色地带处理规则预设 |
| 证据 | 10 | 6 | 酶学核心文献（E1-E6）均为 metadata_verified 而非全文 verified；McLennan 1972 全文未取得（pKa 阈值为推断）；GSTe2 结构几何数值为推断 |
| **总分** | **100** | **77** | |

**最大未决风险**: 腔内疏水微环境的有效介电常数极低（ε ~ 2-4），可能使碱的共轭酸 pKa 偏移 5-15 个单位（水相 pKa 10.7 的 TMP 在低介电环境中有效碱强度可能显著升高），从而部分侵蚀"捕获不转化"的安全裕度。此风险无法仅凭溶液化学数据排除，须以材料原位光谱（固态 15N NMR、IR 探针）与 DDE 生成动力学实验直接验证。

**已验证引文（含 DOI/层级）**:
- Clark 1984: 10.1016/0048-3575(84)90018-x, metadata_verified
- Sternburg 1954: 10.1021/jf60042a008, metadata_verified
- GSTe2 2005: 10.1016/j.ibmb.2005.03.008, metadata_verified
- Lipke 1959: 10.1016/S0021-9258(18)69878-3, metadata_verified
- McLennan 1972: EPA HERO 2147592, metadata_verified
- Wang 2008: 10.1016/j.jmb.2008.09.010, metadata_verified
- Cram 1986: 10.1002/anie.198610391, metadata_verified

**建议**: **revise**。总分 77 低于通过线 85。主要失分在证据完整性（核心酶学文献未全文核验）与可转译性（-CCl3 亚腔精度控制）。修订方向：(1) 全文核验 E4 Lipke 1959 与 E6 Wang 2008 以获取底物特异性定量参数与活性位点几何；(2) 以 DFT 计算（B3LYP-D3/def2-TZVP）标定 C-H···TMP 氢键能与 E2 过渡态能垒；(3) 收窄材料架构至离散笼（策略 C）以提升几何精度；(4) 补充低介电环境 pKa 偏移的定量估算（Born 方程或连续介质模型）。
