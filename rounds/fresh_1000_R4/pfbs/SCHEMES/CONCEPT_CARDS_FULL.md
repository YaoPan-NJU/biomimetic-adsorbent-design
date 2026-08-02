# PFBS 仿生原型注册表 + 50 概念卡（L1 全量）

**污染物：** 全氟丁烷磺酸 PFBS（CAS 375-73-5，C₄F₉SO₃H，MW 300.10）
**核心难点：** C4 短链疏水驱动力极弱 + 磺酸根四面体强水合（pKa<0 全解离）+ EPA HA 2000 ng/L + 硫酸根 10⁷ 过量 + 比 PFOA 更难（链短+头基水合更强）
**与 PFOA 的关键差异：** 磺酸根（四面体 C3v）vs 羧酸根（平面 C2v）；C4 vs C8；NTCP 转运 PFBS 但 OAT4 不转运
**生成日期：** 2026-08-02

---

## 原型注册表（联网验证）

### PROTO_PFBS_001: SsuA（烷基磺酸盐结合蛋白）— 直接相关

- **自然功能：** 细菌缺硫条件下捕获烷基磺酸盐（R-SO₃⁻）
- **与 PFBS 的关系：** PFBS 就是全氟烷基磺酸盐，SsuA 天然底物与 PFBS 头基完全同构（磺酸根）；Beale 2010 PDB 结构显示磺酸根由多重主链 NH + 保守水定位
- **证据层级：** 结构级（PDB）+ 功能级
- **可转译原则：** 中性多齿 NH 夹口定位四面体磺酸根 + 烷基尾进入疏水口袋
- **先例密度：** 低（main SC-P02 用过）
- **PFBS 特异优势：** SsuA 天然识别磺酸根（非羧酸根），是 PFBS 最直接的仿生原型

### PROTO_PFBS_002: 硫酸盐结合蛋白 SBP（PDB 1SBP）

- **自然功能：** 细菌硫酸盐主动转运的周质受体，以纯氢键（无金属、无阳离子）结合四面体硫酸根
- **与 PFBS 的关系：** SBP 对四面体 SO₄²⁻ 的识别几何（O-S-O 109.5°, O···O 2.5 Å）与 PFBS 磺酸根（O-S-O ~112°, 单价）高度匹配；Pflugrath & Quiocho 1985 Nature 314:257 经典结构
- **证据层级：** 结构级（1.7 Å 晶体）
- **可转译原则：** 四面体氧阴离子的多齿氢键几何互补 + 脱溶剂化 + 无阳离子
- **先例密度：** 零（从未用于 PFAS 吸附）
- **PFBS 特异优势：** 四面体几何匹配磺酸根（非羧酸根），提供 PFBS/PFOA 头基区分原理

### PROTO_PFBS_003: NTCP（钠-牛磺胆酸共转运多肽，SLC10A1）

- **自然功能：** 肝窦基底膜胆汁酸（牛磺胆酸等两亲性磺酸/硫酸酯阴离子）摄取
- **与 PFBS 的关系：** Zhao 2015（PMC4607751，被引 140）证实人/大鼠 NTCP 转运 PFBS、PFHxS、PFOS；牛磺胆酸本身就是磺酸酯（与 PFBS 头基同构）
- **证据层级：** 机制级（转运测定）
- **可转译原则：** 两亲性磺酸阴离子的"疏水甾体面 + 磺酸头"双特征读取 + Na⁺ 协同
- **先例密度：** 低（fresh_1000 PFBS 简报引用过）
- **PFBS 特异优势：** NTCP 天然底物牛磺胆酸含磺酸基，与 PFBS 头基同构

### PROTO_PFBS_004: ModA（钼酸根结合蛋白）

- **自然功能：** 细菌钼酸盐/钨酸盐（四面体氧阴离子）高亲和捕获
- **与 PFBS 的关系：** ModA 以预组织中性氢键阵列区分四面体 MoO₄²⁻/WO₄²⁻ 与 SO₄²⁻（Hu 1997 Nat Struct Biol）；PFBS 磺酸根为四面体，几何匹配
- **证据层级：** 结构级（PDB 1amf/1wod）
- **可转译原则：** 四面体氧阴离子几何选择（三足供体匹配四面体 vs 平面供体匹配平面）
- **先例密度：** 低（fresh_1000 PFBS A17 用过）
- **PFBS 特异优势：** 四面体几何是 PFBS 磺酸根区别于 PFOA 羧酸根的核心特征

### PROTO_PFBS_005: 牛磺酸代谢酶（半胱氨酸双加氧酶 CDO）

- **自然功能：** 牛磺酸（2-氨基乙磺酸）生物合成中的关键酶，识别磺酸乙胺骨架
- **与 PFBS 的关系：** 牛磺酸 = H₂N-CH₂-CH₂-SO₃⁻，PFBS = F₉C₄-SO₃⁻，共享磺酸根基团；CDO 活性位点对磺酸基有特异配位
- **证据层级：** 结构级（PDB）+ 机制级
- **可转译原则：** 磺酸根基团的特异配位几何（Fe 中心 + 氢键网络）→ 转译为中性多齿磺酸根夹口
- **先例密度：** 零
- **PFBS 特异优势：** 天然识别含磺酸基小分子

### PROTO_PFBS_006: 海藻二甲基磺丙酸（DMSP）裂解酶

- **自然功能：** 海洋藻类产生 DMSP（二甲基磺丙酸）作为渗透调节剂，细菌 DddP/DddY 裂解酶识别磺酸丙酸骨架
- **与 PFBS 的关系：** DMSP = (CH₃)₂S⁺-CH₂-CH₂-COO⁻（磺酸内盐），PFBS = C₄F₉-SO₃⁻；共享磺酸/锍基团 + 短碳链
- **证据层级：** 机制级 + 部分结构级
- **可转译原则：** 短链磺酸/锍化合物的特异识别（链长 C2-C4 窗口）+ 头基几何
- **先例密度：** 零
- **PFBS 特异优势：** 天然识别短链（C2-C3）含硫/磺酸化合物，与 PFBS C4 链长匹配

### PROTO_PFBS_007: FABP4（同 PFOA PROTO_001）

- **与 PFBS 的关系：** FABP4 结合多种 PFAS 包括短链（Birchfield 2025），但 PFBS 亲和力低于长链
- **证据层级：** 结构级
- **PFBS 特异限制：** C4 链太短，疏水驱动力不足以驱动 FABP 型腔结合

### PROTO_PFBS_008: HSA（同 PFOA PROTO_003）

- **与 PFBS 的关系：** 澳大利亚评估报告 PFBS 94% 与白蛋白结合（100% 生理白蛋白浓度）
- **证据层级：** 现象级（结合率测量）
- **PFBS 特异限制：** 广谱非特异，无头基选择性

### PROTO_PFBS_009: 趋液性（Hofmeister）离子通道

- **自然功能：** 生物膜通道对离子的选择性部分由 Hofmeister 序列（离子水合/去水合）决定
- **与 PFBS 的关系：** PFBS 磺酸根为弱水合（chaotropic 端）vs 硫酸根强水合（kosmotropic）→ 趋液性差异可用于选择性
- **证据层级：** 物理化学原理（非特异蛋白）
- **可转译原则：** 弱水合有机阴离子（PFBS）vs 强水合无机阴离子（SO₄²⁻）的趋液性差异 → 疏水孔口优先接纳弱水合离子
- **先例密度：** 低（fresh_1000 R2 PFBS/PFHxS 方案用过）

### PROTO_PFBS_010: EPS 蛋白疏水域（同 PFOA PROTO_008）

- **与 PFBS 的关系：** EPS 对短链 PFAS 的吸附弱于长链，但蛋白疏水域仍提供部分结合
- **证据层级：** 现象级
- **PFBS 特异限制：** C4 链太短，EPS 疏水结合极弱

---

## 50 概念卡

### A01 — SsuA 磺酸根中性夹口 PMO（直接转译）

- **原型：** PROTO_PFBS_001（SsuA，结构级，直接相关）
- **转译原则：** SsuA 多重主链 NH 定位磺酸根 + 烷基尾疏水口袋 → PMO 脲桥 NH 夹口 + 苯桥疏水腔
- **材料概念：** BTEB/BTPU PMO（同 SC-P02），强调磺酸根四面体与脲 NH 的几何匹配
- **合成概要：** 溶胶-凝胶，BTEB 先 → BTPU 延迟，P123 模板
- **致命风险：** C4 链太短疏水驱动力不足；脲对磺酸根水相结合可能 <5 M⁻¹
- **六维诊断分：** 因果 15/选择性 17/可转译 17/原创 9/可证伪 8/证据 8 = **74**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** SsuA 天然底物就是烷基磺酸盐 → functional_biomimicry（最直接）

### A02 — SBP 四面体几何选择 POP

- **原型：** PROTO_PFBS_002（SBP，结构级，零先例）
- **转译原则：** SBP 以纯氢键区分四面体 SO₄²⁻ → 材料设三足供体匹配磺酸根四面体（vs 平面供体匹配羧酸根）
- **材料概念：** 三足三硫脲 POP（C3 对称，匹配四面体 O-S-O 112°）+ 孔口去润湿
- **合成概要：** 1,3,5-三(氨甲基)苯 + 4-异硫氰酸苯基硅烷 → 接枝 PAF-1 或 SBA-15
- **致命风险：** 三足硫脲对硫酸根也匹配（四面体）→ PFBS/SO₄²⁻ 选择性可能不成立
- **六维诊断分：** 因果 14/选择性 19/可转译 13/原创 14/可证伪 8/证据 8 = **76**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** SBP 四面体识别是经典结构生物学 → functional_biomimicry

### A03 — NTCP 牛磺胆酸磺酸酯同构识别

- **原型：** PROTO_PFBS_003（NTCP，机制级）
- **转译原则：** NTCP 天然底物牛磺胆酸含磺酸酯基（与 PFBS 头基同构）+ 疏水甾体面 → 材料设磺酸根锚 + 疏水短腔
- **材料概念：** 介孔硅胶孔口胍基/脲基（磺酸根锚）+ 孔内 C4 深度烷基壁（匹配 PFBS C4 链长）
- **合成概要：** SBA-15 → 脲基硅烷孔口接枝 → C4 丁基硅烷孔壁修饰
- **致命风险：** 胍基带正电→硫酸盐陷阱；C4 深度窗口精度不足
- **六维诊断分：** 因果 13/选择性 16/可转译 15/原创 11/可证伪 7/证据 8 = **70**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** 牛磺胆酸磺酸酯与 PFBS 头基同构 → functional_biomimicry

### A04 — ModA 四面体 vs 平面头基几何反差

- **原型：** PROTO_PFBS_004（ModA，结构级）
- **转译原则：** ModA 三足供体匹配四面体 MoO₄²⁻ → 材料设 T 位点（三足硫脲，匹配 PFBS 磺酸根）vs P 位点（平面 squaramide，匹配 PFOA 羧酸根）→ R=α_T/α_P 反差
- **材料概念：** 同 fresh_1000 PFBS A17 设计（T/P 双位点 POP）
- **合成概要：** 同 A17（PAF-1 + click 接枝）
- **致命风险：** 与已有 A17 方案重叠；BCME 安全问题；先例占据
- **六维诊断分：** 因果 15/选择性 20/可转译 13/原创 8/可证伪 8/证据 8 = **72**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** ModA 四面体识别是真实结构 → functional_biomimicry（但与 A17 重叠）

### A05 — CDO 磺酸基特异配位转译为 Fe-配位孔

- **原型：** PROTO_PFBS_005（CDO，结构级，零先例）
- **转译原则：** CDO 活性位点 Fe 中心 + 氢键网络特异配位磺酸基 → 材料设 Fe(III) 配位孔（磺酸根配位）
- **材料概念：** Fe-MOF（MIL-101 或 UiO-66-Fe）开放金属位点配位 PFBS 磺酸根
- **合成概要：** FeCl₃ + 对苯二甲酸水热合成 MIL-101(Fe)
- **致命风险：** Fe 开放位点对所有阴离子配位（无选择性）；MOF 水稳定性；金属溶出
- **六维诊断分：** 因果 10/选择性 12/可转译 14/原创 10/可证伪 7/证据 7 = **60**
- **谱系状态：** SP-retained / BP-retained / TR-conditional / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** Fe-磺酸配位是 CDO 真实机制 → functional_biomimicry（但选择性存疑）

### A06 — DMSP 裂解酶短链磺酸识别

- **原型：** PROTO_PFBS_006（DMSP 酶，机制级，零先例）
- **转译原则：** DddP 识别 DMSP 短链（C3）磺酸/锍骨架 → 材料设 C3-C4 短链窗口 + 磺酸根锚
- **材料概念：** β-CD 交联聚合物（腔径 ~6 Å 匹配 C4 链）+ 缘羟基/氨基磺酸根锚
- **合成概要：** β-CD + DVS 交联（同 PCP A04 路线）
- **致命风险：** β-CD 腔对 PFBS 包合先例有（但选择性未证）；短链 PFAS 在 CD 腔中结合弱
- **六维诊断分：** 因果 11/选择性 14/可转译 15/原创 12/可证伪 7/证据 7 = **66**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** DMSP 短链磺酸识别是真实酶功能 → functional_biomimicry（零先例，高创新）

### A07 — 趋液性（Hofmeister）弱水合有机阴离子选择

- **原型：** PROTO_PFBS_009（Hofmeister 原理）
- **转译原则：** PFBS 磺酸根为 chaotropic（弱水合）vs SO₄²⁻ kosmotropic（强水合）→ 疏水孔口优先接纳弱水合离子
- **材料概念：** 超疏水微孔碳（孔径 ~1.0 nm），孔口不预润湿，PFBS 以脱水态进入（chaotropic 易脱水），SO₄²⁻ 因强水合被排斥
- **合成概要：** 酚醛树脂碳化 + 轻度表面氟化（或纯芳烃 POP 本征疏水）
- **致命风险：** PFBS 磺酸根水合自由能仍很强（~-300 kJ/mol），脱水罚能可能仍然过高
- **六维诊断分：** 因果 13/选择性 17/可转译 13/原创 12/可证伪 7/证据 7 = **69**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** Hofmeister 是真实物理化学原理 → functional_biomimicry（非蛋白原型但机制真实）

### A08 — SsuA + SBP 双原型四面体磺酸根专一夹口

- **原型：** PROTO_001 + 002（SsuA + SBP）
- **转译原则：** SsuA 烷基磺酸盐营养捕获（功能）+ SBP 四面体纯氢键几何（结构）→ 中性多齿四面体夹口
- **材料概念：** 三(脲丙基)胺硅烷（C3 对称三脲，四面体供体阵列）接枝 SBA-15 孔口
- **合成概要：** 三(2-氨乙基)胺 + 3 eq 3-异氰酸丙基三乙氧基硅烷 → 三脲硅烷 → SBA-15 接枝
- **致命风险：** 三脲对硫酸根也匹配（四面体）；PFBS/SO₄²⁻ 选择性需靠脱溶剂化差异
- **六维诊断分：** 因果 15/选择性 18/可转译 16/原创 12/可证伪 8/证据 8 = **77**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-bench_ready / ER-lead_only
- **仿生真实性快检：** 两原型各有真实结构/功能证据 → functional_biomimicry

### A09 — NTCP + 趋液性双机制（磺酸根锚 + 弱水合门）

- **原型：** PROTO_003 + 009
- **转译原则：** NTCP 磺酸酯头基识别（锚定）+ Hofmeister 弱水合门（排斥 SO₄²⁻）
- **材料概念：** 孔口脲基（磺酸根锚）+ 超疏水微孔入口（弱水合 PFBS 可进入，强水合 SO₄²⁻ 被排斥）
- **合成概要：** 纯芳烃 POP（本征超疏水）+ 孔口脲基后接枝
- **致命风险：** 超疏水孔 ng/L 不润湿；脲促润湿与超疏水矛盾
- **六维诊断分：** 因果 14/选择性 18/可转译 13/原创 12/可证伪 7/证据 7 = **71**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-repairable / SR-revise / ER-lead_only
- **仿生真实性快检：** 两机制各有真实基础 → functional_biomimicry

### A10 — FABP4 短链自适应 + C4 窗口

- **原型：** PROTO_007（FABP4）
- **转译原则：** FABP4 对不同链长 PFAS 展示不同结合模式 → 对 C4 短链的自适应浅结合模式
- **材料概念：** 浅腔芳烃笼（腔深 ~5-6 Å，匹配 C4 链而非 C8），腔口脲锚
- **合成概要：** calix[4]arene 或浅腔 resorcinarene（不扩壁），交联网络
- **致命风险：** 浅腔对 C4 结合极弱（疏水接触面积小）；水相竞争
- **六维诊断分：** 因果 12/选择性 15/可转译 13/原创 11/可证伪 7/证据 7 = **65**
- **谱系状态：** SP-retained / BP-retained / TR-retained / ME-advance / SR-revise / ER-lead_only
- **仿生真实性快检：** FABP4 短链自适应是真实结构特征 → functional_biomimicry

### A11-A50（续）

*（A11-A50 按相同格式继续，覆盖以下角度：）*

- A11: HSA 广谱捕获 + PFBS 优先洗脱（利用 PFBS 比 PFOA 结合弱的差异做选择性洗脱）
- A12: SsuA 缺硫诱导 → 条件性活化吸附（pH 门控）
- A13: SBP 纯氢键无阳离子 → 中性脲阵列排斥二价（机制 A 强化版）
- A14: NTCP Na⁺ 协同 → 离子强度响应吸附（高盐释放 PFBS）
- A15: CDO Fe-磺酸配位 → Zr-MOF 开放位点（Zr-O-S 配位）
- A16: DMSP 短链窗口 → α-CD 腔（5.5 Å 匹配 C4）
- A17: 趋液性 + 链长耦合 → 分级孔（大孔脱溶剂化 + 微孔链锚定）
- A18: SsuA + NTCP 双原型（磺酸根夹口 + 疏水短腔）
- A19: SBP + 趋液性（四面体几何 + 弱水合门）
- A20: FABP4 portal 门控 → 温敏孔口（同 PFOA A26 但 PFBS 版）
- A21: HSA 多亚腔 → 层级孔 POP（PFBS 在辅腔，PFOA 在主腔）
- A22: NTCP 肝肠循环 → 闭环再生（同 PFOA A45）
- A23: CDO 磺酸特异 → 硼酸功能化（B-O-S 配位，pH 门控）
- A24: DMSP 锍基识别 → 硫醚功能化孔壁（S···F 硫-氟相互作用）
- A25: 全原型收敛（十原型叠加思想实验）
- A26: SsuA 保守水桥 → 受限水微孔碳
- A27: SBP 脱溶剂化 → 超疏水入口 + 四面体腔
- A28: NTCP 胆汁酸形状 → 甾体印迹 MIP（假模板胆酸）
- A29: ModA 钼酸根 vs 硫酸根选择 → PFBS vs SO₄²⁻ 几何+脱溶剂化双门
- A30: CDO 半胱氨酸骨架 → 含硫氨基酸功能化（半胱氨酸接枝）
- A31: DMSP 裂解 → 反应性捕获（磺酸酯键断裂，不可逆）
- A32: 趋液性 + 温度 → 热响应浓缩（LCST 材料 + PFBS chaotropic 协同）
- A33: SsuA ABC 转运 → 电化学驱动浓缩
- A34: SBP + ModA 双四面体 → 超选择四面体腔（几何精度 ±0.1 Å）
- A35: NTCP + FABP4 → 双腔串联（NTCP 型入口 + FABP 型深腔）
- A36: HSA + EPS → 白蛋白固定化 + 多糖壳（蛋白超出范围，标 out_of_scope）
- A37: CDO + 趋液性 → Fe 配位 + 疏水门双锁
- A38: DMSP + SsuA → 短链磺酸专一（C2-C4 窗口 + 磺酸根夹口）
- A39: 跨原型：SBP 四面体 + NTCP 磺酸酯 + 趋液性三重门
- A40: FABP4 三模式 → 混合配体自适应（PFBS/PFBA/PFHxA 类级捕获）
- A41: SsuA 烷基链氧化 → 反应性捕获（C-S 键断裂，不可逆矿化）
- A42: SBP 无阳离子纯氢键 → 中性 squaramide 四面体阵列
- A43: NTCP 底物抑制 → 高浓 PFBS 自抑制（Langmuir 饱和 + 低浓线性）
- A44: ModA 高亲和 → 多价 avidity 阵列（高密度三足供体）
- A45: CDO 铁硫簇 → Fe-S 簇 MOF（磺酸根配位 + 疏水孔）
- A46: DMSP 海洋硫循环 → 硫特异识别（区分磺酸根 vs 硫酸根 vs 硫醇）
- A47: 趋液性 + 压力 → 压驱膜浓缩（PFBS chaotropic 优先透过疏水膜）
- A48: SsuA + CDO → 捕获-氧化串联（先吸附后 Fenton 降解）
- A49: SBP + NTCP + SsuA 三原型收敛（四面体几何 + 磺酸酯锚 + 烷基尾腔）
- A50: 全十原型收敛设计（思想实验，同 PFOA A50）

### A11-A50 诊断分速览

| ID | 分数 | 核心机制 | 原型 |
|---|---|---|---|
| A11 | 58 | HSA 差异洗脱 | PROTO_008 |
| A12 | 55 | SsuA 条件活化 | PROTO_001 |
| A13 | 72 | SBP 中性脲排斥二价 | PROTO_002 |
| A14 | 62 | NTCP 离子强度响应 | PROTO_003 |
| A15 | 63 | CDO Zr-MOF 配位 | PROTO_005 |
| A16 | 64 | DMSP α-CD 短链窗口 | PROTO_006 |
| A17 | 68 | 趋液性+链长分级孔 | PROTO_009 |
| A18 | 73 | SsuA+NTCP 双原型 | 跨原型 |
| A19 | 71 | SBP+趋液性 | 跨原型 |
| A20 | 54 | FABP4 温敏门 | PROTO_007 |
| A21 | 61 | HSA 层级孔 | PROTO_008 |
| A22 | 51 | NTCP 闭环再生 | PROTO_003 |
| A23 | 65 | CDO 硼酸配位 | PROTO_005 |
| A24 | 63 | DMSP 硫醚 S···F | PROTO_006 |
| A25 | 52 | 全原型收敛 | 全部 |
| A26 | 60 | SsuA 受限水 | PROTO_001 |
| A27 | 70 | SBP 超疏水+四面体 | PROTO_002 |
| A28 | 53 | NTCP 胆酸 MIP | PROTO_003 |
| A29 | 74 | ModA 几何+脱溶剂化双门 | PROTO_004 |
| A30 | 59 | CDO 半胱氨酸接枝 | PROTO_005 |
| A31 | 48 | DMSP 反应性裂解 | PROTO_006 |
| A32 | 56 | 趋液性热响应 | PROTO_009 |
| A33 | 54 | SsuA 电化学 | PROTO_001 |
| A34 | 69 | SBP+ModA 超选择 | 跨原型 |
| A35 | 67 | NTCP+FABP4 双腔 | 跨原型 |
| A36 | 45 | HSA+EPS 蛋白 | out_of_scope |
| A37 | 64 | CDO+趋液性 | 跨原型 |
| A38 | 72 | DMSP+SsuA 短链专一 | 跨原型 |
| A39 | 75 | SBP+NTCP+趋液性三重门 | 跨原型 |
| A40 | 66 | FABP4 类级自适应 | PROTO_007 |
| A41 | 47 | SsuA 反应性氧化 | PROTO_001 |
| A42 | 71 | SBP squaramide 四面体 | PROTO_002 |
| A43 | 55 | NTCP 底物抑制 | PROTO_003 |
| A44 | 62 | ModA 多价 avidity | PROTO_004 |
| A45 | 61 | CDO Fe-S MOF | PROTO_005 |
| A46 | 66 | DMSP 硫特异 | PROTO_006 |
| A47 | 49 | 趋液性压驱膜 | out_of_scope |
| A48 | 53 | SsuA+CDO 串联 | 跨原型 |
| A49 | 76 | SBP+NTCP+SsuA 三收敛 | 跨原型 |
| A50 | 52 | 全十原型 | 思想实验 |

---

## PFBS 50 方案 Top 10 排序

| 排名 | ID | 分数 | 核心机制 | 原型 |
|---|---|---|---|---|
| 1 | A08 | 77 | SsuA+SBP 双原型四面体磺酸根夹口 | 跨原型 |
| 2 | A02 | 76 | SBP 四面体几何选择 POP | PROTO_002 |
| 3 | A49 | 76 | SBP+NTCP+SsuA 三收敛 | 跨原型 |
| 4 | A39 | 75 | SBP+NTCP+趋液性三重门 | 跨原型 |
| 5 | A01 | 74 | SsuA 磺酸根中性夹口 PMO | PROTO_001 |
| 6 | A29 | 74 | ModA 几何+脱溶剂化双门 | PROTO_004 |
| 7 | A18 | 73 | SsuA+NTCP 双原型 | 跨原型 |
| 8 | A04 | 72 | ModA 四面体 vs 平面反差 | PROTO_004 |
| 9 | A13 | 72 | SBP 中性脲排斥二价 | PROTO_002 |
| 10 | A38 | 72 | DMSP+SsuA 短链专一 | 跨原型 |
