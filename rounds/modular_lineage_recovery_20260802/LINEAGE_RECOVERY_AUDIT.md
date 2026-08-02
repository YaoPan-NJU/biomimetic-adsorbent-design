# 现行高价值路线的设计谱系试审计

日期：2026-08-02。该文件只使用仓库已核验的场景、证据和裁决，不增加新文献事实，不改变任何E1/E2状态，不授权采购、合成或实验。

## 1. 试审计目的

本轮把现有“整套方案”裁决拆为SP场景、BP生物原型、TR转译原则、ME材料实现、SR合成路线和ER实验释放六个模块。重点验证：材料制造或结构精度风险是否错误地连带否定了上游资产，以及现有“备份”是否真的保持同一个硬功能对应。

## 2. 谱系裁决

| 谱系 | SP | BP | TR | 当前材料实现 | 最早可能断裂 | 谱系处置 |
|---|---|---|---|---|---|---|
| `L-SCPFAS-01` 短链PFAS含水头基夹口—相邻低极性区 | retained | retained：SsuA为主，Bug/TRAP为支持 | retained：中性含水头基定位与相邻尾部占位分区 | SC-P02/PG-PMO为E1；SC-P03、SC-P08、SC-P09是被否决的实现或近先例体 | SC-P02若只因延迟共缩合不能形成孔口梯度，断裂在ME/SR；若同组成空间体在实际水中无增益，断裂在TR | `advance_current_embodiment`；制造失败时保留谱系并再平台化，因果功能失败时终止或重新转译 |
| `L-BPA-01` DmpR/PoxR固定单酚锚—可换壁门 | retained | retained：水相酚识别与效应物谱证据 | retained但有水相净锚风险：固定单锚与邻近壁身份共同改变双酚谱 | BPA20-01/AG-COF为E1；BPA20-04是较低复杂度候选，但原子级壁门更弱 | 晶格/孔径无法匹配属于ME/SR；去锚和换门均无独立谱效应属于TR | `advance_current_embodiment`；BPA20-04不能自动继承“备份”身份，必须证明仍实现同一TR，否则属于重新转译 |
| `L-DDT-01` 膜链有序度—软相分配—水化入口 | retained | retained：膜相态与脂链长度对DDT分配的非单调作用 | retained：用可测软相有序度而非总疏水量控制家族分配 | DDT50-01/LPO-SIP为E1；DDT50-02/03为链长扫描；DDT50-04为无模板膜分配实现 | 壳层或假模板制造失败属于ME/SR；`POSE`失败但`PACKING`通过只否决浅印迹实现；`PACKING`失败直接击穿TR | `advance_current_embodiment`；POSE失败时保留谱系并转向DDT50-04类无模板实现，PACKING失败时停止该转译原则 |
| `L-GENX-01` Bug/TauA头基固定—水合代价—支化醚增量 | retained | retained：羧酸钳与水合代价；旧HSA三点口袋仍无效 | class-wide头基/水合原则retained；GenX专属dummy几何conditional | GX50-01/BGE-SIP为concept_valid、M0阻断；GX50-02/03只是假模板几何变体 | `DUMMY-STOP`首先击穿GenX专属ME/TR，不击穿Bug/TauA的class-wide原则；SC-P02不受影响 | `repair_current_embodiment`限M0；若dummy方向性失败，拒绝GenX专属谱系，不以换dummy无限续命，保留class-wide谱系 |
| `L-DCP-01` EPS水化屏障—后置浅腔 | conditional | retained：EPS屏障为主，7M1I/5MA0只作姿态支持 | retained as hypothesis：屏障后置浅腔需场景和材料因果共同验证 | DCP20-01为concept_valid；DCP20-07/08不完整保留EPS屏障TR | 当前最早断裂在SP第二独立场景来源，不是材料合成 | `retain_prototype_retranslate`之前先关闭SP；环境门未关时不通过换材料推进E1 |
| `L-S1SYN-01` FABP脂肪酸功能启发的头基—有限链区 | retained | conditional：天然脂肪酸功能成立，PFOA只属B类机制参考 | revise：功能清单尚未冻结为确切、可制造的人工识别单元 | 尚无合格ME；过去材料漂移到肽/蛋白是错误实现 | 最早断裂在TR，不是载体或SR | `retain_prototype_retranslate`；不能通过反复更换载体掩盖人工识别单元未冻结 |

## 3. 对现有流程的具体修正

1. SC-P03、SC-P08等“材料终止”不再被解释为SsuA/Bug谱系终止。它们只是没有提供比SC-P02更好的可制造实现。
2. AG-COF制造失败不会自动否定DmpR/PoxR单锚—壁门原则；但MAPy梯度珠只有在同一硬对应可测时才是同谱系备份，不能因“更容易合成”直接继承。
3. DDT路线已有最清楚的失败分流：`POSE`和`PACKING`必须分别判定。前者失败可保留膜分配谱系，后者失败才否定核心转译。
4. DCP当前受场景模块阻断，材料再平台化不能修复环境证据缺口。
5. S1-SYN当前应重新转译TR，继续换载体属于错误层级修复。

## 4. 潘尧补充审阅视角的试用结论

补充视角最适合进入ME/SR和跨模块一致性审计，不应提前限制原型或材料创意。以后每个E1候选在Reviewer裁决前增加：初学实验者可操作性检查、合成专家逐步化学检查、设计—规格—合成—表征—再生一致性检查，以及难题—原型—机制—材料—合成—工程六环链检查。

具体经验项不直接成为禁用规则。例如偶联试剂、后修饰堵孔、磁性组分质量罚或强酸碱风险，都必须结合当前反应体系和可核查资料判断。未经针对性验证的经验只能生成待查问题，不能单独触发`embodiment_rejected`。

## 5. 状态影响与下一步

- SC-P02、BPA20-01和DDT50-01的E1纸面状态不变，性能仍未证实。
- GX50-01与DCP20-01继续为`concept_valid`，阻断模块分别为GenX专属TR/ME和DCP场景SP。
- 历史`terminated`记录不改写；后续引用时区分`embodiment_rejected`与`terminate_lineage`。
- 下一轮优先对所有仍为`concept_valid`且SP、BP、TR较强的路线补齐模块台账，再决定是修当前材料、再平台化还是停止谱系。
