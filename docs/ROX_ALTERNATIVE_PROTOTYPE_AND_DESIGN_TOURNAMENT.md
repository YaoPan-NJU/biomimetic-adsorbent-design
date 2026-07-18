# ROX替代仿生原型与设计路线同门比较

日期：2026-07-18
状态：开放式深检索完成一轮；不设固定方案数量
目的：防止“先找到生物膜证据，所以最后只能做生物膜＋印迹”的路径依赖

## 1. 共同问题冻结

目标不是在纯水中证明ROX可以被某种材料吸附，而是在市政二级出水中同时实现：

- 对约0.1–1.0 μg/L ROX的可测、快速去除或富集；
- 相对ERY、CLA、AZI的非单调判别；
- DOM、盐和真实水中仍可解释的机制；
- 非蛋白、可合成、可回收和可再生的材料实体。

ROX、ERY和CLA的主要热力学碱性pKa都约8.8，AZI还具有第二个碱性中心。任何只依靠负电、疏水或酸性陷获的路线都必须先解释为什么不会同时偏好CLA或AZI。

## 2. 新发现的真实ROX原型

### 2.1 吞噬细胞酸性区室富集

^14C直接实验显示，ROX在巨噬细胞和中性粒细胞中的胞内/胞外浓度比为14–190；巨噬细胞中约一半回收药物定位于溶酶体，中性粒细胞中约三分之一定位于嗜天青颗粒。摄取可逆、受外液酸化抑制，并在人体肺泡细胞中有体内分布证据。

这比普通生物膜故事更直接：目标物本身、数量级富集、亚细胞位置和动态边界都存在。可转译物理原理是“少量中性ROX跨越低极性界面，进入酸性区室后质子化，反向通量降低”。

但该原型不是ROX专一识别。不同细胞体系中ROX可高于ERY或CLA，AZI通常因二碱性结构获得更强酸性区室积累。它解决的是弱碱性大环内酯富集，不自动解决ROX判别。

核心来源：

- Carlier MB, et al. *Cellular uptake and subcellular distribution of roxithromycin and erythromycin in phagocytic cells*. J Antimicrob Chemother (1987). https://doi.org/10.1093/jac/20.suppl_b.47
- Hand WL, et al. *Entry of roxithromycin into human polymorphonuclear leukocytes*. AAC (1987). https://doi.org/10.1128/AAC.31.10.1553
- Chastre J, et al. *Pulmonary disposition of roxithromycin*. AAC (1987). https://doi.org/10.1128/AAC.31.9.1312
- Ishiguro M, et al. *Penetration of macrolides into human polymorphonuclear leucocytes*. J Antimicrob Chemother (1989). https://doi.org/10.1093/jac/24.5.719

### 2.2 阴离子磷脂界面分配

ROX可直接结合含磷脂酰肌醇脂质体。构象分析指向糖基进入疏水域、宏环靠近界面的取向；总体响应为ERY≤ROX<红霉胺≤AZI。它提供了无需蛋白的膜界面映射，却同样反证了ROX专一性。

来源：Mingeot-Leclercq et al. *Interactions of macrolide antibiotics with phospholipids*. Toxicol Appl Pharmacol (1999). https://doi.org/10.1006/taap.1999.8632

### 2.3 其他原型的否决

- 植物根系可富集ROX，但细胞壁、膜、液泡和代谢贡献未分开，不具可转译因果链。
- 微藻体系中ROX生物吸附/累积贡献较小，后期以降解为主。
- MacAB-TolC可直接转运ROX，但它是多种大环内酯的多特异主动外排泵；复制蛋白机械传递既超出非蛋白材料范围，也不能提供ROX专一性。
- P-gp、Ca²⁺相关摄取和其他细胞转运证据互相交织，不能冻结成ROX特异转运位点。

## 3. 非印迹人工识别检索裁决

| 路线 | ROX直接证据 | 近邻比较 | 当前处置 |
|---|---|---|---|
| β-CD/HP-β-CD | 有制剂复合/载药证据 | 无可信水相Ka、包合方向和ERY/CLA/AZI比较 | 仅可溶筛选 |
| γ-CD及衍生物 | 未找到可靠ROX湿实验 | 无 | lead_only |
| CB[n] | 无完整ROX直接水相数据 | 预计读取共有质子化去糖胺 | 终止主路线 |
| calixarene/pillararene | 无ROX直接数据 | 主要是电荷/疏水类别识别 | 终止主路线 |
| Cu/Zn配位 | 比较在甲醇；ROX不优于CLA/AZI | 反向 | 终止主路线 |
| 单脲/硫脲/酰胺 | 无ROX水相删除体证据 | 无 | 终止主路线 |
| ROX印迹 | 有结合和选择透过先例 | 已报道有限但可测 | 保留人工选择模块 |

## 4. 路线同门比较

### 路线A：生物膜功能启发＋表面印迹吸附微球

状态：`concept_valid`。
优势：严格保留“吸附材料”范围；真实生物膜在1 μg/L下直接吸附ROX；表面印迹已有制造先例；批量和固定床验证直观。
弱点：仿生原型只提供类别富集；当前pSBMA锚定、质量账本、空间对照和同位素模板分析未关闭；ROX-MIP先例拥挤。
处置：保留，但不得默认获胜。见`rounds/rox_bf1_deep_design_1/`。

### 路线B：溶酶体启发的酸性囊泡/微胶囊

状态：`E0_mechanism_probe / terminated_as_ROX_selective_adsorbent`。
优势：仿生故事最强；理论酸性区室富集可达约10^3量级；动态对照清楚。
否决：ROX、ERY和CLA相近pKa使平衡富集比主要由pH差决定；AZI很可能更强；梯度稳定与837 Da ROX快速穿膜互相冲突；固定床形态不佳。
处置：只保留2×2脂质体机制探针，不分配完整材料资源。见`rounds/rox_lys1_probe/`。

### 路线C：溶酶体启发的“选择通透—酸性锁定”膜

状态：`lead_only / scope_and_water_gate_required`。
核心：ROX印迹薄层先选择性促进ROX跨膜，酸性接收相再把进入的ROX质子化并维持汇条件；对应吞噬细胞的膜进入—酸性区室锁定串联，而不是单独表面吸附。

这一路线有一个关键直接先例：2009年ROX印迹复合膜在乙醇体系中报告2.24 μmol/g结合容量，并给出ROX相对ERY、AZI和红霉素琥乙酯约1.75、2.46、2.67的选择因子，同时将传输解释为促进渗透。它证明“ROX印迹可以成为选择通透层”，但完全没有证明中性水、DOM或二级出水中的行为。

来源：Yu JY, et al. *Synthesis and Properties of Molecularly Imprinted Composite Membranes of Roxithromycin*. Advanced Materials Research 87–88 (2009) 80–85. https://doi.org/10.4028/www.scientific.net/AMR.87-88.80

最小2×2机制门：

| 组别 | ROX印迹 | feed/receiver pH梯度 |
|---|---:|---:|
| M00 | NIP | 无 |
| M10 | MIP | 无 |
| M01 | NIP | pH 7.5→4.5 |
| M11 | MIP | pH 7.5→4.5 |

另设ERY同源替代模板膜。ROX、ERY、CLA、AZI按同一nmol/L进入feed；同时测feed下降、膜吸附、receiver累积和总质量平衡。只有MIP×梯度交互显著、ROX通量和receiver富集均优于三种近邻，才能说明“选择通透—酸性锁定”成立。

继续阈值：

- 水相M11的ROX/ERY与ROX/CLA通量选择性≥1.5，ROX/AZI≥1.2；
- M11的ROX接收相累积至少是M10、M01中较大者的1.5倍；
- 交互项95%置信区间下限>0；
- 6 h质量平衡80–120%，膜不可只通过不可逆吸附制造feed下降；
- 5 mg-C/L DOM下ROX通量保留≥70%；
- ROX-d7/d0模板泄漏低于分析阈值。

停止项：出现目标迟滞而非促进传输；CLA或AZI持续高于ROX；接收相不富集；只能在乙醇中工作；膜位点很快饱和；酸接收相反向污染feed。

工程出口不是普通吸附柱，而是中空纤维或平板膜接触器，酸性接收液循环浓缩。因此它可能形成更强论文，但属于“仿生选择性分离材料”而不再是纯吸附材料。只有潘尧允许这一范围扩展，才值得冻结完整SOP。

### 路线D：阴离子磷脂界面仿生两亲材料

状态：`control_only`。
原因：ROX直接膜结合证据强，材料映射清楚，但原始顺序预测AZI高于ROX。适合作为类别富集/膜分配对照，不适合ROX主方案。

### 路线E：单独CD/大环主体或双主体材料

状态：`lead_only`，未达到材料设计。
仅当可溶主体面板在纯水中同时达到`Ka_ROX/Ka_ERY≥2`、`Ka_ROX/Ka_CLA≥2`和`Ka_ROX/Ka_AZI≥1.5`，并用NMR定位ROX进入区域，才允许材料化。当前没有这样的证据。

## 5. 当前排序

这里不按概念漂亮程度，而按“论文故事＋效果机会＋机制可拆分＋工程范围”排序：

1. **路线A**：仍是严格吸附范围内最接近实验的路线，但必须重新设计，当前不是E1。
2. **路线C**：科学上可能优于A，故事和机制更强；但需要水相促进传输门，并涉及从吸附材料扩展到膜分离材料。
3. **路线B**：强生物故事、弱ROX选择性，终止为主方案。
4. **路线D**：可作机制对照。
5. **路线E**：缺直接选择性证据，暂不材料化。

## 6. 决策

本轮没有保护候选A，也没有因为溶酶体故事更漂亮就忽略选择性反证。当前最负责任的推进是：

- 严格吸附主线：重构路线A，去掉无证据的天然空间梯度和未锚定pSBMA，优先解决ROX模板空腔水相保真度及同源模板双差异；
- 高上限旁路：保留路线C的最小平板膜2×2门，但在用户确认是否允许“选择性膜分离材料”后才扩展为完整材料；
- 路线B/D/E全部保留证据和否决理由，不再消耗完整SOP资源。
