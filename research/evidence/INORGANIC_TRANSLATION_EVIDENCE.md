# 磷酸盐/PstS-PBP 与硝酸盐/NrtA 的生物机制到可合成材料证据

> 检索日期：2026-07-17  
> 用途：下一轮仿生硬对应门禁，不用于材料性能预测。

## 1. 证据等级

- **直接支持（D）**：来源直接研究对应蛋白、目标阴离子、固定化方式或明确的合成材料行为。
- **邻近先例（A）**：来源证明某个材料构件、表征方法或释放策略可实施，但没有复制目标蛋白的完整机制。
- **设计假说（H）**：由直接证据和邻近先例组合得到的待验证映射。假说不能作为已证实性能或硬对应证据。

## 2. 门禁结论

### 2.1 磷酸盐/PstS-PBP

**生物静态对应可以通过，生物动态对应可以通过，材料动态对应仍需实验。** E. coli PBP 的同一 T141D 变体已有无配体结构 1OIB 和磷酸根结合结构 1IXG，可进行直接 apo/bound 结构比较；野生型和同家族结构又给出完整脱水、12至14个氢键及关键酸性残基/偶极作用的直接依据。[P1][P2] 荧光标记 PBP 的动力学表明先结合、后闭合的两步过程，PiBP-FRET 和固定化 PBP 进一步证明蛋白工程及表面固定可行。[P3][P4]

门禁不能把蛋白级选择性直接转写为人工凝胶选择性。水相胍基分子夹、双核 Zn 受体和可按需释放的聚胺水凝胶仅证明“多点口袋、金属协同和温和释放”能够分别实现，尚没有一个来源把三者组合成 PstS 式双叶材料，也没有来源证明该组合在硫酸盐、碳酸氢根和 DOM 同时存在时保持蛋白级选择性。[P5][P6][P7][M1]

### 2.2 硝酸盐/NrtA

**生物静态对应可以通过；实验性 apo/bound 动态对应暂不通过。** NrtA 的 1.5 Å 硝酸根结合结构 2G29 直接支持双结构域 C-clamp 和被埋藏的硝酸根口袋，但没有配对的实验 apo 结构。[N1] 2022 年工作用 ITC、突变和分子动力学确认 K269 锚定位点、硝酸根/亚硝酸根共享口袋及结合后的构象总体重排；其中 apo 轨迹由结合态晶体结构去除配体后平衡得到，不能替代 apo 晶体、NMR、SAXS 或单分子 FRET 证据。[N2]

三脲受体和电再生季铵盐电极分别证明平面硝酸根受体及按需电释放可合成，但前者的选择性实验在含有机溶剂体系中，后者是普通离子交换而非 NrtA 几何识别。[N3][N4] 因此，当前可以提出 NrtA 启发的静态口袋；若要把“硝酸根诱导 C-clamp 闭合”列为动态硬对应，必须新增直接的蛋白或材料开闭测量。

## 3. 核心证据组

### [P1] E. coli PBP 的 apo/bound 结构对

- **来源**：
  - N. Yao, P. S. Ledvina, A. Choudhary, F. A. Quiocho. *Modulation of a salt link does not affect binding of phosphate to its specific active transport receptor.* **Biochemistry**, 1996. [DOI: 10.1021/bi952686r](https://doi.org/10.1021/bi952686r); apo T141D 结构 [PDB 1OIB](https://www.rcsb.org/structure/1OIB)。
  - Z. Wang, H. Luecke, N. Yao, F. A. Quiocho. *A low energy short hydrogen bond in very high resolution structures of protein receptor-phosphate complexes.* **Nature Structural Biology**, 1997. [DOI: 10.1038/nsb0797-519](https://doi.org/10.1038/nsb0797-519); phosphate-bound T141D 结构 [PDB 1IXG](https://www.rcsb.org/structure/1IXG)。
- **定位**：RCSB 结构条目标题、配体清单和 primary citation；1OIB 无磷酸根配体，1IXG 含 PO4。
- **等级**：**D**。
- **直接支持**：同一 PBP T141D 变体存在无配体和磷酸根结合结构，可对两结构域相对运动和口袋封闭程度做定量比较。
- **适用边界**：结构对是 T141D 变体，且来自不同晶体研究；未经实际结构叠合不得预报闭合角度，也不得把变体运动幅度无条件外推到 PstS/PBP-1 或人工材料。

### [P2] 关键口袋作用不是单纯正电吸附

- **来源**：Hartmut Luecke, Florante A. Quiocho. *High specificity of a phosphate transport protein determined by hydrogen bonds.* **Nature**, 1990. [DOI: 10.1038/347402a0](https://doi.org/10.1038/347402a0)。补充结构边界见 P1 的 Yao et al. 1996。
- **定位**：Nature 论文结构结果；Yao et al. 摘要和 RCSB primary-citation abstract。
- **等级**：**D**。
- **直接支持**：配体在 E. coli PBP 中完全脱水并被埋藏，形成 12 个氢键；Arg135 盐桥存在，但改变邻近盐桥未显著改变亲和力，说明局部氢键和偶极作用是主要贡献。Asp56 参与识别质子化磷酸根。
- **适用边界**：残基编号和氢键数属于具体蛋白；不能据此直接指定人工材料单体比例或推定对硫酸根/砷酸根的选择性倍数。
- **材料约束**：若人工口袋只有季铵正电位点而无定向氢键和脱水微环境，不足以称为 PstS/PBP 静态硬对应。

### [P3] 位点工程和开闭动力学可被荧光直接读取

- **来源**：Martin Brune, Jackie L. Hunter, Steven A. Howell, Stephen R. Martin, Theodore L. Hazlett, John E. T. Corrie, Martin R. Webb. *Mechanism of Inorganic Phosphate Interaction with Phosphate Binding Protein from Escherichia coli.* **Biochemistry**, 1998. [DOI: 10.1021/bi9804277](https://doi.org/10.1021/bi9804277)。
- **定位**：摘要；A197C-MDCC 标记、稳态/时间分辨荧光和动力学模型。
- **等级**：**D**。
- **直接支持**：A197C 位点可特异连接香豆素探针；高浓度磷酸根下速率饱和支持“先结合、后伴随结合裂隙闭合的构象变化”两步模型。
- **适用边界**：荧光变化来自标记蛋白局部环境，不等同于测得两个结构域的绝对距离；人工材料需要第二种结构测量排除局部极性变化。

### [P4] FRET 与表面固定化均有直接先例

- **来源 A**：Hong Gu et al. *A novel analytical method for in vivo phosphate tracking.* **FEBS Letters**, 2006. [DOI: 10.1016/j.febslet.2006.09.048](https://doi.org/10.1016/j.febslet.2006.09.048)。
- **定位 A**：摘要；Synechococcus PiBP 与 eCFP/Venus 融合，纯化探针对磷酸根产生 FRET 变化。
- **来源 B**：Izumi Kubo. *Potentiometric phosphate-sensing system utilizing phosphate-binding protein.* **Analytical and Bioanalytical Chemistry**, 2002. [DOI: 10.1007/s00216-001-1138-1](https://doi.org/10.1007/s00216-001-1138-1)。
- **定位 B**：摘要；PBP 交联固定在硝酸纤维素膜并获得磷酸根选择性电位响应。
- **等级**：两者均为 **D**。
- **直接支持**：PBP/PiBP 能接受荧光蛋白融合或膜上交联固定而保留可检测的磷酸根响应。
- **适用边界**：两项工作是传感，不是批量吸附；没有证明固定化后位点密度、循环释放、二级出水稳定性或蛋白酶耐受性。

### [P5] 水相胍基分子夹可合成，但选择性证据不等同于正磷酸盐吸附

- **来源**：Hannes Y. Kuchelmeister, Carsten Schmuck. *Nucleotide recognition in water by a guanidinium-based artificial tweezer receptor.* **Chemistry – A European Journal**, 2011. [DOI: 10.1002/chem.201003393](https://doi.org/10.1002/chem.201003393)。
- **定位**：摘要；两条对称肽臂、芳香支架和胍基头基的合成，以及中性缓冲水中 1:1 配合。
- **等级**：**A**。
- **邻近先例**：证明含胍基和肽臂的水溶性人工夹可以合成，并能在中性缓冲水中结合磷酸根/核苷酸。
- **适用边界**：核苷酸结合还包含碱基的 π–π 作用；该来源没有证明正磷酸盐相对硫酸盐、碳酸氢根和 DOM 的选择性，也没有材料循环数据。

### [P6] 双核 Zn 距离可调的水相磷酸根受体

- **来源**：Gianluca Ambrosi et al. *Phosphates Sensing: Two Polyamino-Phenolic Zinc Receptors Able to Discriminate and Signal Phosphates in Water.* **Inorganic Chemistry**, 2009. [DOI: 10.1021/ic900231h](https://doi.org/10.1021/ic900231h)。
- **定位**：摘要；两个双核 Zn(II) 受体以不同 Zn–Zn 距离在 pH 6–10 水溶液中区分 Pi 与 PPi。
- **等级**：**A**。
- **邻近先例**：证明金属中心间距和桥联几何可以转化为水相磷酸根形状识别，并可用光学信号读取。
- **适用边界**：该体系是分子传感器，不是吸附材料；未覆盖金属泄漏、硫酸盐/DOM 竞争和多次再生。不能把 Zn–Zn 桥联自动称为 PstS 模拟。

### [P7] 可按需温和释放的磷酸盐水凝胶

- **来源**：Jiangfeng Xu, Kirill Efimenko, Christopher B. Gorman, Yaroslava G. Yingling, Lisa Castellano, Jan Genzer. *Functional Hydrogels for Selective Phosphate Removal from Water and Release on Demand.* **Langmuir**, 2025. [DOI: 10.1021/acs.langmuir.5c00679](https://doi.org/10.1021/acs.langmuir.5c00679)。
- **定位**：摘要；PEI/PMVEMA 水凝胶、pH 条件、硝酸根竞争和低浓度 NaOH 解吸。
- **等级**：**D**，仅对该水凝胶行为。
- **直接支持**：聚胺/聚酸水凝胶可在水中捕获磷酸盐，并在低于 0.001 M NaOH 条件下释放；捕获/释放可通过 pH 调节实现。
- **适用边界**：该材料不是 PstS 双叶口袋；摘要只明确硝酸根竞争，不能外推到硫酸盐、碳酸氢根、砷酸根或 DOM；其数值不能作为新材料预测值。

### [N1] NrtA 只有硝酸根结合晶体结构

- **来源**：Nicholas M. Koropatkin, Himadri B. Pakrasi, Thomas J. Smith. *Atomic structure of a nitrate-binding protein crucial for photosynthetic productivity.* **PNAS**, 2006. [DOI: 10.1073/pnas.0602517103](https://doi.org/10.1073/pnas.0602517103); [PDB 2G29](https://www.rcsb.org/structure/2G29)。
- **定位**：1.5 Å 晶体结构和 Results；硝酸根位于两个结构域之间的 C-clamp 裂隙。
- **等级**：**D**。
- **直接支持**：NrtA 是双结构域 C-clamp，硝酸根被结合裂隙包围；C 端扩展可能稳定口袋或参与转运相关构象变化。
- **适用边界**：2G29 是硝酸根结合态，没有实验 apo 配对结构；“可能参与构象变化”是原论文推测，不能称为直接闭合证据。

### [N2] NrtA 关键残基、突变、热力学和构象重排

- **来源**：Ke Ji, Kiheon Baek, Weicheng Peng, Kevin A. Alberto, Hedieh Torabifard, Steven O. Nielsen, Sheel C. Dodani. *Biophysical and in silico characterization of NrtA: a protein-based host for aqueous nitrate and nitrite recognition.* **Chemical Communications**, 2022. [DOI: 10.1039/D1CC05879G](https://doi.org/10.1039/D1CC05879G)。
- **定位**：正文 Results、Figure 1–2、Table 1。
- **等级**：ITC、差示扫描荧光和 K269A 为 **D**；apo/bound 构象比较为 **A/H**，因为来自 MD。
- **直接支持**：K269 为锚定位点，Q155、H196、G240 提供额外氢键，L71、W102、L124、P222、V239 构成低极性口袋环境。K269A 失去硝酸根和亚硝酸根引起的浓度依赖热稳定化。20 °C、HEPES/50 mM NaCl 中 ITC 显示两种阴离子均为 1:1 结合，且硝酸根亲和强于亚硝酸根。
- **邻近支持**：MD 中 apo NrtA 采样更宽构象分布，阴离子结合降低口袋附近协同运动并改变溶剂可及表面积；Q155 离开口袋而 T190 补充氢键。
- **适用边界**：apo、硝酸根和亚硝酸根轨迹均从硝酸根结合晶体结构出发；MD 不是实验 apo 结构。结果也明确说明 NrtA 同时结合硝酸根和亚硝酸根，不能宣称绝对硝酸根专一。
- **材料约束**：K269 类锚定位点可作为删位对照；Q155/T190 的水介导重排提示人工口袋不能被设计成完全无水、刚性三点受体而不做水合验证。

### [N3] 三脲平面受体是可合成先例，但不在纯水中

- **来源**：Michelle M. Watt, Lev N. Zakharov, Michael M. Haley, Darren W. Johnson. *Selective Nitrate Binding in Competitive Hydrogen Bonding Solvents: Do Anion–π Interactions Facilitate Nitrate Selectivity?* **Angewandte Chemie International Edition**, 2013. [DOI: 10.1002/anie.201303881](https://doi.org/10.1002/anie.201303881)。
- **定位**：摘要、NMR 滴定和晶体/模型讨论；三脚架脲受体、平面硝酸根及氟化芳环。
- **等级**：**A**。
- **邻近先例**：三脚架脲可以围绕平面硝酸根形成氢键；氟化受体在 10% DMSO-d6/CDCl3 中表现出相对卤离子的硝酸根偏好，作者提出阴离子–π 作用解释。
- **适用边界**：实验不是纯水，也不是二级出水；阴离子–π 是提出的机制，不能直接转写为水相吸附选择性。脲位点在水中会受到强溶剂竞争。

### [N4] 电势触发硝酸根释放有直接材料先例

- **来源**：James W. Palko, Diego I. Oyarzun, Byunghang Ha, Michael Stadermann, Juan G. Santiago. *Nitrate removal from water using electrostatic regeneration of functionalized adsorbent.* **Chemical Engineering Journal**, 2018. [DOI: 10.1016/j.cej.2017.10.161](https://doi.org/10.1016/j.cej.2017.10.161)。
- **定位**：摘要、Highlights 和 Conclusions；CTAB 季铵盐功能化活性炭电极及电再生。
- **等级**：**D**，仅对电再生材料行为。
- **直接支持**：季铵盐活性炭可被动离子交换吸附硝酸根，并通过施加电势释放，无需化学再生剂。
- **适用边界**：选择性来自普通离子交换，不是 NrtA 形状识别；12 次循环后可访问容量仅为初始值的一部分，说明“可电释放”不等于“高循环保持”。不能把其容量或循环结果移植到新材料。

### [M1] 二级出水必须使用的代表性竞争矩阵

- **来源**：S. K. Zheng, J. J. Chen, X. M. Jiang, X. F. Li. *A comprehensive assessment on commercially available standard anion resins for tertiary treatment of municipal wastewater.* **Chemical Engineering Journal**, 2011. [DOI: 10.1016/j.cej.2011.03.005](https://doi.org/10.1016/j.cej.2011.03.005)。
- **定位**：摘要和实际二级出水柱实验；代表性水样含 67 mg/L 硫酸盐、1.30 mg P/L、8.50 mg/L 硝酸盐和 3.30 mg/L DOM。
- **等级**：**D**，仅对该水样和实验。
- **直接支持**：真实二级出水同时存在高背景硫酸盐、营养盐和 DOM，且需要动态柱和再生实验评价。
- **适用边界**：单个工艺水样不代表所有污水厂。数值用于建立一个代表性压力测试，不得当作本地水样组成。

## 4. 从证据可直接导出的实现约束

| 约束 | 证据级别 | 可执行含义 | 不允许的外推 |
|---|---|---|---|
| PstS/PBP 静态口袋必须包含定向多点氢键和受限水合环境 | D，[P1][P2] | 人工材料至少设置“随机正电位点”与“预组织多点位点”对照 | 不能预报人工口袋复制蛋白选择性倍数 |
| PstS/PBP 动态闭合可用位点荧光或 FRET 读取 | D，[P3][P4] | 在两个叶片或盖片上布置供受体，并以锁开材料为因果对照 | 单一荧光强度变化不能独立证明几何闭合 |
| PBP 可交联固定 | D，[P4] | 允许把蛋白固定化作为机制验证样品或正对照 | 不能据传感结果推定吸附容量和循环寿命 |
| 胍基夹和双核金属间距可在水相实现磷酸根识别 | A，[P5][P6] | 可并行筛查“纯有机多点夹”与“金属协同夹” | 不得把核苷酸或 PPi 选择性当作正磷酸盐/硫酸盐选择性 |
| 温和碱触发磷酸盐释放可实现 | D/A，[P7] | 可把低浓度碱再生列为邻近工艺窗口 | 不得预设 PstS 式夹体在相同条件下释放 |
| NrtA 静态口袋需要 K269 类锚点和多点氢键/低极性协同 | D，[N1][N2] | K269 类位点删除必须进入因果对照；硝酸根和亚硝酸根必须同时测试 | 不能宣称 NrtA 完全排斥亚硝酸根 |
| NrtA 实验 apo–bound 闭合仍缺失 | D/H，[N1][N2] | 动态硬对应必须新增实验结构信号 | MD 不能替代 apo 结构、FRET 或 SAXS |
| 三脲平面夹可合成 | A，[N3] | 可作为小分子/聚合物位点化学的候选起点 | 有机溶剂选择性不能外推到二级出水 |
| 硝酸根可通过电势按需释放 | D/A，[N4] | 电导骨架和电触发再生可作为独立工程模块 | 电再生不证明 NrtA 仿生，也不保证循环保持 |

## 5. 动态测量的证据边界

1. **PBP/PstS 优先测量**：P3 直接支持位点特异荧光动力学，P4 直接支持 PiBP-FRET。材料阶段应采用“FRET/位点荧光 + 吸附量”同步测量，并用锁开、半口袋和随机位点对照。
2. **NrtA 优先测量**：N2 直接支持 ITC、差示扫描荧光和突变验证，但构象证据来自 MD。需要新增双位点 FRET、溶液 SAXS 或等价实验，证明目标结合确实改变两个结构域/材料叶片间距。
3. **QCM-D 的角色**：当前核心来源没有直接的 PstS/NrtA-QCM-D 开闭实验。QCM-D 可作为表面结合、释放和水合层变化的邻近测量，但信号包含耦合水，不能单独证明闭合；这一用途属于 **H**。
4. **SAXS 的角色**：当前 NrtA 来源没有实验 SAXS；用 apo/target-bound SAXS 提取整体尺寸或距离分布属于 **H**，应与 FRET 和突变/锁开对照联合。

## 6. 可逆释放的证据边界

- PBP/PstS 的生理释放涉及与转运组件相互作用，检索到的结构和荧光文献没有给出可直接移植到吸附材料的再生条件。任何 pH、盐、竞争配体或电触发释放均为材料设计变量，不是生物事实。
- P7 直接证明特定 PEI/PMVEMA 水凝胶可用低浓度 NaOH 释放磷酸盐；只可作为磷酸盐材料的邻近再生窗口。
- N4 直接证明特定季铵盐电极可电势触发硝酸根释放；只可作为导电材料模块的邻近先例。
- “闭合增强选择性、开态促进释放”仍为 **H**。需要同时测定构象信号、解吸速率和循环结构恢复，不能只测末端去除率。

## 7. 复杂水基质的最低验证矩阵

基于 M1，后续材料门禁至少包括：

- 超纯水中的目标阴离子单组分结合；
- `SO4²⁻/HCO3⁻/Cl⁻` 逐一竞争和混合竞争；
- 磷酸盐体系加入硝酸根、砷酸根作为结构近邻或机制对照；
- 硝酸盐体系加入亚硝酸根作为 NrtA 已知共配体；
- DOM 梯度、真实二级出水和过滤后同源水样；
- 批量选择性之外的固定床穿透、温和再生和至少五次循环；
- 蛋白/肽路线增加固定化取向、活性位点可达性、浸出和蛋白酶稳定性；这些项目是工程必要条件，不是现有来源已证明的性能。

## 8. 下一门禁所需的最小新增证据

### 磷酸盐方案

1. 对 1OIB/1IXG 或选定 PstS/PBP 结构做统一编号的结构叠合，报告叶片距离、口袋体积和关键残基，而非引用家族通用角度。
2. 选择纯有机胍基夹或双核金属夹之一作为主位点化学，另一种保留为机制对照，避免无证据地堆叠相互作用。
3. 用 FRET 与结合量同步证明闭合；用锁开材料证明闭合对选择性或抗置换有独立贡献。
4. 在硫酸盐、碳酸氢根、砷酸根和 DOM 存在下重新建立选择性，不能沿用 P7 的硝酸根单一竞争结论。

### 硝酸盐方案

1. 先用重组 NrtA 做 K269A 和至少一个氢键位点突变的水相结合对照，确认所选缓冲/离子背景下的口袋依赖性。
2. 获得 apo/硝酸根/亚硝酸根的双位点 FRET 或溶液 SAXS；在此之前，“硝酸根诱导 C-clamp 闭合”只能标记为假说。
3. 将三脲受体从有机混合溶剂迁移到水相前，先做小分子模型的 `NO3⁻/NO2⁻/SO4²⁻/HCO3⁻/Cl⁻` 竞争，不直接进入材料放大。
4. 若采用电再生，只把电导骨架视为释放模块；必须另设普通季铵盐电极对照，以证明任何新增选择性来自 NrtA 式几何而非离子交换。

