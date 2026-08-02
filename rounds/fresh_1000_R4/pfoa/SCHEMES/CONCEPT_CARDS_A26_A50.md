# PFOA 50 概念卡（L1 全量）A26-A50

## A26 — FABP4 portal helix 门控转译为温敏孔口

- **原型：** PROTO_PFOA_001（FABP4，结构级）
- **转译原则：** FABP4 α-helix II 门控配体进出（开放/闭合构象）→ 温敏聚合物孔口（LCST 开关）
- **材料概念：** 介孔硅胶孔口接枝 PNIPAM-co-脲基短刷，25°C 开放（PFAS 进入），40°C 闭合（浓缩锁定），脲基提供头基锚
- **合成概要：** SBA-15 → ATRP 接枝 NIPAM + 脲基丙烯酸酯共聚刷
- **致命风险：** PNIPAM 响应温度不响应 PFAS（非目标诱导）；闭合后再生需降温+溶剂洗；先例多
- **六维诊断分：** 因果 9/选择性 11/可转译 14/原创 7/可证伪 7/证据 7 = **55**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** 门控是 FABP4 真实特征，但温敏不是 PFAS 诱导 → mechanism_informed（弱）

## A27 — hL-FABP 配体交换色谱

- **原型：** PROTO_PFOA_002（hL-FABP，结构级）
- **转译原则：** FABP 在细胞内释放脂肪酸给靶酶（配体交换）→ 材料先捕获 PFAS 再用竞争性配体洗脱
- **材料概念：** 芳烃疏水树脂（捕获）+ 油酸钠/环糊精溶液（竞争洗脱），模拟 FABP→靶酶的配体递送
- **合成概要：** 商用 DVB/苯乙烯树脂 + 再生液优化（油酸钠 10 mM）
- **致命风险：** 本质是普通树脂 + 竞争洗脱，仿生仅为再生策略命名；无选择性机制
- **六维诊断分：** 因果 8/选择性 8/可转译 16/原创 4/可证伪 7/证据 7 = **50**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** 删除仿生后就是树脂+洗脱 → rational_chemical

## A28 — HSA 药物竞争位点转译为分子印迹

- **原型：** PROTO_PFOA_003（HSA，结构级）
- **转译原则：** Sudlow I 同时结合华法林/PFOA（竞争位点）→ 以华法林类似物为假模板印迹 PFOA 腔
- **材料概念：** 4-乙烯基吡啶/EGDMA 表面印迹珠，假模板为全氟辛酸甲酯（避免 PFOA 泄漏）
- **合成概要：** 悬浮聚合，PFOA-Me 模板，4-VP/EGDMA=1:4，60°C AIBN 引发
- **致命风险：** PFAS-MIP 先例极多（2020-2026 数十篇）；模板泄漏；无独立选择性机制
- **六维诊断分：** 因果 8/选择性 9/可转译 16/原创 3/可证伪 7/证据 7 = **50**
- **谱系状态：** SP-retained / BP-conditional / TR-invalid / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** MIP 不是仿生 → rational_chemical（原型为装饰性）

## A29 — OAT4 肾小管上皮细胞极性膜转译为 Janus 膜

- **原型：** PROTO_PFOA_004（OAT4，机制级）
- **转译原则：** 肾小管上皮细胞顶膜（OAT4 面向管腔）与基底膜（面向血液）极性不对称 → 不对称膜（一面捕获一面释放）
- **材料概念：** 不对称 PVDF 膜：顶层致密脲功能化（PFAS 捕获），底层大孔支撑（渗透液侧），错流过滤
- **合成概要：** 相转化法 PVDF 膜 + 表面接枝脲基丙烯酸（UV 引发）
- **致命风险：** 膜过程不是吸附（项目范围限固体吸附剂）；通量与选择性矛盾
- **六维诊断分：** 因果 9/选择性 12/可转译 12/原创 9/可证伪 6/证据 7 = **55**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-embodiment_rejected（膜非吸附剂）/ SR-bench_ready / ER-out_of_scope
- **仿生真实性快检：** 极性膜是真实细胞特征 → functional_biomimicry（但超出项目范围）

## A30 — SsuA ABC 转运体 ATP 驱动转译为电化学浓缩

- **原型：** PROTO_PFOA_005（SsuA，结构级）
- **转译原则：** SsuA 将底物递送给 ABC 转运体，ATP 水解驱动 uphill 转运 → 电化学驱动 PFAS 浓缩
- **材料概念：** 导电碳电极表面脲功能化，开路吸附 PFAS，施加负电位排斥释放（电化学再生）
- **合成概要：** 玻碳电极/碳毡 + 重氮盐接枝脲基芳烃
- **致命风险：** 电化学再生不是仿生（ATP 驱动是化学能非电能）；电极面积有限
- **六维诊断分：** 因果 8/选择性 11/可转译 13/原创 9/可证伪 7/证据 6 = **54**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** ATP→电化学转译跳跃大 → mechanism_informed（弱）

## A31 — TauA 底物诱导域闭合转译为分子钳

- **原型：** PROTO_PFOA_006（TauA，机制级）
- **转译原则：** TauA 结合底物后两域闭合（Venus flytrap 机制）→ 材料设柔性分子钳（PFAS 诱导闭合锁定）
- **材料概念：** 双脲臂柔性分子钳（二苯醚铰链），PFAS 头基桥联两脲臂→闭合，锁定全氟链
- **合成概要：** 二苯醚-4,4'-二胺 + 2 eq 芳基异氰酸酯→双脲钳，接枝于硅胶
- **致命风险：** 水相分子钳闭合驱动力不足（无疏水核心）；柔性铰链在水中无预组织
- **六维诊断分：** 因果 11/选择性 15/可转译 12/原创 12/可证伪 7/证据 7 = **64**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 域闭合是 TauA/SBP 真实机制 → functional_biomimicry

## A32 — 氟核糖开关 RNA 适配体转译为 MIP 腔

- **原型：** PROTO_PFOA_007（氟核糖开关，机制级）
- **转译原则：** 核糖开关以 RNA 三级结构形成精确配位口袋 → 分子印迹模拟 RNA 腔（形状+氢键阵列）
- **材料概念：** PFOA 直接模板 MIP，功能单体为 2-乙烯基嘧啶（模拟 RNA 碱基氢键面）+ 甲基丙烯酸
- **合成概要：** PFOA 模板 + 2-VPy/MAA/EGDMA 本体聚合，研磨筛分
- **致命风险：** PFOA 模板泄漏（环境释放）；嘧啶-羧酸根水相氢键极弱；MIP 先例饱和
- **六维诊断分：** 因果 8/选择性 10/可转译 14/原创 5/可证伪 7/证据 6 = **50**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** RNA 适配体→MIP 是常见类比但无特异性 → rational_chemical

## A33 — EPS 群体感应转译为密度响应释放

- **原型：** PROTO_PFOA_008（EPS，现象级）
- **转译原则：** 生物膜群体感应（QS）在细胞密度达标后触发 EPS 重塑 → 材料在 PFAS 负载达标后触发释放
- **材料概念：** 负载响应型水凝胶：PFAS 积累改变局部疏水性→凝胶相变→释放浓缩 PFAS 液滴
- **合成概要：** PNIPAM-co-氟碳丙烯酸酯水凝胶（PFAS 积累降低 LCST→相变释放）
- **致命风险：** 相变浓度阈值难以精确设定；释放后凝胶需重新溶胀；非特异
- **六维诊断分：** 因果 7/选择性 8/可转译 11/原创 12/可证伪 5/证据 5 = **48**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** QS 是真实生物现象，但材料"密度响应"不是 PFAS 特异 → mechanism_informed（弱）

## A34 — SP-A 磷脂膜重构转译为脂质体捕获

- **原型：** PROTO_PFOA_009（SP-A，类比级）
- **转译原则：** SP-A 在肺泡表面重构磷脂膜（管状髓磷脂）→ 人工脂质体/囊泡捕获 PFAS（PFAS 插入脂质双层）
- **材料概念：** DPPC/胆固醇脂质体（模拟肺表面活性膜），PFAS 以两亲性插入脂质双层，离心/过滤分离
- **合成概要：** 薄膜水化法 DPPC/Chol（7:3）脂质体，挤出 100-200 nm
- **致命风险：** 脂质体不是固体吸附剂（项目范围）；分离困难；成本高；不可再生
- **六维诊断分：** 因果 7/选择性 9/可转译 8/原创 10/可证伪 5/证据 6 = **45**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-embodiment_rejected（非固体吸附剂）/ SR-bench_ready / ER-out_of_scope
- **仿生真实性快检：** 膜插入是真实物理过程，但超出项目范围 → out_of_scope

## A35 — NTCP 肝窦内皮窗孔转译为分级孔碳

- **原型：** PROTO_PFOA_010（NTCP，机制级）
- **转译原则：** 肝窦内皮细胞有 100-200 nm 窗孔（fenestrae），允许血浆蛋白（含 PFAS-HSA 复合物）通过到达肝细胞 → 大孔-介孔-微孔三级碳
- **材料概念：** 三级孔碳：大孔 100-200 nm（传质）+ 介孔 4-8 nm（DOM 预筛）+ 微孔 1-2 nm（PFAS 捕获）
- **合成概要：** 双模板法（PS 微球 + F127）+ 酚醛树脂碳化
- **致命风险：** 分级孔碳先例极多；微孔捕获 PFAS 无选择性机制；本质是传质优化非识别
- **六维诊断分：** 因果 9/选择性 9/可转译 16/原创 5/可证伪 7/证据 7 = **53**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** 窗孔是真实结构，但转译为分级孔碳是通用工程 → rational_chemical

## A36 — FABP4 脂肪酸 β-氧化递送转译为捕获-降解串联

- **原型：** PROTO_PFOA_001（FABP4，结构级）
- **转译原则：** FABP4 将脂肪酸递送给过氧化物酶体进行 β-氧化降解 → 材料先捕获 PFAS 再递送给降解催化剂
- **材料概念：** 双功能颗粒：外层脲/芳烃捕获 PFAS + 内层负载光催化剂（TiO₂/g-C₃N₄），UV 照射下原位降解
- **合成概要：** 核壳：g-C₃N₄ 核 + 介孔 SiO₂ 壳（脲功能化）
- **致命风险：** PFAS 光降解极慢（C-F 键能 485 kJ/mol）；捕获-降解耦合效率未知；项目范围为吸附非降解
- **六维诊断分：** 因果 9/选择性 11/可转译 12/原创 11/可证伪 6/证据 6 = **55**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 递送-降解是 FABP4 真实下游功能 → functional_biomimicry（但降解超出吸附范围）

## A37 — hL-FABP 配体结合热力学转译为焓驱动低温吸附

- **原型：** PROTO_PFOA_002（hL-FABP，结构级）
- **转译原则：** FABP-PFAS 结合为放热过程（ΔH<0，Fan 2025）→ 低温有利于吸附 → 材料设计为焓驱动（非熵驱动）
- **材料概念：** 高密度氢键供体孔壁（多脲/多硫脲），利用焓驱动在低温（10-15°C，冬季出水）增强吸附
- **合成概要：** 介孔硅胶 + 多脲硅烷高覆盖接枝（目标 >2 mmol NH/g）
- **致命风险：** 水相氢键焓被水竞争抵消；高密度接枝堵孔；温度效应可能 <2 倍
- **六维诊断分：** 因果 11/选择性 12/可转译 15/原创 9/可证伪 7/证据 7 = **61**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** 放热结合是 FABP-PFAS 真实热力学特征 → functional_biomimicry

## A38 — HSA 脂肪酸结合位点 7（FA7）转译为深腔芳烃笼

- **原型：** PROTO_PFOA_003（HSA，结构级）
- **转译原则：** HSA FA7 位点（subdomain IIIA）深埋疏水腔 + 极性入口 → 深腔芳烃笼（calix[4]arene 或 resorcinarene）
- **材料概念：** 四磺化 calix[4]arene 交联网络，深腔匹配 PFOA 全氟链（腔深 ~8 Å），上缘磺酸基提供水溶性+静电辅助
- **合成概要：** calix[4]arene 磺化 + 甲醛交联（或 DVS 交联），水相沉淀聚合
- **致命风险：** 磺酸基带负电→与 PFAS 羧酸根排斥；calix[4]arene 腔径 ~5 Å 可能太窄
- **六维诊断分：** 因果 11/选择性 14/可转译 14/原创 9/可证伪 7/证据 7 = **62**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** FA7 深腔是 HSA 真实结构 → functional_biomimicry

## A39 — OAT4 尿酸/有机酸竞争转译为抗尿酸盐 PFAS 选择

- **原型：** PROTO_PFOA_004（OAT4，机制级）
- **转译原则：** OAT4 天然底物是尿酸，PFAS 是"劫持"底物 → 材料设计对 PFAS 优先于尿酸（利用全氟链疏水增量）
- **材料概念：** 脲基功能化碳（捕获头基）+ 氟碳修饰微孔（全氟链特异疏水），尿酸（无氟链）不进入氟碳微孔
- **合成概要：** 活性炭 + 脲基硅烷接枝 + 气相氟碳硅烷微孔修饰
- **致命风险：** 含氟修饰环境风险；尿酸在二级出水中浓度远低于 PFAS（不是主要竞争物）
- **六维诊断分：** 因果 10/选择性 14/可转译 13/原创 10/可证伪 7/证据 7 = **61**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 底物竞争是 OAT4 真实药理学 → functional_biomimicry

## A40 — SsuA 缺硫诱导表达转译为条件性激活

- **原型：** PROTO_PFOA_005（SsuA，结构级）
- **转译原则：** SsuA 仅在缺硫条件下表达（CysB 调控）→ 材料"条件性激活"：正常状态惰性，特定条件激活捕获
- **材料概念：** 光活化吸附剂：偶氮苯-脲基 POP，UV 照射后偶氮苯 trans→cis 改变孔口几何，激活 PFAS 捕获
- **合成概要：** 偶氮苯二胺 + 醛缩合 COF
- **致命风险：** 光活化不是 PFAS 诱导（非目标响应）；偶氮苯 COF 水稳定性差；先例有
- **六维诊断分：** 因果 8/选择性 11/可转译 12/原创 11/可证伪 6/证据 6 = **54**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 条件表达是真实调控，但光活化不是 PFAS 特异 → mechanism_informed（弱）

## A41 — TauA 底物通道蛋白 TolC 外排转译为单向阀

- **原型：** PROTO_PFOA_006（TauA，机制级）
- **转译原则：** 细菌外排泵 TolC 形成单向通道（底物进入后不可逆排出）→ 材料设"单向阀"孔口（PFAS 进入后锁定）
- **材料概念：** 棘轮型孔口：入口宽（PFAS 进入）→ 中段窄（全氟链通过但不可回退）→ 深腔锁定
- **合成概要：** 漏斗形介孔（大孔→微孔梯度），或 DNA 纳米棘轮（概念级）
- **致命风险：** 热力学可逆性（平衡下无单向阀）；棘轮需要能量输入；概念不可实现
- **六维诊断分：** 因果 7/选择性 13/可转译 6/原创 13/可证伪 4/证据 5 = **48**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-embodiment_rejected / SR-revise / ER-lead_only
- **仿生真实性快检：** 单向转运是外排泵真实特征，但热力学禁止被动单向阀 → 转译不成立

## A42 — 氟核糖开关 CrcB 氟外排泵转译为氟选择性膜

- **原型：** PROTO_PFOA_007（氟核糖开关，机制级）
- **转译原则：** CrcB/EriC 是氟离子特异外排通道（CLC 家族）→ 氟选择性透过膜（PFAS 截留，F⁻ 透过）
- **材料概念：** 纳滤膜表面修饰氟选择性通道（仿生 CLC 孔道几何），PFAS 被截留而无机氟透过
- **合成概要：** 聚酰胺纳滤膜 + 表面接枝含氟选择性通道分子
- **致命风险：** 膜过程超出项目范围；PFAS 在二级出水中不是以 F⁻ 形式存在
- **六维诊断分：** 因果 6/选择性 10/可转译 8/原创 12/可证伪 5/证据 6 = **47**
- **谱系状态：** SP-conditional / BP-conditional / TR-conditional / ME-embodiment_rejected / SR-revise / ER-out_of_scope
- **仿生真实性快检：** CrcB 是真实氟通道，但 PFAS≠F⁻ → 转译不成立

## A43 — EPS 蛋白-多糖协同转译为双组分复合珠

- **原型：** PROTO_PFOA_008（EPS，现象级）
- **转译原则：** EPS 中蛋白（疏水结合）与多糖（亲水屏障）协同 → 双组分复合：蛋白核（BSA 交联）+ 多糖壳（壳聚糖/海藻酸钠）
- **材料概念：** BSA-戊二醛核（PFAS 疏水结合）+ 壳聚糖-TPP 壳（DOM 排斥 + 机械保护）
- **合成概要：** BSA 乳化交联核 → 壳聚糖/TPP 离子凝胶包壳
- **致命风险：** 蛋白核超出项目范围（需潘尧开放）；壳层传质阻力；BSA 无 PFAS 选择性
- **六维诊断分：** 因果 9/选择性 8/可转译 12/原创 7/可证伪 6/证据 7 = **49**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-embodiment_rejected（蛋白）/ SR-bench_ready / ER-out_of_scope
- **仿生真实性快检：** 蛋白-多糖协同是 EPS 真实组织 → functional_biomimicry（但蛋白超出范围）

## A44 — SP-A 磷脂管状髓磷脂转译为层状介孔

- **原型：** PROTO_PFOA_009（SP-A，类比级）
- **转译原则：** SP-A 诱导磷脂形成管状髓磷脂（tubular myelin，层状-管状相变）→ 层状介孔材料（层间捕获 PFAS）
- **材料概念：** 层状双氢氧化物（LDH）或层状硅酸盐，层间疏水修饰（CTAB/全氟硅烷），PFAS 插入层间
- **合成概要：** Mg/Al-LDH 共沉淀 + CTAB 层间交换
- **致命风险：** LDH 层间 PFAS 交换先例多（2019-2026）；CTAB 引入阳离子→硫酸盐陷阱
- **六维诊断分：** 因果 8/选择性 10/可转译 15/原创 5/可证伪 7/证据 7 = **52**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** 管状髓磷脂是真实结构，但 LDH 层间交换是普通化学 → rational_chemical

## A45 — NTCP 胆汁酸肠肝循环转译为闭环再生床

- **原型：** PROTO_PFOA_010（NTCP/ASBT，机制级）
- **转译原则：** 胆汁酸在回肠（ASBT）吸收→门静脉→肝脏（NTCP）再摄取→胆汁分泌→回肠（闭环）→ 材料设计闭环再生
- **材料概念：** 双床闭环：吸附床（捕获 PFAS）→ 再生液循环 → 浓缩床（小体积高浓 PFAS）→ 再生液回用
- **合成概要：** 吸附床：脲基 GAC；浓缩床：强碱 AER（小体积）；再生液：50% MeOH
- **致命风险：** 本质是工艺设计非材料创新；AER 浓缩床无仿生成分
- **六维诊断分：** 因果 8/选择性 9/可转译 15/原创 5/可证伪 7/证据 7 = **51**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** 肠肝循环是真实生理，但工艺设计不是材料仿生 → rational_chemical

## A46 — 跨原型：FABP4 腔 + 氟核糖开关 F 识别双锁

- **原型：** PROTO_001 + 007
- **转译原则：** FABP4 疏水腔锁定全氟链 + 氟核糖开关 F⁻ 配位几何锁定 C-F 键 → 双锁（链+氟）
- **材料概念：** 深腔芳烃笼（链锁定）+ 腔壁碘/硒卤键供体（C-F σ-空穴锁定），双机制协同
- **合成概要：** 碘代 resorcinarene 笼合成（多步）
- **致命风险：** 水相卤键 <2 kJ/mol；碘代笼合成极难；双锁是否真正交待验证
- **六维诊断分：** 因果 12/选择性 17/可转译 9/原创 14/可证伪 7/证据 6 = **65**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 两原型各有真实证据，双锁是设计创新 → functional_biomimicry（高风险高创新）

## A47 — 跨原型：OAT4 链长阈值 + EPS 屏障双层

- **原型：** PROTO_004 + 008
- **转译原则：** 外层 EPS 屏障排斥 DOM + 内层 OAT4 链长阈值选择性捕获 ≥C6 PFAS
- **材料概念：** 核壳珠：壳为 PHEMA 水化屏障（DOM 排斥），核为 C6 深度盲腔 POP（链长阈值）
- **合成概要：** 悬浮聚合 St/DVB 核（C6 烷基修饰盲腔）+ HEMA/EGDMA 壳
- **致命风险：** 核壳界面传质；C6 盲腔精度；壳层非特异
- **六维诊断分：** 因果 12/选择性 17/可转译 14/原创 11/可证伪 7/证据 7 = **68**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 两原型各有真实功能，双层组织是设计创新 → functional_biomimicry

## A48 — 跨原型：SsuA 夹口 + SP-A 界面定位

- **原型：** PROTO_005 + 009
- **转译原则：** SsuA 头基夹口（水相识别）+ SP-A 界面定位（在气-液或液-固界面富集）→ 材料在固-液界面富集 PFAS
- **材料概念：** 超疏水-亲水图案化表面：亲水区（脲基）捕获 PFAS 头基，超疏水区排斥水相→PFAS 在界面富集
- **合成概要：** 硅片/GAC 表面光刻或微接触印刷：亲水脲基区 + 超疏水氟碳区（或纯烃区）
- **致命风险：** 图案化表面在流动体系中不可控；超疏水区含氟有环境风险；规模化不可能
- **六维诊断分：** 因果 9/选择性 13/可转译 10/原创 12/可证伪 6/证据 6 = **56**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 界面定位是 SP-A 真实功能 → mechanism_informed

## A49 — 跨原型：TauA 脱溶剂化 + FABP4 自适应多模式

- **原型：** PROTO_006 + 001
- **转译原则：** 孔口脱溶剂化门（TauA，排斥硫酸根）+ 腔内自适应多模式结合（FABP4，容纳不同链长）
- **材料概念：** 超疏水微孔入口（脱溶剂化）→ 腔内柔性多芳烃壁（自适应不同链长 PFAS）
- **合成概要：** 纯芳烃 POP（本征超疏水微孔 ~1.2 nm）→ 腔内多萘基柔性侧链（自适应）
- **致命风险：** 超疏水孔 ng/L 水相不润湿→PFAS 也不进入；柔性壁无预组织
- **六维诊断分：** 因果 12/选择性 16/可转译 12/原创 12/可证伪 7/证据 7 = **66**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 两原型各有真实机制 → functional_biomimicry

## A50 — 跨原型：全十原型收敛设计

- **原型：** PROTO_001-010 全部
- **转译原则：** 十原型功能收敛：SsuA 夹口（头基）+ TauA 脱溶剂化（门控）+ OAT4 链长阈值（深度）+ FABP4 自适应（腔）+ HSA 多亚腔（分级）+ NTCP 双特征（协同）+ EPS 屏障（抗污）+ SP-A 界面（富集）+ 氟核糖开关（氟识别）+ ASBT 梯度（再生）
- **材料概念：** 理想化多级材料：外壳 PHEMA 屏障 → 超疏水微孔门 → 脲基夹口 → C6 深度盲腔 → 萘壁自适应 → 卤键氟识别 → pH 梯度再生
- **合成概要：** 不可合成（概念级思想实验）
- **致命风险：** 完全不可实现；十机制叠加是否真正交无法验证；思想实验非设计方案
- **六维诊断分：** 因果 8/选择性 20/可转译 3/原创 15/可证伪 3/证据 5 = **54**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-embodiment_rejected（不可合成）/ SR-route_rejected / ER-lead_only
- **仿生真实性快检：** 十原型各有真实证据，但收敛设计不可实现 → 思想实验（非可执行方案）

---

## PFOA 50 方案快速排序（L1 诊断分降序）

| 排名 | ID | 分数 | 核心机制 | 原型 |
|---|---|---|---|---|
| 1 | A09 | 77 | OAT4 双正交门（squaramide+C6 窗口） | PROTO_004 |
| 2 | A25 | 77 | 三机制叠加（SsuA+TauA+OAT4） | 多原型 |
| 3 | A08 | 74 | OAT4 链长阈值盲腔 | PROTO_004 |
| 4 | A01 | 73 | FABP4 疏水腔 PMO | PROTO_001 |
| 5 | A13 | 70 | TauA 脱溶剂化门控超疏水孔 | PROTO_006 |
| 6 | A11 | 69 | SsuA 中性夹口 PMO | PROTO_005 |
| 7 | A02 | 68 | FABP4 三模式自适应笼 | PROTO_001 |
| 8 | A47 | 68 | OAT4+EPS 双层 | 跨原型 |
| 9 | A03 | 66 | FABP4 门控 COF | PROTO_001 |
| 10 | A24 | 65 | NTCP 全氟链螺旋互补 | PROTO_010 |
| 11 | A22 | 65 | NTCP 双特征读取 | PROTO_010 |
| 12 | A46 | 65 | FABP4+氟核糖开关双锁 | 跨原型 |
| 13 | A49 | 66 | TauA+FABP4 脱溶剂化+自适应 | 跨原型 |
| 14 | A07 | 64 | HSA Trp214 π-酸腔 | PROTO_003 |
| 15 | A31 | 64 | TauA 分子钳 | PROTO_006 |
| 16 | A06 | 63 | HSA 多亚腔 POP | PROTO_003 |
| 17 | A38 | 62 | HSA FA7 深腔 calixarene | PROTO_003 |
| 18 | A37 | 61 | hL-FABP 焓驱动低温 | PROTO_002 |
| 19 | A39 | 61 | OAT4 抗尿酸盐选择 | PROTO_004 |
| 20 | A12 | 60 | SsuA 保守水桥 | PROTO_005 |
| 21-50 | ... | 45-60 | （见各卡片） | ... |
