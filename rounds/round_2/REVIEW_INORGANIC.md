# Round 2 交叉复审：D1 修订稿与 D4 终止审计

## 1. 判定口径

- `design-closed`：分子、反应、对照或停机规则已冻结；只关闭设计歧义，不代表材料性能成立。
- `experiment-open`：决定性证据尚未取得，原 high issue 仍未关闭。
- `critical`：缺口不能由当前架构或局部修订关闭，触发终止。

`advance` 仍要求总分不低于 85、无 critical/high 未解决，并具备可信静态与动态硬对应及可交接 SOP。

## 2. 独立复评分与决定

| 方案 | causal_closure /20 | selective_adsorption_mechanism /20 | biomimetic_fidelity /20 | originality /15 | experimental_falsifiability_and_controls /15 | evidence_integrity /10 | 总分 | 决定 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| D1 磷酸盐 | 16 | 15 | 17 | 12 | 14 | 9 | **83** | **revise，不 pass** |
| D4 硝酸盐 | 5 | 8 | 8 | 6 | 10 | 10 | **47** | **reject，终止确认** |

D1 的结构、对照和预注册程度已足以进入分阶段实验，但得分仍低于 85，且五项核心 high 仍是 experiment-open。D4 的 47 分为完整旧概念的终止状态复核分，不是重开评分。

## 3. D1 逐项复审

| issue_id | 严重度 | Round 2 状态 | 复审裁决 | 关闭要求 |
|---|---|---|---|---|
| R1-REV-INORG-D1-001 | high | **experiment-open** | 三种分子与随机几何对照已冻结，但尚无 1OIB/1IXG 定量映射，也无全水相预组织增量 | 合成前补叶间距离/口袋体积映射；随后以 ITC、竞争和置换证明 `Gstatic` 达标，否则停止固定化 |
| R1-REV-INORG-D1-002 | high | **experiment-open** | 形态、砷酸根、金属/胶体诊断和阈值已设计闭合，科学主张仍待真实水证据 | 排除沉淀、桥联和胶体路径，且实际活度背景下仍优于 R-Rand 与强基准 |
| R1-REV-INORG-D1-003 | high | **experiment-open** | R-Lock、标签互换、寿命 FRET 和 DEER 定义充分；桥连体是否真锁在可比开放态未知 | DEER 证实可比开放态；占据、寿命 FRET、DEER 与抗置换同向，锁开体消除动态增量；否则删除动态主张 |
| R1-REV-INORG-D1-004 | high | **experiment-open** | 理论载量公式、3×3 矩阵和床阈值已冻结；但当前只以 R-Rand 为工程参照，未完整带入商用树脂、P7 水凝胶和固定化 PBP 的分角色基准 | 补强基准矩阵与同床体积比较；取得同时满足位点利用率、突破、传质和压降的窗口 |
| R1-REV-INORG-D1-005 | high | **experiment-open** | 组件兼容、老化组和五次早期循环门禁已冻结，无温和再生结果 | 结构、开态、下一轮闭合、选择性和接枝量共同恢复；无持续浸出或漂移 |
| R1-REV-INORG-D1-006 | low | **design-closed** | 蛋白数字按物种分账，固定化 PBP 只作机制参照，上一轮问题维持关闭 | 后续不得恢复成单位质量容量基准 |
| R1-REV-INORG-D1-007 | medium | **experiment-open** | 受体密度×OEG 矩阵和双归一已冻结，抗污与可达性的共同窗口尚未取得 | DOM 降低、目标扩散与动态容量同时满足预注册阈值，且对照按活性位点和床体积配平 |
| R1-REV-INORG-D1-008 | medium | **design-closed** | 效应量、工程阈值、漂移和停机规则均已预注册；五次循环没有被写成长周期稳定 | 在解码前冻结重复数、功效与方法定量限，禁止事后改阈值 |
| R2-REV-INORG-D1-009 | high | **experiment-open** | 新发现：修订稿仍不是可直接交接的 bench-scale SOP，缺试剂当量、反应/纯化条件、批量、柱装填及基准执行细节 | Round 3 先形成可执行 SOP 与强基准计划，经化学可行性复核后再开实验；仅有反应顺序不能关闭 |

### D1 决定

**revise。** 分子架构和因果设计可以继续，不需要推倒重写；R1-REV-INORG-D1-003 若因 R-Lock 不可比而失败，必须按既定规则删除动态主张，届时 D1 失去终选资格。当前不能把预注册阈值当作已获得的关闭证据。

## 4. D4 终止完整性与逐项状态

| issue_id | Round 2 状态 | 复审裁决 |
|---|---|---|
| R1-REV-INORG-D4-001 | **critical** | NrtA 无实验 apo/硝酸根/亚硝酸根构象分布；人工开闭不能补足生物动态。终止触发正确。 |
| R1-REV-INORG-D4-002 | **design-closed by separation** | 电释放已移出 D4，只能另立 N4 型普通导电吸附项目。 |
| R1-REV-INORG-D4-003 | **experiment-open, archived** | 水相静态口袋可独立筛查，但结果不回填 D4 资格。 |
| R1-REV-INORG-D4-004 | **design-closed by termination** | 固相动态/FRET 不再投入；重开后须重新设计。 |
| R1-REV-INORG-D4-005 | **design-closed by termination** | 载量、OEG、导电与压降矩阵不再以 D4 名义执行。 |
| R1-REV-INORG-D4-006 | **design-closed by separation** | 氮质量平衡属于独立电再生子项目，不用于补 D4 动态。 |
| R1-REV-INORG-D4-007 | **experiment-open, archived** | K269 类锚点静态筛选可保留，不能宣称硝酸盐专一或 NrtA 动态。 |
| R1-REV-INORG-D4-008 | **design-closed by termination** | 目标命名和长期阈值须在任何新项目中重新注册。 |

D4 终止审计完整：明确了唯一 critical、说明局部材料表征为何不能关闭、停止双叶/碳毡/FRET 投入、将静态与电释放拆为独立子项目、规定了重开所需的蛋白实验结构证据，并明确不再占用终选名额。**决定维持 reject。**

## 5. Round 3 路线建议

### D1 能否作为唯一主候选

**可以作为 Round 3 唯一主候选，但只能称 working primary，不是 pass。** 理由是 PBP/PstS 是当前无机轨道中唯一同时具有直接生物静态结构对和结合后闭合动力学的原型；D1 的人工实现也已具备可执行的分阶段淘汰逻辑。Round 3 必须依次完成结构映射与 SOP、可溶受体水相门禁、R-Lock 动态因果，再决定是否进入 3×3 固相和柱实验。前一级失败不得继续投入后一级。

### 是否需要重新开放实现路线

**需要，但只开放一个受限备份实现，不重启 D4。** D1 的柔性肽夹在水相选择性、分子内桥连和工程载量上存在单点失败风险。建议建立 `D1-B`：定向固定 PBP/PiBP 的蛋白—多孔载体杂化路线，作为机制保持型备份。P4 只支持固定化传感，不能预设吸附床性能；D1-B 必须独立通过活性位点密度、固定方向、蛋白泄漏/蛋白酶稳定、二级出水选择性、再生后构象恢复和床容量门禁。

D1-B 在这些门禁前不获得 finalist 身份，也不得用蛋白传感响应替代工程容量。P7 水凝胶和商用树脂继续作为工程基准，不升级为仿生备选。
