# fresh_1000 Round 2 — 新一轮千方案马拉松

> 版本：v1.0 | 日期：2026-07-29 | 状态：计划

---

## 1. 目标与范围

### 1.1 总目标

- 20 种污染物 × 50 方案 = **1000 方案槽**
- 每个方案必须与 R1 已覆盖的角度/机制/材料组合**正交**（不重复）
- 通过线：**85/100**，零未决 critical/high
- 创新性清单（`INNOVATION_CHECKLIST.md` A-E 五维）必须通过
- 仿生原型库从 83 条扩充至 **150+** 条

### 1.2 与 R1 的关系

- R1 已完成 ~33+ 方案（含 9 个正式通过方案 + 5+ 个自评通过方案），经 10 轮迭代
- R2 的 1000 个方案槽**独立于 R1**，不继承 R1 的方案编号
- R1 的通过方案作为"已占据机制空间"记录于 `R1_OCCUPIED_SPACE.yaml`，R2 须避开
- R1 的终止方案作为"已知陷阱"注入 R2 设计，避免重复踩坑
- R1 的自评通过但未经正式裁决的方案，R2 可选择性补完正式裁决流程

### 1.3 质量目标

- 每种污染物至少 **3 个通过方案**
- 全计划至少 **60 个通过方案**（6% 通过率）
- 通过方案须通过独立攻击-裁决流程
- 仿生原型库扩充至 150+ 条（当前 83 条，净增 67+）

### 1.4 R1 最终状态基线

| 指标 | R1 数值 |
|------|---------|
| 污染物覆盖 | 20/20 全覆盖 |
| 迭代轮次 | 10 轮 |
| 方案尝试 | 26 attempted |
| 正式通过 | 9（PFOA A02/BPA A01/PFBS A17/NP A01/Dieldrin A01/ROX A01/Octocrylene A01/Endosulfan A01/BDE-209 A07） |
| 终止 | 17 |
| 自评通过（≥85，待正式裁决） | 14 种污染物 |
| 仿生原型库 | 83 条 |
| 弱点级别 | 所有 20 种污染物方案弱点均为 low |

---

## 2. 差异化策略

### 2.1 机制空间去重

- R1 每个已通过方案的选择性机制作为"已占据"记录（见 `R1_OCCUPIED_SPACE.yaml`）
- R2 每个方案须在 EXEC_SPEC 中声明与 R1 已占据机制的**正交性**
- 正交性判据：选择性机制的核心识别维度不同

| R1 已占据识别维度 | 代表方案 | R2 须避开的核心机制 |
|-------------------|---------|-------------------|
| 脲/硫脲氧阴离子洞 | PFOA A02 | 双脲氧阴离子洞 + 机制三分层 |
| DmpR 锚+门 COF | BPA A01 | 固定酚锚 + 桥连区空间门 |
| T/P 双位点头基反差 | PFBS A17 | T 三足硫脲/P squaramide 反差签名 |
| ipso α-四级碳拓扑腔 | NP A01 | Sphingobium ipso 途径几何转译 |
| exo-环氧双氢键腔 | Dieldrin A01 | GABA/Rdl 刚性疏水腔 + 方酰胺 |
| 核糖体 NPET 碱基裂缝 | ROX A01 | 23S rRNA 核苷酸碱基阵列受限读取 |
| 供体-受体 CT 识别腔 | Octocrylene A01 | 电子亏缺氰基丙烯酸酯核 |
| Lewis 酸水解捕获 | Endosulfan A01 | 介孔氧化物 Lewis 酸界面 |
| 脱氯化氢酶双基序 | DDT A01 | β-消除双基序反应性识别 |

### 2.2 材料平台多样性

- R1 已使用的材料平台记录于 `R1_OCCUPIED_SPACE.yaml`
- R2 **优先使用 R1 未覆盖的材料平台**
- 材料平台多样性作为创新性 B 维的加分项

R1 已覆盖材料平台：
- PAF-1（PFOA A02）
- 晶态 β-酮烯胺 COF（BPA A01）
- POP 接枝活性炭/多孔聚合物（PFBS A17）
- 非蛋白间苯二酚芳烃深腔笼（NP A01）
- SBA-15 介孔硅 + 方酰胺（Dieldrin A01）
- 全有机刚性凹形裂缝半笼（ROX A01）
- 离散分子笼（Octocrylene A01）
- 介孔氧化物（Endosulfan A01）
- 萘扩展 resorcinarene 离散笼（DDT A01）

R2 优先探索的新材料平台方向：
- 共价有机框架（COF）新拓扑
- 超交联聚合物（HCP）功能化变体
- 分子印迹聚合物（MIP）新模板策略
- 多孔有机聚合物（POP）新骨架
- 碳纳米管/石墨烯衍生受限腔
- 氢键有机框架（HOF）
- 共价三嗪框架（CTF）
- 大环主体功能化材料（柱芳烃/杯芳烃新衍生物）
- 仿生矿化衍生材料
- DNA 纳米结构模板材料

### 2.3 仿生原型扩展

- R1 使用过的仿生原型记录于 `R1_OCCUPIED_SPACE.yaml`
- R2 **优先使用 R1 未覆盖的仿生原型**
- 仿生原型库从 83 条扩充至 150+ 条

R1 已覆盖仿生原型（9 个通过方案）：
1. 丝氨酸蛋白酶氧阴离子洞原理（PFOA A02）
2. DmpR 型固定酚感应转录因子（BPA A01）
3. ModA/NTCP 几何识别原理（PFBS A17）
4. Sphingobium ipso 羟基化途径（NP A01）
5. GABA/Rdl 刚性疏水腔（Dieldrin A01）
6. 23S rRNA NPET 核苷酸碱基阵列（ROX A01）
7. 光合反应中心电子预组织（Octocrylene A01）
8. 矿物表面 Lewis 酸水解界面（Endosulfan A01）
9. 脱氯化氢酶 β-消除双基序（DDT A01）

R2 优先探索的新原型方向（从 83 条库中未使用者 + 新挖掘）：
- 传质与分级结构类：木质部导管、硅藻壳、骨单位
- 自组装类：病毒衣壳、铁蛋白笼、微管
- 界面分配类：肺表面活性剂、细胞膜脂筏
- 动态响应类：含羞草触觉运动、松果体褪黑素节律
- 生物矿化类：贝壳珍珠层、有孔虫壳
- 降解/转化类：还原脱卤酶、CYP450、白腐真菌木质素过氧化物酶
- 其他分子识别类：TTR 反向模式通道、SBP 预组织氢键、lipocalin 尺寸窗口

---

## 3. 中间产物持久化策略

### 3.1 仿生设计库扩展

每个方案的设计过程中，以下中间产物须独立提取并持久化：

#### (a) 仿生原型卡片

- 文件：`rounds/fresh_1000_R2/prototype_cards/<prototype_id>.yaml`
- 内容：原型名称、来源（蛋白/非蛋白/动态）、适用污染物、识别机制、文献支撑、R1 是否已使用
- 每个新发现的原型独立成卡
- 格式：

```yaml
prototype_id: PROTO_R2_XXX
name: "<原型名称>"
source_type: protein | nonprotein | dynamic | mineral | supramolecular
biological_origin: "<生物来源描述>"
applicable_pollutants: ["<slug1>", "<slug2>"]
recognition_mechanism: "<识别机制简述>"
literature_support:
  - doi: "<DOI>"
    title: "<标题>"
    year: <年份>
    claim_supported: "<支持的主张>"
    evidence_tier: fact | source_backed_lead | inference | design_hypothesis
r1_used: false  # R1 是否已使用
r2_first_used_in: "<scheme_id>"  # R2 首次使用于
```

#### (b) 机制映射记录

- 文件：`rounds/fresh_1000_R2/mechanism_maps/<pollutant>_<mechanism>.yaml`
- 内容：识别机制名称、仿生来源、材料实现、选择性签名、水相可行性评估
- 每个机制-污染物组合独立记录
- 格式：

```yaml
mechanism_id: MECH_<pollutant>_<NNN>
pollutant: "<slug>"
mechanism_name: "<机制名称>"
biological_source: "<仿生来源>"
material_implementation: "<材料实现方式>"
selectivity_signature:
  primary_dimension: "<主选择性维度>"
  orthogonal_dimensions: ["<正交维度1>", "<正交维度2>"]
aqueous_feasibility:
  tfg_assessment: pass | fail | borderline
  dehydration_penalty_kj_mol: <数值>
  net_binding_free_energy_kj_mol: <数值>
r1_overlap: false  # 是否与 R1 机制重叠
```

#### (c) 角度地图更新

- 文件：`rounds/fresh_1000_R2/angle_maps/<pollutant>_ANGLES.yaml`
- 内容：R1 已覆盖角度（锁定）、R2 新角度（待探索）、角度预分类
- 每个污染物的角度地图随 R2 推进持续更新
- 格式：

```yaml
pollutant: "<slug>"
r1_locked_angles:
  - angle_id: A01
    mechanism: "<R1 机制>"
    scheme: "<R1 方案编号>"
    status: passed | terminated | self_eval_passed
r2_new_angles:
  - angle_id: R2_A01
    mechanism: "<R2 新机制>"
    pre_screen:
      tfg: pass | fail | borderline
      pads_score: <数值>
      odc_dimensions: <数值>
      verdict: S | A | B | X
    status: pending | in_progress | passed | terminated
```

### 3.2 知识图谱构建

- 文件：`rounds/fresh_1000_R2/knowledge_graph.yaml`
- 内容：原型-机制-材料-污染物的四维关联网络
- 用途：支持后续仿生设计库扩展和论文撰写
- 格式：

```yaml
knowledge_graph:
  version: "1.0"
  last_updated: "<日期>"
  nodes:
    prototypes: [<prototype_id>, ...]
    mechanisms: [<mechanism_id>, ...]
    materials: [<material_platform>, ...]
    pollutants: [<slug>, ...]
  edges:
    prototype_mechanism: [[proto_id, mech_id, evidence_strength], ...]
    mechanism_material: [[mech_id, material, feasibility], ...]
    mechanism_pollutant: [[mech_id, slug, selectivity_score], ...]
  statistics:
    total_prototypes: <N>
    total_mechanisms: <N>
    total_materials: <N>
    total_pollutants: 20
    connectivity_density: <N>
```

### 3.3 提取时机

- 每个方案完成 r1 设计后**即提取中间产物**（不需等到通过）
- 终止方案也提取"负面知识"（什么不可行、为什么）
- 每完成一种污染物的全部 R2 方案后，汇总更新该污染物的角度地图

---

## 4. 执行策略

### 4.1 Phase A 复用与扩展

- R1 已完成 20/20 污染物的 Phase A（BRIEF + DESIGN_SPACE）
- R2 **复用 R1 的 Phase A 文件**（`rounds/fresh_1000/<slug>/BRIEF.md` + `DESIGN_SPACE.md`）
- 须扩展角度地图：标注 R1 已覆盖角度，新增 R2 候选角度
- 每种污染物的 R2 角度地图 = R1 角度地图 + R2 新增角度
- Phase A+ 快速预筛（TFG + PADS + ODC）对 R2 新角度重新执行

### 4.2 Phase B 执行

- 每槽 15-25 分钟串行执行
- 每槽 2 轮设计-攻击-裁决，至多 3 次重建
- 每完成一个方案即提取中间产物
- 每个方案独立提交并推送到 `origin/Ultimate`

### 4.3 执行优先级

| 优先级 | 污染物组 | 理由 |
|--------|---------|------|
| **第一优先** | R1 已有通过方案的污染物（PFOA/BPA/PFBS/NP/Dieldrin/ROX/Octocrylene/Endosulfan/DDT/BDE-209） | 补充更多正交方案，加深方案库深度 |
| **第二优先** | R1 有方案但未通过的污染物（DCP26/PFHxS/GenX/PCP/β-HCH/Chloroform/HCBD/PCB-209/DDE） | 新角度突破，利用 R1 失败教训 |
| **第三优先** | R1 硬骨头污染物（TCDD/DCP26/PFHxS/BDE-209 等） | 需创新识别轴，先例密集或机制挑战大 |

### 4.4 广度优先策略

- 每种污染物至少 **1 个 R2 方案**后才开始第二种
- 20 种全部访问一轮后回溯补角
- 广度优先第一轮目标：M2 里程碑

### 4.5 R1 陷阱注入

每个污染物的 R2 设计须注入 R1 已知陷阱：

| 失败模式 | R1 案例 | R2 规避策略 |
|---------|---------|-----------|
| FM1 先例饱和 | PFOA 10 槽 9 终止 | PADS 评估前置，直接先例 ≥4 篇换角度 |
| FM2 单参数单调 | DCP26 3 槽全终止 | ODC 检查前置，须 ≥2 正交维度 |
| FM3 中性氢键对强水合阴离子 | GenX A01=36 分 | TFG 检查前置，永久阴离子须额外正交维度 |
| FM4 框架内拮抗 | PFOA A09 天花板 77 | 设计阶段识别拮抗对，角度选择阶段规避 |

---

## 5. 质量门控

### 5.1 预筛机制（继承 R1 + 新增）

| 预筛 | 全称 | 检查内容 | R2 新增 |
|------|------|----------|---------|
| **TFG** | 热力学可行性门 | 结合自由能 vs 竞争物 vs ng/L 工况 | — |
| **PADS** | 先例密度评估 | 直接/方向/平台先例扣分 | R1 已占据机制空间额外扣分 |
| **ODC** | 正交维度检查 | ≥2 正交维度，非单参数单调 | — |
| **R1-DEDUP** | R1 去重检查 | 与 R1 已占据机制/材料/原型正交性 | **新增** |

### 5.2 R1-DEDUP 预筛详情

**检查内容**：
1. 选择性机制核心识别维度是否与 R1 已通过方案重叠
2. 材料平台是否与 R1 已通过方案相同
3. 仿生原型是否与 R1 已通过方案相同
4. 角度定义是否与 R1 已终止方案的失败角度本质相同

**判定规则**：
- 机制 + 材料 + 原型三者均与 R1 某通过方案相同 → **不通过**，换角度
- 机制与 R1 终止方案本质相同（已证明不可行） → **强烈建议换角度**，除非可声明新正交维度
- 仅材料平台相同但机制不同 → **通过**，但 PADS 加扣平台先例分

### 5.3 评分标准（继承 R1）

六维量表 100 分制（参见 `GLOBAL_SPEC.md` G4）：

| 维度 | 满分 |
|------|------|
| 因果闭环 | 20 |
| 选择性吸附机制 | 25 |
| 人工材料可转译性 | 20 |
| 原创性 | 15 |
| 实验可证伪与对照 | 10 |
| 证据完整性 | 10 |

- 通过线：**≥ 85/100**
- 零未决 critical/high
- 创新性清单必须通过
- 含至少 1 条硬功能对应
- 提供可信的台架合成 SOP
- 每个核心主张均映射到测量与因果对照

### 5.4 科学评审（继承 R1）

- 通过方案须经过独立科学评审
- 评审维度：仿生映射正确性 + 吸附性能可行性
- 评审者不得读取设计者隐藏推理

---

## 6. 里程碑

| 里程碑 | 目标 | 条件 |
|--------|------|------|
| **M1** | 仿生原型库扩充至 120 条 | Phase A 扩展完成 + 新原型挖掘 |
| **M2** | 20/20 污染物各至少 1 个 R2 方案 | 广度优先第一轮完成 |
| **M3** | 100 个 R2 方案完成 | Phase B 批量推进 |
| **M4** | 30 个 R2 方案通过 | 质量筛选 |
| **M5** | 60 个 R2 方案通过 | 最终目标 |
| **M6** | 知识图谱完成 | 四维关联网络构建 |

---

## 7. 文件结构

```
rounds/fresh_1000_R2/
├── SPEC.md                    # 本文件
├── STATUS.yaml                # 实时状态追踪
├── R1_OCCUPIED_SPACE.yaml     # R1 已占据机制空间记录
├── DECISIONS.md               # 决策日志
├── prototype_cards/           # 仿生原型卡片（每个新原型独立 .yaml）
├── mechanism_maps/            # 机制映射记录（每个机制-污染物组合独立 .yaml）
├── angle_maps/                # 角度地图更新（每个污染物独立 .yaml）
├── knowledge_graph.yaml       # 知识图谱（原型-机制-材料-污染物四维网络）
├── <pollutant>/               # 各污染物目录
│   ├── BRIEF.md              # 继承 R1（符号链接或复制）
│   ├── DESIGN_SPACE.md       # 继承 R1 + R2 扩展
│   └── SCHEMES/              # R2 方案文件
│       └── R2_<Snn>_A<nn>_<简述>.md
└── _wip/                     # 工作中间文件
```

---

## 8. 与 R1 Spec 框架的关系

- **继承** `GLOBAL_SPEC.md` 全部要素（G1-G10）
- **继承** 分类 Spec（5 组：A-PFAS / B-酚类 / C-有机氯 / D-卤代小分子 / E-大环紫外）
- **继承** 执行 Spec 格式
- **新增** R1-DEDUP 预筛
- **新增** 中间产物持久化要求（原型卡片、机制映射、角度地图、知识图谱）
- **新增** 仿生原型库扩充目标（83 → 150+）
- **新增** R1 陷阱注入机制

---

## 9. 污染物清单（与 R1 相同）

| 序号 | 简称 | 全称 | slug | R1 状态 |
|------|------|------|------|---------|
| 1 | TCDD | 2,3,7,8-四氯二苯并-p-二噁英 | tcdd | R1: A01=70 revise_phase0（卤键笼，天花板 ~78-82） |
| 2 | 2,6-DCP | 2,6-二氯苯酚 | dcp26 | R1: A01-A03 全终止，A04 进行中（卤键 σ 空穴） |
| 3 | β-HCH | β-六氯环己烷 | betahch | R1: A01=45 终止（γ-CD 包合被实验反向否定） |
| 4 | 三氯甲烷 | 三氯甲烷（氯仿） | chloroform | R1: A01=45 终止（α-CD 尺寸匹配，亲和力缺口） |
| 5 | PCP | 五氯苯酚 | pcp | R1: A01 自评 85-87（TTR 反向模式通道） |
| 6 | PFBS | 全氟丁烷磺酸 | pfbs | R1: A17=85 通过（T/P 双位点头基反差） |
| 7 | PFHxS | 全氟己烷磺酸 | pfhxs | R1: A01/A07 全终止（头基/链长识别内禀硬度） |
| 8 | PFOA | 全氟辛酸 | pfoa | R1: A02=85 通过（脲/硫脲氧阴离子洞 POP） |
| 9 | GenX | 六氟环氧丙烷二聚酸 | genx | R1: A01=36/A03=61 全终止（中性氢键不可行） |
| 10 | HCBD | 六氯丁二烯 | hcbd | R1: A02 进行中（卤键供体阵列） |
| 11 | BDE-209 | 十溴二苯醚 | bde209 | R1: A07=85 通过（r5 通过） |
| 12 | BPA | 双酚 A | bpa | R1: A01=86 通过（DmpR 锚+门 COF） |
| 13 | NP | 壬基酚 | np | R1: A01=92 通过（ipso α-四级碳拓扑腔） |
| 14 | PCB-209 | 多氯联苯-209 | pcb209 | R1: A01+A03 进行中（扭转轮廓×卤键） |
| 15 | 奥克立林 | 奥克立林 | octocrylene | R1: A01=85 通过（供体-受体 CT 识别腔） |
| 16 | DDE | 滴滴伊 | dde | R1: A01=75 revise（平面轮廓形状读出） |
| 17 | DDT | 滴滴涕 | ddt | R1: A01=86 通过（脱氯化氢酶双基序） |
| 18 | 狄氏剂 | 狄氏剂 | dieldrin | R1: A01=89 通过（exo-环氧双氢键腔） |
| 19 | 硫丹 | 硫丹 | endosulfan | R1: A01=85 通过（Lewis 酸水解捕获） |
| 20 | ROX | 罗红霉素 | rox | R1: A01=85 通过（核糖体 NPET 碱基裂缝） |

---

## 10. 执行顺序

R2 执行顺序按五梯队（继承 R1 化学分组 + 优先级排序）：

| 梯队 | 分组 | 污染物 | R2 执行依据 |
|------|------|--------|-----------|
| 1 | A 组（PFAS） | PFOA, PFBS, PFHxS, GenX | R1 机制理解最深，R2 须找全新识别轴 |
| 2 | D 组（酚类） | BPA, NP, 2,6-DCP | R1 有 2 个通过方案，R2 补充正交方案 |
| 3 | E 组（大环/紫外） | ROX, Octocrylene | R1 已有通过方案，R2 扩展类内选择性 |
| 4 | C 组（有机氯） | DDT, DDE, Dieldrin, Endosulfan, β-HCH, TCDD, PCB-209 | R1 有 3 个通过方案，R2 加深疏水腔/几何识别 |
| 5 | B 组（卤代/其他） | PCP, HCBD, Chloroform, BDE-209 | R1 先例稀疏，R2 探索新识别轴 |

每个梯队内部按污染物执行 Spec 完成顺序推进；梯队间不严格串行，但高梯队优先。

---

## 11. 节奏与推送

- Phase A 扩展（角度地图 + R1 锁定标注）：每种污染物 1 份 R2 角度地图
- Phase B 以单个方案槽为单位执行（每槽一个独立工作流，设计-攻击-裁决串行，约 15-25 分钟）
- 每完成一个方案（通过或终止）：单独提交并推送 `origin/Ultimate`
- `STATUS.yaml` 每批更新；`HANDOFF.md` 与 `PROJECT_STATE.yaml` 每个污染物完成时更新
- 证据台账 `research/evidence/evidence_ledger.csv` 按批追加核验条目
- 中间产物（原型卡片/机制映射/角度地图）每方案完成后即提取

---

## 12. 历史教训继承

R2 继承 R1 全部历史教训，包括但不限于：

1. **水相脱水罚分**：中性氢键供体对强水合阴离子的水相选择性结合本质弱（GenX A01=36, PFHxS A01=70）
2. **先例饱和**：PFOA 10 槽 9 终止，反映 PFAS 吸附先例真实饱和
3. **单参数单调陷阱**：DCP26 3 槽全终止，选择性退化为 pKa 单调
4. **框架内拮抗**：PFOA A09 捕获-抗污拮抗四轮持续未解
5. **ng/L 动力学**：反应性捕获方案在 pM 浓度碰撞频率不足
6. **热力学不可能三角**：Dieldrin A03 Koc ~5×10⁶ vs 离散主体 Ka 差 3 数量级
7. **实验反向否定**：β-HCH A01 γ-CD 包合被 Hosangadi 1985 实验反向否定

---

## 附录：R1 关键数据引用

- R1 规约：`rounds/fresh_1000/SPEC.md`
- R1 全局 Spec：`rounds/fresh_1000/GLOBAL_SPEC.md`
- R1 最终状态：`rounds/fresh_1000/STATUS.yaml`
- R1 决策日志：`rounds/fresh_1000/DECISIONS_2026-07-21.md`
- 仿生原型库：`data/bmdl_snapshot/biological_prototypes.json`（83 条）
- 创新性清单：`INNOVATION_CHECKLIST.md`
- 仿生设计框架：`docs/BIOMIMETIC_DESIGN_FRAMEWORK.md`
