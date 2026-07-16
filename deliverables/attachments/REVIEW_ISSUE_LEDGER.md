# 审查问题与终态

## 终选方案

| 方案 | 历史裁决 | 最终裁决 | 设计级问题 | 仍待实验的主要风险 |
|---|---|---|---|---|
| D1-A | 89/revise | 93/pass | 0 critical，0 high | 水相汇聚、锁开体可比性、FRET/ROESY共证、真实水选择性、再生、成本 |
| D1-B | 80/revise → 86/revise | 89/pass | 0 critical，0 high | 蛋白表达/apo、固定负载、50 BV、HDX-MS、温和再生、蛋白酶/微生物 |

### D1-A 关闭记录

| issue | 问题 | 修订 | 终态 |
|---|---|---|---|
| R3-D1A-001 | TEMPO/DEER 与化学路线和工作水相不相容 | 改为25 °C同位素编辑ROESY，与寿命FRET共证 | design-closed |
| R3-D1A-002 | 保护基、标记顺序和AzAla保存不清楚 | 冻结Dde/Boc、裂解后标记、两次SPAAC放行 | design-closed |
| R3-D1A-003 | R-Lock可能不是单分子锁开体 | 冻结唯一桥、拓扑、聚集、开放和静态等效门 | design-closed；experiment risk |
| R3-D1A-004 | R-Rand锚点和支架密度不可比 | 改为一锚点、同官能团双臂异构体池 | design-closed；experiment risk |
| R3-D1A-005 | 单臂删除体不可执行 | 冻结R-Aonly/R-Bonly结构、SPPS、标记和物料配平 | design-closed；experiment risk |
| R3-D1A-006 | `Γacc` 到容量多1000倍 | 改为 `qth,access=0.030974Γacc` 并闭合干基/床/BV单位 | design-closed；experiment risk |
| R3-D1A-007 | 蛋白酶、微生物和azide替代解释 | active/失活蛋白酶、过滤×azide、CFU、质量平衡 | design-closed；experiment risk |
| R3-D1A-008 | 柱与再生操作不够冻结 | 固定床尺寸、流速、终点、积分和独立再生床 | design-closed；experiment risk |

### D1-B 关闭记录

| issue | 问题 | 修订 | 终态 |
|---|---|---|---|
| D1B-01 | 固定投料与床目标不闭合，后续又漏乘动态利用率 | 冻结Cin/BV/成本，反算负载；柱前只用 `BVmax,dynamic` | design-closed；experiment risk |
| D1B-02 | 构建体和apo状态未冻结 | RCSB双记录核对、FASTA/SHA、apo/1:1门 | design-closed；experiment risk |
| D1B-03 | sortase连接可能只是非特异残留 | 身份hold point、活性/水解比、跨结点肽、去酶和变性保留 | design-closed；experiment risk |
| D1B-04 | 2% MDCC亚群不能自动代表主床 | NEM/MDCC动力学等价、双步模型和HDX-MS正交判据 | design-closed；experiment risk |
| D1B-05 | 随机固定对照的1%释放子群有选择偏差 | 删除取向增量主张；B-RAND降为可选探索，不参与pass | closed by claim removal |
| D1B-06 | 再生可能只恢复去除率而损伤蛋白 | 全分段质量平衡、结构/选择性同步恢复、只再生组 | design-closed；experiment risk |
| D1B-07 | azide、蛋白酶和微生物效应不可分 | IC-UV方法、LOQ/无抑制门、多位点肽和完整蛋白泄漏 | design-closed；experiment risk |
| D1B-08 | 只比较受损蛋白，缺强工程基准 | `Gα`、唯一RESIN-1身份门、单位床体积突破和50 BV绝对线 | design-closed；experiment risk |

## 被否决概念

| 方案 | 主要否决理由 | 可保留内容 |
|---|---|---|
| 克拉霉素/核糖体 | A2062结合态异质性不是目标诱导门控 | 局部静态识别和痕量分析预实验 |
| PFOA/hL-FABP | PFOA特异动态证据不足，门户运动不能硬映射 | 双位点和PFAS链长谱静态筛查 |
| 硝酸盐/NrtA | 只有结合态晶体结构，apo来自模拟 | NrtA静态口袋及普通电再生子项目 |
| ODV/SERT | 盐响应材料壳不是SERT动态硬对应 | 静态印迹与通用抗污研究 |

完整攻击原文和Reviewer理由保存在 `rounds/round_1/`、`rounds/round_2/` 和 `rounds/round_3/`，本表不替代历史记录。
