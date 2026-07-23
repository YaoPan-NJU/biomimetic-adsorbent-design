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
| SL03 | chloroform | A04 | 单位点多弱作用协同预组织识别腔 | — | 在途 | — | 待写 |
| SL04 | HCBD | A01 | 环糊精空腔长度匹配+腔口卤键 | — | 在途 | — | 待写 |
| SL05 | TCDD | A05/A10（待定，避 A01 冲突） | 还原反应性捕获 或 平面受限腔+侧位氯锚定 | — | 在途 | — | 待写 |

## 承重证据核验状态（本会话 WebSearch 直核）

- BDE-209：PceA 结构 **PDB 4UR0**（Bommer 2014 Science；angle map 误记 4UQU 已更正）、norpseudo-B12（Biochemistry 2021 10.1021/acs.biochem.1c00271）、亦转化芳基卤（PDBj 5M8Y）；脱溴速率随溴数单调、BDE-209 半衰期 18 s（Tokarz 2008 ES&T 10.1021/es071989t）——均 verified。先例：分子笼 POP 吸附/传感 PFOA（Chen 2023 PMID 36538618）verified。
- PCB-209：非共平面 PCB 激动 PXR/CAR、共平面 PCB-77 不激活（Al-Salman 2012 10.1016/j.taap.2012.05.016）verified；扭转联苯分子识别先例（Weh 2023 Nat Commun 10.1038/s41467-023-35851-3）verified；PCB-209 无实测水浓度（Wolkersdorfer 2025 综述）verified 负面发现。
- TCDD：还原脱氯 peri 路径收敛 2,3,7,8（Barkovskii & Adriaens 1996 PMID 8953727）verified。
- chloroform：麻醉剂高亲和疏水腔弱极性作用（Liu/Loll/Eckenhoff 2005 FASEB J 19:567-576）verified。
- HCBD：CD-氯代溶剂增溶去除（Boving 等，HERO 3545601，被引 110）verified——但为增溶非选择性吸附，选择性吸附仍空白。

## 诚实总评（本批次前两槽）

BDE-209/PCB-209 首轮均 revise（66/64）、零 critical。这与这 5 个污染物在执行顺序中靠后、角度地图普遍标注内禀硬度（logKow 单调陷阱、水相弱卤键、无实测浓度、降解路线与好氧场景错配、先例收窄）一致，非降标。承重原型与选择性轴均经外部核验、无编造；主要缺口为工程/靶标合理性与选择性对照，重建方向已逐槽登记。二者均作为**中间设计入库**，供后续 r2 重建或仿生设计库扩充引用。
