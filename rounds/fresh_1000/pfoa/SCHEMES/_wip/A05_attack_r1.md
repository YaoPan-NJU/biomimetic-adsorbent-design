# S01_A05 攻击报告（第 1 轮）

攻击者上下文：只读 SPEC.md、BRIEF.md、INNOVATION_CHECKLIST.md 与方案全文。未读设计者隐藏推理。联网核验经 Crossref 与 OpenAlex API 完成。

## 一、DOI 抽查结果（e 证据有效性）

共抽查 9 条 DOI，8 条确认存在且标题/期刊/年份与方案主张一致，1 条未能独立定位。

| 编号 | DOI | 核验途径 | 结果 |
|---|---|---|---|
| E1 | 10.1021/jacs.8b09842 | Crossref | 存在。Cotruvo, JACS, 2018 线上/2018 卷。标题 "Lanmodulin: A Highly Selective Lanthanide-Binding Protein..." 匹配。 |
| E2 | 10.1021/acs.biochem.8b01019 | Crossref | 存在。Cook, Biochemistry, 2018 线上/58 卷 2019。标题 "Structural Basis for Rare Earth Element Recognition by Methylobacterium extorquens Lanmodulin" 匹配。 |
| E3 | 10.1039/d1cp03628a | OpenAlex | 存在。Featherston & Cotruvo, PCCP, 2021。标题 "Lanthanide-dependent coordination interactions in lanmodulin: a 2D IR and molecular dynamics simulations study" 匹配。 |
| E4 | 10.1039/d2qi00933a | Crossref | 存在。Inorg Chem Front, 2022。标题 "Lanmodulin peptides – unravelling the binding of the EF-Hand loop sequences stripped from the structural corset" 匹配。 |
| E5 | 10.1038/s41586-023-05945-5 | Crossref | 存在。Mattocks, Nature, 2023。标题 "Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer" 匹配。 |
| PCN-999 | 10.1021/jacs.3c14487 | Crossref | 存在。JACS, 2024。标题 "Exceptionally High Perfluorooctanoic Acid Uptake in Water by a Zirconium-Based Metal-Organic Framework through Synergistic Chemical and Physical Adsorption" 匹配。 |
| Fe-MOF-808 | 10.1021/jacs.5c23392 | OpenAlex | 存在。JACS, 2026。标题 "Atomically Precise Engineering of Synergistic Binding Sites in a Zirconium Metal-Organic Framework for the Capture of Perfluorooctanoic Acid"。摘要确认 "Fe-MOF-808, a novel porous material obtained by incorporating binuclear iron species into the Zr6O8 nodes of the MOF-808 framework"，与方案描述一致。Crossref 未收录（可能因 2026 年新刊）。 |
| ACS Omega | 10.1021/acsomega.5c05815 | OpenAlex | 存在。ACS Omega, 2025。标题 "Influence of Charge Compensating Anions on the Adsorption of Perfluorobutanesulfonate in MOF-808" 匹配。Crossref 未收录。 |
| Adv Funct Mater | 10.1002/adfm.202409932 | Crossref | 存在。AFM, 2024。标题 "Chemically Tailored Metal-Organic Frameworks for Enhanced Capture of Short- and Long-Chain Per- and Polyfluoroalkyl Substances from Water" 匹配。 |
| Zr-PTA (Angew 2026) | 方案未给 DOI | 检索未命中 | 无法独立核验。方案已标注此风险（W3、W9）。 |

结论：方案证据引用在存在性层面可靠，未发现编造或错配。核心 LanM 五条证据（E1-E5）全部确认。先例文献全部确认。唯一缺口为 Zr-PTA（Angew 2026）无 DOI、未能定位，方案已如实标注。所有核验仍为摘要/题录级，全文未读，方案已如实声明。

## 二、致命与严重缺陷

### C1（critical）热力学反转：LanM 预组织原则的电荷维度在转译中被倒置

方案声称转译 LanM 的"预组织与几何约束主导选择性"原则，且该选择性"不依赖电荷"。但 LanM 的实际选择性方向是：预组织羧酸配体阵列偏好高电荷 Ln3+（3+），拒绝低电荷 Ca2+（2+）。10^8 选择因子中，电荷差（3+ vs 2+）是主要热力学贡献之一；E1（Cotruvo 2019）的 Pro→Ala 突变实验表明，预组织主要贡献于拒绝 Ca2+（Ca 响应从 mM 移至 μM），而 Ln3+ 皮摩尔亲和力在突变后保留，说明 Ln3+ 结合本身有强静电与配位化学基础，预组织是选择性的放大器而非唯一来源。

方案的 MOF 转译要求：预组织 Zr 口袋偏好低电荷羧酸根（-1），拒绝高电荷硫酸根（-2）。这与 LanM 的选择性方向在电荷维度上完全反转。LanM 的预组织放大静电 discrimination（偏好更高电荷）；方案要求预组织克服静电 discrimination（偏好更低电荷）。方案将此框架为"不依赖电荷"，但实际上硫酸根（-2）对 Zr(IV)（硬酸）的静电与 HSAB 优势是必须被克服的热力学障碍，而非可忽略的背景。

这不是"零假设可能成立"的概率问题，而是转译逻辑的结构性缺陷：方案提取的"原则"（预组织控制选择性）在原型中沿电荷梯度方向工作，在转译中必须逆电荷梯度工作，而方案未提供任何机制解释为何同一原则在反转方向上仍然有效。

### C2（critical）零假设 H0 大概率成立，方案核心机制建立在逆已知配位化学的方向上

Zr(IV) 是经典硬酸，硫酸根与磷酸根是经典硬碱。Zr(IV) 对磷酸根/硫酸根的强亲和力是分析化学与环境工程中的已知事实（锆基除磷除砷材料文献体量极大）。方案自身的 W1 承认"硫酸根与磷酸根等硬碱含氧阴离子与 Zr 开放位强结合属已知配位化学倾向"，并将 F1 设为失败判据。但方案将这一近乎确定的配位化学事实处理为"待检验假设"，而非机制设计的硬约束。

具体而言，方案提出的几何窗口依据为羧酸根 O-O 约 2.2 Å（双齿螯合）对硫酸根 O-O 约 2.4 Å（四面体），差异仅 0.2 Å。Zr(IV) 离子半径 0.72 Å（CN=6）至 0.84 Å（CN=8），Zr-O 键长约 2.0-2.2 Å，配位数 6-8 可变，配位几何柔性远高于 EF-hand 蛋白折叠位点。0.2 Å 的 O-O 差异远在 Zr(IV) 配位球自然柔性范围之内，不足以产生显著的几何选择。LanM 的 EF-hand 位点由蛋白骨架刚性约束（脯氨酸约束、结构支架），配体位置精度在 0.1 Å 量级；MOF-808 的 Zr 开放位由 μ3-O/μ3-OH 桥连的 Zr6 簇提供，配位几何远不如蛋白位点精确。类比在结构精度层面不成立。

方案的核心假设 H1 需要同时克服：(1) 硫酸根的电荷优势（-2 vs -1），(2) 硫酸根的 HSAB 硬度优势，(3) 硫酸根在 mM 浓度对 PFOA 在 ng/L 的 10^6-10^9 摩尔比优势。仅靠封端配体刚性变化（甲酸→苯甲酸→4-甲基苯甲酸）产生的预组织度差异，无法克服这三重劣势。

## 三、严重缺陷（high）

### H1 先例饱和：JACS 2026 Fe-MOF-808 已实现"原子精确工程化协同结合位点"

经 OpenAlex 核验，doi:10.1021/jacs.5c23392 标题为 "Atomically Precise Engineering of Synergistic Binding Sites in a Zirconium Metal-Organic Framework for the Capture of Perfluorooctanoic Acid"，摘要确认在 MOF-808 的 Zr6O8 节点掺入双核铁物种以工程化协同结合位点。该论文与方案的核心概念（在 Zr-MOF 节点上工程化结合位点以选择性捕获 PFOA）高度重叠。方案声称的三项增量区别（预组织刚性系列、ng/L 头基族选择因子、D1 对 D2 定量分解）均为同一平台上的增量实验，而非新概念。

加上 PCN-999（JACS 2024，开放位容量机制）、化学裁剪 MOF（Adv Funct Mater 2024）、MOF-808 阴离子效应（ACS Omega 2025），Zr-MOF 捕 PFOA 的先例密度在 2024-2026 已达四篇以上高水平期刊。方案的增量窗口极窄。E 维度（先例区分）判定为不通过或边界不通过。

### H2 几何窗口的结构基础薄弱

方案将 LanM 的"预组织几何约束"转译为"封端配体刚性控制 Zr 位配位几何"。但 LanM 的几何约束来自蛋白骨架对四个 EF-hand 环的精确空间定位（脯氨酸约束、甘氨酸介导的局部构象、相邻 EF-hand 融合），配体羧酸基团的位置由蛋白三级结构决定，精度在亚埃量级。MOF-808 的 Zr 开放位由 Zr6O4(OH)4 簇的 μ3-OH 位提供，封端配体（甲酸根、苯甲酸根）通过 Zr-O 键配位，其位置由簇的晶体学对称性决定，封端交换改变的是配体体积与电子效应，而非配位几何的精确预组织度。

将"甲酸→苯甲酸→4-甲基苯甲酸"封端系列等同于"预组织度梯度"是概念性过度延伸。甲酸与苯甲酸的区别主要是位阻与疏水性，而非"柔性 vs 刚性"对配位几何的约束。苯甲酸根与 4-甲基苯甲酸根的刚性差异可忽略（两者均为刚性芳基），该系列实际上主要检验的是位阻效应而非预组织度。

### H3 单齿结合模式瓦解几何窗口论证

方案的几何窗口论证依赖羧酸根的双齿螯合配位（O-O 约 2.2 Å 匹配预组织口袋）。但 PFOA 的 C7F15 全氟尾链体积大（范德华截面约 5-6 Å），在 Zr 开放位上形成显著位阻，不利于双齿螯合配位。更可能的结合模式为单齿配位（一个羧酸氧与 Zr 结合，另一个氧朝向溶剂）。若 PFOA 以单齿模式结合，则不存在 O-O 匹配要求，"几何窗口"论证的核心结构基础消失。

方案提及"单齿或双齿配位"但未区分两种模式下几何窗口论证的有效性差异。若为单齿，D1 轴退化为普通的 Zr-羧酸根配位化学（硬酸-硬碱），不再具有"几何窗口"新意。

## 四、中等缺陷（medium）

### M1 仿生原则非 LanM 独有

"预组织控制选择性"是超分子化学教科书原则（Cram 1988 诺贝尔演讲、Lehn 1990），远早于 LanM 的发现（2018）。方案声称该原则"非常规化学直觉可得"，但预组织原则在冠醚、穴醚、环糊精、分子印迹等领域已被广泛认知和应用 35 年以上。LanM 是该原则在稀土识别中的一个生物实例，但原则本身并非 LanM 特有。

方案的仿生转译创新（C 维度）判定为边界：转译方向（蛋白预组织→MOF 封端预组织）有一定新意，但底层原则不构成"不可由常规化学直觉得到"的设计原则。

### M2 封端刚性系列混杂变量未分离

甲酸→乙酸→苯甲酸→4-甲基苯甲酸系列同时改变：(1) 配体体积（甲酸 < 乙酸 < 苯甲酸 ≈ 4-甲基苯甲酸），(2) 疏水性（甲酸亲水 < 苯甲酸疏水），(3) 电子效应（pKa：甲酸 3.75、乙酸 4.76、苯甲酸 4.20、4-甲基苯甲酸 4.34），(4) 位阻（甲酸最小、苯甲酸/4-甲基苯甲酸最大）。方案将此系列解释为"预组织度梯度"，但实验观测到的任何摄取差异无法归因于单一变量。方案的因果对照设计（"同框架、同 Zr 含量、同孔结构、仅封端刚性不同"）在实际中不成立：封端交换改变的不只是刚性。

### M3 D2 轴（疏水腔）合成可行性为设计假设

氨基均苯三甲酸（H3BTC-NH2）与 H3BTC 混合连接体共合成 MOF-808 时，氨基可能在溶剂热条件下配位 Zr(IV)，干扰节点组装或改变拓扑。后合成酰化（丙酸酐/苯甲酰氯）在 MOF 孔道内的扩散与反应均匀性未经验证。方案已标注 F5 失败判据，但 D2 轴失败后方案退化为单轴 D1（几何窗口），而 D1 本身面临 C1/C2/H2/H3 的根本性质疑。

### M4 选择性声称的 D 维度存在循环论证

方案声称"选择性不可由单一物化参数单调解释"，并以"logKow 不能解释 PFOA 对 PFOS 差异、电荷不能解释羧酸根对硫酸根反转"为据。但后者恰恰是问题所在：电荷（与 HSAB 硬度）确实预测硫酸根结合更强，而方案需要几何窗口克服这一预测。如果几何窗口不存在（H0 成立），则选择性确实可被单一参数（电荷/硬度）单调解释——方向与方案期望相反。D 维度的"通过"取决于 H1 是否被实验拒绝，而非先验成立。

## 五、轻微缺陷（low）

### L1 证据层级

E1-E4 为摘要核验、全文未读。摘要中的定量主张（10^8 选择因子、微摩尔 vs 皮摩尔、约 10^6 下降）在全文中可能有更精确的限定条件。E5 为元数据核验。多数先例为元数据或摘要核验。方案已如实标注，不构成造假，但影响证据完整性得分。

### L2 工程可行性

(a) 5000 BV 在 ng/L 尺度对 MOF 材料极为苛刻。MOF-808 孔窗约 6-8 Å 与 PFOA 截面约 5-6 Å 接近（方案 W4），颗粒内扩散可能严重限速，EBCT 5-10 min 可能不足。(b) NaOH 再生液对 MOF-808 节点的长期影响：Zr-O 键在强碱下可水解，封端交换后的位点稳定性可能低于母体。(c) Zr 浸出判据 10 μg/L 在多次碱再生循环后可能难以满足。(d) Zr 基材料成本高（ZrOCl2·8H2O + DMF 溶剂热 + 多步封端交换），与 β-CD 聚合物或 GAC 相比经济性差。

### L3 Zr-PTA（Angew 2026）先例未核验

方案 W3 已标注。若该先例已含头基几何选择性主张，则 E 维度直接不通过。本轮检索未能定位该文献。

### L4 方案自评分 67/100 的诚实性

方案自估 67 分，低于 85 通过线，主要扣分项（零假设不利、先例饱和、全文核验缺口）与本攻击报告的核心发现一致。自评分基本合理，可能略高（因果闭环与选择性机制两项在 C1/C2 成立的前提下应进一步扣分）。

## 六、先例检索补充（f 维度）

经 OpenAlex 与 Crossref 系统检索，Zr-MOF 捕 PFOA/PFAS 的 2024-2026 先例至少包括：

1. PCN-999（JACS 2024, doi:10.1021/jacs.3c14487）：开放位 + 物理吸附增强，1089 mg/g（mg/L 级）
2. Fe-MOF-808（JACS 2026, doi:10.1021/jacs.5c23392）：Zr6O8 节点掺双核铁，原子精确工程化协同结合位点，2081/3120 mg/g
3. 化学裁剪 MOF（Adv Funct Mater 2024, doi:10.1002/adfm.202409932）：短链与长链 PFAS
4. MOF-808 阴离子效应（ACS Omega 2025, doi:10.1021/acsomega.5c05815）：电荷补偿阴离子影响 PFBS 吸附
5. 介孔 Zr-MOF 摄 PFOS（Inorg Chem 2019, doi:10.1021/acs.inorgchem.9b00380）：方案引用，元数据核验
6. Zr-PTA（Angew 2026）：未能独立核验

其中第 2 条（Fe-MOF-808）与方案概念重叠度最高：同为 MOF-808 平台、同为节点工程化、同为选择性 PFOA 捕获。方案的增量贡献（封端刚性系列作为因果工具）是在已发表平台上的增量实验设计，独立发表性判定为不通过或严重边界。

## 七、总体判定

方案在证据诚实性、实验设计规范性、失败判据可证伪性方面表现良好（对应陷阱 5、6、8、9、11 的处理均合规）。竞争物矩阵设计合理，报告口径强制要求正确。

但方案的核心机制（预组织配位几何窗口）存在两个 critical 级结构缺陷：(1) LanM 原则的电荷维度在转译中被倒置，方案未提供反转有效的机制论证；(2) Zr(IV) 对硫酸根/磷酸根的已知强亲和力构成近乎确定的热力学障碍，0.2 Å O-O 差异与封端刚性变化不足以克服。方案自身将零假设设为"大概率成立"（W1），但仍在核心机制设计中将其处理为待检验假设而非硬约束，导致整个 D1 轴的科学基础不稳。

先例饱和（high）进一步压缩增量窗口。在 Fe-MOF-808（JACS 2026）已实现"原子精确工程化协同结合位点"的前提下，封端刚性系列的增量贡献不足以支撑独立发表。

建议：方案需从根本上重新审视 D1 轴的机制方向。若坚持 Zr-MOF 平台，可能需要将选择性来源从"几何窗口克服电荷"转为"利用羧酸根与磺酸根在 Zr 位配位模式的已知差异"（单齿/双齿 vs 单齿，配位键数差异），但这将削弱仿生转译深度。或者，放弃 Zr-MOF 平台，转向配位几何更精确可控的人工受体（如分子印迹、共价有机框架的定向孔道），但将失去 MOF-808 平台的先例对照优势。
