# BMDL客观结构审计

> 数据来源：只读 PostgreSQL 快照  
> BMDL来源提交：`bd92dff5ddedc8e9f0c99be9d075f68641fefe16`  
> 导出安全状态：default transaction read only = `on`，transaction read only = `on`

## 结论

BMDL适合作为结构化原型线索和证据诚实性检查工具，但当前数据不足以直接决定新污染物选择性吸附材料。主要原因是有机微污染物匹配多处于探索通道，设计转译中推断内容占比高，并且多个目标会反复返回少数常见原型。正式设计必须先冻结模型独立方案，再根据配对盲评决定BMDL是进入设计辅助、仅做证据核验，还是完全退出设计阶段。

## 快照事实

| 指标 | 数值 | 解释 |
|---|---:|---|
| biological_prototypes | 48 | 包含primary、reference和quarantined等类别 |
| pollutant_profiles | 44 | 污染物画像数量 |
| match_weights | 130 | 原型与污染物的匹配记录 |
| performance_data原始行 | 3015 | 含重复导入，不可作为证据量 |
| 去除代理ID后的唯一性能行 | 1076 | 用于后续证据审查的最大候选集合 |
| 重复性能行 | 1939 | 占原始行的64.3% |
| 直接证据匹配 | 46 | 占匹配记录的35.4% |
| literature设计转译 | 10 | 总设计转译49条 |
| llm_inference设计转译 | 39 | 不得直接支持硬对应 |

## 匹配质量

- Lane分布：{"exploratory": 68, "lead": 54, "fact": 8}。
- 候选诚实性：{"inference": 68, "lead": 54, "fact": 8}。
- 高频原型：chitosan(27), polydopamine-coating(19), bone-structure(17), oyster-shell(14), plant-tannin(13), silk-fibroin(8), sulfate-reducing-bacteria(7), iron-oxidizing-bacteria(5)。
- PFOA、PFOS、BPA、SMX、CIP和Roxithromycin的候选主要集中于：chitosan(6), polydopamine-coating(5), plant-tannin(3), diatom-frustule(2), lotus-leaf(1), bone-structure(1)。

上述重复说明BMDL会把芳香性、疏水性、带电或含氢键位点的有机污染物压缩到相似原型族。该结果可提供起始线索，但不足以证明原型具备目标污染物选择性，更不能替代从生物识别、跨膜运输、门控结合或可逆释放机制出发的库外探索。

## 使用约束

1. BMDL结果不得在model-only方案冻结前进入设计者上下文。
2. `weight`仅表示规则或特征匹配，不解释为性能、选择性或真实可信度。
3. `exploratory`和`llm_inference`只能形成待核验线索。
4. 每项进入硬对应的机制必须回到原始文献核实生物功能、适用条件和可移植边界。
5. `performance_data`必须按自然字段去重，并逐条核实指标类型、材料归属和实验条件后才能引用。

## 待完成的正式判定

在十种候选污染物的问题陈述冻结后，对每种污染物分别生成model-only和bmdl-assisted方案，由隔离Reviewer盲评。最终按`research_contract.yaml`中的6/10胜出、平均提升5分、原创性下降不超过2分等门槛决定BMDL的角色。
