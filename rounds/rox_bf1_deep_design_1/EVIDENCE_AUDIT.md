# ROX-BF1 证据审计

## 审计结论

ROX的环境入场、真实生物膜吸附以及表面印迹可制造性均有一手研究支持；但天然生物膜只证明了阳离子大环内酯的类别富集，现有ROX印迹对近邻同系物的选择性也有限。因而本方案只能把“负电水化基质＋分级孔隙/厚度控制扩散”作为仿生硬对应，把ROX模板编码空腔明确标为非生物人工识别模块。

当前没有证据支持Cu/Zn位点、单个脲/硫脲/酰胺或未改性环糊精能在中性水中专一读取ROX的C9醚肟侧链。这些路线不进入主材料。

## 核心事实与边界

| 编号 | 可使用的事实 | 证据强度 | 禁止外推 |
|---|---|---|---|
| R1 | 五座污水厂ROX平均出水浓度为197–254 ng/L | Tier 1，全文数据 | 不能写成所有样本的浓度范围 |
| R2 | 在1 μg/L、受控膜厚生物膜中，ROX、ERY和CLA均发生显著吸附 | Tier 1，直接实验 | 不能写成ROX特异性 |
| R3 | 500 μm生物膜中ROX/ERY/CLA的平衡Kd几乎相同，厚度、孔隙和扩散影响分配 | Tier 1，直接实验 | 不能指定某个EPS官能团为ROX位点 |
| R4 | 好氧颗粒污泥中ROX去除部分受吸附能力影响 | Tier 1，摘要级 | 不能将EPS共变写成因果位点 |
| R5 | ROX准确差异结构是9-[O-[(2-methoxyethoxy)methyl]oxime]，简称C9醚肟侧链 | Tier 1，结构/药物化学 | 不能简化成C=N–O–CH3 |
| R6 | ROX、ERY、CLA、AZI的实测pKa约为8.82、8.83、8.79、8.96 | Tier 1，统一方法实测 | 普通阴离子交换不能据此声称ROX选择性 |
| R7 | ROX/ERY表面印迹分离因子曾仅为1.21 | Tier 1，直接材料研究 | “有印迹”不等于近邻选择性充分 |
| R8 | 2026 COF表面印迹报道64.58 mg/g、IF 2.40、四循环91.4% | Tier 1，摘要级 | 不能外推为真实二级出水连续处理性能 |
| R9 | ROX假模板整体柱可表现为大环内酯类别识别 | Tier 1，全文 | 不能把ROX模板自动等同于单分子特异性 |
| R10 | 金属—大环内酯比较实验在甲醇中进行；ROX未优于CLA/AZI | Tier 1，直接比较 | 不能把金属配位写成水相醚肟专一读取 |
| R11 | β-CD/HP-β-CD能够包合ROX | Tier 1，直接材料研究 | 不能写成相对ERY/CLA/AZI的ROX选择性 |

## 仿生硬对应

| 生物特征 | 来源支持 | 人工材料实现 | 预期功能 | 测量 | 因果对照 |
|---|---|---|---|---|---|
| 水化、负电的生物膜/EPS固相富集质子化大环内酯 | Torresi et al., Water Research 2017 | MAA富集的薄层交联网络；pH 7.5时羧酸盐提供类别预富集 | 将ng/L ROX从水相定位到近表面活性域 | pH滴定、ζ电位、ROX/阳离子药物Kd | 等孔容无MAA体；等电荷非印迹体 |
| 生物膜孔隙、密度和厚度共同调节分配与扩散 | 同上 | 250–500 μm刚性多孔微球、50–150 nm选择层、10–30 nm水化表皮 | 缩短传质路径，同时保留可达吸附域 | 截面深度成像、粒径/孔容、动力学和床层压降 | 等组成随机体、空间反转体、厚层系列 |

ROX形状编码空腔不在上表中冒充天然功能。它是为解决“天然原型不具ROX专一性”而附加的人工识别模块。

## 关键来源

1. Torresi E, et al. *Diffusion and sorption of organic micropollutants in biofilms with varying thicknesses*. Water Research 123 (2017) 388–400. https://doi.org/10.1016/j.watres.2017.06.027
2. Yu Z, et al. *Enhancement of PPCPs removal by shaped microbial community of aerobic granular sludge under condition of low C/N ratio influent*. Journal of Hazardous Materials 394 (2020) 122583. https://doi.org/10.1016/j.jhazmat.2020.122583
3. Xing L, et al. *Insights into the occurrence, elimination efficiency and ecological risk of antibiotics in rural domestic wastewater treatment facilities along the Yangtze River Basin, China*. Science of the Total Environment 837 (2022) 155824. https://doi.org/10.1016/j.scitotenv.2022.155824
4. Sun C, et al. *Spatial distribution and risk assessment of certain antibiotics in 51 urban wastewater treatment plants in the transition zone between North and South China*. Journal of Hazardous Materials 437 (2022) 129307. https://doi.org/10.1016/j.jhazmat.2022.129307
5. Li L, et al. *Occurrence and fate of antibiotics and heavy metals in sewage treatment plants and risk assessment of reclaimed water in Chengdu, China*. Chemosphere 272 (2021) 129730. https://doi.org/10.1016/j.chemosphere.2021.129730
6. Zrnčić M, et al. *Determination of thermodynamic pKa values of pharmaceuticals from five different groups using capillary electrophoresis*. Journal of Separation Science 38 (2015). https://doi.org/10.1002/jssc.201401057
7. Schlünzen F, et al. *Structural basis for the interaction of antibiotics with the peptidyl transferase centre in eubacteria*. Nature 413 (2001). https://doi.org/10.1038/35101544
8. Tang Z, Ma X. *Preparation of roxithromycin molecularly imprinted layer-coated silica and its selective adsorption properties*. Chemical Industry and Engineering Progress 35 (2016) 1162–1166. https://doi.org/10.16085/j.issn.1000-6613.2016.04.031
9. Song X, et al. *Preparation and Application of Molecularly Imprinted Monolithic Extraction Column for the Selective Microextraction of Multiple Macrolide Antibiotics from Animal Muscles*. Polymers 11 (2019) 1109. https://doi.org/10.3390/polym11071109
10. Zhao J, et al. *Eco-friendly deep eutectic solvent-mediated COF-based surface molecularly imprinted polymers for specific adsorption and determination of roxithromycin*. Sustainable Chemistry and Pharmacy 2026, 102500. https://doi.org/10.1016/j.scp.2026.102500
11. Hamdan II. *Comparative in vitro investigations of the interaction between some macrolides and Cu(II), Zn(II) and Fe(II)*. Pharmazie 58 (2003). https://storage.imrpress.com/IMR/pharmazie/application/223.pdf
12. Masood F, et al. *Characterization and application of roxithromycin loaded cyclodextrin based nanoparticles for treatment of multidrug resistant bacteria*. Materials Science and Engineering C 61 (2016). https://doi.org/10.1016/j.msec.2015.11.076
13. Wang et al. *Adsorption performance and mechanism of antibiotics from aqueous solutions on porous boron nitride–carbon nanosheets*. Environmental Science: Water Research & Technology (2020). https://doi.org/10.1039/D0EW00117A
14. Gokhale et al. *Multifunctional zwitterionic hydrogels for the rapid elimination of organic and inorganic micropollutants from water*. Nature Water (2024). https://doi.org/10.1038/s44221-023-00180-8
15. Ding J, et al. *Determination of roxithromycin from human plasma samples based on magnetic surface molecularly imprinted polymers followed by LC–MS/MS*. Journal of Chromatography B 1021 (2016) 221–228. https://doi.org/10.1016/j.jchromb.2015.08.001
