# Ultimate fresh_1000_R4 科学与合成深审

日期：2026-08-02  
输入：`origin/Ultimate@d26d423cb84160cd962c1a2c6cc813544632556e`  
审查边界：市政二级出水、非蛋白人工吸附材料、非传统/混合模式离子交换主材料、最低正式释放级别 E1。  
状态：独立检索、设计审查、首次攻击、潘尧补充视角与 Reviewer 裁决均已完成。

## 1. 结论

本轮没有发现可以直接进入潘尧人工论证和 ImageGen 绘图的方案。

- R4 名义上有 1000 个编号，但只有 140 个独立展开概念卡；400 个编号没有逐项记录，另外 460 个只有表格短语或诊断分。
- 20 个污染物中，只有 PFOA、PFBS、PFHxS、BPA、NP 和 ROX 的市政二级出水吸附场景通过本轮证据门；8 个场景需要暂停并补证，6 个场景应终止。
- R4 压缩出的 19 个材料实体中，**0/19** 同时满足确切化学实体、反应闭合、可执行计量、空间主张可制造、关键 QC、可成型和可验证对照这组严格 E1 合成条件。
- BPA–DmpR 与短链 PFAS–SsuA/Bug 是最值得保留的上游谱系；NP 的污染问题和 Bayram 过程证据也值得保留。但 R4 给它们选择的 COF、PMO 或深腔网络实现均未过材料/合成门。
- Dieldrin、PFBS/OAT4、氟离子核糖开关、DMSP 等若干原型存在方向相反、对象不一致或化学分类错误，不能靠改材料修复。
- 因为不存在零 critical/high 的 E1/E2 实现，本轮**不生成图片**。在当前项目规则下，为未过门方案画“候选材料说明图”会把概念占位符视觉固化为貌似真实的化学实体，反而妨碍人工审阅。

这不是“1000 个想法没有价值”。更准确的结论是：R4 在 SP/BP/TR 层发现了少数有价值谱系，但把很多尚未实例化的 ME/SR 当作已完成材料，并让总分补偿了硬门失败。后续应从保留谱系重新开始小分子模型或制造优先的平台化，不能继承 R4 的 `pass` 或分数。

## 2. 审查方法

审查按 `SP 场景—BP 生物原型—TR 转译原则—ME 材料实现—SR 合成路线—ER 实验释放` 六模块进行：

1. 先冻结二级出水场景和分析相态；场景无效者不进入深材料设计。
2. 对承重生物主张优先查原始结构、转运、酶学或环境过程论文；毒性靶标和催化结合只作辅助。
3. 对材料家族查直接污染物先例、水相竞争、离子形态、DOM/无机盐干扰和骨架稳定性。
4. 把每条合成路线拆成确切起始物、反应类型、计量、顺序、纯化、结构确认、空间分布确认和成型 QC。
5. 独立攻击后，再使用潘尧提供的经验视角检查新手可执行性、安全、放大、全文一致性和六段仿生故事；这些视角只补充审查，不代替科学门。
6. Reviewer 只允许 `E1_ready`/`E2_ready` 进入 owner 图示包；评分不允许补偿任何硬门。

## 3. 输入真实性

详细计数见同目录 `INPUT_AUDIT_AND_LINEAGE_MANIFEST.md`。最关键的数据事实是：

| 层级 | 数量 | 可支持的审查深度 |
|---|---:|---|
| 独立展开概念卡 | 140 | 可开始核对 SP/BP/TR/ME，但多数不能审 SR |
| 仅表格短语或诊断分 | 460 | 只能归谱系，不能判材料与合成正确性 |
| 无逐 ID 记录 | 400 | 不能称为可审计设计 |
| R4 合计编号 | 1000 | 不是 1000 个独立、完整材料方案 |

R4 的 L2 也不是 150 次逐方案深审：5 个方案有新增完整文件，5 个引用旧方案，24 个只在批次摘要中处理，116 个被批量归并。所谓“19 个真正独立材料实体”还包含扭转角腔、平面腔等非化学实体，并把本应拆开的 NPET 碗与 PVI 刷合并。

## 4. 场景门：20 个污染物

`valid` 只表示可以继续审查 BP/TR/ME，不表示已有可放行材料。

| 污染物 | 主要一手/官方证据 | 裁决 | 对设计的约束 |
|---|---|---|---|
| PFOA | 中国市政出水 3–107 ng/L；美国多厂均值约 9.7 ng/L。[中国](https://doi.org/10.1016/j.envpol.2012.12.019)，[美国](https://doi.org/10.1021/acs.est.4c12167) | valid | PFAS 混合物、EfOM、主要阴离子和连续柱穿透必须是主实验。 |
| PFBS | 中国/美国多厂均有检出，短链常规去除困难。[中国](https://doi.org/10.1016/j.envint.2022.107447)，[美国](https://doi.org/10.1021/acs.est.4c12167) | valid | 不允许只用去离子水高浓度容量；需以最差短链成员报告。 |
| PFHxS | 中国全国调查与美国多厂均支持最终出水存在。[中国](https://doi.org/10.1016/j.envint.2022.107447)，[美国](https://doi.org/10.1021/acsestwater.4c00541) | valid | 作为中链磺酸 PFAS；工业输入高值不能当生活污水典型值。 |
| GenX/HFPO-DA | 中国五厂全部低于 0.5 ng/L，而其他调查提示区域性风险；结果不一致。[中国数据](https://static1.squarespace.com/static/5759f142c6fc085e2d4b8854/t/62a75184c958fc5231e3b225/1655132548884/HFPO-DA_Data_Reports_US_China_Statera_May_2022.pdf)，[美国](https://doi.org/10.1021/acsestwater.4c00541) | conditional | 暂停 GenX 专属材料；先闭合生活污水主导厂的分布和来源。 |
| BPA | 厦门七厂溶解/吸附相监测，出水中位数约 177 ng/L。[发生](https://doi.org/10.1016/j.envpol.2017.03.018)，[EfOM 干扰](https://doi.org/10.1016/j.chemosphere.2012.01.026) | valid | 现实入口为几十至数百 ng/L；BPS/BPF、酚类、PAC/GAC 是必需竞争与基准。 |
| NP | 天津一年监测年均约 2.92 µg/L；广东 38 厂溶解态证据支持持续存在。[天津](https://doi.org/10.1016/j.chemosphere.2009.06.036)，[广东](https://doi.org/10.1016/j.scitotenv.2020.136689) | valid | 必须覆盖 NP 异构体和 NP1EO/NP2EO/NPEC，防止把前体转化误判为负去除。 |
| ROX | 珠三角多厂与一年期监测支持几十至数百 ng/L。[四厂](https://doi.org/10.1016/j.watres.2007.06.023)，[一年监测](https://doi.org/10.1007/s11270-021-05053-y) | valid | 目标应是大环内酯类别相对 EfOM/类外阳离子药物，而非强行单分子分辨。 |
| Octocrylene | 全国检出、厦门未检出和东北单厂风险结果互相不一致。[厦门](https://doi.org/10.1016/j.jhazmat.2013.11.056)，[东北](https://doi.org/10.1016/j.chemosphere.2024.142179) | conditional | 先做未过滤/0.45 µm/颗粒三相监测，证明吸附优于强化固液分离。 |
| 2,6-DCP | 仅有一套可用多厂官方计划，缺第二独立地区和中国数据。[官方报告](https://www.healthywa.wa.gov.au/~/media/Files/Corporate/general%20documents/water/Groundwater%20replenishment/PCRP%20Chapter6-9.pdf) | conditional | 暂停材料释放，先补场景与分析口径。 |
| PCP | 现代市政二级出水分布不足，且 pH 7 主要为阴离子。 | invalid | 停止当前市政二级出水主场景。 |
| DDT | 单一波兰厂支持亚 ng/L ΣDDT，但水/颗粒分相不足。[原始研究](https://doi.org/10.1007/s11270-021-05261-6) | conditional | 先补第二地区和相态证据；不得把 ΣDDT 当 p,p'-DDT。 |
| DDE | 同一研究缺独立 DDE 中心分布。[原始研究](https://doi.org/10.1007/s11270-021-05261-6) | conditional | 应先研究 OCP 家族和颗粒相，不先做单一 DDE 材料。 |
| Dieldrin | EPA 九厂只有零散可定量样本，无现代中国分布。[EPA](https://www.epa.gov/sites/default/files/2018-11/documents/occurrence-cec-wastewater-9-treatment-work.pdf) | invalid | 停止当前场景。 |
| Endosulfan | 单一波兰厂、亚 ng/L、异构体/硫酸酯与相态未闭合。[原始研究](https://doi.org/10.1007/s11270-021-05261-6) | conditional | 先监测，不进入材料深设计。 |
| β-HCH | 只有 ΣHCH 中心值，β-HCH 独立负荷不足。[原始研究](https://doi.org/10.1007/s11270-021-05261-6) | conditional | 先闭合异构体分布。 |
| BDE-209 | 合肥厂出水仍检出，但主要由沉降/污泥转移去除。[原始研究](https://doi.org/10.1016/S1001-0742(12)60201-0) | conditional | 先证明溶解/胶体相存在独立吸附缺口。 |
| PCB-209 | 官方监测约 pg/L，缺清楚工程负荷与中国证据。[官方报告](https://www.crd.ca/media/file/2022-core-area-wastewater-facilities-environmental-monitoring-program-report) | invalid | 检出能力不等于吸附工程意义。 |
| HCBD | 爱尔兰 EPA 研究均低于 LOD，无中国阳性分布。[官方报告](https://www.epa.ie/publications/monitoring--assessment/waste-water/Part-A-Final-Report-Effluent-Characterisation-Study-November-2012.pdf) | invalid | 停止当前场景。 |
| TCDD | 多厂报告没有检出 2,3,7,8-TCDD；TEQ 不能代替单体浓度。[官方报告](https://www.healthywa.wa.gov.au/~/media/Files/Corporate/general%20documents/water/Groundwater%20replenishment/PCRP%20Chapter6-9.pdf) | invalid | 停止当前场景，禁止用混合物 TEQ 回填。 |
| Chloroform | 主要在氯化后生成，不是一般二沉出水问题。[EPA](https://www.epa.gov/sites/default/files/2020-11/documents/chloroform.pdf)，[华东](https://doi.org/10.1016/j.watres.2019.03.072) | invalid | 可另立消毒副产物控制项目，不能混入当前主场景。 |

汇总：6 valid、8 conditional、6 invalid。

## 5. BP/TR 证据裁决

| R4 承重原型/规则 | 一手证据复核 | 裁决 |
|---|---|---|
| DmpR/PoxR 酚识别 | 6IY8 直接显示 phenol 在疏水小腔中由 His100/Trp128 区域定位；支持“固定极性锚＋邻接疏水/形状环境”，但不是 BPA 直接证据。[DmpR](https://doi.org/10.1038/s41467-020-16562-5) | **保留 BP/TR，BPA 为近似物推断。**R4 单个吡啶 N 不是原型完整复刻。 |
| SsuA 烷基磺酸盐摄取 | 天然摄取功能成立；R4 引用的 2010 结构是 apo，不能支持其水桥几何。已有 holo 研究可支持含水磺酸头定位。[apo](https://doi.org/10.1107/S1744309110006226)，[holo](https://doi.org/10.1371/journal.pone.0080083) | **保留功能谱系，纠正结构证据。** |
| Bug/TRAP 羧酸夹钳 | 天然有机酸转运的羧酸夹钳成立，但对 GenX 支链醚羧酸只有类比。[Bug](https://doi.org/10.1016/j.jmb.2007.08.006) | **保留一般头基—整体占位 TR；GenX 专属 Y 腔不受支持。** |
| OAT4 “C6 阈值” | 直接转运研究中 PFHxS/PFOA/PFOS 等有摄取而 PFBS 没有，但链长与头基同时变化；没有结构、突变或 C5 系列，不能证明 ≥C6 或 10 Å 盲腔。[OAT4](https://doi.org/10.1007/s00204-022-03428-6) | **降为反向筛选线索；删除精确深度主张。** |
| SBP 硫酸盐四面体识别 | 硫酸盐的多氢键几何真实，但天然优选物正是二级出水中的高浓度竞争阴离子。[SBP](https://doi.org/10.1038/314257a0) | **不能支撑 PFAS-over-sulfate 选择性；作为负向竞争警告。** |
| Bayram NP ipso 过程 | NP 的 alpha-quaternary 碳依赖代谢真实。[机制](https://doi.org/10.1074/jbc.M413446200)，[路径](https://doi.org/10.1128/AEM.02994-06) | **保留 SP/BP；TR 只能写成催化/电子约束启发，不能直接等同静态深腔亲和。** |
| NPET–ROX | ROX 与核糖体靶点相互作用真实。[NPET](https://doi.org/10.1016/j.jmb.2004.07.095) | **B 类几何证据；毒性/药理靶标不能单独通过 Gate A。** |
| FcRn pH 门 | FcRn pH 功能真实但与 ROX 捕获无关。[FcRn](https://doi.org/10.1016/S0969-2126(98)00008-2) | **删除 ROX 专属仿生主张；最多是通用 pH 开关灵感。** |
| DDT 脱氯化氢酶/膜分配 | 催化和膜分配存在，但催化碱位不能自动转译为可逆静态吸附。[酶学](https://doi.org/10.1016/S0021-9258(18)69878-3)，[膜分配](https://doi.org/10.1016/0005-2736(86)90414-1) | **保留过程证据，当前静态碱位 TR 驳回。** |
| Dieldrin 环氧化物水解酶 | 经典实验明确报告 dieldrin/endrin 抗该酶攻击。[原始实验](https://doi.org/10.1016/0048-3575(80)90111-X) | **致命方向错误；终止该 BP/TR。** |
| Fluoride riboswitch→有机氟 | 核糖开关识别自由 F−，不是共价 C–F。[原始论文](https://doi.org/10.1126/science.1215063) | **致命对象错误；终止。** |
| DMSP→PFBS | DMSP 是带正电 sulfonium 与 carboxylate 的两性离子，不是 sulfonate。[DddP](https://doi.org/10.1111/mmi.13119) | **化学分类错误；终止该映射。** |
| FABP4→短链 PFSA | 2025 结构直接支持 PFOA/PFDA/PFHxDA 等宽谱 PFCA 结合，不支持 PFBS/PFHxS 专属。[FABP4](https://doi.org/10.1021/jacsau.5c00504) | **只作宽谱几何参考。** |
| LinA→β-HCH | HCH 异构体过程成立，但 β-HCH 的低反应性是负向拒绝，不是正向捕获。[LinA](https://doi.org/10.1111/1462-2920.12009) | **当前“识别缺失”TR 驳回。** |
| DHPB/PceA→2,6-DCP | 直接结构/过程证据强。[DHPB](https://doi.org/10.1016/j.jinorgbio.2022.111944)，[PceA](https://doi.org/10.1038/ncomms15858) | **保留 B 类结构线索；SP 未闭合，不能释放。** |

多原型叠加不提高证据等级。一个直接功能原型加两个毒性靶标或通用物化类比，仍然只有一个直接功能原型。

## 6. 19 个材料实体的化学与制造裁决

| # | R4 实体 | 最早断裂点 | Reviewer 裁决 |
|---:|---|---|---|
| 1 | NP 深腔 resorcinarene 网络 | ME/SR：缺兼具深壁、酚锚和交联手柄的确切单体；高官能交联会凝胶并埋腔 | `reject_embodiment_retain_lineage`；先做离散主体溶液模型，再单点低密度固定。 |
| 2 | BPA β-酮烯胺 COF 门系列 | SR：定制吡啶二胺、R 基、合成纯化均未冻结；变体不能默认同晶格 | `reject_embodiment_retain_lineage`；先做可溶锚/门模型。 |
| 3 | Dieldrin 苯基-SBA-15＋方酰胺 | BP：EH 证据相反；ME 只能得到统计双功能表面 | `terminate_lineage`（当前 BP/TR）；材料仅可作普通疏水/氢键对照。 |
| 4 | PFHxS resorcinarene 盲腔 | SR：R4 所写 CuAAC/异氰酸酯连接不成立，C4/C3 几何与“链长=腔深”均错误 | `reject_embodiment_retain_lineage`，但须先删除 OAT4 精确深度主张。 |
| 5 | BTEB/BTPU PMO＋C6 封底 | ME/SR：延迟加料不证明孔口分子定位；C6 硅烷只会缩孔/改润湿/堵孔，不会制造盲底 | `reject_embodiment_retain_lineage`。PMO 可保留为统计双区机制筛选，不得画固定 C6 腔。 |
| 6 | DDT 碱位 PMO＋C12 壁 | TR/SR：所谓水相中性超强碱会质子化；随机 C12 接枝不等于膜链有序；还会转化为反应捕获 | `reject_embodiment_retain_BP_only`；先做均相速率与产物。 |
| 7 | PFBS 三脲-SBA-15 | TR/ME：tren＋3 异氰酸硅烷可形成三脲，但柔性链不保证四面体；SBP 会优先提示 sulfate 竞争 | `control_only`；不能以“精确四面体夹口”进入 E1。 |
| 8 | GenX 支链腔 PMO | ME：GenX 甲酯加入普通溶胶凝胶不会形成 Y 形腔，且删除了关键羧酸头 | `reject_embodiment`; SP 又为 conditional。 |
| 9 | ROX NPET 碗＋PVI 刷 | ME/SR：NPET 碗无单体，PVI 刷无引发剂/链长/Cu 清除/堵孔 SOP；组合无制造基础 | `split_and_reject`; PVI-GAC 仅可作通用 pH/电荷对照。 |
| 10 | PCP 卤键＋酚锚＋β-CD/SBA-15 | SP invalid；三元随机接枝不能形成同一识别位点 | `terminate_current_scenario`。 |
| 11 | β-HCH 轴向氯“缺失识别” | TR/ME：没有正结合能、单体或骨架 | `reject`; SP conditional。 |
| 12 | Octocrylene NDI 笼＋Michael 位点 | BP/TR/ME：未实例化；β-碳强位阻；不可逆反应耗尽容量 | `reject`; 先做均相 k2 与产物谱，且 SP conditional。 |
| 13 | DCP 2,6-双氯轮廓腔 | SP conditional；ME 无单体/模板固定/聚合路线 | `retain_concept_only`；先补场景，再考虑 carrier-first 薄层印迹。 |
| 14 | BDE-209 卤键＋醚氧 | TR：把碘/硒功能单元和污染物卤素的供受体方向混淆；无确切 POP | `reject`; SP conditional。强水相卤键需专门电子贫化卤键供体，不能从普通 C–Cl/C–Br 外推。[水相卤键](https://doi.org/10.1038/nchem.2111) |
| 15 | TCDD 芘/萘 POP＋侧位卤键 | SP invalid；随机芳香网络不能编码 2,3,7,8 图案 | `terminate_current_scenario`; POP 仅作普通疏水/π 对照。 |
| 16 | PCB-209 扭转角腔 | SP invalid；ME 只是约 85° 的文字占位符 | `terminate_current_scenario`。 |
| 17 | DDE 平面腔 | SP conditional；ME 无化学结构，普通芳香孔只产生疏水/π 分配 | `reject_embodiment`。 |
| 18 | Endosulfan MOF-808/POM | SP conditional；POM 未定义且功能是催化水解而非可逆吸附 | `reject_as_adsorbent`; 若另立反应路线需完整产物/毒性/元素平衡。 |
| 19 | α-CD/DVS–CHCl3 | SP invalid；合成本身成熟但只是已知包结/材料基线 | `control_only`; CHCl3–CD 水相缔合已有直接先例。[先例](https://doi.org/10.1246/bcsj.62.3718) |

### 材料家族层面的先例攻击

- BPA–COF 的孔径、π–π和氢键吸附已有直接先例，R4 只有在可制造并证明“DmpR 锚/门空间变量”独立增益时才有新意。[BPA–COF](https://doi.org/10.1039/D1RA02342J)
- BPA 表面/半共价/假模板 MIP 已形成密集先例；把 AG-COF 简化为普通 BPA-MIP 虽然更容易合成，但会丢失独立创新，不是同一谱系的合格再平台化。[表面假模板](https://doi.org/10.1016/j.jhazmat.2010.02.083)，[半共价 SBA-15](https://doi.org/10.1016/j.apsusc.2018.04.017)
- 中性脲–疏水 POP 已能在水中识别阴离子；“脲＋疏水孔”本身不是空白。[脲 POP](https://doi.org/10.1039/D0SC02941F)
- 阳离子深腔主体已用于 PFAS；若新主体仍主要靠固定正电，就必须按离子交换/静电主导审查。[PFAS 深腔主体](https://doi.org/10.1021/jacs.5c04762)
- 阳离子 β-CD 的短链 PFAS 捕获被 1 mM sulfate 显著抑制，说明带电主客体不能绕过真实水阴离子竞争。[阳离子 β-CD](https://doi.org/10.1021/acscentsci.2c00478)
- 胺/氟烷基 PMO 的 PFAS 捕获已有直接工作，且作者将静电识别为主导；新 PMO 只有经等 IEC、等疏水量、等孔结构对照证明的空间增益才有独立贡献。[PFAS–PMO](https://doi.org/10.1016/j.jhazmat.2023.131047)
- DDT 在亚 ng/L 对活性炭已有极高分配；R4 的普通疏水孔必须超过这一真实基线，而不是只报告高去除率。[DDT–AC](https://doi.org/10.1016/j.watres.2009.06.031)
- ROX–D101 印迹树脂和 2026 COF 表面印迹已有直接先例；PVI/印迹路线的新颖性空间很小。[D101](https://doi.org/10.13386/j.issn1002-0306.2017.19.014)，[COF–MIP](https://doi.org/10.1016/j.scp.2026.102500)

## 7. 有界再平台化结果

本轮对保留谱系进行了制造优先的有界搜索，没有把“存在下一种可能材料”误写成“已经优化完成”。

| 谱系 | 尝试的制造优先实现 | 保留资产 | 未通过 E1 的原因 | 当前状态 |
|---|---|---|---|---|
| BPA–DmpR | 可溶双酚/吡啶锚模型；成熟 BPA dummy-MIP/半共价 MIP 作为制造基线 | valid SP；DmpR 酚锚＋邻接疏水环境 | 可溶模型尚未证明水相锚/门增益；普通 MIP 先例占满且不能体现 DmpR 门变量；AG-COF 单体/SOP 未闭合 | `lineage_retained_E0` |
| 短链 PFAS–SsuA/Bug | BTEB PMO＋模板保留时外表面短时胺化，再完全封端为中性脲，随后去模板；与均匀接枝体做空间单变量 | valid SP；含水头基定位＋邻接低极性区 | 外表面选择性功能化有方法先例，但迁移到 phenylene-PMO 并转成脲仍是推断；不能保证孔口共定位；PMO 在中性/偏碱连续流下的 Si/功能层稳定性是 high 风险 | `lineage_retained_E0` |
| NP–Bayram | 已验证离散 cavitand 溶液模型→单点低密度固定于大孔载体 | valid SP；NP 直接生物过程 | alpha-quaternary 依赖首先是催化/电子规则；尚无目标/异构体水相选择性的小分子证据；定制主体昂贵且多步 | `lineage_retained_model_gate` |
| ROX 类别 | 低 DP PVI-co-HEMA/GAC 短刷，只保留 pH 捕获/释放 | valid SP；大环内酯类工程目标 | FcRn 与 ROX 无直接对应；ROX 在 pH 7 主要为阳离子，PVI/阴离子材料容易退化为普通电荷或离子交换；直接印迹先例拥挤 | `control_only` |
| DCP | carrier-first 后的纳米薄层表面印迹 | DHPB/PceA B 类结构 | SP conditional；位置异构体增益、模板泄漏和第二场景源均未闭合 | `scenario_blocked` |

外表面短时功能化可作为制造工具，但不是已证成的孔口人工识别单元。已有研究显示短时 APTMEES 处理可以偏向外表面，而延长时间会进入内孔；这支持“时间是可制造变量”，也同时否定“模板在孔中就必然只改外表面”的简单假设。[外表面功能化](https://doi.org/10.1016/j.micromeso.2016.10.023)

## 8. 对既有主分支 E1 登记的影响

R4 深审还暴露出主分支三个历史 E1 包的承重缺口。按不可继承原则，本轮 Reviewer 重新裁决如下：

| 历史包 | 新发现的最早断裂点 | 新状态 |
|---|---|---|
| SC-P02 / PG-PMO | ME/SR：延迟共缩合不能保证所画的孔端 BTPU/内腔 BTEB 空间结构；缺少可重复制造该变量的直接先例 | `E1_withdrawn_lineage_retained` |
| BPA20-01 / AG-COF | SR：确切二胺/R 系列、单体制备、纯化和同晶格性未冻结；开放介孔不等于局部门 | `E1_withdrawn_lineage_retained` |
| DDT50-01 / LPO-SIP | SP：当前可用证据不足以稳定定义市政二级出水溶解相 DDT 工程负荷；颗粒/胶体与 ΣDDT 口径未闭合 | `E1_withdrawn_scenario_blocked` |

这三项撤回不等于性能被实验否定，也不终止其上游谱系；它只纠正“纸面包已经可以直接开做”的过早表述。正式 E1/E2 登记因此暂时清空。

## 9. 潘尧补充视角审查

在独立攻击完成后，按用户提供的 review skill 做了补充检查：

- **新手执行：** R4 多数路线缺精确结构、当量、加料次序、停留时间、洗涤终点、失败外观和安全处置，无法由非原作者准确复现。
- **合成专家：** 多个方案把“官能团能反应”误当成“功能位点会以指定空间关系形成”；硅烷自缩合、先后接枝竞争、凝胶点、孔堵和模板残留没有进入反应账本。
- **工程放大：** SBA-15/PMO 粉末的水解、磨耗、压降、残余 CTAB/Si/有机层浸出和每床体积位点数普遍没有闭合。
- **全文一致性：** R4 自己承认 PFHxS A14 选择方向相反、Endosulfan 是催化而非吸附、PCB-209 场景存疑，却仍给 `pass`；总分掩盖了模块冲突。
- **六段故事：** 场景、原型、转译、材料、合成、工程中常有一至三段仍是占位符。最常见的断裂是“真实生物过程→静态吸附亲和”以及“设计几何→实际可制造空间结构”。

这些检查没有替代模型的科学判断，但确认了本轮 0 个 owner-ready 方案不是因为门槛过于形式化，而是存在真实、可定位的承重缺口。

## 10. Reviewer 最终释放登记

| 状态 | 数量 | 对象 |
|---|---:|---|
| E2_ready | 0 | 无 |
| E1_ready | 0 | 无 |
| owner review / ImageGen eligible | 0 | 无 |
| upstream lineage retained | 3 个主要谱系 | BPA–DmpR、短链 PFAS–SsuA/Bug、NP–Bayram |
| scenario blocked | 8 个污染物 | GenX、Octocrylene、2,6-DCP、DDT、DDE、Endosulfan、β-HCH、BDE-209 |
| current scenario terminated | 6 个污染物 | PCP、Dieldrin、PCB-209、HCBD、TCDD、Chloroform |

因此，本轮没有更新 ImageGen 提示词，也没有调用 ImageGen。只有当某一再平台化实现补齐确切实体、逐步 SOP、空间/QC 证据路径和因果对照并通过重新攻击后，才会生成 A 生物证据—B 功能抽象—C 候选材料与合成的版本锁定图示包。

## 11. 下一轮唯一研究动作

不再从 R4 评分表中横向扩展。按信息增益排序，下一轮先对 **BPA–DmpR 谱系做可溶最小模型门**：

1. 选择可购买或一至两步可制备的、结构确切的人工识别单元模型；
2. 在 pH 6.5–8.0、真实离子强度和可控 DOC 下，测 BPA/BPF/BPS/phenol 的竞争结合或谱学扰动；
3. 用删除锚、错位锚和等疏水平面分子排除单纯 logD/π 面积；
4. 只有存在预注册的非单调几何增益，才重新选择 COF、表面印迹或其他固体平台；
5. 若最小模型失败，终止 DmpR→人工静态锚门 TR，而不是继续换载体。

短链 PFAS 谱系排第二：先验证模板保留的外表面短时功能化能否在 phenylene-PMO 上稳定制造可测的中性脲空间差异，并同时完成 Si/有机层浸出；在此之前不恢复 SC-P02 的 E1。

## 12. 证据边界

- 文献能够验证已知科学、直接先例和合成反应，但不能证明一个尚未合成的新材料已经具有预期性能。
- “化学正确”在本报告中指：没有已知承重反应错误，质子化/水相竞争被显式处理，合成路线能得到所声明实体，且未知性能被写成可证伪假设。
- 本轮覆盖论文和官方报告先例，未完成 PMO、cavitand、MIP、COF 和环糊精方向的完整专利 claim chart；因此任何未来论文新颖性结论仍需单独专利检索。
- 未授权采购、合成或实验。
