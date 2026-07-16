# 有机污染物生物机制到可合成材料的证据门禁

## 目的与判定规则

本文件为 O-去甲基文拉法辛（ODV）/SERT、克拉霉素/核糖体和 PFOA/PFAS/FABP 三条设计线准备下一轮证据门禁。证据分为三类：

- **直接支持：** 目标物与指定生物原型的结合、结构或功能实验，或目标物材料的真实合成与测试。
- **邻近先例：** 结构类似物、同蛋白其他配体或同类材料平台的实验。邻近先例只能证明可行性边界，不能外推为目标事实。
- **设计假说：** 由前两类证据提出、但尚无直接实验支持的材料对应或测量方案。

搜索命中、摘要中的泛化表述和计算预测不单独升级为硬事实。材料性能只在原论文的目标物、介质和实验条件范围内有效。

## 一、ODV / SERT

### 1. 直接生物机制

**OT01｜直接支持**  
Darlene C. Deecher, Chad E. Beyer, Grace Johnston, Jenifer Bray, S. Shah, M. Abou-Gharbia, Terrance H. Andree. “Desvenlafaxine Succinate: A New Serotonin and Norepinephrine Reuptake Inhibitor.” *Journal of Pharmacology and Experimental Therapeutics*, 2006. [DOI](https://doi.org/10.1124/jpet.106.103382)

- **定位：** 摘要；competitive radioligand binding 与 uptake assays。
- **直接支持：** ODV 的琥珀酸盐在表达人 hSERT 的细胞体系中竞争性结合，报道 `Ki = 40.2 ± 1.6 nM`；抑制 `[3H]5-HT` 摄取的 `IC50 = 47.3 ± 19.4 nM`。这证明 ODV 与 hSERT 存在直接功能性相互作用。
- **适用边界：** 研究没有 ODV-hSERT 结构，不能给出 ODV 在中央位点的取向、残基接触或 ODV 诱导的构象状态。琥珀酸盐药物制剂数据也不能直接等同于环境水中游离 ODV 的吸附行为。

**OT02｜邻近先例**  
Jonathan A. Coleman, Eric Gouaux. “Structural basis for recognition of diverse antidepressants by the human serotonin transporter.” *Nature Structural & Molecular Biology*, 2018. [DOI](https://doi.org/10.1038/s41594-018-0026-8)

- **定位：** 摘要与中央位点结构比较。
- **直接支持：** 丝氨酸转运体与 sertraline、fluvoxamine、paroxetine 的晶体结构显示，化学结构不同的抗抑郁药占据中央底物位点并稳定 outward-open 构象。
- **适用边界：** 三种配体均不是 ODV。该研究可限定“中央口袋 + outward-open 稳定”的蛋白机制，但不能把其残基接触复制为 ODV 接触图。

**OT03｜邻近先例**  
Jonathan A. Coleman, Evan M. Green, Eric Gouaux. “X-ray structures and mechanism of the human serotonin transporter.” *Nature*, 2016. [DOI](https://doi.org/10.1038/nature17629)

- **定位：** 摘要；PDB 5I6X、5I6Z、5I71、5I73、5I74、5I75；central/allosteric site 描述。
- **直接支持：** paroxetine 或 `(S)-citalopram` 位于 TM1、3、6、8、10 之间的中央结合位点并锁定 outward-open 状态；细胞外前庭另有 allosteric site。
- **适用边界：** 这是抑制剂锁定状态，不是完整 Na+/Cl− 交替转运循环；不能据此声称 ODV 会驱动“外开到内开”或目标诱导夹持。

### 2. 水环境与分析边界

**OT04｜直接环境证据**  
María Jesús García-Galán, Larissa Arashiro, Lúcia H. M. L. M. Santos, Sara Insa, Sara Rodriguez-Mozaz, Damià Barceló, Ivet Ferrer, Marianna Garfí. “Fate of priority pharmaceuticals and their main metabolites and transformation products in microalgae-based wastewater treatment systems.” *Journal of Hazardous Materials*, 2020. [DOI](https://doi.org/10.1016/j.jhazmat.2019.121771)

- **定位：** 摘要；ODV removal 与 biomass concentration。
- **直接支持：** ODV 在藻类二级处理系统中表现出低生物降解和有限去除，报道范围为 13–39%；文拉法辛及其代谢物的生物吸附/富集参与去除。
- **适用边界：** 这是高率藻塘二级处理，不代表所有常规二级出水；本地二级出水中的 ODV、文拉法辛和 N-去甲基代谢物仍需实测。

### 3. 对材料实现的约束

- **可保留的静态假说：** 以“芳香/阳离子中心 + 羟基差异位点”的多点口袋区分 ODV 与文拉法辛。OT01 证明 ODV 结合 hSERT，OT02/OT03 证明中央位点能够容纳不同抗抑郁药；两者结合仍不能给出 ODV 残基图。
- **不得写成事实的动态假说：** `Na+/Cl− 耦合的 ODV 诱导两叶闭合`。现有结构只证明相邻抗抑郁药稳定 outward-open 状态；若构造盐耦合凝胶，其动态行为属于材料设计，不是 ODV/SERT 已证实对应。
- **最低竞争集：** 文拉法辛、N-去甲基文拉法辛、代表性 SSRI/SNRI、阳离子表面活性剂和 DOM。只与无关药物比较不能证明选择性。
- **最低测量集：** LC-MS/MS 同时定量 ODV 与母体/代谢物；QCM-D 或 FRET 只作为材料开闭读出；必须用 `NaCl/NaNO3/KCl/KNO3` 正交条件排除总离子强度造成的普通凝胶收缩。
- **路线拥挤度判断：** 抗抑郁药中央位点结构较成熟，ODV 专属环境吸附材料证据仍稀缺。当前门禁没有找到 ODV 表面印迹或 ODV-蛋白/肽杂化吸附的直接原始研究，这一缺口不能用 SSRI 或一般药物 MIP 填补。

### 4. 门禁结论

ODV 已通过“目标物确实直接作用于 hSERT”的门禁，尚未通过“目标物专属口袋残基”和“目标物诱导动态构象”门禁。下一轮设计可使用 SERT 作为真实生物原型，但静态位点布局和盐耦合开闭必须标记为设计假说，并把 ODV/文拉法辛成对竞争作为首要证伪实验。

## 二、克拉霉素 / 核糖体出口隧道

### 1. 直接生物结构与动态边界

**OT05｜直接支持**  
Wen Zhang, ZhiFei Li, Yufan Sun, Peng Cui, Jianhua Liang, Qinghe Xing, Jing Wu, Yanhui Xu, Wenhong Zhang, Ying Zhang, Lin He, Ning Gao. “Cryo-EM structure of *Mycobacterium tuberculosis* 50S ribosomal subunit bound with clarithromycin reveals dynamic and specific interactions with macrolides.” *Emerging Microbes & Infections*, 2022. [DOI](https://doi.org/10.1080/22221751.2021.2022439)

- **定位：** 摘要；Results “Alternative conformation of A2062”; Figure 2–3；PDB 7F0D / EMDB EMD-31398。
- **直接支持：** 3.3 Å cryo-EM 结构把克拉霉素定位于 NPET 靠近 P 位点的区域；邻近核苷酸包括 2503、2505、2508、2509 和 A2062。A2062 在复合物中呈两种构象，其中一态通过界面水分子接近 desosamine；论文还指出 desosamine 对紧密结合重要，内酯环和 cladinose 部分更具柔性。
- **可转译边界：** 可直接提取“有限通道、desosamine 锚定、局部 A2062 摆动、界面水参与”四个特征。A2062 双构象不等于整个出口隧道闭合，也不证明克拉霉素单独产生宏观闸门。
- **物种边界：** A2062 对不同大环内酯和不同物种的响应不同；论文明确指出相关机制仍未完全解决，不能把 *M. tuberculosis* 结构当作通用细菌常数。

**OT06｜直接/历史结构支持**  
Jeffrey L. Hansen, Joseph A. Ippolito, Nenad Ban, Poul Nissen, Peter B. Moore, Thomas A. Steitz. “The Structures of Four Macrolide Antibiotics Bound to the Large Ribosomal Subunit.” *Molecular Cell*, 2002. [DOI](https://doi.org/10.1016/S1097-2765(02)00570-1)

- **定位：** 四种大环内酯-50S 复合结构及其结合位点比较。
- **直接支持：** 大环内酯占据大亚基出口隧道的定义位置，为宏环、糖基和通道几何比较提供结构基础。
- **适用边界：** 早期低分辨结构中的克拉霉素构象后来被 OT05 指出可能受分辨率限制而误判；材料设计应以 OT05 的 7F0D 为优先结构，而不是复制旧构象。

### 2. 可合成相邻先例与拥挤度

**OT07｜邻近材料先例**  
Jiayin Zhao, Gohar Zubair, Liju Tan, Yu Qiao, Yanbo Tian, Jiangtao Wang. “Eco-friendly deep eutectic solvent-mediated COF-based surface molecularly imprinted polymers for specific adsorption and determination of roxithromycin.” *Sustainable Chemistry and Pharmacy*, 2026. [DOI](https://doi.org/10.1016/j.scp.2026.102500)

- **定位：** 摘要；COF support、surface imprinting、selectivity/reuse/environmental-water recovery。
- **直接支持：** 相邻大环内酯罗红霉素已经可在 COF 载体上进行表面印迹；论文报告了实际合成、选择性、重复使用和加标环境水回收。
- **适用边界：** 目标是罗红霉素，不是克拉霉素；加标环境水不是二级出水痕量竞争吸附。该论文证明“大环内酯表面空穴可制造”，也说明纯静态印迹已拥挤，不能构成克拉霉素仿生动态的新意。

**OT08｜直接环境与分析证据**  
Christa S. McArdell, Eva Molnar, Marc J.-F. Suter, Walter Giger. “Occurrence and Fate of Macrolide Antibiotics in Wastewater Treatment Plants and in the Glatt Valley Watershed, Switzerland.” *Environmental Science & Technology*, 2003. [DOI](https://doi.org/10.1021/es034368i)

- **定位：** 摘要；SPE-LC/MS 与 LC/MS/MS 确证；treated WWTP effluent results。
- **直接支持：** 瑞士三座 WWTP 处理出水中检测到克拉霉素、罗红霉素和 erythromycin-H2O；克拉霉素夏季为 57–330 ng/L。
- **适用边界：** 处理流程终点不能在未核对工艺前统一改称“二级出水”；20 多年前的瑞士浓度不能替代本地实测。该分析框架支持将同类大环内酯放入同一 LC-MS/MS 竞争方法。

### 3. 动态门控与测量的邻近先例

**OT09｜邻近动态材料先例**  
Yukiya Kitayama, Manabu Isomura. “Gas-stimuli-responsive molecularly imprinted polymer particles with switchable affinity for target protein.” *Chemical Communications*, 2018. [DOI](https://doi.org/10.1039/C7CC09889H)

- **定位：** 论文的 shell nanocavity 与 CO2/N2 switchable affinity 实验。
- **直接支持：** 表面壳层纳米空穴可以与响应聚合物组合，使亲和力在外部气体刺激下切换。
- **适用边界：** 目标是蛋白，刺激是外加气体；它只证明“表面印迹 + 可切换壳层”可合成，不能证明克拉霉素能够自行触发 A2062 式门控。

**OT10｜邻近测量先例**  
Mariacristina Gagliardi, Marco Cecchini. “Core/shell molecularly imprinted nanoparticles: optimized synthesis and application in QCM-D biosensing.” *RSC Advances*, 2025. [DOI](https://doi.org/10.1039/D5RA02297E)

- **定位：** core/shell MIP nanoparticle synthesis 与 QCM-D application。
- **直接支持：** 核壳印迹纳米颗粒可以通过 QCM-D 联合读取质量和耗散变化，适合比较结合量与软层构象/黏弹性响应。
- **适用边界：** 不是克拉霉素体系；QCM-D 耗散变化也不能单独证明“闭合”，需要 FRET、孔道电导或结构表征交叉验证。

### 4. 对材料实现的约束

- **静态设计应复制：** 受限通道、desosamine 锚定、宏环体积匹配、A2062 邻近局部柔性和界面水，而不是笼统的“π-π + 氢键”。
- **动态设计应缩小为局部门：** 最有证据的动态单元是 A2062 的局部双构象。合成材料可测试“孔壁单个可摆动核碱基/杂环位点”的占据响应；把两片大聚合物翼描述成核糖体整体闭合没有证据。
- **最低竞争集：** 阿奇霉素、罗红霉素、红霉素/erythromycin-H2O 和带正电的大分子药物。需要同时检验十四元与十五元大环、糖基差异及代谢/降解物。
- **最低动态读出：** 局部门位点 FRET 或环境敏感荧光、纳米通道电导和 QCM-D 三者至少两项；永久固定门位点和无门位点为因果对照。
- **路线拥挤度判断：** 大环内酯表面印迹已出现 COF/DES 路线，静态空穴新意为中低；“克拉霉素-特异局部 A2062 模拟门 + 同类竞争 + 二级出水”仍有空白，但制造难度高。

### 5. 门禁结论

克拉霉素已通过“目标物直接结构”和“局部构象异质性”门禁，是三条线中最接近一静一动硬对应的候选。动态对应必须限定为 A2062 邻近的局部摆动及界面水重排；若设计仍采用普通表面 MIP 而没有可测的局部门，它只能算静态印迹材料。

## 三、PFOA / PFAA / hL-FABP

### 1. 直接结合、残基与构象边界

**OT11｜直接支持**  
Nan Sheng, Juan Li, Hui Liu, Aiqian Zhang, Jiayin Dai. “Interaction of perfluoroalkyl acids with human liver fatty acid-binding protein.” *Archives of Toxicology*, 2016. [DOI](https://doi.org/10.1007/s00204-014-1391-7)

- **定位：** 摘要；fluorescence displacement、ITC、Asn111/Arg122 substitution 与 molecular simulation。
- **直接支持：** PFOA/PFNA 与 hL-FABP 以 1:1 化学计量表现为中等亲和，PFHxS 较弱，PFHxA 未检测到结合；亲和力随碳数增加。Asn111→Asp 导致 PFAA 亲和损失，支持 Asn111 对初始外位点结合的重要性；Arg122→Gly 改变结合化学计量，计算显示其破坏 PFOA 疏水堆积和氢键。
- **证据边界：** Asn111/Arg122 结果结合了突变与计算解释；不能把模拟构象当作 PFOA-FABP 的实验原子结构。实验显示 hL-FABP 对 PFAA 链长高度敏感，也说明该蛋白不是 PFOA 专属受体。

**OT12｜直接天然配体动态边界**  
Jun Cai, Christian Lücke, Zhongjing Chen, Ye Qiao, Elena Klimtchuk, James A. Hamilton. “Solution Structure and Backbone Dynamics of Human Liver Fatty Acid Binding Protein: Fatty Acid Binding Revisited.” *Biophysical Journal*, 2012. [DOI](https://doi.org/10.1016/j.bpj.2012.04.039)

- **定位：** 摘要；human L-FABP/oleate complex；portal/gap backbone mobility；PDB 2LKK。
- **直接支持：** hL-FABP 是 β-clam，能够容纳两分子油酸；内层油酸羧酸与 R122 胍基形成氢键，第二分子的羧酸靠近 portal。NMR 显示 portal/gap 区域骨架迁移率较高。
- **关键否定边界：** 两分子油酸结合没有引起蛋白整体构象的实质变化。因此可转译的是“门户/缝隙局部呼吸与可达性”，不能写成 FABP 整体发生 Venus-flytrap 式闭合。油酸不是 PFOA，该动态只属于邻近天然配体证据。

**OT13｜直接同类结合谱**  
Lianying Zhang, Xiao-Min Ren, Liang-Hong Guo. “Structure-Based Investigation on the Interaction of Perfluorinated Compounds with Human Liver Fatty Acid Binding Protein.” *Environmental Science & Technology*, 2013. [DOI](https://doi.org/10.1021/es4026722)

- **定位：** 摘要；17 种 PFC 的 fluorescence displacement 与 chain-length trend。
- **直接支持：** 12 种 PFCA 对 hL-FABP 的亲和随 C4–C11 链长显著增加，超过 C11 后略降，为“腔体长度/疏水填充”提供实验约束。
- **适用边界：** 结构解释仍包含模型；链长趋势会造成广谱长链 PFAS 偏好，不能自动形成 PFOA 对 PFNA/PFDA 的选择性。

### 2. 可合成材料、抗污与拥挤度

**OT14｜邻近材料先例**  
Huiqin Guo, Yu Liu, Wentian Ma, Liushui Yan, Kexin Li, Sen Lin. “Surface molecular imprinting on carbon microspheres for fast and selective adsorption of perfluorooctane sulfonate.” *Journal of Hazardous Materials*, 2018. [DOI](https://doi.org/10.1016/j.jhazmat.2018.01.018)

- **定位：** 摘要；carbon microsphere surface polymer、DMC/TFMA bifunctional monomers、competition/regeneration。
- **直接支持：** PFOS 表面印迹层可在碳微球上合成；双功能单体同时提供电荷与含氟相互作用，平衡时间约 1 h，酸性条件下有特异结合，并可用甲醇/乙酸再生。
- **适用边界：** 目标是 PFOS 而非 PFOA，且优选 pH 3、使用有机/酸再生；不能证明市政二级出水的 PFOA 选择性或温和再生。该研究表明 PFAS 静态表面印迹路线已有多年积累。

**OT15｜直接 PFOA 传感/抗污先例**  
Xiaoyu Zhu, Cheng Chen, Xingao Qin, Ying Wang. “β-Cyclodextrin Imprinted Film Embedded with Methylene Blue: A Host-Guest Sensitive Electrochemical Strategy for PFAS Detection.” *Journal of Hazardous Materials*, 2025. [DOI](https://doi.org/10.1016/j.jhazmat.2024.136870)

- **定位：** 摘要；electropolymerization、hydration layer、real-water sensing、analogue comparison。
- **直接支持：** β-CD 与亚甲蓝可在 PFOA 存在下电聚合成主客体印迹膜；β-CD 形成亲水水化层并改善抗污，同时提供电化学读出。论文报告真实水样 PFOA 检测及相对其他全氟类似物更高的印迹响应。
- **适用边界：** 这是传感薄膜，不是具备工程容量和再生数据的吸附床；电流信号不能直接转为去除性能。该工作也说明“β-CD + PFOA 印迹 + 抗污”本身已经拥挤。

### 3. 二级出水与分析边界

**OT16｜直接环境证据**  
Juhee Kim, Xiaoyue Xin, Gary L. Hawkins, Qingguo Huang, Ching-Hua Huang. “Occurrence, Fate, and Removal of PFAS in Small- and Large-Scale Municipal Wastewater Treatment Facilities in the United States.” *ACS ES&T Water*, 2024. [DOI](https://doi.org/10.1021/acsestwater.4c00541)

- **定位：** 全文及 supporting information；final effluent detection tables。项目证据台账 E001 已完成核验。
- **直接支持：** 九座受调查市政 WWTP 最终出水中 PFOA、PFOS、PFBS、PFHxS 均为 100% 检出，HFPO-DA 为 67%；活性污泥处理与部分短链 PFCA 增加相关。
- **适用边界：** 美国九座设施不能外推为所有污水厂；最终出水不应在未核对流程时统一改称二级出水。本地试验应使用同批水样的目标 PFAS、前体和竞争 PFAS 全谱定量。

### 4. 对材料实现的约束

- **静态设计应采用两阶段口袋：** Asn111 类外位点负责羧酸头基初始定位，Arg122 类内位点和有限腔体负责深层固定；材料必须通过位点删除和链长序列证明两阶段作用，不能只看 PFOA 容量。
- **动态设计应限定为门户呼吸：** OT12 支持 portal/gap 高迁移率，同时否定大幅整体闭合。可合成实现应是局部软门户或可达性变化，不应描述为整个“贝壳”夹闭。
- **最低竞争集：** PFHxA、PFNA、PFOS、PFHxS、HFPO-DA、天然脂肪酸和阴离子表面活性剂。特别需要检验 PFOA/PFNA，因为 FABP 证据显示两者均能结合。
- **最低动态读出：** 门户 FRET/环境敏感荧光与 QCM-D 或小角散射至少两类；永久开放门户、固定门户、无 Asn111 类外位点、无 Arg122 类内位点均需保留。
- **路线拥挤度判断：** PFAS 表面 MIP、β-CD 主客体和亲水抗污层均已有实证，静态路线拥挤度高。真正未闭合的是“受 FABP 残基分工约束的两阶段进入 + 局部门户动态 + 二级出水混合 PFAS 竞争”。

### 5. 门禁结论

PFOA 已通过直接 hL-FABP 结合、关键残基和链长依赖门禁；动态部分只能通过天然油酸研究支持局部门户迁移率，不能声称 PFOA 诱导整体闭合。下一轮最合理的材料对应是“两阶段头基定位/内腔固定 + 局部门户呼吸”，而不是再做一个 β-CD 或含氟单体静态印迹材料。

## 四、跨路线的合成与测量结论

| 维度 | 证据允许的实现 | 仍属假说或缺口 |
|---|---|---|
| 表面印迹 | 大环内酯相邻物的 COF 表面印迹（OT07）；PFOS 碳微球表面印迹（OT14）；PFOA β-CD 电聚合印迹膜（OT15） | ODV 专属印迹、克拉霉素专属动态印迹、FABP残基分工式 PFOA 印迹均缺直接先例 |
| 动态门控 | 响应壳层可切换 MIP 亲和（OT09）；QCM-D 可读核壳印迹层质量/耗散（OT10） | “目标物自行触发”而非外部气体、温度或盐度引起的门控，三条目标线均未被材料论文直接证明 |
| 蛋白/肽杂化 | 当前筛得来源未提供 ODV/SERT、克拉霉素/rRNA 或 PFOA/FABP 的吸附材料杂化实证 | 若使用蛋白片段、核酸或肽门，应作为新合成路线并单独验证稳定性、泄漏和真实水抗污 |
| 抗污支架 | β-CD 水化层改善 PFOA 传感膜抗污（OT15） | 抗污传感不等同于长期吸附床抗 DOM 覆盖；需要吸附前后 TOC、QCM-D 和位点可用率 |
| 痕量分析 | ODV/代谢物可用同步 LC-MS/MS；克拉霉素与相邻大环内酯已有 SPE-LC-MS/MS 环境方法（OT08）；PFAS 需混合物全谱分析（OT16） | 本地二级出水方法检出限、基质效应、回收率和空白污染必须重新验证 |

## 五、建议的下一门禁顺序

1. **克拉霉素：** 以 PDB 7F0D 为结构唯一优先版本，先证明 A2062 类局部门位点可合成、可摆动且能区分三种相邻大环内酯。
2. **PFOA：** 先做 Asn111 类外位点与 Arg122 类内位点的双删除实验；若两阶段作用不能分离，不进入动态门户开发。
3. **ODV：** 先补 ODV 的位点突变、结构或可靠建模-实验交叉证据；在此之前，盐耦合开闭只能作为高风险材料假说。

当前证据强度排序为：**克拉霉素局部动态结构 > PFOA直接结合与门户边界 > ODV直接结合但缺目标结构**。三条路线均尚未获得“目标诱导动态可合成材料”的直接实证，因此下一轮不能省略永久开放/固定门和近似物竞争对照。
