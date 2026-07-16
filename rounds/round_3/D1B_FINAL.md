# D1-B 终稿：定向固定真实 PBP 的痕量磷酸盐抛光备选

## 1. 主张边界与冻结路线

D1-B 用真实 *E. coli* phosphate-binding protein（PBP）保留原生静态口袋和结合后闭合动态，避免重新构造蛋白口袋。P1/P2 支持 PBP 的 apo/bound 结构、完全包埋和多点氢键；P3 支持 A197C-MDCC 的先结合后构象变化动力学；P4 只证明 PiBP/PBP 可产生 FRET/电位响应并可固定化。P4 是传感先例，不能证明本材料的位点密度、吸附床容量、二级出水选择性、再生或寿命。由于每个大分子蛋白最多提供一个磷酸盐位点，D1-B 仅定位为低 `Cin` 条件下的痕量抛光备选，不主张高容量或主体除磷。

唯一主蛋白定义为 `pelB | PBP-321(T141D/A197C) | LPETG | HHHHHH`，各模块之间不增加未声明 linker。`PBP-321` 指 1OIB 与 1IXG 共用、逐残基完全一致的 321 aa 成熟 *E. coli* PBP T141D 链；主变体在该成熟链编号 197 将 Ala 改为 Cys，D56N 对照再在编号 56 将 Asp 改为 Asn。信号肽切除后的可溶前体必须为 `PBP-321(T141D/A197C)-LPETGHHHHHH`；sortase 反应后固定结点必须为 `PBP-321(T141D/A197C)-LPET-GGGK(支架锚定)-NH2`。主吸附亚群 Cys197 用 N-ethylmaleimide（NEM）封端，2 mol% 同构建体用 MDCC 标记。固定化唯一主路为 C 端 sortase A 连接，不得暗换序列、连接区或固定方式。

主供应路线冻结为实验室重组表达和纯化。序列身份以受控附件 `deliverables/attachments/PBP_CONSTRUCTS.fasta` 和来源记录 `research/evidence/PBP_CONSTRUCT_PROVENANCE.md` 为唯一文本来源，不在本稿另行手抄残基串。已核验冻结值为：1OIB/1IXG 共用321 aa成熟T141D链 `SHA-256=78558e51049eec070b0f3249ffa8617b37a45b912436af1274ed746b57931a96`；A197C主成熟变体 `SHA-256=5f90614377b9f30b131c0df1c67cbef7daf8af2be860c1fa5f78fc327a533d25`；D56N/A197C对照成熟变体 `SHA-256=f77e94a790526b535c8e766b143b25377b46966bb415dc05e7336f37e96964b1`；主变体加 `LPETGHHHHHH` 的332 aa可溶前体 `SHA-256=d249767e91791d500c87a84e9e95274f74b675665cf4df8c4aae747fe79312ff`。克隆启动前必须通过 `SEQ-ID-01`：两附件存在，FASTA长度与上述值一致，重新计算的四个SHA全部匹配，并记录理论质量和人工复核签名。密码子优化DNA只可由已验收蛋白序列生成，不在本稿猜写DNA。sortase固定产物另建质量记录并排除离去的 `G-His6`。任一附件、长度或SHA不符时禁止DNA订单、克隆、成本核算和蛋白实验。定制外包仅可供应相同序列；外购不同物种PBP、未知构建体或普通“phosphate-binding protein”不能替换。

## 2. 材料组成与空间结构

- **蛋白：** 98 mol% NEM-PBP(A197C)-LPETG 与 2 mol% MDCC-PBP(A197C)-LPETG。报告比例按摩尔数配制，不按荧光强度回算。
- **支架：** 90–150 μm 交联氨基化大孔琼脂糖微球。该支架用于低压柱和水相蛋白固定；不得把传感膜数据换算为其床性能。
- **定向手柄：** 支架胺先接 DBCO，随后点击 `H-GGGK(N3)-NH2`，由 Lys 侧链叠氮固定，使 N 端 GGG 暴露给 sortase。
- **抗污背景：** 剩余表面胺用 2 kDa mPEG-NHS 封端；蛋白、GGG 与 OEG 密度以实测值为准。
- **储存：** 成品短期置于 20 mM HEPES、150 mM NaCl、0.02% sodium azide、pH 7.4，4 °C，避光，不冻结。进入吸附或微生物实验前以无菌 HEPES 洗 20 个床体积，不得把含叠氮化钠材料接触目标水。

### 2.1 生物特征—材料实现—功能—测量—对照

| 对应 | 生物特征与来源边界 | 材料实现 | 预期功能 | 直接测量 | 因果对照 |
|---|---|---|---|---|---|
| 静态硬对应 | P1/P2 支持真实 PBP 完全包埋磷酸盐、多点氢键和受限水合；具体氢键数只属于对应蛋白 | 不拆分口袋，直接固定完整 PBP；C 端单点连接只统一固定端点，裂隙可达性仍须实测 | 在高背景阴离子中保留口袋依赖占据，而非支架离子交换 | 饱和化学计量、离子色谱、竞争分配、D56N 删位与真实水突破 | B-D56N、B-INACT、B-BLANK、RESIN-1 |
| 动态硬对应 | P3 直接支持 A197C-MDCC 的先结合后构象变化动力学；P4 支持蛋白响应可在固定体系读取 | 2 mol% MDCC-PBP 与 98 mol%同构建体共固定，主床仍由无荧光蛋白承担 | 证明固定后蛋白仍可在占据时产生可逆构象响应 | 占据量与时间分辨 MDCC 同步；解吸后基线复位 | B-NOREP、B-INACT、B-D56N、B-BLANK 和无磷酸盐离子强度空白 |
| 单点共价固定工艺 | 生物来源不证明 C 端固定优于随机固定，故不主张取向增量 | LPETG–GGG sortase 单点连接，OEG 保持水相可达 | 获得身份明确、可测泄漏的共价蛋白床 | 共价结点、单位固定蛋白的 `factive`、泄漏和床性能 | B-BLANK；B-RAND 仅作可选探索，不参与硬对应或pass |
| 可逆释放 | 允许来源没有可移植的 PBP 再生条件 | 冻结乙酸/NaCl 温和洗脱并复位 | 释放磷且保留蛋白结构和下一轮选择性 | P 质量平衡、MDCC 基线、活性、特征肽泄漏 | 只再生不捕获老化组、B-INACT 和 RESIN-1 |

只有静态占据、动态报告、共价身份和工程床性能分别通过删位、失活、无报告体、空白和强树脂对照，D1-B 才能使用“机制保持型蛋白—材料”表述。sortase结点或荧光响应单独通过均不等于吸附剂成功。

## 3. 理论容量与工程上限

`SEQ-ID-01` 通过后，分别计算可溶前体和 sortase 固定产物的精确质量。容量换算只使用固定后保留的 PBP 蛋白部分质量：`M_NEM,fixed` 与 `M_MDCC,fixed` 均包含 `PBP-321-LPET` 及对应 Cys197 加合物，排除离去的 `G-His6`；固定 PBP 摩尔数以同位素稀释特征肽 LC-MS 为主，不把支架 GGGK/OEG 质量算入蛋白负载。混合平均质量为

`M_mix,fixed = 0.98 M_NEM,fixed + 0.02 M_MDCC,fixed`。

按每个 PBP 只有一个 1:1 磷酸盐位点，蛋白自身上限为：

- `qth,protein(P) = 30.974 / M_mix,fixed` mg P/g fixed-PBP；
- `qth,protein(PO4) = 94.971 / M_mix,fixed` mg PO4/g fixed-PBP。

若实测负载为 `L` mg fixed-PBP/g dry composite 或 `Lbed` mg fixed-PBP/mL-bed，活性位点比例为 `factive=nPi,sat/nPBP`，则：

- `qth,composite(P)=L×30.974/(1000 M_mix,fixed)`，`qactive,composite=factive×qth,composite`；
- `qth,bed(P)=Lbed×30.974/(1000 M_mix,fixed)`，`qactive,bed=factive×qth,bed`；
- 柱前动态上限固定为 `qdynamic,bed=Umin×qactive,bed`，`BVmax,dynamic=1000×qdynamic,bed/Cin`。`BVmax,active` 只作中间量，不能用于柱前放行。

本路线的设计点冻结为：`Cin,design=0.10 mg P/L=0.10 μg P/mL`、`BVreq=50`、`factive,min=0.50`、`Umin=0.30`、`Vrxn=2.0 mL/mL-bed`，以及 `Costmax=5000 RMB/1.0 mL 论文验证床`。成本口径包括该床实际消耗的 PBP 表达/外包、sortase、琼脂糖、DBCO/OEG/GGG、NEM/MDCC 和一次性纯化耗材，按发票与同批分摊记录；不含仪器折旧和人员工时，禁止用未发生的目录价替代。

对 1.0 mL 床，50 BV 在设计浓度下含 `5.000 μg P`。冻结反算结果为：

- 理想固定量 `nfixed,ideal=5.000/30.974=0.16143 μmol PBP/mL-bed`，仅对应 `factive=U=1`；
- 放行最低固定量 `nfixed,min=5.000/(30.974×0.50×0.30)=1.0762 μmol PBP/mL-bed`；
- `Lbed,min=1.0762×M_mix,fixed` mg fixed-PBP/mL-bed；
- 此时 `qth,bed=0.033333 mg P/mL-bed`、`qactive,bed=0.016667 mg P/mL-bed`、`qdynamic,bed=0.30×0.016667=0.005000 mg P/mL-bed`，因此 `BVmax,dynamic=1000×0.005000/0.10=50.00`；
- 100 μL sortase 预试得到共价固定收率 `Yfix` 后，`nfeed,min=1.0762/Yfix μmol/mL-bed`，`Cfeed,min=0.5381/Yfix mM`。

主柱资格固定使用 `Cin,design=0.10 mg P/L` 和 `BVreq=50`。本地三批同一节点水样仍须报告；若任一批 `Cin` 上侧置信限高于0.10 mg P/L，须用该更高值重算并仍满足50 BV，不得稀释水样获得资格。放大前实测GGG支架最大共价负载 `Lbed,max`、PBP在sortase缓冲液4 h无聚集的 `Csol,max`、`Yfix` 和单床实际成本。分别报告 `BVmax,th=1000qth,bed/Cin`、`BVmax,active=1000qactive,bed/Cin` 和唯一柱前判据 `BVmax,dynamic=1000×Umin×qactive,bed/Cin`。若 `Lbed,min>Lbed,max`、`Cfeed,min>0.8Csol,max`、实际成本超过5000 RMB，或 `BVmax,dynamic<50`，D1-B在柱试验前淘汰。

## 4. 台式 SOP

### 4.1 重组表达与纯化：主路

1. 序列验收通过后，将主构建体和删位对照 `PBP(T141D/D56N/A197C)-LPETG-His6` 分别克隆入 pET-22b(+)；pelB 引导周质表达。Sanger 确认成熟链全长、T141D/A197C、D56N（对照）、pelB 切割边界和 C 端 `LPETG-His6`；纯化后以 N 端测序或完整质量确认信号肽正确去除。
2. 单克隆接入 50 mL LB、100 μg/mL ampicillin，37 °C、200 rpm、12–16 h。按 1% v/v 接入 1 L Terrific Broth、100 μg/mL ampicillin，37 °C 培养至 OD600 0.6–0.8。
3. 加 IPTG 至 0.20 mM，18 °C、180 rpm 诱导 16 h。4 °C、5000×g 离心 15 min。所有培养与废物按重组 *E. coli* BSL-1 流程灭活。
4. 周质渗透休克：菌体重悬于 20% sucrose、30 mM Tris、1 mM EDTA、pH 8.0，4 °C 轻混 10 min；离心后以冰冷 5 mM MgSO4 重悬 10 min，再离心收上清。全程禁用磷酸盐缓冲液。
5. Ni-NTA 平衡液为 20 mM HEPES、300 mM NaCl、10 mM imidazole、pH 7.5。4 °C 上样，以 20 个柱体积含 30 mM imidazole 的同缓冲液洗涤，250 mM imidazole 洗脱。
6. 以分子筛在 20 mM HEPES、150 mM NaCl、pH 7.4 中分离单体；收集主峰。SDS-PAGE 纯度须不低于 95%，SEC 单体峰不低于 90%，intact LC-MS 与已验收序列质量相符。普通缓冲空白只证明游离磷背景，不能证明蛋白处于 apo。
7. 每批取定量蛋白经 10 kDa 超滤，离子色谱测滤液游离 Pi；另取同量蛋白以 6 M guanidine-HCl、70 °C 处理 10 min，超滤/换液后测从蛋白释放的总结合 Pi。定义 `fapo=1−nPi,bound/nPBP`，要求 `fapo≥0.95`。对通过批次再做磷酸盐饱和滴定，扣除预占位后 `nPi,sat/nPBP` 必须为 0.90–1.10。自由 Pi、总结合 Pi、apo 分数和再结合化学计量同时进入后续 `factive` 与再生质量平衡。
8. 纯化蛋白 4 °C 最长保存 48 h；需延后时加无磷酸盐 10% glycerol 分装，−80 °C 保存，仅允许一次冻融。冻融后重新测 apo 分数、SEC 和结合化学计量。外包备份必须按同一条目验收。

### 4.2 Cys197 封端与 2 mol% 报告亚群

1. 主蛋白以 0.5 mM TCEP、4 °C 处理 15 min，立即用脱盐柱换入 20 mM HEPES、100 mM NaCl、pH 7.0。
2. 98% 主亚群加 1.10 mol equiv NEM，4 °C、避光反应 60 min；2% 报告亚群加 1.10 mol equiv MDCC，4 °C、避光反应 2 h。过量试剂分别用脱盐柱去除。
3. intact LC-MS 确认单标记；UV/Vis 确认 MDCC 标记度。NEM 与 MDCC 亚群分别测 `Kd`、`kon/koff`、再结合 1:1 化学计量和 apo 分数；各项相对差异须不超过 20%，且活性均不低于未修饰双变体的 80%。超限时报告亚群不能代表主床，动态路线停止。
4. 按蛋白摩尔数将 NEM 与 MDCC 亚群混为 98:2，并同时制备 100% NEM、100% MDCC 微量固定化批次。固定后分别由 MDCC 吸收/荧光质量平衡和同位素稀释特征肽 LC-MS 计算两亚群固定收率及混合床实际比例；固定后 MDCC 摩尔分数必须为 2.0%±0.5%，否则报废。另制 100% NEM 的 reporter-free 材料，用于证明染料不贡献吸附、DOM 或再生。

### 4.3 GGG/OEG 多孔支架

1. 取 1.0 mL packed aminated agarose，依次以 10 mL water、10 mL 50 mM sodium bicarbonate pH 8.3 洗涤。用 TNBS 或等价方法测表面胺 `nNH2`。
2. 在 2.0 mL bicarbonate buffer、10% v/v DMSO 中，加入相对于 `nNH2` 的 0.099 equiv non-cleavable DBCO-NHS、0.001 equiv DBCO-PEG-disulfide-NHS 和 0.80 equiv 2 kDa mPEG-NHS，22 °C 端对端混合 2 h。总 DBCO 仍为 0.10 equiv，其中 1 mol% 为分析用可裂解手柄。洗去游离 NHS 酯后，以 0.10 M acetic anhydride、50 mM bicarbonate、10% v/v DMSO、pH 8.3 处理 30 min，乙酰化剩余支架胺。
3. 依次以 20 mL bicarbonate buffer、20 mL water、20 mL HEPES buffer 洗涤。加入相对于实测 DBCO 的 2.0 equiv `H-GGGK(N3)-NH2`，20 mM HEPES、150 mM NaCl、pH 7.4，22 °C 混合 4 h。
4. 以 20 个床体积 HEPES 洗涤。通过 DBCO 消耗、肽氮/元素分析及 OEG 质量增量计算 GGG 和 OEG 密度。无蛋白载体使用同批支架。

### 4.4 C 端 sortase 定向固定

1. sortase 身份门冻结为 `SORTASE-ID-01`：*S. aureus* sortase A `Δ59-His6`。现有受控输入未提供可核验的酶序列或产品身份，故不编造货号。启动前必须记录以下二选一来源：在制时保存完整 DNA/蛋白序列、质粒、宿主、纯化 SOP 与批号；外购时保存制造商、产品名、货号、批号、COA 和该批完整蛋白序列。两种来源均须满足 SDS-PAGE 纯度≥90%、intact LC-MS 与理论质量相差≤0.02%、4 °C 储存液/期限明确，并以同一 LPETG/GGG 底物测转肽和水解。定义 1 U 为 25 °C、pH 7.5 下每分钟生成 1 nmol 转肽产物，水解不计活性；转肽/水解摩尔比须≥10。`SORTASE-ID-01` 任一字段缺失则禁止固定化。
2. 先以 100 μL bed 做收率预试，取得 `Yfix`、`Lbed,max` 和 `Csol,max`。正式 1.0 mL bed 的反应体积固定为 2.0 mL，PBP 浓度使用第 3 节反算的 `Cfeed,min`，不得固定为 100 μM；sortase 投料为 PBP 的 5 mol%，且总活性不少于 5 U/μmol PBP。反应液为 50 mM Tris、150 mM NaCl、10 mM CaCl2、pH 7.5，25 °C、空气气氛、避光端对端混合 4 h。
3. 收集全部上清和洗液，分别定量未反应 PBP、游离 `G-His6`、水解 `PBP-LPET` 和 sortase。载体依次用 10 BV 反应缓冲、10 BV 0.50 M NaCl/HEPES、10 BV 20 mM imidazole/HEPES 洗涤；再与 Ni-NTA magnetic beads 轻混 30 min 清除 His6-sortase，移除磁珠后用 20 BV HEPES 洗涤。成品中 sortase 特征肽必须低于方法定量限。
4. 从每批取 2% 支架，以 10 mM TCEP、室温 30 min 裂解分析手柄，靶向 LC-MS/MS 必须检出跨结点 `PBP-...-LPET-GGGK...` 肽；同时量化水解 `PBP-LPET`。另取等量支架经 8 M urea、1 M NaCl、室温 1 h 变性/竞争洗涤，共价 PBP 保留须不低于 90%。结点不可检出、水解/非特异吸附占主导或酶去除失败，整批报废。
5. 以氨基酸分析和上清/洗液质量平衡求 `L/Lbed`，以饱和磷酸盐结合量求 `factive`，并用实测 `Lbed/factive` 与冻结 `Umin=0.30` 重算 `qdynamic,bed` 和 `BVmax,dynamic`。材料置储存液4 °C、避光；七天后仍未使用则重新测 `factive`、亚群比例、MDCC基线、sortase残留和泄漏。

### 4.5 B-RAND 可选探索性工艺参照

1. B-RAND 不承担取向因果、备选pass或任何失败合同，只在资源允许时作为探索性工艺参照。若实施，随机标记试剂记为 `RAND-REAGENT-ID-01`：单一结构的 azido-PEG4-NHS，保存结构式、分子式、纯度、来源/批号及完整质量；身份字段不全则跳过B-RAND，不影响核心实验启动。
2. 使用与 B-ORI 同批、完成 NEM/MDCC 98:2 分账的 PBP，浓度固定为 50 μM，缓冲液为 20 mM HEPES、150 mM NaCl、pH 7.5。azido-PEG4-NHS 以 10 mM 无水 DMSO 储液加入 0.50 mol equiv，终 DMSO≤1% v/v，4 °C 反应30 min；加 Tris-HCl 至20 mM、4 °C 10 min 终止，以 SEC 换回 HEPES 缓冲液。
3. intact LC-MS 解卷积分为0、1、2和≥3标记，并记录可溶PBP的 `fapo`、1:1化学计量、`Kd` 和单体比例。所有结果仅作描述，不设置可影响D1-B资格的放行窗口，也不得从平均标记数推断固定后单/多点比例。
4. B-RAND 使用与 B-ORI 同批、同 DBCO/OEG 投料的支架，但不进行 GGG 点击。按预试固定收率调节随机标记 PBP 投料，在20 mM HEPES、150 mM NaCl、pH7.4、22 °C 端对端混合4 h；收集上清后依次洗10 BV HEPES、10 BV 0.50 M NaCl/HEPES、20 BV HEPES。剩余 DBCO 用相对于未反应 DBCO 2.0 equiv 的 `acetyl-GGGK(N3)-NH2` 在同缓冲液22 °C反应4 h封闭，再洗20 BV。

### 4.6 批次放行与记录

每批建立唯一编号并保存质粒测序、培养批次、纯化色谱、intact LC-MS、SEC、MDCC/NEM 标记度、支架胺/DBCO/GGG/OEG 密度、sortase 反应质量平衡、蛋白负载、`factive`、磷酸盐流程空白和七日稳定性。以下任一项不得用后续吸附表现补救：序列不符；可溶蛋白纯度或单体比例不达标；主亚群/报告亚群活性低于门槛；磷酸盐背景高于方法定量限；sortase 后蛋白负载无法闭合；初始泄漏超过固定量0.1%。批次失败后只能重新制备，禁止选择性删除异常数据或把不同蛋白批次拼成同一重复。B-RAND 不进入核心批次放行。

## 5. 对照与强基准矩阵

| 编号 | 材料 | 切断的因果链 |
|---|---|---|
| B-ORI | 定向固定活性 PBP，98:2 报告混合 | 完整 D1-B |
| B-NOREP | 定向固定 100% NEM-PBP | 检验 MDCC 是否改变吸附、DOM 或再生 |
| B-D56N | 定向固定 T141D/D56N/A197C PBP | 仅在 SEC、CD、DSF、apo 分数、表面可达性和固定收率与主蛋白可比时，作为 Asp56 口袋扰动对照；不能按活性位点配平 |
| B-INACT | B-ORI 固定后在 HEPES 中 70 °C 处理 30 min | 只用于非特异吸附、DOM、泄漏和柱背景，不用于证明口袋、动态或定向固定 |
| B-RAND | 按第4.5节可选制备的随机赖氨酸固定样品 | 仅作探索性工艺描述，不承担取向因果、核心对照、备选pass或失败合同 |
| B-BLANK | GGG/OEG 支架，不加 PBP；经历 sortase 和全部洗涤 | 支架、sortase 残留和非特异截留 |
| SOL-PBP | 同批可溶 PBP | 固定前机制与活性参照，不作为床容量基准 |
| RESIN-1 | 经 `RESIN-ID-01` 验收的唯一强碱性Ⅰ型季铵阴离子交换树脂，Cl⁻型 | 唯一非仿生工程容量、突破和再生强基准 |

主工程比较以B-ORI、B-BLANK和RESIN-1为核心。B-D56N按折叠蛋白量和残余位点分账，不要求 `factive` 与主蛋白配平；若D56N的SEC/CD/DSF或表面可达性不可比，删除“口袋删位”归因。B-INACT只给背景上限，B-NOREP支撑报告亚群因果。B-RAND不进入任何核心结论。

### 5.1 唯一非仿生树脂 RESIN-1 的身份门与 SOP

现有受控输入没有可核实的商业产品，故不编造货号。`RESIN-ID-01` 只接受一个实际批号：苯乙烯-DVB 基强碱性Ⅰ型季铵阴离子交换树脂、Cl⁻型。实验前必须在本节受控记录填写制造商、产品名、货号、批号、交换基型、COA总交换容量、含水率、粒径范围和储存条件；独立测得的湿床Cl⁻交换容量须在COA换算值±15%内。字段不全、批号更换或实测不符时，全部 B-ORI/RESIN-1 比较不得启动。

1. 取5.0 mL湿树脂，不研磨、不筛分；以去离子水10 BV洗涤，再以1.0 M NaCl、0.5 BV/min流过10 BV，静置30 min，继续流过10 BV，将树脂统一为Cl⁻型。
2. 以去离子水20 BV、随后20 mM HEPES/150 mM NaCl/pH7.4 20 BV平衡，直至连续3 BV电导相差≤2%、pH为7.4±0.1且浊度不高于缓冲空白+3SD。
3. 另取1.0 mL平衡树脂，以1.0 M NaNO3、0.5 BV/min置换20 BV，离子色谱积分全部Cl⁻，计算 `IECwet` mmol Cl⁻/mL-bed；完成后重复步骤1–2复位。`IECwet` 与COA换算值偏差>15%则该批拒收。
4. B-ORI 与 RESIN-1 均装填1.0 mL床，使用相同 `Cin=0.10 mg P/L`、竞争水、温度、BV/min、取样时点和三次独立批次。RESIN-1 再生固定为1.0 M NaCl、0.5 BV/min 20 BV，随后HEPES 20 BV复位；树脂采用自身冻结再生条件，不把该条件移植给 PBP。
5. RESIN-1 只使用验收通过的同一产品/批号；不得在看到结果后更换“更强”或“更弱”树脂。若库存不足以完成全部独立批次，整组比较延后而非混批。

## 6. 全实验矩阵与判据

### 6.1 静态口袋、定向与动态保留

在20 mM HEPES、150 mM NaCl、pH7.4、20 °C中分别测试可溶和固定后的100% NEM、100% MDCC与98:2混合体。离子色谱/快速淬灭测占据与结合/解吸动力学，stopped-flow MDCC测构象报告。固定后两亚群的 `Kd`、`kon/koff` 与固定收率相对差异均须≤20%，B-ORI 的 `factive`≥0.50；B-NOREP 与 B-ORI 的床体积占据差异须在±5%内。

动力学模型在解码前冻结。以固定后MDCC报告浓度0.10 μM，在 `0、0.25、0.5、1、2、5、10×Kd` Pi下各做5次技术重复、覆盖3个独立批次。单步模型为 `K1: F(t)=F∞+Aexp(−kt)`；双步模型为 `K2: F(t)=F∞+Afexp(−kf t)+Asexp(−ks t)`，约束 `kf>ks>0`。只有 `AICc(K1)−AICc(K2)≥10`、三个批次均支持慢相，且 `ks([Pi])` 的饱和模型相对线性模型 `ΔAICc≥10`，才保留P3式两步动力学；否则按单步局部环境响应处理。

HDX-MS SOP冻结为：可溶100% NEM、100% MDCC及由1 mol%可裂解手柄释放的固定化分析亚群均调至10 μM；apo与 `10×各自Kd` Pi且实测占位≥90%两态，在20 °C以同组成D2O缓冲液启动交换，时间点固定为10、60、600、3600 s，每点2次技术重复、3个独立批次；0 °C加入终浓度0.8% formic acid淬灭至pH2.5，在线pepsin消化和LC-MS分析。序列门通过后，按1OIB/1IXG映射在解码前登记裂隙/铰链候选肽；总序列覆盖≥80%，每个候选区至少2条重叠肽。

HDX模型固定为 `H0`（肽段、时间、批次效应，不含配体项）与 `H1`（增加配体及配体×时间项）。只有 `AICc(H0)−AICc(H1)≥10`、多重校正 `q≤0.05`、至少2个预登记裂隙/铰链肽在连续2个时间点 `|ΔD|≥0.50 Da`，且NEM、MDCC和固定化释放亚群方向一致，才判为共同保护变化。仅MDCC强度/寿命变化、单一肽或事后挑选肽段不能证明主床动态。

只有实际固定后 98:2 比例合格、NEM/MDCC 动力学等价、占据与慢相同步、HDX-MS 同向、解吸后两种基线复位时，才称主床保留 PBP 动态。B-D56N 仅在折叠可比时支持口袋参与；B-INACT 仅排除背景。任一亚群分账或第二判据失败，删除主床动态硬对应并取消备选资格。

### 6.2 选择性、形态和金属排除

竞争集固定为 `SO4²⁻/HCO3⁻/Cl⁻/NO3⁻/砷酸根`，先逐一竞争，再按本地二级出水实测活度做全混合。覆盖本地 pH 及上下各 0.5 个单位，报告 `H2PO4−/HPO4²−` 分数。同步测 Ca/Mg/Fe/Al、过滤前后 P、粒径/浊度和材料上 P/金属共定位。

机制批次实验冻结为：每管0.100 mL packed material加入10.00 mL溶液，20 mM HEPES、150 mM NaCl、pH7.40±0.05、20.0±0.5 °C，端对端20 rpm混合240 min；材料为B-ORI、B-BLANK、RESIN-1，以及仅在折叠门通过时的B-D56N。Pi固定为0.10 mg P/L（3.228 μM）；`SO4²⁻/HCO3⁻/砷酸根`逐一实验均为Pi摩尔浓度的100倍（322.8 μM），全混合实验同时加入三者各322.8 μM；另以三批本地水实测组成原样验证。取样时间固定为0、5、15、30、60、120、240 min，120–240 min浓度变化>5%则该材料/条件不满足平衡，`α`不得计算。每个条件在每次独立蛋白/固定化批次做3个技术重复，共3个独立批次。

所有浓度先换算为 μmol/mL。对B-ORI/B-D56N，以B-BLANK作配对过程空白；对RESIN-1，以无树脂同容器作配对过程空白。对离子 `i`：`q_i={[(C0_i−Ce_i)_material−(C0_i−Ce_i)_paired-blank]×V}/Vbed`，其中 `V=10.00 mL`、`Vbed=0.100 mL`；`Kd_i=q_i/Ce_i`，单位为mL-solution/mL-bed；`α(Pi/X)=Kd_Pi/Kd_X`。若空白校正后 `q_i≤0` 或 `Ce_i<LOQ`，该 `α` 记为不可估计，不得以无穷大替代。三竞争物的工程增量定义为 `Gα={Π_X[α_B-ORI(Pi/X)/α_RESIN-1(Pi/X)]}^{1/3}`，`X=SO4²⁻、HCO3⁻、砷酸根`。

工程主指标固定为单位床体积的实际混合水10%突破与上述成对选择性；按 `factive` 归一只作机制次指标。`Gα` 点估计须≥1.50且按3个独立批次计算的95% CI下限≥1.25；B-ORI 的 `BV10%,Pi` 同时须达到50。只有相对D56N或失活体显著，而相对RESIN-1/B-BLANK无最小效应时，降级为机制/传感样品。

过滤前后去除差异超过 5%、粒径/浊度超过空白加 3SD 或 P 与金属共沉积时，判为非口袋路径并停机。E016 的家族选择性倍数不作为门槛，也不得用单位活性位点的高亲和掩盖单位床体积负载不足。

### 6.3 DOM、蛋白酶和微生物

DOM 采用0、1×和3×本地TOC，另做过滤后与未过滤同源二级出水。测TOC覆盖、`factive`、MDCC基线、磷酸盐选择性、扩散和蛋白泄漏。3×TOC后活性与选择性须各保留至少70%，B-BLANK的支架背景不得解释B-ORI增量；否则抗污背景无效。

叠氮分析固定为阴离子交换离子色谱，抑制电导为主检测、210 nm UV为保留时间确认；不指定未经核实的商业色谱柱货号，实际柱身份、批号和分离度须写入方法记录。标准曲线固定为0、0.05、0.10、0.25、0.50、1.00、2.00 mg NaN3/L，方法放行要求 `LOQ≤0.10 mg/L`、LOQ点信噪比≥10、6次重复RSD≤20%、HEPES与二级出水中0.10/0.50 mg/L加标回收80%–120%，azide与相邻阴离子分离度≥1.5。未达到任一项则方法不合格，不能以“未检出”放行。

任何真实水/微生物试验前，连续最后3个1-BV洗液、合并末5-BV洗液和进水均须低于该LOQ；“洗20 BV”本身不构成关闭证据。另以确认无azide的同源水分别加0和0.10 mg/L NaN3，24 h后CFU与ATP比值的90% CI均须落在0.90–1.10，证明该LOQ水平无可测抑制；若不满足，须降低LOQ并重新验证，材料不得进入微生物稳定性评价。

蛋白酶压力试验：10 μg/mL proteinase K、25 °C、2 h；随后加 PMSF 至 1 mM、10 min 终止，并以 20 BV HEPES 洗涤。所有材料设置同浓度 PMSF 但不加 proteinase K 的抑制剂对照。分别测 `factive`、N 端/内部/C 端三个特征肽、`LPET-GGGK` 结点肽和完整蛋白 SEC-immunoblot；单一内部肽只证明碎片存在。活性保留低于 80%、完整蛋白信号下降或累计泄漏超过初始固定蛋白 1%即失败。该剂量是加速压力条件，不冒充环境浓度。

微生物试验在确认无 azide 后，以过滤/未过滤二级出水 25 °C 循环 24 和 72 h，并设置无材料水样、B-BLANK、灭活同源水、无菌 B-ORI 和未过滤 B-ORI。逐时点做溶解/颗粒 P 与总 P 质量平衡、CFU/ATP、压降、TOC、生物膜、`factive`、多位点肽和完整蛋白泄漏。微生物摄取/释放对 P 的贡献无法由无材料/灭活水扣除，或 72 h 后活性/选择性低于初始 70%、压降超过 B-BLANK 1.20 倍、出现持续蛋白水解，均否决直接真实水床。72 h 通过只称短期压力通过，不外推运行寿命。

### 6.4 固定床和理论载量核验

只有 `Cin=0.10 mg P/L、BVreq=50、Lbed,max/Csol,max、Costmax=5000 RMB` 和实测 `Yfix` 同时放行，才装填1.0 mL packed bed。20 °C下先以无菌HEPES在0.5 BV/min平衡20 BV，再分别在0.2、0.5、1.0 BV/min测单盐和实际混合水突破；按 `C/C0=0.10` 计算 `qdyn,10%`、传质区和 `U`。每个流速的核心比较为B-ORI、B-BLANK和RESIN-1，实际水再加入折叠可比的B-D56N。B-RAND若制备，只归档探索结果，不参与柱放行。

放行要求：`U≥0.30`，B-ORI达到50 BV和第6.2节相对RESIN-1的最小选择性效应，压降不超过B-BLANK的1.20倍。若 `BVmax,dynamic<50`、选择性只存在于批量低负荷或单位床体积容量不足，直接否决抛光床用途，不改名为高容量材料。

### 6.5 再生、循环、泄漏和储存

再生主路线冻结为 `50 mM sodium acetate、0.50 M NaCl、pH 5.5`，20 °C，以0.5 BV/min流过10 BV，静置30 min，再流过10 BV；随后用20 BV HEPES pH7.4复位。该条件是待证材料变量，不是PBP生理释放条件。

先在 100 μL 床上做一次兼容门禁，并同步运行 B-BLANK、B-NOREP 和只再生不捕获老化组。收集装载、洗涤、酸盐再生和复位的全部分段流出物；P 质量平衡先扣除第 4.1 节实测的预占位 Pi 和支架背景。P 回收须为 90–110%，复位后 `factive`、选择性、MDCC 基线与 HDX-MS 保护方向均保留至少 90%，完整蛋白/多位点肽泄漏低于固定量 0.1%。任一失败即停止，不升级到更强酸碱或有机溶剂。

通过后做五次早期捕获—释放循环，继续保留 B-BLANK、B-NOREP 和只再生组。第五次动态容量、选择性、MDCC 响应和 cycle 1/5 HDX-MS 方向须各保留初始 80%以上；每循环完整蛋白泄漏低于 0.1%，总 P 质量平衡 90–110%，无持续压降上升。容量恢复但结构、选择性或完整蛋白稳定性漂移，仍判无可逆窗口。五次循环不写成长周期稳定。

储存稳定性在 4 °C、避光条件测 1、7、14、28 d；每点测 `factive`、MDCC 基线、SEC/特征肽泄漏和无菌状态。28 d 活性低于初始 80%即不支持库存化。含 sodium azide 的储存液不得进入吸附数据，首批 20 BV 洗液作为危险废液收集。

### 6.6 分析质量控制与统计冻结

至少使用三次独立表达/固定化批次；每批的批量吸附和柱试验均设技术重复。样品编码在积分规则、异常排除和质量平衡完成后再解码。离子色谱每批设置溶剂空白、支架空白、进水加标回收、平行样和中间浓度校准核查；真实水若基质回收不在预注册范围，先修正方法，不解释材料差异。MDCC 同时记录强度、寿命和散射/吸收背景，DOM 自发荧光用 B-BLANK 与 B-NOREP 扣除。蛋白泄漏在缓冲液中用总蛋白法与特征肽 LC-MS 交叉核查，在真实水中以特征肽为主。

所有 go/no-go 指标、重复数、检出限、置信区间和多重比较方法在样品解码前冻结。选择性只在 95% CI 支持且跨独立批次同向时成立；单个最佳批次、单个流速或单一 DOM 水平不能关闭问题。未达到效应量时按失败合同执行，不通过追加重复把边缘结果改为通过。

## 7. 失败合同与 D1-A 切换

D1-A 在可溶受体水相几何、可比锁开体或温和再生任一门禁失败时，启动 D1-B；不要求等待 D1-A 完成固相放大。D1-B 只有同时通过以下四个独立门禁才获得备选资格：

1. 唯一序列/apo 状态、sortase 共价结点和本地 `Cin/BVreq` 反算三项预检通过；B-ORI 的 `factive` 证明真实 PBP 口袋在支架上可用；
2. 实际混合水中选择性不能由沉淀、DOM 截留或支架解释；
3. `qth,bed`、`BVmax,dynamic`、`U` 与实测突破达到 `BVreq`；
4. NEM/MDCC 亚群等价、第二结构判据、再生、蛋白酶/微生物、完整蛋白泄漏和五次循环全部通过。

以下任一项触发 D1-B 终止：序列或 apo 分数不闭合；最低蛋白负载超过 `Lbed,max/Csol,max/Costmax`；sortase 结点不可检出；NEM/MDCC 亚群不等价或 HDX-MS 不支持主床动态；D56N 整体失稳而没有有效口袋扰动对照；实际混合水最小选择性效应或 `BVreq` 不达标；蛋白酶/微生物导致超限失活；没有温和释放窗口；完整蛋白泄漏或床压降超限。不得用提高蛋白投加、缩短运行或只报告传感响应掩盖失败。B-RAND失败不触发D1-B终止，因为它不承担核心结论。

D1-B 失败时回到 D1-A；若 D1-A 已因上述核心门禁失败，则两案均不强选，项目回到新原型/新实现搜索。D1-B 当前是完整、可执行的备选方案，不是已有性能结果，也不因使用真实 PBP 自动获得 pass。

## 8. 安全与废物

重组菌培养、Ni-NTA 洗脱液、MDCC/NEM、DBCO-NHS、DMSO、sortase、proteinase K、砷酸根、废水和 sodium azide 分流管理。NEM/MDCC/DBCO 避光并在通风橱内操作；proteinase K 避免气溶胶和皮肤接触；砷酸根进入专用含砷危废。叠氮化钠有急性毒性，禁止与酸或重金属管路接触、禁止入下水道。未过滤二级出水按潜在病原样品处理，使用相应个人防护并在批准流程下灭活。含蛋白材料不得高温灭菌后继续用于性能测试。

## 9. Attack response

| attack_id | 定向修订 | 当前状态/失败条件 |
|---|---|---|
| D1B-01 | 取消固定100 μM；由 `Cin/BVreq/factive/U/Yfix` 反算 `nfixed,min/Lbed,min/Cfeed,min`；柱前只用含 `Umin` 的 `BVmax,dynamic` 放行 | `critical design-closed, experiment-open`；超过 `Lbed,max/Csol,max/Costmax` 或 `BVmax,dynamic<BVreq` 即淘汰 |
| D1B-02 | 构建体改为 1OIB/1IXG 共用 T141D 成熟链来源的 T141D/A197C；加入双 PDB 序列、编号、成熟边界、理论质量、Sanger/N 端验收；测游离 Pi、变性释放总结合 Pi、`fapo` 和再结合 1:1 | 克隆前门禁；`fapo<0.95`、化学计量不在 0.90–1.10 或序列加工不闭合即失败 |
| D1B-03 | 冻结 *S. aureus* sortase A Δ59-His6 身份与单位；按活性投酶；检出 `LPET-GGGK` 结点、量化水解副产物，Ni-NTA 去酶并做尿素/盐共价保留 | 结点不可检出、水解/非特异吸附主导或 sortase 残留超限即报废 |
| D1B-04 | 固定前后分别测 NEM/MDCC 的比例、固定收率、`Kd/kon/koff`；加入快速 Pi 占据、MDCC 慢相饱和和 HDX-MS 第二判据 | 亚群差异超过 20%、固定后比例不合格、双步/HDX 失败即删除主床动态并取消备选资格 |
| D1B-05 | D56N仅作折叠可比的口袋扰动，失活体只作背景；B-RAND因无法从1%可裂解子群无偏恢复全床固定点数，降为可选探索样品 | 核心结论只使用D56N、失活、B-BLANK、B-NOREP和RESIN-1；B-RAND不参与pass或失败合同 |
| D1B-06 | 再生加入 B-BLANK、B-NOREP、只再生组、预占位 Pi 扣除和全分段流出物；cycle 1/5 加 HDX-MS 与完整蛋白泄漏 | 释放、`factive`、选择性、MDCC/HDX、质量平衡或泄漏任一不过线即终止，不升级强条件 |
| D1B-07 | azide 由定量限门禁替代固定洗量；微生物加入无材料、B-BLANK、灭活水和无菌材料；proteinase K 用 PMSF 终止；以 N/内部/C 端及结点肽加完整蛋白法分辨裂解/脱落 | 微生物 P 贡献不可分、残余 azide、持续水解或完整蛋白泄漏超限即否决真实水床 |
| D1B-08 | 工程主指标冻结为单位床体积混合水突破；相对 RESIN 的三项选择性几何平均增量≥1.50且 95% CI 下限≥1.25，并同时达到绝对 `BVreq`；活性位点归一仅作机制次指标 | 仅相对失活/受损对照显著、跨批次不复现或效应不足时降级为机制/传感样品，不交接吸附床 |
