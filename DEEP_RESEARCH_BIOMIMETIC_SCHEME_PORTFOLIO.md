# Deep Research: 基于 pollutant_kb 的仿生选择性吸附方案组合

> 生成日期：2026-07-17；研究深度：standard；候选全集：`pollutant_kb.pollutant_index` 的20个顶层条目；本轮输出：10套机制不同的完整概念，推荐前5套。

## TL;DR

本轮不把20种污染物都强行做成方案。先对数据库全集进行环境意义和市政二级出水相关性预筛，再判断是否容易形成可证伪的仿生选择性机制。数据库中的论文数、知识项数和吸附性能项数只用于发现候选和定位文献，不作为环境风险分数。

最终形成10套方案，覆盖PFOA、PFBS/PFHxS/PFOS、HFPO-DA（GenX）、BPA、罗红霉素、壬基酚、奥克立林、五氯苯酚和2,6-二氯苯酚。初步推荐前5套：

1. **PFOA—hL-FABP两阶段门户口袋**，87/100；
2. **BPA—ERRγ双酚几何夹**，85/100；
3. **HFPO-DA（GenX）—HSA醚酸分叉口袋**，84/100；
4. **PFBS/PFHxS—HSA链长闸门**，83/100；
5. **罗红霉素—23S rRNA出口隧道局部门**，82/100。

这些分数是方案组合阶段的资源排序，不是吸附性能预测，也不代表已经通过最终的一静一动硬对应门槛。推荐前5套先进入下一轮原始文献补证、材料结构冻结和攻击评审；其余5套作为备选路线保存。

## Executive Summary

数据库全集中，PFAS、BPA、罗红霉素、壬基酚和奥克立林最适合当前市政二级出水论文主线：它们既有现实监测或法规/毒理意义，也能提出可被竞争物、位点删除、锁开和错配腔对照推翻的选择性机制。传统POPs和2,6-二氯苯酚并非没有环境意义，但水相二级出水证据、当前暴露相关性或目标专属生物结构不足，因此只保留为低优先级方案或场景储备。

十套方案不是十种污染物的一一对应，而是十条机制路线。PFAS内部故意设置了蛋白门户、β-环糊精主客体和HSA链长闸门三种不同机制，以测试“选择性来自哪里”；BPA和罗红霉素分别提供受体几何夹和核糖体局部门两条高论文潜力路线。前5推荐不表示可以立即合成，必须先完成目标物直接证据、真实水样门槛和仿生攻击。

## 1. 预筛规则

环境意义和二级出水相关性是评分前的硬门槛。候选必须满足：

1. 属于有机污染物，优先为新污染物或持久性有机污染物；
2. 有独立监测、法规或毒理资料支持其环境/健康关注；
3. 在市政污水处理厂进水、二级/最终出水或污泥—水相转移中具有可核实的现实关联；
4. 存在竞争吸附、痕量富集、同系物区分或DOM干扰等具体选择性难题；
5. 至少存在一条可以被实验推翻的生物识别转译路线。

第1—3项不计分，任何一项不能立住时不得由仿生新颖性补偿。通过硬门槛后，方案按以下100分排序：因果闭环20、选择性机制20、仿生保真度20、原创性15、可证伪性与对照15、证据完整性10。

## 2. pollutant_kb 20种污染物预筛

| 数据库污染物 | 环境/二级出水判断 | 方案潜力判断 | 本轮处理 |
|---|---|---|---|
| BPA | 通过。多个市政污水厂检出，具有内分泌干扰关注，但浓度和季节有变化。[S2][S3] | 高。存在直接ERRγ结构和明确的双酚近邻竞争。 | 进入方案5 |
| PFOA | 通过。市政最终出水中高频检出，且受PFAS法规和混合暴露关注。[S1][S4] | 高。蛋白结合结构、链长依赖和竞争体系都可建立。 | 进入方案1、2 |
| PFBS | 通过。市政出水高频检出，短链PFAS去除和竞争更困难。[S1][S4][S5] | 高。HSA链长/磺酸头基和β-CD两类路线可区分。 | 进入方案2、4 |
| PFHxS | 通过。市政出水高频检出，属于受关注PFAS。[S1][S4] | 中高。适合做PFBS/PFHxS/PFOS链长竞争，而非孤立单溶质。 | 进入方案2、4 |
| HFPO-DA（GenX） | 通过。市政出水有检出，短链醚型结构带来常规疏水吸附难题。[S1][S4] | 高。HSA两位点结构提供醚酸分叉识别线索。 | 进入方案3 |
| 罗红霉素 | 通过。多个污水处理系统中检出，去除可波动甚至出现表观负去除，具有抗生素残留和混合暴露关注。[S6][S7] | 高。大环内酯出口隧道结构可转译为受限局部通道。 | 进入方案6 |
| 壬基酚 | 通过。市政监测中常见，具有雌激素活性并在水相—污泥间分配。[S8][S9] | 中。环境意义较强，但商业壬基酚是异构体混合物，直接受体结构证据弱。 | 进入方案7 |
| 奥克立林 | 通过。市政污水中检出并主要向污泥分配，属于日化来源新污染物。[S10][S11] | 中。真实场景明确，但生物结合证据多为BSA或计算推断。 | 进入方案8 |
| 五氯苯酚 | 条件通过。旧监测和监管资料支持环境关注，但现代二级出水水相证据有限，且受pH影响。[S12] | 中。TTR甲状腺素通道有直接竞争和卤代酚结构先例。 | 进入方案9，低优先级 |
| 2,6-二氯苯酚 | 条件通过。氯酚环境危害明确，但本轮没有找到足够直接的市政二级出水监测；需先做本地水样和历史监测核验。[S13] | 中。氯酚降解酶底物口袋可提供几何假说，但材料转译和水相关联均较弱。 | 进入方案10，暂不推荐 |
| 十溴二苯醚 | 条件通过。EPA监测中可检出PBDE，但209同系物接近方法定量下限且有污染空白问题。[S14] | 中。环境意义高，水相方案容易退化为疏水分配或颗粒吸附。 | 不进入10套，保留为后续固相专题 |
| DDT | 条件通过。历史市政监测可检出，但主要是疏水、颗粒/污泥关联的传统POPs。[S14] | 低中。难以建立污水二级出水水相选择性仿生闭环。 | 不进入10套 |
| DDE | 条件通过。与DDT同属历史POPs，二级出水关联有限。[S14] | 低。可做同系物分辨，但缺少直接生物口袋依据。 | 不进入10套 |
| TCDD | 条件通过。毒理意义极高，但本轮没有足够市政二级出水水相证据。 | 中高。AhR配体口袋有生物意义，但场景门槛不足。 | 不进入10套，作为高危低检出储备 |
| 狄氏剂 | 条件通过。旧市政监测可检出，但水相风险和当前暴露相关性不够稳定。[S14] | 低。以疏水/颗粒分配为主，难做分子级仿生选择性。 | 不进入10套 |
| β-六氯环己烷 | 条件通过。历史农药污染物，二级出水现实关联弱。 | 低。缺少可直接转译的专一生物口袋。 | 不进入10套 |
| 硫丹 | 条件通过。EPA旧监测有进/出水线索，但定量和现代相关性弱。[S14] | 低中。高疏水性会掩盖仿生识别贡献。 | 不进入10套 |
| 六氯丁二烯 | 条件通过。持久性关注存在，市政监测证据稀疏。 | 低。缺少高保真生物识别原型。 | 不进入10套 |
| PCB-209 | 条件通过。环境持久性高，但顶层数据库覆盖和水相监测很弱。 | 低。更适合颗粒/沉积物而非二级出水选择性吸附。 | 不进入10套 |
| 三氯甲烷 | 通过发生，但不适合作为本项目吸附目标。它主要是氯化副产物，且低分子挥发性强。[S15] | 低。吸附材料选择性和论文闭环均不占优。 | 作为场景干扰物，不做方案 |

这一步的结果不是否定数据库中的其他污染物，而是将水相二级出水论文与传统疏水POPs/挥发性副产物区分开。十套方案优先服务于前一类目标。

## 3. 十套完整方案

### S1. PFOA—hL-FABP两阶段头基定位—门户呼吸口袋

**核心链条。** hL-FABP对PFAA存在直接结合和链长依赖；Asn111类外位点、Arg122类内位点以及高迁移率portal/gap共同限定“先定位羧酸头基、再将全氟链送入腔体”的机制。[S16][S17][S18] 这不支持PFOA诱导整个蛋白大幅闭合，只支持局部门户可达性变化。

**材料方案。** 在介孔硅或亲水多孔有机骨架表面固定两段短肽/聚酰胺：入口段提供胍基样正电和定向氢键，内段提供受限低极性腔体；两段由带荧光对的柔性门户连接。材料不使用含氟模板或游离含氟单体。

**静态—动态对应。** 静态硬对应是羧酸头基的入口定位加全氟链的腔体匹配；动态对应限定为门户开合/呼吸导致的可达性变化。测量PFOA、PFNA/PFHpA、PFBA、PFOS、PFHxS、PFBS和油酸的竞争穿透、ITC/SPR、FRET/QCM-D。锁开门户、删除外位点、删除内位点和随机位点为因果对照。

**成功/失败合同。** 若PFOA相对PFBA、PFBS和油酸的选择性提升与门户FRET同步，且锁开或删除任一位点后同步消失，则方案成立。若随机位点达到同等选择性，或所有长链PFAS均无差别占据，则PFOA特异性失败。

**主要风险。** hL-FABP并非PFOA专一受体，静态PFAS印迹路线已拥挤；材料必须证明两阶段作用的独立贡献。[S19]

### S2. PFOA/PFOS/PFHxS/PFBS—β-环糊精主客体—链长分流网络

**核心链条。** β-环糊精作为天然环状主体，以疏水腔体容纳全氟链，外缘羟基和阳离子交联点与阴离子头基作用。β-CD对PFOA的主客体结合和聚合物去除PFAS已有材料先例。[S20][S21][S22]

**材料方案。** 构建带固定阳离子交联点的β-CD多孔网络，控制β-CD腔体密度和网络溶胀。用两种交联密度形成短链可进入、长链滞留的梯度床，材料不把总容量解释为选择性。

**静态—动态对应。** 静态对应是天然环腔—全氟链包合作用；动态对应是腔体占据和网络溶胀改变可达性。测量PFBA/PFBS/PFHxS/PFOA/PFOS/GenX的选择性序列、竞争等温线、柱穿透和再生。非环状交联聚合物、无阳离子交联点和固定溶胀网络为对照。

**成功/失败合同。** 只有当链长/头基组合能预测穿透次序，并且删除β-CD腔体或固定网络后选择性显著下降，才保留主客体机制。若普通疏水树脂或活性炭给出同等结果，方案降级为常规吸附基线。

**主要风险。** β-CD路线已有较多报道，交联剂和电荷可能成为真正机制；混合PFAS和DOM下的再生仍是关键问题。

### S3. HFPO-DA（GenX）—HSA IIIA醚酸分叉口袋

**核心链条。** HPFO-DA/HFPO-DA与人血清白蛋白III A亚域存在两处结合位点，醚氧、支化链和羧酸头基提供区别于PFOA长直链的局部极性和几何信息。[S23]

**材料方案。** 制备表面接枝的双半口袋：入口设置羧酸定位的胍基/酰胺位点，内腔设置一个定向氢键位点读取醚氧，并用浅短腔限制支化链轮廓。采用亲水壳层减少DOM覆盖。

**静态—动态对应。** 静态对应是羧酸头基、醚氧和支化链三点同时匹配；动态对应是两半口袋在三点占位后发生局部靠近。用FRET、原位红外和竞争柱实验检测HFPO-DA/PFOA/PFHxA/PFBA/PFBS。

**成功/失败合同。** 若醚氧位点删除只降低HFPO-DA而不等比例降低PFOA，且可动材料的HFPO-DA选择性高于固定开态材料，则机制成立。若延长疏水腔后PFOA总是替代HFPO-DA，说明设计退化为链长分配。

**主要风险。** HSA结构证据针对HPFO-DA/C6O4同类命名体系，环境水中的具体形态、pH和模板泄漏必须单独核对。

### S4. PFBS/PFHxS/PFOS—HSA IIIA磺酸头基—链长闸门

**核心链条。** PFAS与HSA IIIA亚域的结合受磺酸头基的静电/氢键和氟碳链长共同影响，Arg410、Asn391和Tyr411类位点构成头基锚定，腔体长度决定停留和穿透。[S24]

**材料方案。** 在介孔载体表面固定胍基、酚羟基和一条可调长度的低极性侧壁，制成C4、C6、C8三种可交换腔长。将三种材料串联成小型柱，直接读出链长闸门而非单点容量。

**静态—动态对应。** 静态对应是磺酸头基三点锚定；动态对应是链长匹配调节侧壁和入口停留时间。用PFBS/PFHxS/PFOS、PFOA、PFBA、硫酸盐、胆汁酸和阴离子表面活性剂竞争，测穿透、解吸和盐强度响应。

**成功/失败合同。** 如果C4/C6/C8腔长分别对PFBS/PFHxS/PFOS产生可重复的穿透顺序，并在删除头基位点或固定侧壁后消失，方案成立。若高盐和DOM使所有PFAS无差别吸附，则不具备二级出水选择性。

**主要风险。** 静电吸附会被背景离子掩盖；短链PFAS对有机质和无机离子更敏感，必须把实际水基质作为第一批实验，而不是最后验证。[S5]

### S5. BPA—ERRγ双酚几何夹—受体式入口收缩

**核心链条。** ERRγ结构显示BPA的两个酚羟基与Glu275/Arg316形成氢键，芳香残基Phe435/Phe450提供疏水夹持，BPA与ERRγ的直接结合结构为1.6 Å级别。[S25] 受体口袋的动态入口变化需要单独验证，不能直接从静态结构推断。

**材料方案。** 在亲水交联壳层内布置两个方向固定的酚羟基受体和一对芳香侧壁，限制BPA的中心异丙叉几何。两侧壁用柔性短链相连，构成可测的入口收缩单元。

**静态—动态对应。** 静态对应是“双酚羟基—双氢键＋双芳香侧壁”的几何夹持；动态对应是BPA跨接两侧后触发入口收缩的材料假说。用BPA、BPF、BPS、BPZ、雌二醇、壬基酚和DOM进行竞争，测FRET、QCM-D、吸附热和真实二级出水选择性。

**成功/失败合同。** 只有BPA同时产生双点结合和入口收缩，且删除一个羟基受体或锁开入口后选择性下降，才可宣称ERRγ启发的选择性。若随机酚/芳香树脂已经达到相同BPA/BPS/BPF分辨率，仿生主张失败。

**主要风险。** BPA是数据库中覆盖最多的污染物，普通印迹、β-CD和疏水树脂路线拥挤；论文价值取决于几何夹持的独立因果贡献，而不是容量。

### S6. 罗红霉素—23S rRNA出口隧道—局部核苷酸摆门

**核心链条。** 大环内酯占据50S核糖体肽出口隧道；克拉霉素结构显示desosamine锚定、有限通道和A2062局部构象异质性。[S26][S27] 罗红霉素本身已有分子印迹吸附先例，但缺少其专属核糖体结构，故动态转译必须标为假说。

**材料方案。** 在介孔硅/COF表面制备两亲性狭缝：一侧为疏水宏环壁，另一侧为阴离子/氢键位点模拟desosamine邻近区域；入口放置可摆动杂环或核碱基样门位点。使用罗红霉素作模板，但不把普通MIP空穴当作仿生本身。

**静态—动态对应。** 静态对应是宏环尺寸、糖基正电中心和通道内壁的多点匹配；动态对应缩小为门位点局部摆动/界面水重排。测罗红霉素、克拉霉素、阿奇霉素、红霉素、螺旋霉素和代谢物竞争，配合FRET/QCM-D/纳米通道电导。

**成功/失败合同。** 若门位点删除只损失罗红霉素的选择性和可逆释放，而普通表面印迹仍保留静态容量，则局部门机制成立。若所有大环内酯均同样结合且门位点不影响动力学，方案降级为普通印迹。

**主要风险。** 罗红霉素缺少直接核糖体复合结构，近邻克拉霉素的A2062证据不能直接转给罗红霉素；这是必须在下一轮优先补的证据缺口。

### S7. 壬基酚—ER/GPER酚羟基锚定—可调烷基尾腔

**核心链条。** 壬基酚在市政水体和污泥中具有检出及雌激素活性，但商业样品是异构体混合物。[S8][S9] ER竞争和GPER细胞/对接证据支持“酚羟基锚定＋疏水尾部”的识别假说，尚无目标专属三维结构。[S28]

**材料方案。** 做异构体分辨的表面口袋：固定酚羟基氢键位点，设置可改变深度和分支容忍度的C9尾腔；用不同模板分别做直链和支链壬基酚口袋，形成一对比较材料。

**静态—动态对应。** 静态对应是酚羟基极性锚定和烷基尾部疏水腔；动态对应仅作为尾腔可压缩/可扩张假说。用4-n-壬基酚、支链NP、辛基酚、BPA/BPF、雌二醇和NP1EO/NP2EO竞争。

**成功/失败合同。** 若不同尾腔对异构体产生可重复选择性，且删除酚羟基锚定位点后选择性显著下降，方案成立。若只有总疏水性决定吸附，或商业异构体无法分辨，方案停止。

**主要风险。** 直接生物证据弱、异构体混合复杂，方案适合做高质量对照型论文，不适合作为第一主方案。

### S8. 奥克立林—蛋白疏水口袋—腈酯双极性锚定

**核心链条。** 奥克立林在市政污水中检出，且大部分负荷转入污泥，水相和固相去向均具有环境意义。[S10][S11] BSA结合和计算研究可提供疏水口袋与腈酯极性锚定的邻近依据，但没有目标—蛋白晶体结构。[S29]

**材料方案。** 在亲水纤维表面制备宽口疏水腔，腔底设置腈基/酯羰基定向氢键位点；通过柔性盖片控制大体积UV过滤剂进入，避免单纯相分配。

**静态—动态对应。** 静态对应是腈酯极性锚定＋芳香/烷基疏水腔；动态对应是大体积分子进入后盖片位移的材料假说。以奥克立林、阿伏苯宗、奥克西林酸乙酯、二苯甲酮-3和DOM竞争，并同时测水相去除和污泥释放。

**成功/失败合同。** 如果腈酯位点删除后奥克立林/同类UV过滤剂选择性消失，且盖片影响可逆释放，才保留。若仅由疏水分配决定，则作为普通疏水吸附基线，不再称仿生。

**主要风险。** 生物原型证据最低，水相浓度低而污泥负荷高；应在确认研究目标是二级出水水相后再投入材料开发。

### S9. 五氯苯酚—TTR甲状腺素通道—卤代酚几何筛

**核心链条。** 五氯苯酚与转甲状腺素蛋白（TTR）存在竞争结合，卤代酚在甲状腺素通道中有结构先例；邻位卤素和酚羟基共同影响通道占位。[S12][S30]

**材料方案。** 在介孔硅中构建刚性芳香通道，通道入口设置酚羟基氢键位点，内部设置可容纳邻位氯原子的卤素/芳香壁。用2,4,6-TCP、2,4-DCP、2,6-DCP和溴酚做结构竞争。

**静态—动态对应。** 静态对应是酚羟基锚定和卤代芳香通道；动态对应是通道侧壁因卤素数目/邻位模式发生微小重排的假说。测pH形态、盐度、竞争吸附和柱穿透。

**成功/失败合同。** 若卤素数和邻位模式可以预测选择性，并在无酚锚定位点或柔性通道对照中消失，方案成立。若PCP仅因疏水性吸附，或pH变化完全解释结果，方案否决。

**主要风险。** 现代二级出水证据不足，旧TTR竞争资料和溴酚结构不能直接等同于PCP材料机制；只能作为低优先级方案。

### S10. 2,6-二氯苯酚—氯酚羟化酶底物口袋—邻位氯几何门

**核心链条。** 氯酚降解酶的底物构效关系提示酚羟基和邻位氯取代共同决定进入疏水底物口袋；该路线的生物事实主要来自酶底物研究，而不是二级出水吸附材料。[S31]

**材料方案。** 制备带酚羟基定向氢键位点和两个邻位氯容纳凹槽的表面口袋，以介孔MOF或耐水交联聚合物承载。可加入可逆柔性盖片，但不能把酶催化所需金属/氧化还原步骤假装成吸附机制。

**静态—动态对应。** 静态对应是酚羟基＋邻位双氯的三点几何；动态对应只是底物进入后口袋局部收缩的假说。测2,6-DCP、PCP、2,4-DCP、2,4,6-TCP、苯酚和氯酚异构体的选择性，并做真实二级出水加标回收。

**成功/失败合同。** 只有在本地二级出水或独立监测确认目标现实存在，并且邻位氯几何对选择性有独立贡献时才继续。若水样中长期未检出，或普通疏水材料即可达到相同结果，立即停止。

**主要风险。** 目前环境门槛和目标专属生物结构均不足，因此本方案只用于保持用户指定污染物的备选覆盖，不进入前5。

## 4. 方案排序与推荐

| 排名 | 方案 | 分数 | 环境门 | 主要优点 | 首要缺口 |
|---:|---|---:|---|---|---|
| 1 | S1 PFOA—hL-FABP两阶段门户 | 87 | 通过 | PFAS场景强，头基—链长—门户三层可测 | 动态只能主张局部门户，不能写整体闭合 |
| 2 | S5 BPA—ERRγ双酚夹 | 85 | 通过 | 直接结构证据强，环境意义明确，近邻竞争清楚 | 普通印迹拥挤，必须证明双点几何和动态独立贡献 |
| 3 | S3 GenX—HSA醚酸分叉口袋 | 84 | 通过 | 醚氧/支化链提供真正区别于PFOA的选择性问题 | HPFO-DA命名和环境形态、模板泄漏需核对 |
| 4 | S4 PFBS/PFHxS—HSA链长闸门 | 83 | 通过 | 短链PFAS环境意义强，混合竞争实验价值高 | 盐和DOM可能压过头基识别 |
| 5 | S6 罗红霉素—rRNA出口局部门 | 82 | 通过 | 抗生素场景和局部核苷酸动态最容易形成论文故事 | 罗红霉素缺少自身复合结构，近邻转译风险高 |
| 6 | S2 PFAS—β-CD主客体网络 | 78 | 通过 | 工程实现成熟，适合做混合PFAS基准和备选 | 路线拥挤，容易退化为普通主客体吸附 |
| 7 | S9 PCP—TTR卤代酚通道 | 72 | 条件通过 | 卤代酚几何比较和TTR结构可形成清楚对照 | 二级出水水相证据老且弱 |
| 8 | S7 壬基酚—ER/GPER尾腔 | 70 | 通过 | 现实环境意义和异构体选择性有应用价值 | 商业异构体混合，缺少直接三维受体结构 |
| 9 | S8 奥克立林—蛋白疏水口袋 | 67 | 通过 | 新兴日化污染物、污泥—水相迁移有现实场景 | 生物证据弱，疏水分配混杂严重 |
| 10 | S10 2,6-DCP—氯酚羟化酶口袋 | 63 | 待核验 | 用户指定目标，邻位氯几何可证伪 | 缺少直接二级出水监测和材料转译证据 |

## 5. 推荐前5的推进顺序

第一阶段同时推进S1、S3、S4，构成一个PFAS内部竞争矩阵，但三套材料必须使用不同机制：S1强调羧酸头基—门户，S3强调醚氧/支化链，S4强调磺酸头基—链长闸门。这样可以用同一批二级出水和同一套LC-MS/MS方法比较三种仿生逻辑，避免将“PFAS去除”写成单一疏水吸附。

第二阶段推进S5和S6。S5的环境意义和结构证据最扎实，适合作为有机内分泌干扰物主线；S6的局部核苷酸门具有更高原创性，但必须先完成罗红霉素自身或同类大环内酯结构证据核验。

S2作为工程备选：如果S1或S4在DOM/盐背景下不能保持选择性，β-CD网络可以提供更稳妥的PFAS工程基准，但不应自动成为仿生主案。S7—S10暂不投入完整合成，先完成环境门和直接生物证据核验。

## 6. 必须先完成的攻击问题

- S1/S3/S4是否只是不同名字的疏水/静电吸附？必须做位点删除、腔长错配、固定开态和普通树脂对照。
- S5是否只是BPA分子印迹？必须证明BPA/BPS/BPF几何差异和入口动态的独立贡献。
- S6是否把克拉霉素结构错误转给罗红霉素？必须核对罗红霉素特异结构或降低仿生表述。
- S2是否把β-CD本身的已知主客体效应包装成新生物机制？应将它作为工程基准/备选，不默认进入主案。
- S7—S10是否能在真实二级出水中达到可检出浓度和可验证选择性？没有场景证据时不进入终审。

## 7. 方法与证据边界

本轮采用两路并行检索：一组核查市政污水、法规和环境监测，另一组核查蛋白/核糖体/酶结构及材料转译先例。主要事实由原始论文、EPA/官方资料或原始结构论文支持；对接、同类蛋白和相邻材料只作为邻近先例，不升级为目标物直接事实。所有动态材料行为均标记为设计假说，必须用锁开、删位点、错配腔和真实竞争物实验裁决。

## 参考文献

[S1] Kim et al. *Occurrence, Fate, and Removal of PFAS in Small- and Large-Scale Municipal Wastewater Treatment Facilities in the United States*. ACS ES&T Water, 2024. https://pubmed.ncbi.nlm.nih.gov/39698553/ ; DOI: 10.1021/acsestwater.4c00541.  Tier 1.

[S2] Sun et al. *Occurrence and removal of bisphenols in seven wastewater treatment plants in Xiamen, China*. Environmental Pollution, 2017. DOI: 10.1016/j.envpol.2017.03.018. Tier 1.

[S3] *Occurrence of multiple bisphenols in municipal wastewater and removal in sequencing batch reactors*. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9736069/. Tier 1.

[S4] U.S. EPA. *PFAS National Primary Drinking Water Regulation* and economic analysis, 2024. https://www.epa.gov/system/files/documents/2024-04/pfas-npdwr_final-rule_ea.pdf. Tier 1.

[S5] Tavasoli et al. Municipal wastewater PFAS fate and removal study, 2021. DOI: 10.1039/D1EM00032B. Tier 1.

[S6] Choi et al. Antibiotics in wastewater treatment plant effluent, including roxithromycin. Environmental Toxicology and Chemistry, 2008. DOI: 10.1897/07-143.1. Tier 1.

[S7] Japanese four-STP macrolide removal study, 2009. DOI: 10.2166/wst.2009.067. Tier 1.

[S8] Lee and Peart. Canadian municipal alkylphenol survey. Environment Canada. https://publications.gc.ca/site/eng/9.872704/publication.html. Tier 1.

[S9] U.S. EPA. Nine POTW contaminants of emerging concern report, 2009. https://www.epa.gov/sites/production/files/2018-11/documents/occurrence-cec-wastewater-9-treatment-work.pdf. Tier 1.

[S10] Liu et al. Full-scale municipal WWTP occurrence and fate of octocrylene, 2012. DOI: 10.1016/j.envpol.2011.10.009. Tier 1.

[S11] Magi et al. UV-filter occurrence in a Genoa WWTP, 2013. DOI: 10.1039/C2AY26163D. Tier 1.

[S12] PCP–TTR competition and halogenated-phenol channel studies. DOI: 10.1016/0009-2797(90)90034-K; DOI: 10.1107/S0907444900008568. Tier 1.

[S13] 2,6-dichlorophenol municipal monitoring gap and chlorophenol analog records. https://pubchem.ncbi.nlm.nih.gov/compound/7245. Tier 2/3; not sufficient for a final environmental claim.

[S14] U.S. EPA 9-POTW report, legacy organochlorines and PBDEs. Same source as [S9], sections on pesticides/PBDEs. Tier 1.

[S15] U.S. Geological Survey reconnaissance of chloroform in municipal effluents. https://www.usgs.gov/publications/reconnaissance-selected-organic-contaminants-effluent-and-ground-water-fifteen. Tier 1.

[S16] Sheng et al. *Interaction of perfluoroalkyl acids with human liver fatty acid-binding protein*. Archives of Toxicology, 2016. DOI: 10.1007/s00204-014-1391-7. Tier 1.

[S17] Zhang et al. *Structure-Based Investigation on the Interaction of Perfluorinated Compounds with Human Liver Fatty Acid Binding Protein*. Environmental Science & Technology, 2013. DOI: 10.1021/es4026722. Tier 1.

[S18] Cai et al. *Solution Structure and Backbone Dynamics of Human Liver Fatty Acid Binding Protein*. Biophysical Journal, 2012. DOI: 10.1016/j.bpj.2012.04.039. Tier 1.

[S19] Guo et al. PFOS surface molecular imprinting on carbon microspheres. Journal of Hazardous Materials, 2018. DOI: 10.1016/j.jhazmat.2018.01.018. Tier 1.

[S20] HSA–PFOA crystal structure. Protein Science, 2021. DOI: 10.1002/pro.4036; PDB 7AAI. Tier 1.

[S21] β-Cyclodextrin/PFOA host–guest study. Chemical Research in Toxicology, 2018. DOI: 10.1021/acs.chemrestox.8b00002. Tier 1.

[S22] DFB-β-cyclodextrin polymer for PFAS removal. Journal of the American Chemical Society, 2017. DOI: 10.1021/jacs.7b02381. Tier 1.

[S23] HFPO-DA/GenX–HSA interaction and two-site structure. ACS Chemical Research in Toxicology, 2022. DOI: 10.1021/acs.chemrestox.2c00211; PDB 7Z57. Tier 1.

[S24] PFAS binding in HSA domain IIIA and chain-length effects. RSC Advances, 2017. DOI: 10.1039/C7RA02963B. Tier 1.

[S25] Matsushima et al. BPA binding to ERRγ. Journal of Biochemistry, 2007. DOI: 10.1093/jb/mvm158; PDB 2E2R. Tier 1.

[S26] Zhang et al. Cryo-EM structure of *M. tuberculosis* 50S bound with clarithromycin. Emerging Microbes & Infections, 2022. DOI: 10.1080/22221751.2021.2022439; PDB 7F0D. Tier 1.

[S27] Hansen et al. Structures of macrolides bound to the large ribosomal subunit. Molecular Cell, 2002. DOI: 10.1016/S1097-2765(02)00570-1. Tier 1.

[S28] GPER/nonylphenol evidence. Steroids, 2022. DOI: 10.1016/j.steroids.2022.109114. Tier 2; no direct receptor crystal.

[S29] Octocrylene–BSA interaction and computational protein-pocket evidence. Journal of Molecular Structure, 2024. DOI: 10.1016/j.molstruc.2024.138190. Tier 2.

[S30] TTR halogenated phenol structures. Acta Crystallographica D, 2000. DOI: 10.1107/S0907444900008568. This is a bromophenol/TTR structural precedent, not a PCP crystal. Tier 1.

[S31] Chlorophenol hydroxylase substrate SAR and pocket evidence. Primary enzyme study, 2014. Source details require final DOI spot-check before hard correspondence.

## Source Extracts

- **[S1] PFAS municipal study:** nine municipal WWTPs were analyzed for 40 PFAS; PFOA, PFOS, PFNA, PFBS and PFHxS were detected at 100% frequency among the regulated set, HFPO-DA at 67%, and the reported mixture hazard index was 0.2–6.1 for the specified PFAS mixture. This does not establish a universal frequency for every plant.
- **[S2] BPA municipal survey:** seven Xiamen WWTPs reported median BPA of 1318 ng/L in influent and 177 ng/L in effluent; the result is a city/monitoring-period summary, not a universal plant-level removal constant.
- **[S6][S7] Roxithromycin:** roxithromycin was detected in WWTP studies; the Japanese four-STP study reported removal from −32% to 59%. The Hong Kong study establishes occurrence in influent/effluent but should not be used to transfer the Japanese removal range.
- **[S10] Octocrylene:** a full-scale municipal plant study found octocrylene in influent and biosolids, with most hydrophobic UV-filter load associated with sorption/partitioning and high aqueous removal. Biosolid association is not proof of irreversible accumulation.
- **[S16][S17][S18] PFOA/FABP:** PFAA binding, chain-length dependence and portal/gap dynamics support a two-stage recognition hypothesis; they do not prove PFOA-induced global closure.
- **[S20] PFOA/HSA:** PDB 7AAI is a 2.10 Å hSA–PFOA–myristate complex; the structure contains multiple PFOA/FA sites and therefore cannot be treated as a single unique PFOA pocket.
- **[S23] HFPO-DA/HSA:** PDB 7Z57 is a ternary hSA–HFPO-DA–myristate structure with two HFPO-DA molecules in the relevant fatty-acid sites; this is a specific ternary complex, not a universal HSA stoichiometry.
- **[S25] BPA/ERRγ:** PDB 2E2R is a 1.60 Å ERRγ ligand-binding-domain/BPA complex; Kd and hydrogen-bond contacts support static geometry, not a material dynamic gate.
- **[S26][S27] Macrolides:** roxithromycin has a 50S/23S rRNA NPET structure (PDB 1JZZ); A2058/A2059 are classical neighboring sites, while A2062/A2503 rearrangements are best treated as related-macrolide evidence.
- **[S12][S30] PCP/TTR:** PCP competition with T4 is biochemical evidence; the bromophenol/TTR crystal structures are a reverse structural precedent, not a PCP crystal structure.

## Methodology

The standard-depth run used two parallel retrieval agents for municipal occurrence/risk and biomimetic structure/material translation, followed by a separate citation-verification pass on ten high-impact claims. Sources were triangulated across primary papers, PDB records, PubMed and official EPA/USGS/Environment Canada records. When a source supported only an analog, a docking model, or a related pollutant, the claim was downgraded to a neighboring precedent or design hypothesis. The portfolio intentionally stops before isolated designer/attacker/reviewer rounds; those rounds begin only after Pan Yao approves the recommended top five.

## Open Questions

1. 2,6-DCP在本项目拟采集的二级出水中是否达到可稳定定量水平，尚未证实；在得到本地水样结果前不能将S10当作正式终选。
2. 罗红霉素缺少自身核糖体复合结构，S6必须先完成目标专属或同类结构边界核验。
3. PFOA、PFBS、PFHxS和GenX的蛋白识别与材料选择性都可能被盐、DOM和其他PFAS压低，必须用同一批二级出水做混合竞争。
4. BPA和β-CD路线容易被普通印迹/主客体吸附先例覆盖，推荐方案必须证明仿生位点和动态单元的因果独立性。
