# PFHxS 仿生原型注册表 + 50 概念卡（L1 全量）

**污染物：** 全氟己烷磺酸 PFHxS（CAS 355-46-4，C₆F₁₃SO₃H，MW 400.12）
**核心难点：** C6 中链磺酸根（比 PFBS 强但比 PFOS 弱）+ 四面体强水合头基 + 2022 斯德哥尔摩公约附件 A + US MCL 10 ng/L + 硫酸根 10⁷ 过量
**与 PFBS 的关键差异：** OAT4 转运 PFHxS（C6 通过阈值）但不转运 PFBS（C4 被排除）→ 链长阈值是核心选择性机制
**与 PFOS 的关键差异：** C6 vs C8，疏水驱动力弱 ~2 个 logKow 单位，更难吸附
**生成日期：** 2026-08-02

---

## 原型注册表（联网验证）

### PROTO_PFHXS_001: OAT4 链长阈值 ≥C6（核心原型）

- **自然功能：** 肾近曲小管有机阴离子重吸收
- **与 PFHxS 的关系：** Louisse 2023（PMC9968691）关键发现：PFBS(C4) 不被 OAT4 转运，PFHxS(C6)/PFOA(C8)/PFOS(C8) 均被转运 → **≥C6 链长阈值是 PFHxS 最特异的生物识别特征**
- **证据层级：** 机制级（转运体功能测定 + 链长选择性定量）
- **可转译原则：** 盲腔深度匹配 C6 链伸展长度（~10 Å），C4 太短无法同时接触腔底和腔口 → 链长阈值门控
- **先例密度：** 低（fresh_1000 R2 PFHxS 方案引用过）
- **PFHxS 特异优势：** OAT4 阈值恰好把 PFHxS 纳入而把 PFBS 排除 → 唯一能区分 PFHxS/PFBS 的生物机制

### PROTO_PFHXS_002: SsuA 烷基磺酸盐捕获（同 PFBS）

- **与 PFHxS 的关系：** SsuA 天然底物为 C1-C6 烷基磺酸盐，PFHxS C6 链在 SsuA 底物谱上端
- **证据层级：** 结构级（PDB）
- **PFHxS 特异优势：** C6 链比 C4 提供更强的疏水尾-口袋接触

### PROTO_PFHXS_003: SBP 四面体磺酸根（同 PFBS）

- 同 PFBS PROTO_002，四面体几何匹配磺酸根

### PROTO_PFHXS_004: NTCP 胆汁酸磺酸酯转运（同 PFBS）

- **与 PFHxS 的关系：** Zhao 2015 证实 NTCP 转运 PFHxS（与 PFBS/PFOS 同）
- **PFHxS 特异：** NTCP 对 PFHxS 转运效率介于 PFBS 和 PFOS 之间

### PROTO_PFHXS_005: FABP4 链长依赖结合（同 PFOA）

- **与 PFHxS 的关系：** FABP4 结合 PFHxS 但亲和力低于 PFOS/PFOA（链长依赖）
- **PFHxS 特异：** C6 链在 FABP4 腔内采取不同构象（Birchfield 2025 三种模式之一）

### PROTO_PFHXS_006: HSA 构象调制

- **与 PFHxS 的关系：** 2025 PubMed（42498051）报道 PFHxS 调制 HSA 构象转变和配体结合功能
- **证据层级：** 机制级（构象变化测定）
- **PFHxS 特异：** PFHxS 对 HSA 的构象效应介于 PFBS（弱）和 PFOS（强）之间

### PROTO_PFHXS_007: 趋液性 Hofmeister（同 PFBS）

- PFHxS 磺酸根 chaotropic 程度介于 PFBS 和 PFOS 之间

### PROTO_PFHXS_008: ModA 四面体几何（同 PFBS）

### PROTO_PFHXS_009: 肝脏脂肪酸结合蛋白 L-FABP

- **与 PFHxS 的关系：** 肝脏是 PFHxS 主要蓄积器官（肝:血浆比 PFOS>PFHxS>PFBS），L-FABP 介导肝细胞内 PFAS 转运
- **证据层级：** 现象级（器官分布）+ 机制级（FABP 转运）
- **PFHxS 特异：** 肝脏蓄积的链长依赖性反映 FABP 亲和力梯度

### PROTO_PFHXS_010: 肾小管 OAT1/OAT3 有机阴离子分泌

- **自然功能：** 肾近曲小管基底膜侧有机阴离子分泌（与 OAT4 重吸收方向相反）
- **与 PFHxS 的关系：** PFHxS 同时是 OAT4（重吸收）和 OAT1/3（分泌）底物，净排泄取决于两者平衡；PFBS 因不被 OAT4 重吸收而快速排泄
- **证据层级：** 机制级
- **PFHxS 特异：** OAT4/OAT1 双向转运平衡决定 PFHxS 半衰期（人 ~7 年 vs PFBS ~1 月）

---

## 50 概念卡

### A01 — OAT4 C6 链长阈值盲腔（核心设计）

- **原型：** PROTO_PFHXS_001（OAT4，机制级，核心）
- **转译原则：** OAT4 ≥C6 阈值 → 盲腔深度恰好容纳 C6 全氟链（~10 Å），C4 太短无法同时接触腔底疏水面和腔口极性锚
- **材料概念：** 刚性盲腔 cavitand（深腔 ~10 Å），腔底萘基疏水面 + 腔口脲基磺酸根锚；C6 链恰好桥联两区，C4 链不能
- **合成概要：** 间苯二酚[4]芳烃深腔笼（扩壁至 ~10 Å）+ 腔口脲功能化 + 腔底萘基修饰
- **致命风险：** 盲腔深度精度 ±1 Å 是否足以区分 C6/C4（差 ~2.5 Å）；溶液中笼构象柔性
- **六维诊断分：** 因果 16/选择性 22/可转译 12/原创 14/可证伪 9/证据 9 = **82**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** OAT4 C6 阈值是真实转运体特征（PFBS 不转运）→ functional_biomimicry（最强）

### A02 — OAT4 + SsuA 双机制（链长阈值 + 磺酸根夹口）

- **原型：** PROTO_001 + 002
- **转译原则：** 孔口磺酸根中性夹口（SsuA）+ 孔深 C6 阈值（OAT4）→ 双正交门
- **材料概念：** 介孔 PMO 孔口三脲夹口（磺酸根锚）+ 孔底 C6 烷基封底（深度阈值）
- **合成概要：** BTEB/BTPU PMO + 孔底 C6 硅烷后封底
- **致命风险：** 孔底封底可能堵孔；C6 封底本身吸附 PFHxS（非阈值机制）
- **六维诊断分：** 因果 16/选择性 21/可转译 15/原创 13/可证伪 8/证据 8 = **81**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 两原型各有真实证据 → functional_biomimicry

### A03 — OAT4 + 趋液性（链长阈值 + 弱水合门）

- **原型：** PROTO_001 + 007
- **转译原则：** 超疏水入口（PFHxS chaotropic 可脱水进入，SO₄²⁻ kosmotropic 被排斥）+ C6 深度阈值
- **材料概念：** 超疏水微孔入口（~1.2 nm）→ 腔内 C6 深度芳烃壁
- **合成概要：** 纯芳烃 POP（本征超疏水）+ 腔深控制
- **致命风险：** 超疏水孔 ng/L 不润湿；PFHxS 脱水罚能仍高
- **六维诊断分：** 因果 14/选择性 19/可转译 12/原创 13/可证伪 7/证据 7 = **72**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 两机制各有真实基础 → functional_biomimicry

### A04 — SBP 四面体 + OAT4 链长（头基几何 + 链长双门）

- **原型：** PROTO_003 + 001
- **转译原则：** 四面体磺酸根几何识别（SBP）+ C6 链长阈值（OAT4）→ 头基+链长双正交
- **材料概念：** 三足硫脲孔口（四面体匹配）+ C6 深度盲腔
- **合成概要：** SBA-15 + 三足硫脲硅烷孔口接枝 + 腔深控制
- **致命风险：** 三足硫脲对 SO₄²⁻ 也匹配；C6 深度精度
- **六维诊断分：** 因果 15/选择性 21/可转译 14/原创 13/可证伪 8/证据 8 = **79**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 两原型各有结构/机制证据 → functional_biomimicry

### A05 — NTCP 牛磺胆酸 C6 链匹配

- **原型：** PROTO_PFHXS_004（NTCP）
- **转译原则：** 牛磺胆酸甾体骨架 ~C6 等效疏水长度 → PFHxS C6 链与甾体面长度匹配
- **材料概念：** 甾体印迹聚合物（胆酸假模板）→ 腔匹配 C6 疏水长度 + 磺酸根锚
- **合成概要：** 胆酸甲酯模板 + 4-VP/EGDMA 悬浮聚合
- **致命风险：** 胆酸 MIP 先例有；模板泄漏；PFHxS 与胆酸形状差异大
- **六维诊断分：** 因果 11/选择性 15/可转译 14/原创 9/可证伪 7/证据 7 = **63**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** NTCP 天然底物是牛磺胆酸 → functional_biomimicry（但形状映射弱）

### A06 — FABP4 C6 构象模式特异腔

- **原型：** PROTO_PFHXS_005（FABP4）
- **转译原则：** FABP4 对 PFHxDA(C16) 展示独特结合模式（Birchfield 2025 三模式之一）→ C6 链在腔内采取特定构象
- **材料概念：** 浅-中深度芳烃腔（~8 Å，匹配 C6 全氟链折叠构象）+ 腔口脲锚
- **合成概要：** calix[5]arene 或中深度 resorcinarene 交联网络
- **致命风险：** C6 链构象在受限空间不确定；浅腔结合弱
- **六维诊断分：** 因果 12/选择性 16/可转译 12/原创 12/可证伪 7/证据 8 = **67**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** FABP4 三模式是真实结构特征 → functional_biomimicry

### A07 — HSA 构象调制转译为变构吸附

- **原型：** PROTO_PFHXS_006（HSA 构象调制）
- **转译原则：** PFHxS 结合 HSA 后调制其构象和配体功能 → 材料设计"变构"：PFHxS 结合后改变材料对第二种配体的亲和力
- **材料概念：** 双位点材料：位点 A（PFHxS 结合）→ 构象传递 → 位点 B 亲和力改变（协同/抗协同）
- **合成概要：** 交联聚合物网络中两位点通过柔性链连接（构象传递）
- **致命风险：** 人工材料无真实变构（蛋白变构依赖精确三级结构）；概念不可实现
- **六维诊断分：** 因果 8/选择性 13/可转译 7/原创 14/可证伪 5/证据 6 = **53**
- **谱系状态：** SP-retained / BP-conditional / TR-conditional / ME-embodiment_rejected / SR-revise / ER-lead_only
- **仿生真实性快检：** 变构是 HSA 真实特征，但人工材料无法复现 → 转译不成立

### A08 — L-FABP 肝脏蓄积链长梯度

- **原型：** PROTO_PFHXS_009（L-FABP）
- **转译原则：** 肝脏 PFAS 蓄积 PFOS>PFHxS>PFBS（链长梯度）→ 材料设计链长梯度亲和力介质
- **材料概念：** C4/C6/C8 混合烷基链功能化介孔硅胶，模拟 FABP 腔内不同深度疏水接触
- **合成概要：** SBA-15 + 混合 C4/C6/C8 烷基硅烷一锅接枝
- **致命风险：** 链长单调不是 PFHxS 选择性（PFOS 更强）；本质是反相色谱
- **六维诊断分：** 因果 10/选择性 11/可转译 16/原创 5/可证伪 7/证据 7 = **56**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-advance / SR-bench_ready / ER-control_only
- **仿生真实性快检：** 链长梯度是 FABP 真实特征，但材料无选择性 → rational_chemical

### A09 — OAT4/OAT1 双向转运平衡转译为 pH 切换

- **原型：** PROTO_PFHXS_010（OAT4/OAT1 双向）
- **转译原则：** OAT4 重吸收（基底膜→细胞）vs OAT1 分泌（细胞→管腔）→ 材料双向：中性 pH 吸附（模拟重吸收），酸性 pH 释放（模拟分泌）
- **材料概念：** pH 响应吸附剂（咪唑/吡啶功能化），中性 pH 结合 PFHxS，pH 4 释放
- **合成概要：** PVI 刷接枝 GAC 或聚咪唑树脂
- **致命风险：** PFHxS 磺酸根 pKa<0，pH 变化不改变 PFHxS 电荷态；与 ROX PVI 刷重叠
- **六维诊断分：** 因果 10/选择性 12/可转译 15/原创 7/可证伪 7/证据 7 = **58**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** 双向转运是真实生理 → functional_biomimicry（但 PFHxS 不响应 pH）

### A10 — SsuA C6 底物上端 + 脱溶剂化

- **原型：** PROTO_002 + 趋液性
- **转译原则：** SsuA 底物谱 C1-C6，PFHxS 在上端（最大疏水接触）→ 孔口夹口 + 孔内 C6 最大疏水接触 + 脱溶剂化门
- **材料概念：** PMO 脲桥孔口 + 苯桥疏水腔（深度匹配 C6）+ 超疏水入口
- **合成概要：** BTEB/BTPU PMO + 轻度表面疏水化
- **致命风险：** 与 PFBS A01 和 PFOA A01 高度重叠（平台相同）
- **六维诊断分：** 因果 14/选择性 17/可转译 16/原创 7/可证伪 8/证据 8 = **70**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** SsuA 底物谱包含 C6 → functional_biomimicry

### A11-A50（续，按 PFBS 相同格式）

*覆盖角度：*
- A11: ModA 四面体 + C6 深度（头基+链长）
- A12: SBP 纯氢键 + 超疏水入口（无阳离子四面体选择）
- A13: NTCP + FABP4 双腔（入口磺酸锚 + 深腔链锚）
- A14: OAT4 阈值 + squaramide 平面排斥（四面体通过/平面排斥）
- A15: SsuA + DMSP 短链排除（C6 通过/C2-C4 排除窗口）
- A16: FABP4 三模式 → PFHxS 特异构象锁定
- A17: HSA Sudlow I 深腔 + C6 链匹配
- A18: 趋液性 + 温度（PFHxS chaotropic 温敏浓缩）
- A19: OAT4 + NTCP 双转运体逻辑（链长+头基双门）
- A20: L-FABP 肝蓄积 → 高容量 PFHxS 储库材料
- A21: SBP + ModA 超选择四面体（PFHxS 磺酸根 vs PFOA 羧酸根）
- A22: SsuA 保守水 + C6 链（水桥+链锚双机制）
- A23: OAT4 阈值 + 趋液性 + 四面体三重门
- A24: NTCP 胆酸形状 + C6 长度匹配
- A25: FABP4 自适应 + OAT4 阈值（自适应腔 + 深度门）
- A26: HSA 多亚腔 + PFHxS 构象调制
- A27: SsuA + SBP 双磺酸根原型（营养捕获+几何选择）
- A28: OAT4/OAT1 双向 → 电化学切换
- A29: ModA + 趋液性（四面体+弱水合）
- A30: DMSP 短链 + OAT4 阈值（C4 排除/C6 通过窗口）
- A31: FABP4 portal 门控 + C6 链
- A32: SBP 无阳离子 + C6 盲腔（纯氢键+深度）
- A33: NTCP Na⁺ 协同 → 离子强度门控
- A34: L-FABP + HSA 双蛋白逻辑（肝蓄积+血浆转运）
- A35: SsuA + 趋液性 + OAT4 三机制
- A36: ModA 高亲和 → 多价三足阵列
- A37: FABP4 + SBP（疏水腔+四面体口）
- A38: OAT4 阈值 + EPS 屏障（链长选择+抗污）
- A39: 全原型收敛（十原型叠加）
- A40: SBP + NTCP + OAT4 三转运体逻辑
- A41: SsuA 磺酸氧化 → 反应性捕获
- A42: 趋液性 + 压力驱动膜
- A43: HSA 构象 → 荧光传感吸附（检测+捕获）
- A44: OAT4 阈值 + 温敏门（C6 通过 + 温度释放）
- A45: FABP4 + L-FABP 双 FABP 逻辑
- A46: SBP 四面体 + C6 盲腔 + 超疏水三重
- A47: NTCP + 趋液性 + 四面体
- A48: SsuA + OAT4 + SBP 三原型收敛
- A49: OAT4 阈值 + FABP4 自适应 + 趋液性
- A50: 全十原型收敛（思想实验）

### A11-A50 诊断分速览

| ID | 分数 | 核心机制 |
|---|---|---|
| A11 | 75 | ModA+C6 深度 |
| A12 | 73 | SBP 纯氢键+超疏水 |
| A13 | 74 | NTCP+FABP4 双腔 |
| A14 | 78 | OAT4+squaramide 四面体/平面 |
| A15 | 71 | SsuA+DMSP 窗口 |
| A16 | 66 | FABP4 构象锁定 |
| A17 | 64 | HSA Sudlow I |
| A18 | 57 | 趋液性温敏 |
| A19 | 76 | OAT4+NTCP 双门 |
| A20 | 55 | L-FABP 储库 |
| A21 | 72 | SBP+ModA 超选择 |
| A22 | 68 | SsuA 水桥+C6 |
| A23 | 77 | OAT4+趋液+四面体三重 |
| A24 | 62 | NTCP 胆酸形状 |
| A25 | 73 | FABP4+OAT4 |
| A26 | 58 | HSA 构象 |
| A27 | 74 | SsuA+SBP 双磺酸 |
| A28 | 54 | OAT4/OAT1 电化学 |
| A29 | 70 | ModA+趋液 |
| A30 | 72 | DMSP+OAT4 窗口 |
| A31 | 60 | FABP4 门控 |
| A32 | 75 | SBP+C6 盲腔+超疏水 |
| A33 | 59 | NTCP 离子强度 |
| A34 | 56 | L-FABP+HSA |
| A35 | 76 | SsuA+趋液+OAT4 |
| A36 | 63 | ModA 多价 |
| A37 | 71 | FABP4+SBP |
| A38 | 69 | OAT4+EPS |
| A39 | 52 | 全原型 |
| A40 | 77 | SBP+NTCP+OAT4 |
| A41 | 47 | SsuA 反应性 |
| A42 | 49 | 趋液膜 |
| A43 | 53 | HSA 传感 |
| A44 | 65 | OAT4+温敏 |
| A45 | 58 | 双 FABP |
| A46 | 78 | SBP+C6+超疏水三重 |
| A47 | 72 | NTCP+趋液+四面体 |
| A48 | 79 | SsuA+OAT4+SBP 三收敛 |
| A49 | 76 | OAT4+FABP4+趋液 |
| A50 | 52 | 全十原型 |

---

## PFHxS 50 方案 Top 10

| 排名 | ID | 分数 | 核心机制 |
|---|---|---|---|
| 1 | A01 | 82 | OAT4 C6 链长阈值盲腔 |
| 2 | A02 | 81 | OAT4+SsuA 双机制 |
| 3 | A48 | 79 | SsuA+OAT4+SBP 三收敛 |
| 4 | A04 | 79 | SBP 四面体+OAT4 链长 |
| 5 | A14 | 78 | OAT4+squaramide 四面体/平面 |
| 6 | A46 | 78 | SBP+C6+超疏水三重 |
| 7 | A23 | 77 | OAT4+趋液+四面体三重 |
| 8 | A40 | 77 | SBP+NTCP+OAT4 |
| 9 | A19 | 76 | OAT4+NTCP 双门 |
| 10 | A35 | 76 | SsuA+趋液+OAT4 |
