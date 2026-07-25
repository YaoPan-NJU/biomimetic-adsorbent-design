# S42 · octocrylene · A02 · 氰基与酯羰基偶极定向氢键锚位阵列

- 污染物：奥克立林 OC（CAS 6197-30-4，C24H27NO2，logKow~6.1）
- 角度：A02 氰基与酯羰基偶极定向氢键锚位阵列（cyano + ester carbonyl dipole-directed H-bond anchor array）
- 状态：**terminated**（r1 即终止；双重热力学自证伪 + 选择性反转）
- r1 工作流：设计 ~74→攻击 2c/3h→裁决 55/terminate
- 创新性清单：A 部分通过（极性/偶极维独立于 A01 电子/电荷转移维）、B 通过（预组织双/三 H 键供体位点阵列材料架构）、C 不通过（蛋白口袋排水能力不可转译至 COF 孔壁）、D 不通过（EHMC 甲氧基 pKBHX > OC 氰基，选择性方向大概率反转）、E 部分通过（pKBHX 数据库核验但水相无实验）

## 角色交付
- 设计者（r1）：自评 ~74/100，诚实标注水相偶极 H 键对极弱受体未经溶液实验证实；硫脲 NH 水化能 ~33 kJ/mol 远超氰基-供体 H 键预期收益；EHMC 甲氧基 pKBHX ~0.5-0.7 可能不弱于 OC 氰基 ~0.3-0.5；5 条引用 metadata_verified。
- 攻击者（r1）：2 critical / 3 high。核心发现：脱水罚分 ≥66 kJ/mol 远超 H 键收益 ≤8 + 偶极静电 ≤5 kJ/mol，净 ΔG ≈ +53 kJ/mol；COF 介孔壁（1-3 nm）不具备蛋白口袋排水能力。
- 裁决者（r1）：独立重算 55/100。两项 critical 均验证成立，C1 构成方案内部自证伪。

## Critical 发现（2 条，基础性不可修复）

### C1 · 脱水罚分热力学自证伪
硫脲 NH 脱水罚分 ≥60 kJ/mol 远超 H 键+偶极总收益 ~13 kJ/mol，净 ΔG 为正 ~47 kJ/mol。COF 孔壁（1-3 nm 介孔）不具备蛋白口袋排除本体水的能力。设计者自己的数据（pKBHX、水化能、偶极估算）经标准热力学运算已证明核心机制不可行。所有正面先例（Fleming 2010 晶体结构、Turner 2012 CSD 统计）均在排除本体水的固相/蛋白口袋中。

### C2 · 选择性方向反转
EHMC 甲氧基 pKBHX（0.5-0.7）**高于** OC 氰基（0.3-0.5），加上 EHMC 共享酯羰基（pKBHX ~1.0），供体阵列的总 H 键收益方向不利于 OC——选择性大概率反转，材料可能优先结合 EHMC 而非 OC。

## 裁决六维评分

| 维度 | 得分 | 说明 |
|---|---|---|
| 因果闭环 | 9/20 | 核心机制经设计者自身数据自证伪（净 ΔG 正） |
| 选择性吸附机制 | 10/25 | 选择性方向反转（EHMC > OC） |
| 人工材料可转译性 | 13/20 | COF 孔壁无法实现蛋白级排水 |
| 原创性 | 9/15 | 偶极识别概念有贡献但热力学不可行 |
| 实验可证伪与对照 | 8/10 | 判据体系完整，门控实验设计合理 |
| 证据完整性 | 6/10 | pKBHX 数据库核验但水相无实验 |
| **合计** | **55/100** | **terminated** |

## 证据引用
- Laurence 2009 J Med Chem, DOI 10.1021/jm801331y（pKBHX 数据库，metadata_verified，PMID 19537797）
- Fleming 2010 J Med Chem, DOI 10.1021/jm100762r（腈基药效团综述，metadata_verified，PMC2988972）
- Turner 2012 CrystEngComm, DOI 10.1039/c2ce26052b（腈基 CSD H 键调查，metadata_verified）
- Weiqun 2005 J Mol Struct, DOI 10.1016/j.theochem.2005.06.012（硫脲-水 DFT/MP2，metadata_verified）
- Hopkins 2017 J Hazard Mater, DOI 10.1016/j.jhazmat.2017.05.016（OC 臭氧动力学，metadata_verified）

## 穷尽评估
A02 对 OC 实质耗尽（水相弱受体偶极 H 键识别的热力学硬约束，为基础性物理约束）。残余价值建议移交 A04（迈克尔共价捕获，热力学驱动力更强——共价键能 ~200-400 kJ/mol 远超 H 键 ~5-15 kJ/mol）或 A13（氰基偶极 + L 形腔正交双维协同——但须面对 A02 的脱水罚分问题）。下一候选首选 A04（迈克尔共价）或 A03（L 形腔纯几何）。
