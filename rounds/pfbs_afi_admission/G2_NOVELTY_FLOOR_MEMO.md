# G2 创新性下限门裁定备忘录：PFBS-AFI-GAC(R1a,抗污染水合界面 GAC)

- 规范依据:`orchestration/ADMISSION_GATE_SPEC_DRAFT.md` 第四节(门 2,最高优先级门,不设退回修复通道)
- 执行角色:门 2 检查员(独立文书筛查,不担任该方案后续深设计轮次设计师)
- 日期:2026-07-19
- 输入:`rounds/pfbs_afi_admission/R1A_SCHEME_CONCEPT.md`;`research/evidence/evidence_ledger.csv`;门 1 锚点审计未执行(本次单门执行),方案未以任何 phantom 文献充当新颖性论据(其先验主张全部为"待门 2 检索证实或证伪"的开放表述)
- 检索边界声明:本次检索使用 Crossref REST API 与 PubMed E-utilities 逐条核实题录;无 SciFinder 权限,Crossref/PubMed 阴性结果不充当最终不存在证明;网络检索引擎返回的 AI 摘要仅作线索,其中若干条目标题无法经 Crossref/PubMed 复核定位,按疑似摘要幻觉处理并如实记录

## 一、独立先验密度检索记录

按"识别化学 x 目标物 x 载体 x 应用场景"四轴组合执行五组检索,另加补充检索式。检索式为 Crossref query.bibliographic 与 PubMed term 实际用式。

### 检索组 1:两性离子化学 x PFAS x 碳载体
- 检索式:`zwitterionic activated carbon PFAS adsorption`;`sulfobetaine activated carbon perfluoroalkyl`;`zwitterionic adsorbent PFAS removal`;`betaine biochar PFAS`;`polyzwitterion PFAS adsorption`;PubMed `zwitterionic PFAS adsorption`(21 条)、`zwitterionic perfluoroalkyl adsorbent`(2 条)、`sulfobetaine PFAS`(2 条)
- 结果:**无法定位任何"两性离子吸附剂用于 PFAS 去除"的论文**。PubMed 21 条命中全部为"两性离子型 PFAS 作为被吸附物"(如 ES&T 2026,10.1021/acs.est.5c08377,legacy AFFF 中阴离子与两性离子 PFAS 的吸附),非两性离子吸附剂。网络摘要声称的"Zwitterionic polymer-grafted activated carbon for enhanced removal of PFOA(J. Hazard. Mater. 2023)"经 Crossref 多路题录检索与 PubMed 复核**无法定位**,按疑似 AI 摘要幻觉记录,不作先验也不作空白证明。

### 检索组 2:MPC/磷酰胆碱接枝碳 x 水处理
- 检索式:`MPC grafted activated carbon water treatment`;`phosphorylcholine carbon adsorbent`;`2-methacryloyloxyethyl phosphorylcholine grafted carbon`;`zwitterion functionalized biochar`;`sulfobetaine modified biochar adsorption`;`polyMPC grafted carbon surface`;`phosphorylcholine activated carbon`
- 命中(题录经 Crossref 核实):
  - 10.1016/j.carbon.2014.01.025,phosphorylcholine oligomer grafted graphene oxide,Carbon 2014(细胞毒性研究,非水处理),内容待全文核验
  - 10.1021/acsami.0c01843,phosphorylcholine-modified bifunctional adsorbent,ACS Appl. Mater. Interfaces 2020(铀回收),内容待全文核验
  - 10.1016/j.clay.2014.04.001,dodecyl sulfobetaine 改性蒙脱土吸附 Cu2+/亚甲基蓝,Appl. Clay Sci. 2014,内容待全文核验
- "MPC 接枝 GAC 用于水处理":**无法定位**。

### 检索组 3:抗污涂层 x 吸附剂容量/床寿命保护(存亡轴)
- 检索式:`antifouling coating granular activated carbon`;`NOM fouling adsorbent bed lifetime PFAS`;`antifouling adsorbent micropollutant`;`coating activated carbon reduce NOM adsorption fouling`;`protect adsorbent from fouling coating water treatment`;`NOM preloading micropollutant adsorption activated carbon`;`DOM fouling GAC PFAS breakthrough bed`;`surface modification anion exchange resin NOM fouling`
- 关键命中(题录经 Crossref 核实;标注 PMID 者经 PubMed 摘要级核验):
  - **10.1016/j.jcis.2017.04.024,Cai 等,"Antifouling zwitterionic hydrogel coating improves hemocompatibility of activated carbon hemoadsorbent",J. Colloid Interface Sci. 2017;503:168-177(PMID 28521219,摘要级核验)**:聚羧基甜菜碱(PCB)两性离子水凝胶包覆粉末活性炭;亚甲基蓝在单一蛋白溶液乃至 100% 胎牛血清中的吸附能力不受影响,而裸 PAC 在同等条件下损失约 50%;并可吸附白蛋白结合态胆红素。**该文是"两性离子抗污涂层保护活性炭对小溶质的吸附容量免受大分子污堵"这一机制的直接先验(医疗血液灌流场景,任意污染物条款适用)。**
  - 10.1021/es051285o,Karanfil/Dastgheib/Mauldin,"Exploring Molecular Sieve Capabilities of Activated Carbon Fibers to Reduce the Impact of NOM Preloading on Trichloroethylene Adsorption",ES&T 2006:以 ACF 孔口分子筛效应降低 NOM 预载对微污染物(TCE)吸附的影响;同一问题类(保护弱分配微污染物吸附免受 NOM 污堵),机制为孔径筛分而非涂层,内容待全文核验
  - 10.1016/j.jwpe.2025.109257,层级孔结构缓解 NOM 对活性炭微污染物吸附的干扰,J. Water Process Eng. 2026,内容待全文核验
  - 10.1016/j.seppur.2025.134270,分段投加活性炭缓解 NOM 竞争,Sep. Purif. Technol. 2025,内容待全文核验
  - 10.1016/j.seppur.2014.03.019,阴离子交换除 NOM 及其对活性炭微污染物吸附竞争的影响,Sep. Purif. Technol. 2014,内容待全文核验
  - 10.1016/j.watres.2026.126326,老化 GAC 滤池中 PFAS 的突破与脱附与 DOM 组成的关系,Water Res. 2026,内容待全文核验
  - 10.1016/j.watres.2022.118146,以 DOM 紫外吸收与荧光预测固定床碳对短链 PFAS 的去除,Water Res. 2022,内容待全文核验
  - 离子交换树脂 NOM 污堵另有 MIEX 系列与 Water Res. 2014(10.1016/j.watres.2014.08.027,市政污水深度处理中 AER 污堵的荧光分析)等密集先验
- 结论:"抗污涂层保护吸附介质容量"存在直接先验(JCIS 2017);"保护微污染物吸附免受 NOM/DOM 污堵"这一问题类在水处理领域被孔径工程与工艺级路线密集占据。"两性离子涂层 GAC 用于水处理床寿命保护"这一具体组合在 Crossref/PubMed 可见范围内无法定位直接先验,但按预注册裁定规则,增量 (i) 已须降级(见第二节)。

### 检索组 4:DOM/基质耐受 PFAS 吸附剂(Dichtel 组叙事空间)
- 检索式:`cyclodextrin polymer PFAS humic acid`;`Dichtel cyclodextrin PFAS organic matter`;`beta-cyclodextrin polymer PFAS wastewater organic matter`
- 命中(题录经 Crossref 核实):10.1016/j.watres.2024.121897(Wang/Lin/Dichtel/Helbling,苯乙烯系 beta-CD 聚合物、阴离子交换树脂与活性炭受基质组分抑制的方式各不相同,Water Res. 2024,摘要级待全文核验);10.1038/nature16185(多孔 beta-CD 聚合物快速去除有机微污染物,Nature 2015);10.1021/acscentsci.2c00478(可调阳离子 beta-CD 聚合物平台,ACS Cent. Sci. 2022,台账 E026/E055/E056 已落账);10.1016/j.watres.2025.123631(市政污水 beta-CD 吸附剂,台账 E003)
- 结论:CD 聚合物的基质表现叙事已被 Dichtel 组及台账条目占据;本概念不走 CD 路线,该组检索主要确认"基质耐受"作为论点的拥挤度。

### 检索组 5:两性离子膜微污染物渗透(可迁移性)
- 检索式:`zwitterionic membrane micropollutant`;`zwitterionic nanofiltration micropollutant permeation`;`zwitterionic membrane perfluoroalkyl`;`antifouling membrane micropollutant rejection zwitterion`
- 命中(题录经 Crossref 核实):10.1016/j.memsci.2013.06.029(SI-ATRP 接枝两性离子聚砜膜抗污,J. Membr. Sci. 2013);10.1016/j.memsci.2011.12.021(两性离子超滤膜的蛋白质传输,J. Membr. Sci. 2012);10.3390/membranes11030187(两性离子水凝胶反应涂覆纳滤膜,Membranes 2021);10.1016/j.memsci.2020.118119(两性离子聚合物/PES 膜抗污,2020);膜领域两性离子抗污为成熟密集领域,且已有商业化投资记录(Membrane Technology 2021,10.1016/s0958-2118(21)00001-x)
- 两性离子膜专用于 PFAS:无法定位直接论文;膜法 PFAS 去除另有成熟 NF/RO 文献。结论:膜领域"两性离子水合层排斥大分子、透过小分子"的物理经验成立,支持本概念机制的可迁移性,但膜与传感器抗污属不同问题类,按预注册规则不直接占据增量 (i)。

### 补充命中
- 10.1016/j.eti.2021.101763 与 10.1016/j.jwpe.2021.102093:"zwitterionic adsorbent coating"用于染料废水处理(两性离子涂层本身即吸附相,对象为偶极染料),Environ. Technol. Innov. 2021 与 J. Water Process Eng. 2021,内容待全文核验;属"两性离子吸附涂层用于水处理"的载体化学先验,不涉及容量保护机制。

## 二、增量逐条裁定

| 增量 | 方案自述 | 裁定 | 依据 |
|---|---|---|---|
| (i) 抗污染水合界面维持弱分配短链 PFAS 在真实二级出水中的床寿命 | 应用层级增量 | **(c) 组合式应用级** | 预注册规则触发:JCIS 2017(10.1016/j.jcis.2017.04.024,PMID 28521219 摘要级核验)已演示两性离子水凝胶涂层保护活性炭对小溶质(亚甲基蓝)的吸附容量免受大分子(血清蛋白)污堵,100% FBS 中容量保持 vs 裸 PAC 损失约 50%,属"抗污涂层保护吸附介质容量"的直接先验(任意污染物条款)。机制内核(水合层排斥大分子、透过小溶质)另有膜领域密集先验;问题类(保护微污染物吸附免受 NOM/DOM 污堵)在水处理领域被 ES&T 2006 孔口筛分、JWPE 2026 层级孔、STP 2025/2014 工艺路线占据。剩余新元素仅为具体应用实例的组合(短链 PFAS x GAC x 二级出水 DOM x 床寿命指标),各组件均为已知。 |
| (ii) 尺寸选择性抗污渗透层的层归一化测量构型(sham-GAC 差分 + 跨层渗透阻力对照) | 方法学增量 | **(d) 无增量(作为承重新颖性条目)** | 空白对照差分与跨层传质阻力测量为膜领域与吸附剂表征的常规实验设计;作为实验严谨性设计成立,但不构成可辩护的论文级新颖性。即使按最宽松解读归为 (b) 条件性窄口径(限于本体系实例),亦不能支撑本门通过,裁定结果不变。 |
| (iii) 无氟、无净电荷 GAC 即插即用形态 | 组合式增量,方案自认不构成新颖性基础 | **(c) 组合式应用级** | 与方案自认一致;单独不足以通过,规范与任务口径均确认。 |

## 三、依附性核查

- 本概念的性能主张为床寿命保持(DOM 归因损失的可恢复部分),而非单位位点热力学增强;其物理依据(JCIS 2017 的容量保持演示、膜领域小分子跨两性离子层渗透经验)使该性能事件的先验概率显著高于 v2 的 phantom 增强机制。裁定:三条增量的残余价值**不依附于 v2 型低概率性能事件**。
- 诚实标注:性能事件的量级(床寿命提升 2-4x 与成本案例闭合所需的 DOM 归因损失下限)未经核实,属门 3 存亡变量;门 2 不就量级作裁定,仅确认其非低概率依附。
- 结论:本门裁定依据仅为"无可辩护的非组合式增量",不援引依附性条款。

## 四、创新性评级与裁定

- 评级:**低**。三条候选增量逐条裁定为 (c)、(d)、(c),无可辩护的非组合式增量。
- 裁定:**杀死**。依据规范 4.5 第一条(评级为低,无可辩护的非组合式增量)及任务口径(组合式应用级增量单独不足以通过)。
- 诚实性条款核查:方案简报未以"已核实"措辞掩盖先验缺口,其第 1 节与第 4 节均以开放表述将先验密度留待门 2 检索,规范 4.5 第三条不触发;JCIS 2017 等新增先验占据叙事空间的事实将如实写入门禁记录,供重提版本正面引用。
- 重提条件(规范第七节):须以新版本号从门 1 重走全部四门,且须展示新的非组合式增量;对增量 (i) 的重新措辞不构成重提理由。JCIS 2017 先验的存在意味着任何沿用"两性离子抗污界面保护活性炭容量"机制的重提版本,其承重新颖性必须落在该机制之外的维度(例如仅由仿生结构实现、传统涂层做不到的界面行为),否则门 2 结论不变。

## 五、检索边界与留档

- 检索工具:Crossref REST API(query.bibliographic,type=journal-article 过滤)与 PubMed E-utilities;无 SciFinder 权限,上述"无法定位"条目均不充当最终不存在证明。
- 网络检索引擎 AI 摘要中以下条目无法经 Crossref/PubMed 定位,按疑似摘要幻觉记录,不作先验亦不作空白证明:"Zwitterionic polymer-grafted activated carbon for enhanced removal of PFOA(J. Hazard. Mater. 2023)";"Poly(sulfobetaine) hydrogels for efficient removal of perfluoroalkyl substances";"Zwitterion-functionalized biochar for legacy and emerging PFAS(STOTEN 2024)"。
- 除 JCIS 2017(PubMed 摘要级)与台账已落账条目外,全部内容级结论标注为待全文核验;题录(DOI、刊名、年份)均经 Crossref 或 PubMed 核实。