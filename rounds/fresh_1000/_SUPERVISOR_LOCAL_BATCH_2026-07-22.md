# 监督者本地批次台账（2026-07-22 会话）

## 目的与边界

本会话（用户指令：pull `origin/Ultimate` 最新内容后继续开发，目标为 20 污染物各 50 个仿生吸附方案、排名并**保留全部中间设计入库以扩充仿生设计库**）在 `Ultimate` 分支上**本地推进 Phase B 方案槽，暂不推送**（用户决策：另一执行者会话近 1h 内仍在向 `origin/Ultimate` 推送 dde/endosulfan，为避免"同一时刻一个执行者"冲突，本会话仅本地提交，待用户确认后统一推送/reconcile）。

## 编号约定（避免与全局 S## 冲突）

`origin/Ultimate` 现有全局方案序列已至 **S34**（octocrylene 通过），且有 dde/endosulfan/tcdd/betahch/pcp 等在途槽将在另一会话组装时占用 S35+。为避免双会话争用同一 S 号，本会话产物一律用 **`SL##`（Supervisor-Local）** 前缀本地编号，文件仍置于各污染物 `SCHEMES/` 下。**reconcile 时的动作**：按提交时间与内容将 `SL##` 重编为全局 `S##`（不与另一会话已用号冲突），并入 `STATUS.yaml` 逐槽记录。

## 起步聚焦（用户选定）

启动 5 个尚未进入 Phase B 的污染物：**chloroform / HCBD / BDE-209 / PCB-209 / TCDD**。其中 `tcdd` A01（卤键 σ 穴角度）已由另一会话在 `_wip` 在途（提交 af5c419，66→76→74 stuck），本会话对 tcdd **另取干净角度**（拟 A05 还原反应性捕获 或 A10 平面受限腔+侧位氯锚定），避免 clobber。

## 单方案粒度（用户选定）

**每条按 fresh_1000 完整闭环格式**（九节 + 硬对应六字段 + 攻击七维 + 裁决量表 + 证据台账）。评分门槛不降：通过线 85、零未决 critical/high。诚实评分，revise/terminate 亦全量入库（符合"保留全部中间设计"目标）。

## 本批次逐槽状态

| SL# | 污染物 | 角度 | 题名 | r1 | verdict | critical/high | 文件 |
|---|---|---|---|---:|---|---|---|
| SL01 | BDE-209 | A02 | PceA 双域解耦反应性捕获 | 66 | revise | 0 / 4 | `bde209/SCHEMES/SL01_A02_pceA-dual-domain-reactive-capture_r1-revise.md` |
| SL02 | PCB-209 | A01 | 扭转正交构象形状读出腔（AhR 负面原型反转） | 64 | revise | 0 / 3 | `pcb209/SCHEMES/SL02_A01_torsional-complementary-cavity_r1-revise.md` |
| SL03 | chloroform | A04 | 单位点多弱作用协同预组织识别腔 | 65 | revise | 0 / 3 | `chloroform/SCHEMES/SL03_A04_multi-weak-interaction-cavity_r1-revise.md` |
| SL04 | TCDD | A10 | 平面受限腔+侧位氯锚定双维度 | 67→**r2=74** | revise | 0 / 2 | `tcdd/SCHEMES/SL04_A10_planar-confined-lateral-Cl-anchor_r2-revise.md` |
| SL05 | HCBD | A01 | 环糊精空腔长度匹配+腔口卤键 | 62 | revise（倾向 terminate） | 0 / 3 | `hcbd/SCHEMES/SL05_A01_CD-cavity-length-rim-halogen-bond_r1-revise.md` |
| SL06 | PCB-209 | A16 | PXR 大软疏水腔定向混杂容纳 | 61 | revise（standalone 倾向 terminate/宜耦合） | 0 / 3 | `pcb209/SCHEMES/SL06_A16_PXR-large-soft-cavity_r1-revise.md` |
| SL07 | BDE-209 | A12 | 白腐菌胞外捕获-催化两亲可及性微域 | 68 | revise | 0 / 3 | `bde209/SCHEMES/SL07_A12_white-rot-capture-catalysis-amphiphilic_r1-revise.md` |
| SL08 | PCB-209 | A23 | 多表位正交受体（扭转×卤键×全氯轮廓） | **73** | revise | 0 / 2 | `pcb209/SCHEMES/SL08_A23_multi-epitope-orthogonal-receptor_r1-revise.md` |
| SL09 | BDE-209 | A19 | 多表位正交受体（溴卤键×π 酸×十溴轮廓，平衡吸附） | **72** | revise | 0 / 2 | `bde209/SCHEMES/SL09_A19_multi-epitope-orthogonal-receptor_r1-revise.md` |
| SL10 | chloroform | A19 | 三卤甲基（卤素计数）识别签名 | 68 | revise | 0 / 2 | `chloroform/SCHEMES/SL10_A19_trihalomethyl-halogen-count-signature_r1-revise.md` |
| SL11 | TCDD | A04 | 二芳醚氧锚定+角位轮廓虚拟模板印迹 | 69 | revise | 0 / 2 | `tcdd/SCHEMES/SL11_A04_aryl-ether-angular-profile-virtual-template-MIP_r1-revise.md` |
| SL12 | HCBD | A04 | 类咕啉辅因子反应性捕获（有机卤化物呼吸） | 69 | revise | 0 / 2 | `hcbd/SCHEMES/SL12_A04_corrinoid-reductive-reactive-capture_r1-revise.md` |

**四轮汇总（A→B 循环·真生物原型广度）：**为三个污染物各补一个承重原型经核验的角度：chloroform A19=68（CfrA 氯仿专一酶判别几何，Picott 2024/2025）、TCDD A04=69（Sphingomonas RW1 角位双加氧酶醚骨架识别，Wittich 1992，approach-1 硬对应、优于 A10 的 AhR 几何）、HCBD A04=69（Dehalococcoides HCBD 直接脱氯异构体序列，Shen 核验，强于 SL05）。**累计本会话 12 个闭环方案（SL01–SL12），涵盖 5 污染物：BDE-209×3、PCB-209×3、TCDD×3(含r2)、chloroform×2、HCBD×2。** 分数 61–74，均 revise、零 critical。已批量推送。TCDD/HCBD 各新增的 approach-1 真原型角度（A04）C 维仿生真实性优于首轮。

**三轮汇总（A→B 循环·多表位综合）：**按单角度攻击台账"单维不过 D、须耦合"结论，合成多表位正交受体：PCB-209 A23=73（扭转×卤键×全氯，本会话 pcb209 最高）、BDE-209 A19=72（平衡吸附多表位，正面回应 SL01 “选择性吸附名实不符”攻击）。两者 D（选择性）+E（先例）双维通过，为各污染物最强角度、r2 优先。**累计本会话 9 个闭环方案（SL01–SL09），涵盖 5 污染物；BDE-209/PCB-209 各 3 个互补角度。** 分数 61–74，均 revise、零 critical。已批量推送 origin/Ultimate。

**二轮汇总（A→B 循环）：**LOOP-A 完成 TCDD A10 r2=74（+7，闭合脂质归一化对照；pg/L 亲和力+Å 锚定为 Stage-0 物理可行性门，结构性天花板）。LOOP-B 新增 PCB-209 A16（61，单维单调宜作耦合层）与 BDE-209 A12（68，白腐菌两亲可及性，正对颗粒相真实靶界面，与 SL01 互补）。**累计本会话 7 个闭环方案（SL01–SL07），涵盖 5 污染物，均本地提交、未推送。** 分数分布 61–74，均 revise、零 critical——这 5 个为执行顺序最末、内禀最硬的污染物，首轮不达 85 为诚实结果。

## 承重证据核验状态（本会话 WebSearch 直核）

- BDE-209：PceA 结构 **PDB 4UR0**（Bommer 2014 Science；angle map 误记 4UQU 已更正）、norpseudo-B12（Biochemistry 2021 10.1021/acs.biochem.1c00271）、亦转化芳基卤（PDBj 5M8Y）；脱溴速率随溴数单调、BDE-209 半衰期 18 s（Tokarz 2008 ES&T 10.1021/es071989t）——均 verified。先例：分子笼 POP 吸附/传感 PFOA（Chen 2023 PMID 36538618）verified。
- PCB-209：非共平面 PCB 激动 PXR/CAR、共平面 PCB-77 不激活（Al-Salman 2012 10.1016/j.taap.2012.05.016）verified；扭转联苯分子识别先例（Weh 2023 Nat Commun 10.1038/s41467-023-35851-3）verified；PCB-209 无实测水浓度（Wolkersdorfer 2025 综述）verified 负面发现。
- TCDD：还原脱氯 peri 路径收敛 2,3,7,8（Barkovskii & Adriaens 1996 PMID 8953727）verified。
- chloroform：麻醉剂高亲和疏水腔弱极性作用（Liu/Loll/Eckenhoff 2005 FASEB J 19:567-576）verified。
- HCBD：CD-氯代溶剂增溶去除（Boving 等，HERO 3545601，被引 110）verified——但为增溶非选择性吸附，选择性吸附仍空白。

## 诚实总评（本批次前两槽）

BDE-209/PCB-209 首轮均 revise（66/64）、零 critical。这与这 5 个污染物在执行顺序中靠后、角度地图普遍标注内禀硬度（logKow 单调陷阱、水相弱卤键、无实测浓度、降解路线与好氧场景错配、先例收窄）一致，非降标。承重原型与选择性轴均经外部核验、无编造；主要缺口为工程/靶标合理性与选择性对照，重建方向已逐槽登记。二者均作为**中间设计入库**，供后续 r2 重建或仿生设计库扩充引用。
