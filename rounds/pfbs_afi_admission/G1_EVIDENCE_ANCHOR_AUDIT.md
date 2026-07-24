# G1 证据锚点审计报告(PFBS-AFI-GAC / R1a)

- 门禁:门 1 证据锚点定位检查,依据《方案准入门禁规范》草案 v0.1 第三节
- 方案文档:`rounds/pfbs_afi_admission/R1A_SCHEME_CONCEPT.md`(2026-07-19)
- 台账基线:`research/evidence/evidence_ledger.csv`,编号连续占用至 E061;新增建议自 E062 起,无冲突
- 执行:门 1 检查员(隔离上下文),2026-07-19;本报告不含隐式推理,只含判定表与结论
- 产出文件(建议路径):`rounds/pfbs_afi_admission/G1_EVIDENCE_ANCHOR_AUDIT.md`

## 检索边界声明

本检查以 Crossref API 与 PubMed E-utilities 核实题录,以公开网络检索定位候选文献。无 SciFinder 权限;Crossref 或 PubMed 阴性结果不作为任何文献的最终不存在证明。ACS 与 Wiley 出版商页面在本执行环境返回 403/402,相关两条题录(ACS ES&T Water、AWWA Water Science)已核实而摘要未能在线读取,如实标注。全部内容级数值标注"待全文核验"。网络检索给出的题录线索有两条经核实为错误或不可定位,已剔除并记录于第三节,检索线索未经核实不得落账。

## 一、承重定量值与事实声明清单

| 编号 | 声明(摘自概念简报) | 承重角色 |
|---|---|---|
| C1 | PFBS 在 GAC 床突破 5,000-20,000 BV,长链 100,000-300,000+ BV;v2 评估已记录 E028 错配,须改引全规模柱研究 | 痛点基线;门 3 需求倒推输入 |
| C2 | DOM 竞争吸附与孔口污堵使短链 PFAS 有效床寿命进一步缩短;存亡阈值:DOM 归因损失 ≥2× | 门 3 存亡变量;性能目标 m=2-4× 的相容性前提 |
| C3 | 聚 MPC 或等效两性离子水合界面抑制蛋白质与大分子非特异粘附 | 仿生原理承重事实 |
| C4 | 两性离子水合层允许小离子与小溶质跨层渗透(约 300 Da 阴离子情形直接证据方案自标待查) | 材料可行性承重事实;约束目标 ≥85% 容量保持的前提 |
| C5 | MPC 单体与接枝成本量级(方案设为门 1 待核锚点,未声称具体数值) | 成本约束(复合介质成本比 ≤6)输入 |
| C6 | 两性离子层在高离子强度下保持抗污(总体电中性,预期无硫酸根脆性) | 排除阳离子路线的替代正当性 |
| C7 | 阳离子与胍基路线在 1 mM 硫酸根中崩溃 | 排除清单依据;台账已有 E056/E058/E059,无需新锚点 |
| C8 | 生物原型为细胞膜磷脂酰胆碱两性离子头基强水合界面 | 仿生身份声明;支撑证据链为聚 MPC 涂层抗污记录 |

## 二、锚点审计表

状态图例:全文核验 / 题录摘要级待全文核验 / 无法定位 / 错配。

### C1 PFBS 与长链 PFAS 的 GAC 突破体积区间

| 定位文献 | 题录核实 | 方法学一致性 | 状态 |
|---|---|---|---|
| Appleman TD, Higgins CP, Quiñones O, Vanderford BJ, Kolstad C, Zeigler-Holady JC, Dickenson ERV. Treatment of poly- and perfluoroalkyl substances in U.S. full-scale water treatment systems. Water Research 51 (2014) 246-255. DOI 10.1016/j.watres.2013.10.067 | Crossref 与 PubMed(PMID 24275109)一致 | 美国全规模水厂 GAC 滤床调查,方法学与"全规模柱研究"要求一致;摘要确认去除率随链长变化、短链去除差;PFBS 专属突破 BV 数值在全文,摘要未列 | 题录摘要级待全文核验 |
| McCleaf P, Englund S, Östlund A, Lindegren K, Wiberg K, Ahrens L. Removal efficiency of multiple PFASs in drinking water using GAC and anion exchange column tests. Water Research 120 (2017) 77-87. DOI 10.1016/j.watres.2017.04.057 | Crossref 与 PubMed(PMID 28478297)一致 | 中试规模 GAC/AE 柱,含 PFBS/PFHxS/PFOS,运行 217 天;摘要确认突破时间随链长增加、短链先突破并出现解吸;具体 BV 数值在全文图表 | 题录摘要级待全文核验 |

一致性说明:v2 评估 C-5 项记录的错配(E028 为 Carter and Farrell 2010 批量等温研究,无床体积数据)由本审计改引柱研究修复;Appleman 2014 为全规模,McCleaf 2017 为中试规模,引用时须区分。区间上端"300,000+ BV"在两条摘要中均未出现,全文核验前不得作为已核实值使用。历史错配状态:错配已修复(改引路径成立)。

### C2 DOM 归因床寿命损失(存亡变量)

| 定位文献 | 题录核实 | 方法学一致性 | 状态 |
|---|---|---|---|
| Tajdini B, Vatankhah H, Murray CC, Liethen A, Bellona C. Impact of effluent organic matter on perfluoroalkyl acid removal from wastewater effluent by granular activated carbon and alternative adsorbents. Water Research 241 (2023) 120105. DOI 10.1016/j.watres.2023.120105 | Crossref 与 PubMed(PMID 37270948)一致 | 二级出水 GAC 柱;摘要确认 EfOM(分子量 100-1000 Da)与 PFAA 竞争、孔缩窄与孔口堵塞加直接位点竞争机制;O3-BAF 预处理改善 PFAA 去除,说明存在可恢复的 EfOM 归因损失;损失倍数数值在全文 | 题录摘要级待全文核验 |
| Vatankhah H, Tajdini B, Milstead RP, Clevenger E, Murray C, Knappe D, Remucal CK, Bellona C. Impact of ozone-biologically active filtration on the breakthrough of perfluoroalkyl acids during granular activated carbon treatment of municipal wastewater effluent. Water Research 223 (2022) 118988. DOI 10.1016/j.watres.2022.118988 | Crossref 与 PubMed(PMID 36007399)一致 | 市政污水二级出水 GAC 柱,SEC 与 FT-ICR-MS 表征 EfOM;摘要确认预处理改善 GAC 对 PFAA 的去除与突破行为 | 题录摘要级待全文核验 |
| Mortazavian S, Hooper J, Abusallout I, Hofmann R. Granular Activated Carbon for PFAS Removal in Municipal Wastewater: A Rapid Small-Scale Column Test Study. ACS ES&T Water 5 (2025) 2145-2154. DOI 10.1021/acsestwater.4c00919 | Crossref 核实;出版商页 403,摘要未取 | 市政污水 RSSCT,直接对应本方案应用场景;内容待取 | 题录已核实,摘要与全文待核验 |
| Tang, Knappe D, Meng. Dissolved Organic Matter and Pretreatment Effects on PFAS Removal by Granular Activated Carbon. AWWA Water Science(2026-04-28 上线). DOI 10.1002/aws2.70053 | Crossref 核实;出版商页 402,摘要未取 | 题名即 DOM 与预处理对 GAC 除 PFAS 的影响,方向完全对口;内容待取 | 题录已核实,摘要与全文待核验 |
| Gagliano E, Sgroi M, Falciglia PP, Vagliasindi FGA, Roccaro P. Removal of poly- and perfluoroalkyl substances (PFAS) from water by adsorption: Role of PFAS chain length, effect of organic matter and challenges in adsorbent regeneration. Water Research 171 (2020) 115381. DOI 10.1016/j.watres.2019.115381 | Crossref 核实 | 综述,链长效应与有机质效应的综合证据源 | 题录摘要级待全文核验 |
| Kothawala DN, Köhler SJ, Östlund A, Wiberg K, Ahrens L. Influence of dissolved organic matter concentration and composition on the removal efficiency of perfluoroalkyl substances during drinking water treatment. Water Research 121 (2017) 320-328. DOI 10.1016/j.watres.2017.05.047 | Crossref 与 PubMed(PMID 28570871)一致 | 批量预平衡实验,非柱研究,不得用作床寿命证据;摘要报告 GAC 除 PFAS 对 DOM 的响应随 DOM 类型与链长变化,部分情形下 DOM 存在反而提高去除,显示方向异质性 | 题录摘要级待全文核验;方法学限用标注 |

辅助定位(可选落账):Velten 2011 Water Research(DOI 10.1016/j.watres.2011.04.047,NOM 在 GAC 吸附器中的吸附表征);Kempisty 2022 AWWA Water Science(DOI 10.1002/aws2.1269,地下水与地表水 GAC 除 PFAA 对比)。

存亡变量结论:DOM/EfOM 使 GAC 对 PFAA 床寿命缩短的方向与机制在摘要级多源成立;损失是否达到方案设定的 ≥2× 阈值,摘要级数据既不能确认也不能排除,全文数值提取为门 3 硬前置。Kothawala 2017 的批量异质性信号须在门 3 如实呈现。

### C3 聚 MPC 抗蛋白质与大分子粘附

| 定位文献 | 题录核实 | 方法学一致性 | 状态 |
|---|---|---|---|
| Xu Y, Takai M, Ishihara K. Protein adsorption and cell adhesion on cationic, neutral, and anionic 2-methacryloyloxyethyl phosphorylcholine copolymer surfaces. Biomaterials 30(28) (2009) 4930-4938. DOI 10.1016/j.biomaterials.2009.06.005 | Crossref 与 PubMed(PMID 19560198)一致;网络检索给出的 PMID 19596144 经核实为无关文献,已弃用 | MPC 共聚物 SiO2 表面涂层,蛋白质吸附与细胞粘附实验;摘要确认三种电荷特性涂层均显著低蛋白吸附且零细胞粘附;具体吸附量(ng/cm² 量级)在全文 | 题录摘要级待全文核验 |
| Ladd J, Zhang Z, Chen S, Hower JC, Jiang S. Zwitterionic polymers exhibiting high resistance to nonspecific protein adsorption from human serum and plasma. Biomacromolecules 9(5) (2008) 1357-1361. DOI 10.1021/bm701301s | Crossref 与 PubMed(PMID 18376858)一致 | ATRP 两性离子聚合物刷(羧基甜菜碱甲基丙烯酸酯),未稀释人血清与血浆基质;摘要确认高抗非特异蛋白吸附;两性离子化学为 CB 而非 MPC 的 PC,平板刷而非颗粒,边界如实记录 | 题录摘要级待全文核验 |
| Zhang L, Cao Z, Bai T, Carr L, Ella-Menye JR, Irvin C, Ratner BD, Jiang S. Zwitterionic hydrogels implanted in mice resist the foreign-body reaction. Nature Biotechnology 31 (2013) 553-556. DOI 10.1038/nbt.2580 | Crossref 核实 | 小鼠植入水凝胶抗异物反应,大分子与细胞层级抗污证据 | 题录摘要级待全文核验 |
| Ishihara K, Ueda T, Nakabayashi N. Preparation of phospholipid polymers and their properties as polymer hydrogel membranes. Polymer Journal 22 (1990) 355-360. DOI 10.1295/polymj.22.355 | Crossref 核实 | MPC 磷脂聚合物奠基性工作,同时支撑 C8 仿生谱系 | 题录摘要级待全文核验 |

边界声明:上述证据为蛋白质与细胞在平板涂层或水凝胶上的粘附;DOM 大分子(腐殖质、生物聚合物)在 GAC 颗粒界面上的行为与蛋白质不同,蛋白证据不直接覆盖 DOM。DOM 专属两性离子抗污记录本轮定位到 Sherazi 2022 J Memb Sci 643:120060(DOI 10.1016/j.memsci.2021.120060,两性离子 UF 膜高通量抗污)与 Wang 2015 J Memb Sci 493(DOI 10.1016/j.memsci.2015.06.036,两性离子改性 RO 抗生物污染),两者题录经 Crossref 核实,是否含腐殖酸定量数据待全文核验。

### C4 两性离子层对小离子与小溶质的渗透性

| 定位文献 | 题录核实 | 方法学一致性 | 状态 |
|---|---|---|---|
| Ding, Wu, Wu. Zwitterionic conjoined-network enables loose nanofiltration membrane with ultrahigh dye/salt selectivity. Separation and Purification Technology 380 (2026) 135341. DOI 10.1016/j.seppur.2025.135341 | Crossref 核实 | 疏松纳滤,染料截留而盐透过;支持"水合两性离子层允盐阻大分子"的膜领域经验;NaCl 截留率等数值待全文 | 题录摘要级待全文核验 |
| Ishihara K, Nakabayashi. Hemocompatible cellulose dialysis membranes modified with phospholipid polymers. Artificial Organs 19 (1995) 1215-1221. DOI 10.1111/j.1525-1594.1995.tb02288.x | Crossref 与 PubMed(PMID 8967877)一致 | 纤维素透析膜经磷脂聚合物改性;透析过程本身即小分子跨膜,磷脂聚合物层提供血液相容性;支持"小分子可透、抗大分子粘附"的组合 | 题录摘要级待全文核验 |
| Ishihara 1990 Polymer Journal(同 C3) | Crossref 核实 | MPC 水凝胶膜的渗透性质 | 题录摘要级待全文核验 |

无法定位声明:两性离子接枝薄层在吸附剂颗粒外表面对约 300 Da 阴离子(PFBS)跨层传质阻力的直接证据,本轮检索未能定位;方案简报自身已将该项列为待查不确定性(第 8 节),方案未以此声称任何定量值,故不构成 phantom 锚点,列为深设计测量问题(短柱动力学对照)。

### C5 MPC 单体与接枝成本量级

| 定位对象 | 核实情况 | 状态 |
|---|---|---|
| MPC 化学身份:2-methacryloyloxyethyl phosphorylcholine,C11H22NO6P,分子量 295.27 | PubChem PUG-REST 核实分子式与分子量;CAS 67881-98-5 来自供应商记录 | 身份已核实(Tier 2 商业记录口径) |
| 研究级目录价 | TCI 目录号 M2146 经网络检索快照给出 5 g 约 122-157 USD、25 g 约 385-495 USD(即约 15-31 USD/g);供应商页面直接读取在本环境被 403 阻断;不同检索快照之间价格区间不一致(约 20-600 USD/g),无法收敛 | 无法定位可核验价格页 |
| 工业散装价(NOF Lipidure 等) | 无公开报价;网络检索给出的量级说法不可核实 | 无法定位 |

裁定口径:方案简报未声称具体成本数值,仅将 MPC 单体成本设为门 1 待核锚点,故此处无 phantom;但成本约束(复合介质成本比 ≤6,对照 GAC 约 2-4 USD/kg)的核算输入当前开口。传导:深设计 G0 阶段须取得供应商书面报价(NOF、TCI、BLD Pharm 等)落账;建议同时记录磺基甜菜碱(SBMA)等低价替代单体的报价作为降本路径。

### C6 高离子强度下两性离子抗污保持

| 定位文献 | 题录核实 | 方法学一致性 | 状态 |
|---|---|---|---|
| Ladd 2008 Biomacromolecules(同 C3) | Crossref 与 PubMed 一致 | 未稀释人血清与血浆,离子强度约 150 mM,高于二级出水典型 10-30 mM,属保守覆盖 | 题录摘要级待全文核验 |
| Matsuda Y, Kobayashi M, Annaka M, Ishihara K, Takahara A. Dimension of poly(2-methacryloyloxyethyl phosphorylcholine) in aqueous solutions with various ionic strength. Chemistry Letters 35 (2006) 1310-1311. DOI 10.1246/cl.2006.1310 | Crossref 核实 | 直接考察 MPC 聚合物链尺寸随离子强度变化,与"高离子强度下水合层保持"的机制问题对口 | 题录摘要级待全文核验 |
| Kobayashi M, Terayama Y, Hosaka N, Kaido M, Suzuki A, Yamada N, et al. Friction behavior of high-density poly(2-methacryloyloxyethyl phosphorylcholine) brush in aqueous media. Soft Matter 3 (2007) 740. DOI 10.1039/b615780g | Crossref 核实 | 高密度 PMPC 刷在水介质中的水合润滑行为,支撑水合层稳定性 | 题录摘要级待全文核验 |

边界声明:生理离子强度证据对二级出水为保守覆盖;抗污保持率随离子强度的定量剂量关系待全文核验。

### C7 硫酸根脆性排除依据

台账 E056、E058、E059 已在账并核实,本门无需新锚点;门 3 折减核查直接援引。

### C8 仿生原型身份

细胞膜磷脂酰胆碱头基强水合界面与 MPC 的仿生谱系由 Ishihara 1990(题录已核实)及后续综述性记录支撑;方案对类比范围的诚实限定(仅界面抗粘附性质,不涉跨膜输运功能)与文献记录相符。

## 三、检索纪律事项(剔除与阴性记录)

1. 网络检索给出的"Scott BR, Small MJ, Knappe DRU, NOM 预载对 PFAS 在 GAC 吸附的影响(Water Research 2020)"经 Crossref 多路检索无法定位,按检索幻觉处理,未采用;Knappe 组真实对口文献为 Vatankhah 2022、Tang 2026、Kempisty 2022 等,已另行定位。
2. 网络检索给出的"Belkouteb 2020 Water Research RSSCT"未能定位到该第一作者记录,未采用。
3. 网络检索给出的 Xu 2009 的 PMID 19596144 经 PubMed 核实为无关文献(哮喘管理),正确 PMID 为 19560198;题录信息以 Crossref 记录为准。
4. WRF 项目报告(#4322 类灰色文献)未经核实,未采用。
5. MPC 价格的各检索快照互相矛盾,均未采用为事实;以"无法定位可核验价格页"落记。
6. 无 SciFinder 权限;上述阴性结果不构成任何文献的最终不存在证明。

## 四、台账新增条目建议(编号 E062 起,与在账 E001-E061 无冲突)

| 建议编号 | 条目主题 | 来源与 DOI | 核实层级建议 |
|---|---|---|---|
| E062 | 全规模水厂 GAC 对 PFAS 去除随链长变化,短链去除差 | Appleman 2014, Water Research 51:246-255, 10.1016/j.watres.2013.10.067 | Tier 1, screened_abstract;BV 数值待全文核验 |
| E063 | GAC/AE 柱中 14 种 PFAS 突破时间随链长增加,短链先突破并解吸 | McCleaf 2017, Water Research 120:77-87, 10.1016/j.watres.2017.04.057 | Tier 1, screened_abstract;BV 数值待全文核验 |
| E064 | EfOM(100-1000 Da)与 PFAA 在 GAC 上的竞争,孔堵塞加位点竞争机制,O3-BAF 可部分恢复 | Tajdini 2023, Water Research 241:120105, 10.1016/j.watres.2023.120105 | Tier 1, screened_abstract;损失倍数待全文核验 |
| E065 | O3-BAF 预处理改善市政污水二级出水 GAC 除 PFAA 的突破行为 | Vatankhah 2022, Water Research 223:118988, 10.1016/j.watres.2022.118988 | Tier 1, screened_abstract |
| E066 | 市政污水 GAC 除 PFAS 的 RSSCT 研究 | Mortazavian 2025, ACS ES&T Water 5:2145-2154, 10.1021/acsestwater.4c00919 | Tier 1, 题录已核实,摘要与全文待取 |
| E067 | DOM 与预处理对 GAC 除 PFAS 的影响 | Tang, Knappe, Meng 2026, AWWA Water Science, 10.1002/aws2.70053 | Tier 1, 题录已核实,摘要与全文待取 |
| E068 | PFAS 吸附综述:链长效应、有机质效应、再生难题 | Gagliano 2020, Water Research 171:115381, 10.1016/j.watres.2019.115381 | Tier 1, screened_review |
| E069 | DOM 浓度与组成对 PFAS 去除的影响;GAC 响应方向异质(批量研究,不得用作床寿命证据) | Kothawala 2017, Water Research 121:320-328, 10.1016/j.watres.2017.05.047 | Tier 1, screened_abstract;方法学限用标注 |
| E070 | MPC 共聚物涂层显著低蛋白吸附、零细胞粘附,与表面电荷无关 | Xu 2009, Biomaterials 30(28):4930-4938, 10.1016/j.biomaterials.2009.06.005 | Tier 1, screened_abstract |
| E071 | 两性离子聚合物刷抗未稀释人血清与血浆非特异蛋白吸附 | Ladd 2008, Biomacromolecules 9(5):1357-1361, 10.1021/bm701301s | Tier 1, screened_abstract |
| E072 | 两性离子水凝胶小鼠植入抗异物反应 | Zhang 2013, Nature Biotechnology 31:553-556, 10.1038/nbt.2580 | Tier 1, screened_abstract |
| E073 | MPC 磷脂聚合物奠基工作与仿生谱系 | Ishihara 1990, Polymer Journal 22:355-360, 10.1295/polymj.22.355 | Tier 1, screened_title,待全文核验 |
| E074 | 磷脂聚合物改性纤维素透析膜:小分子可透加血液相容性 | Ishihara 1995, Artificial Organs 19:1215-1221, 10.1111/j.1525-1594.1995.tb02288.x | Tier 1, screened_abstract |
| E075 | 两性离子疏松纳滤膜染料截留而盐透过 | Ding 2026, Separation and Purification Technology 380:135341, 10.1016/j.seppur.2025.135341 | Tier 1, screened_title,待全文核验 |
| E076 | PMPC 链尺寸随离子强度变化 | Matsuda 2006, Chemistry Letters 35:1310-1311, 10.1246/cl.2006.1310 | Tier 1, screened_title,待全文核验 |
| E077 | 高密度 PMPC 刷水介质润滑,水合层稳定 | Kobayashi 2007, Soft Matter 3:740, 10.1039/b615780g | Tier 1, screened_title,待全文核验 |
| E078 | MPC 单体身份:C11H22NO6P,分子量 295.27,供应商记录 CAS 67881-98-5 | PubChem 核实式量;供应商目录记录 | Tier 2, identity_only;价格量级无可核验来源,待供应商报价 |
| 备选 E079 | NOM 在 GAC 吸附器中的吸附表征 | Velten 2011, Water Research, 10.1016/j.watres.2011.04.047 | Tier 1, screened_title |
| 备选 E080 | 地下水与地表水 GAC 除 PFAA 对比 | Kempisty 2022, AWWA Water Science, 10.1002/aws2.1269 | Tier 1, screened_title |

## 五、对后续门的传导

1. 门 3 存亡变量(DOM 归因损失 ≥2×):对口柱研究群已定位(E064-E067,辅助 E079/E080),方向与机制摘要级成立,定量损失倍数摘要级不可得;全文数值提取列为门 3 硬前置。若全文提取显示 DOM 归因损失不足 2×,按方案简报第 5 节自设规则,门 3 即杀。E069 的方向异质性信号(批量条件下 DOM 有时提高 GAC 对 PFAS 去除)须在门 3 如实呈现,不得只引用有利方向。
2. 门 3 成本输入:MPC 无可核验公开价格(E078),供应商书面报价列为深设计 G0 前置;成本比 ≤6 的闭合当前不可判定。
3. 门 2 提示:本审计发现"抗污涂层用于吸附剂床寿命保持"的直接先验未在本轮检索中出现;膜与透析领域的"小分子渗透加抗大分子粘附"记录(E074/E075)占据相邻问题类,门 2 独立先验密度检索时须以四轴组合复核,本审计的阴性结果不构成先验不存在证明(无 SciFinder)。
4. FROZEN_INPUT 写入建议:全部"题录摘要级待全文核验"条目(E062-E077 的内容级数值)列为深设计 G0 硬前置,全文核验完成前不得在深设计文档中以已核实措辞引用具体数值。

## 六、裁定

**通过**(附硬前置条件)。

理由:全部承重定量值与事实声明均定位到真实文献,题录经 Crossref 或 PubMed 核实;无 phantom 锚点;核心数量账本未挂在无法定位的文献群上;台账新编号 E062 起与在账编号无冲突;无文献被错误表征(E028 历史错配由本审计改引柱研究修复;E069 方法学限用已标注;Ladd 2008 的 CB 化学与平板刷边界已标注)。两项"无法定位"(可核验价格页、吸附剂界面直接跨层传质证据)均不涉及方案已声称的定量值,按规范 3.4 不构成杀死或退回条件,转为开口项传导至门 3 与深设计 G0。

硬前置条件(写入 FROZEN_INPUT):
1. E062-E067 的突破体积与 DOM 损失倍数全文数值提取,门 3 启动前完成。
2. E070-E077 的抗污与渗透参数全文核验,深设计 G0 完成。
3. MPC 与接枝路线的供应商书面报价落账,门 3 成本核算前完成。
4. "300,000+ BV"上端与 PFBS 全规模专属突破数值未经全文确认前,方案文档与后续轮次一律以"引用区间待全文核验"表述。