# Round 3 终审 Reviewer：D1-A

## 1. 终审口径与结论

本轮评价“实验方案是否完整可执行”，不要求材料已经获得性能结果。已冻结且可直接判定的实验假说记为 `experiment risk`，不作为未解决 design high；证据外推、化学冲突、不可执行 SOP、无效对照或错误判据仍阻断 pass。

**结论：89/100，`revise`，暂不 pass。** 原 critical 已关闭；仍有 2 项 design high，均可通过局部文本/公式修订解决，不需要重构 D1-A 化学路线。修复后应做一次限域复审，再决定是否作为主方案交接。

## 2. 六维独立评分

| final_scoring | 得分 | 依据 |
|---|---:|---|
| causal_closure（20） | 17 | M0→S1→L0→D1→固相/再生链完整；单臂删位体尚不可执行 |
| selective_adsorption_mechanism（20） | 18 | 竞争物、R-Scramble/R-Rand、树脂/P7、金属/胶体排除和真实水均已纳入 |
| biomimetic_fidelity（20） | 18 | 1OIB/1IXG 定量映射和占据—闭合—抗置换链清楚，未复制蛋白选择性倍数 |
| originality（15） | 13 | 合成双臂肽夹、化学可比锁开体及室温 FRET/ROESY 双读出具有明确增量 |
| experimental_falsifiability_and_controls（15） | 13 | Gate 与切换严格，但单臂 SOP 和容量单位错误会影响裁决 |
| evidence_integrity（10） | 10 | 直接蛋白事实、邻近材料和人工假说分账准确 |
| **总分** | **89/100** | 达到分数线，但 2 项 design high 未关闭 |

## 3. 逐 attack issue 裁决

| attack issue | response 裁决 | 当前严重度/状态 | Reviewer 理由 |
|---|---|---|---|
| R3-D1A-001 | **接受关闭** | design-closed；experiment risk | TEMPO/DEER 被完全删除，改为不含可还原自由基的 25 °C 同位素编辑 ROESY；浓度、缓冲、指认、混合时间、效应量和 FRET 共证均已冻结 |
| R3-D1A-002 | **接受关闭** | design-closed | 中心 Dde、两臂 Boc、A/B 主链 N 端乙酰化、裂解后统计双标/HPLC 分离及两次 AzAla-SPAAC 放行已形成无歧义顺序；Pd/phenylsilane 已删除 |
| R3-D1A-003 | **接受关闭** | design-closed；experiment risk | 唯一桥、自由巯基、单分子双加成、聚集、拓扑、开放态及 `Kd/α/pKa/水合` 等效区间均已冻结；失败即切换且不得换桥 |
| R3-D1A-004 | **接受关闭** | design-closed；experiment risk | R-Rand 改为一锚点双臂异构体池，不再双倍消耗 DBCO；R-Scramble 单独承担主因果，锚点/官能团/OEG 配方可比 |
| R3-D1A-005 | **部分关闭** | **high/open** | `min` 公式、锁开等效 CI 和跨臂 ROESY 判据已修复；但 S1 又要求“两种单臂及其 1:1 混合物”排除独立弱位点，全文没有冻结两种单臂的 N→C 结构、锚点、端基、保护基或合成/纯化 SOP，故该必要对照目前不可执行 |
| R3-D1A-006 | **未关闭** | **high/open** | 总固定、可接近和动态利用率已分账，柱/成本口径也完整；但 `Γacc` 明确使用 µmol/g 时，`qth,access` 应为 `0.030974×Γacc` mg P/g，而正文写成 `30.974×Γacc`，导致 `facc/Udyn` 和工程 go/no-go 相差 1000 倍 |
| R3-D1A-007 | **接受关闭** | design-closed；experiment risk | active/失活 proteinase K、过滤×azide、固定 CFU、azide 残留、水化学、酶活及完整受体/碎片质量平衡均已冻结；替代解释不能分离即停止 |
| R3-D1A-008 | **接受关闭** | design-closed；experiment risk | 柱径/床高、共同进水、pH/温度、流向、流速、重复、终点、积分，以及独立再生床、BV/时间/冲洗和唯一窗口排序均可复现 |

## 4. 必须修订的两项

1. **补全单臂对照：** 为 Arm-A-only 与 Arm-B-only 各写唯一完整结构、AzAla 锚点位置、N/C 端、Arg/Cit/Lys/Cys 端基、SPPS 保护/脱保护、HPLC/LC-MS 放行及可比性门槛；明确非共价 1:1 混合物的总位点、浓度和缓冲。未补前不得以单臂结果关闭跨臂 1:1。
2. **修正容量单位：** 当 `Γacc` 为 µmol/g-dry 时，将 `qth,access` 改为 `0.030974×Γacc` mg P/g-dry；随后重新核对 `facc`、`Udyn`、`Γacc=10 µmol/g` 对应的 0.30974 mg P/g 上限、柱三种容量门槛和成本公式。所有互算必须使用同一干湿换算和共同突破曲线。

两项均是局部设计修复，不需要等待实验结果。修订后若公式、单臂结构和 Gate S1 对照物料账一致，可关闭 design high。

## 5. 剩余 experiment risks

- M0 可能显示冻结肽夹无法覆盖 PBP 相对运动或形成多点汇聚。
- R-Lock 可能因 p-terphenyl 疏水性而难溶、聚集或改变静态亲和。
- R-Flex 可能在全水相中不优于 R-Scramble/R-Rand，或 FRET 与 ROESY 不共证。
- 固相位点密度、DOM/金属背景、微生物/蛋白酶、温和再生、五循环容量及成本可能不过门槛。

这些均已有明确实验和停止条件，属于可接受的实验风险；任何失败必须按 Gate 顺序切换，不能修改序列、桥或阈值继续包装。

## 6. 主/备建议

**主方案建议：D1-A 在上述两项 high 修订并通过限域复审后，作为 primary 进入实验。** 当前版本尚不应直接交接，但修复范围小，且静态/动态生物依据、化学实现与因果门禁最完整。

**备选建议：按 FINALIST_BRIEF 保留 D1-B 的独立 backup 地位。** 本评审未读取或评价 D1-B 的当前实现质量；D1-A 若 M0、S1、L0、D1 或温和再生失败，应按既定合同切换。两案均失败时回到新原型搜索，不强选。

## 7. Final limited re-review

### 7.1 复审范围与最终结论

本次仅依据当前 `D1A_FINAL.md` 与本文件首次终审记录，限域复核上次遗留的两项 design high，并扫描相关修订是否引入新的 critical/high；不重新裁决尚待实验验证、但已冻结判据和失败门的性能假说。

**最终结论：93/100，`pass`。** 两项原 design high 均已按可执行结构、SOP、物料账和单位闭环关闭；未发现修订引入新的 critical/high。这里的 pass 指实验方案已达到交接与执行条件，不表示材料性能已经获得验证。全部 experiment risks 仍须按既定 Gate 实测，失败时执行已冻结的停止或切换规则。

### 7.2 两项原 design high 关闭核验

| issue | final limited re-review | 最终状态 | 核验依据 |
|---|---|---|---|
| R3-D1A-005 | **接受关闭** | design-closed；experiment risk | 第2.2节给出 `Arm*`、R-Aonly/R-Bonly 的唯一 N→C 结构、中心 Lys α/ε 接法、AzAla 锚点、端基和标记体；第6.3节冻结两种删除体各自的保护/脱保护、乙酰封端、CAM、标记、独立纯化及 HPLC/LC-MS/MS/SPAAC 放行 SOP；Gate S1 将 R-Flex、两种单臂和 1:1 混合物按 arm module、Arg/Cit、体积及结构读数配平，并以 `Garm` 下限和 ROESY/FRET 等效 CI 裁决，精度不足亦判失败。原“必要对照不可执行”缺口已消失。 |
| R3-D1A-006 | **接受关闭** | design-closed；experiment risk | 第9节已将 `Γacc` 固定为 µmol accessible site/g-dry，并修正为 `qth,access=0.030974×Γacc` mg P/g-dry；30.974 µg/µmol 的换算、`facc`、干基/床体积换算和 `Udyn` 两条等价公式均显式闭合，且用 `Γacc=10` 对应 0.30974 mg P/g-dry、`Qcol=0.25` 对应 `Udyn=0.807` 完成数量级核查。原 1000 倍单位错误已消失。 |

相关修订未造成新的结构歧义、物料不配平、判据自相矛盾或工程单位断裂；因此本次扫描结果为 **0 critical、0 high**。

### 7.3 最终六维评分

| final_limited_scoring | 得分 | 最终依据 |
|---|---:|---|
| causal_closure（20） | 19 | M0→S1→L0→D1→固相/再生因果链完整，单臂删除体及其非共价混合对照现已可执行 |
| selective_adsorption_mechanism（20） | 18 | 竞争阴离子、独立序列/拓扑对照、树脂/P7、金属/胶体排除及真实水矩阵保持完整 |
| biomimetic_fidelity（20） | 18 | 结构映射与占据—闭合—抗置换链清楚，且未把蛋白事实外推为材料性能既成事实 |
| originality（15） | 13 | 双臂肽夹、化学可比锁开体及室温 FRET/ROESY 双读出仍具明确方法增量 |
| experimental_falsifiability_and_controls（15） | 15 | 两种单臂及 1:1 混合物的合成、放行、物料配平、联合门和 CI 失败规则均已冻结；容量裁决单位闭合 |
| evidence_integrity（10） | 10 | 直接生物事实、邻近材料证据与待验人工假说继续分账，未以未完成性能实验冒充证据 |
| **总分** | **93/100** | **无 critical/high，达到最终 pass 条件** |

### 7.4 Final issue status 与决定

- `R3-D1A-001` 至 `R3-D1A-008`：全部 **design-closed**。
- `R3-D1A-001`、`003`、`004`、`005`、`006`、`007`、`008` 中尚待实测的性能、等效性、容量、耐久与成本结果保留为 **experiment risk**，不回升为 design high。
- 最终决定：**`pass`，D1-A 可作为已冻结的 primary 实验方案交接执行。** 若任一 Gate 失败，必须按正文已冻结规则停止、切换或回到新原型搜索，不得事后改序列、桥、阈值或单位包装结果。
