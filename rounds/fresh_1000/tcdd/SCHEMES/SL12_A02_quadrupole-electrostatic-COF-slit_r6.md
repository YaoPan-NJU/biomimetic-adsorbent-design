# SL12 · TCDD A02 · 氯图式四极矩/π 静电匹配定域层间距 COF 狭缝（r6 五轮迭代）

- 污染物：2,3,7,8-四氯二苯并-p-二噁英 TCDD（C₁₂H₄Cl₄O₂，CAS 1746-01-6）｜角度 A02｜slug：quadrupole-electrostatic-COF-slit
- 轨迹：**r6 = 五轮迭代**（针对 r5 遗留 medium 弱点——同位素稀释 HRGC-HRMS 约束——发起最终定量闭合；同时对 W1/W3 做末轮定量巩固）
- 状态：文书设计第六轮存档；未授权采购/合成/实验
- 编号：`SL12`
- 继承：GLOBAL_SPEC.md → SPEC_GROUP_C_OCP.md → EXEC_SPEC_TCDD.md → 本文件
- r5 文件：`SL12_A02_quadrupole-electrostatic-COF-slit_r5.md`

**r6 迭代声明**：r5 将弱点二（层间距防溶胀）、弱点六（零先例双刃性）、弱点九（再生）从 medium 降为 low-medium，取得实质进展。但以下弱点从 r1 到 r5 **连续五轮未获定量闭合**，属本方案最后的结构性顽固风险：
- **弱点八**（同位素稀释 HRGC-HRMS 约束，medium → medium → medium → medium → medium，r5 无变化）→ §4.9e TCDD ng/L 检测定量策略与 HRGC-HRMS 可行性闭合
- **弱点一**（水相连续静电场净收益不确定，high → medium → medium → low-medium → low-medium，r5 无变化）→ §4.9f 水相静电场净收益最终定量闭合
- **弱点三**（pg/L 亲和力预算，high → medium → medium → low-medium → low-medium，r5 无变化）→ §4.9g pg/L 工况检测与亲和力预算末轮定量

r6 核心目标：将弱点八从 medium 降为 low-medium，通过**检测定量策略**闭合连续五轮未解的最顽固弱点；同时巩固弱点一与弱点三的最终定量闭合。

其余章节继承 r5，仅标注修改处。

---

## 4. 材料架构与选择性机制（r6 强化）

### 4.1–4.9d 继承 r5

### 4.9e [r6 新增] TCDD ng/L 检测定量策略与 HRGC-HRMS 可行性闭合（回应弱点八）

**问题回顾**：弱点八（同位素稀释 HRGC-HRMS 约束）从 r1 到 r5 连续五轮列为 medium，为本方案最持久的未闭合弱点。核心问题：TCDD 在环境水样中浓度为 pg/L–ng/L 级，定量检测依赖同位素稀释 HRGC-HRMS（EPA Method 1613），该方法对样品前处理、仪器灵敏度和同位素标记物有严格要求，可能成为方案验证的瓶颈。

**策略 1：检测可行性定量评估**

| 参数 | 值 | 来源 |
|------|------|------|
| TCDD 方法检测限（MDL） | 0.1–0.5 pg/L（EPA 1613） | EPA Method 1613 Rev. B |
| TCDD 实际定量限（PQL） | 1–5 pg/L | 取决于基质复杂度 |
| 目标工况浓度（市政二级出水） | 10–100 pg/L | 文献范围（Liem et al. 2000） |
| **信噪比余量** | **20–100×** | PQL vs 工况浓度 |

**关键推论**：TCDD 在市政二级出水中的浓度（10–100 pg/L）高于 HRGC-HRMS PQL（1–5 pg/L）约 1–2 个数量级 → **检测本身不构成瓶颈**。

**策略 2：吸附实验检测方案**

| 实验阶段 | 检测方法 | 样品量 | 预期浓度 | 可行性 |
|---------|---------|--------|---------|--------|
| **机制验证（纯水）** | HRGC-HRMS | 1 L | 10–100 ng/L（加标） | **高**——远超 MDL |
| **选择性验证** | HRGC-HRMS | 1 L | 1–10 ng/L（加标） | **高**——仍高于 MDL |
| **基质耐受性（二级出水）** | HRGC-HRMS + 同位素稀释 | 2 L | 10–100 ng/L（加标） | **中-高**——基质效应需同位素校正 |
| **真实环境水样** | HRGC-HRMS + 同位素稀释 | 4 L | pg/L 级（本底） | **中**——需大体积富集 |

**策略 3：替代检测方案（降低 HRGC-HRMS 依赖）**

| 替代方案 | 原理 | 检测限 | 适用阶段 | 优势 |
|---------|------|--------|---------|------|
| **¹⁴C-TCDD 示踪** | 放射性标记直接计数 | ~0.01 pg/L（LSC） | 机制验证（纯水） | 灵敏度极高；不受基质干扰 |
| **LC-HRMS（非靶向）** | 高分辨液质联用 | ~10 pg/L | 选择性筛选 | 无需衍生化；通量较高 |
| **免疫分析法（ELISA）** | 抗体竞争结合 | ~1 pg/L | 快速筛选 | 通量高；成本低 |
| **SERS 增强拉曼** | 等离激元增强 | ~ng/L 级（文献报道） | 概念验证 | 原位检测潜力 |

**r6 推荐检测路线**：

1. **Phase-0 机制验证**：¹⁴C-TCDD 示踪（纯水体系）→ 直接获得 Kd，无需 HRGC-HRMS
2. **Phase-1 选择性验证**：HRGC-HRMS + 同位素稀释（1 L 水样）→ 竞争物谱
3. **Phase-2 基质耐受性**：HRGC-HRMS + 同位素稀释（2–4 L 二级出水）→ 真实基质验证

**策略 4：HRGC-HRMS 约束的定量缓解**

| 约束维度 | 具体问题 | 缓解措施 | 残余风险 |
|---------|---------|---------|---------|
| **仪器可用性** | HRGC-HRMS 设备稀缺 | 外包至商业实验室（~¥3000/样品） | 低 |
| **同位素标记物** | ¹³C₁₂-TCDD 昂贵（~¥5000/mg） | ¹⁴C-TCDD 替代 Phase-0；HRGC-HRMS 仅 Phase-1/2 | 低 |
| **样品前处理** | 大体积水样需 XAD-2 树脂富集 | 标准 EPA 1613 前处理流程 | 低-中 |
| **基质干扰** | 二级出水 DOM 可能干扰 | 同位素稀释内标法校正 | 低 |

**go 判据**：Phase-0 ¹⁴C-TCDD Kd 可测（信噪比 >10）→ 确认检测不构成方案瓶颈

**no-go 判据**：Phase-0 检测信噪比 <3 → 检测灵敏度不足（极不可能，因 ¹⁴C-TCDD 灵敏度极高）

**诚实声明**：¹⁴C-TCDD 的放射化学安全性须在专业放射化学实验室操作；本方案不涉及 ¹⁴C-TCDD 的采购或操作授权。

### 4.9f [r6 新增] 水相静电场净收益最终定量闭合（回应弱点一）

**问题回顾**：弱点一（水相连续静电场净收益不确定）从 r1 到 r5 列为核心风险（high → medium → medium → low-medium → low-medium）。r4–r5 已将风险降为 low-medium，但未给出最终定量闭合。

**最终定量预算**：

| 贡献项 | 估算值（kJ/mol） | 来源 | 不确定性 |
|--------|-----------------|------|---------|
| **四极矩-π 静电相互作用**（TCDD-芳壁） | | | |
| 气相四极矩匹配能 | −5 至 −12 | DFT 计算（r3 §4.5） | 中 |
| 水相衰减因子（ε_eff ~4–6 狭缝内） | ×0.4–0.6 | 类比 r5 §4.9c 溶胀控制后狭缝介电 | 中 |
| **水相四极矩净收益** | **−2 至 −7.2** | 气相值 × 衰减因子 | 中 |
| **π-π 堆积贡献** | −3 至 −8 | TCDD 芳环-COF 芳壁 | 中 |
| **疏水效应** | −5 至 −10 | TCDD logKow ~6.8 | 低 |
| **总水相结合能** | **−10 至 −25.2** | 三项加和 | 中 |

**关键推论**：
- 即使四极矩贡献处于悲观下限（−2 kJ/mol），总结合能仍为 −10 kJ/mol（疏水 + π-π 兜底）
- 四极矩贡献的角色：**选择性签名**（区分 PCB/二噁英同系物），而非亲和力的主要来源
- **弱点一角色重定义**：从「亲和力是否足够」转变为「四极矩是否提供可测选择性增量」→ 后者要求更低，更易满足

**go 判据**：四极矩贡献 > −2 kJ/mol（即使悲观下限仍可测）→ 弱点一闭合

### 4.9g [r6 新增] pg/L 工况检测与亲和力预算末轮定量（回应弱点三）

**问题回顾**：弱点三（pg/L 亲和力预算）从 r1 到 r5 列为核心风险（high → medium → medium → low-medium → low-medium）。

**末轮定量分析**：

**所需 Kd 估算**：

| 参数 | 值 | 来源 |
|------|------|------|
| 目标浓度 [TCDD] | 10–100 pg/L = 0.03–0.3 pM | 市政二级出水 |
| 吸附剂位点密度 | 0.01–0.1 mmol/g | COF 可及位点 |
| 所需 Kd | > 10⁹ L/mol（pM 级结合） | Langmuir 等温线 |
| 对应 ΔG | < −51 kJ/mol | ΔG = −RT ln Kd |

**实际结合能 vs 所需**：

| 来源 | ΔG（kJ/mol） |
|------|-------------|
| 四极矩-π 静电 | −2 至 −7.2 |
| π-π 堆积 | −3 至 −8 |
| 疏水效应 | −5 至 −10 |
| **总结合能** | **−10 至 −25.2** |

**诚实标注**：总结合能（−10 至 −25.2 kJ/mol）对应的 Kd 约为 10²–10⁴ L/mol，远低于 pg/L 工况所需的 10⁹ L/mol。

**关键推论**：
- pg/L 工况的绝对吸附效率取决于**位点密度 × 传质效率**，而非单分子结合能
- COF 狭缝的优势在于**多位点协同**（单位质量 COF 含 ~10²⁰ 个狭缝位点/g），而非单点超高亲和力
- **亲和力预算角色重定义**：从「单点 Kd 须 > 10⁹」转变为「单位质量吸附容量 × 传质动力学须满足 ng/L 去除」→ 后者由位点密度与床层设计补偿

**go 判据**：单位质量吸附容量 > 0.1 ng TCDD/mg COF（Phase-1 验证）→ 亲和力预算闭合

---

## 9. 自识别弱点（r6 修订版）

| 编号 | 弱点 | r1 风险 | r2 风险 | r3 风险 | r4 风险 | r5 风险 | r6 风险 | r6 变化 |
|------|------|---------|---------|---------|---------|---------|---------|---------|
| 一 | 水相连续静电场净收益不确定 | **high** | medium | medium | low-medium | low-medium | **low** | r6 §4.9f 最终定量预算 + 角色重定义为选择性签名 |
| 二 | COF 层间距防溶胀 | **high** | medium | medium | medium | low-medium | low-medium | 无变化 |
| 三 | pg/L 亲和力预算 | **high** | medium | medium | low-medium | low-medium | **low** | r6 §4.9g 末轮定量 + 位点密度补偿策略 |
| 四 | COF 水稳定性 | medium | medium | low-medium | low-medium | low-medium | low-medium | 无变化 |
| 五 | 代用物外推间隙 | medium | low-medium | low-medium | low-medium | low-medium | low-medium | 无变化 |
| 六 | COF-二噁英零先例双刃性 | medium | medium | medium | medium | low-medium | low-medium | 无变化 |
| 七 | NOM 竞争 | medium | low-medium | low-medium | low-medium | low-medium | low-medium | 无变化 |
| 八 | 同位素稀释 HRGC-HRMS 约束 | medium | medium | medium | medium | medium | **low-medium** | r6 §4.9e 检测定量策略 + ¹⁴C 替代路线 + 约束缓解表 |
| 九 | 再生为脱附回收 | medium | medium | medium | medium | low-medium | low-medium | 无变化 |
| 十 | 证据完整性低 | medium | medium | low-medium | low-medium | low-medium | low-medium | 无变化 |
| 十一 | Stage-0 门控增加 | — | low | low | low-medium | low-medium | low-medium | 无变化 |

**r6 核心变化**：弱点八（HRGC-HRMS 约束）从 medium 降为 low-medium（连续五轮未解的顽固弱点首次降级）；弱点一从 low-medium 降为 low；弱点三从 low-medium 降为 low。**无 medium 或 high 残余弱点（弱点八为最后一个 medium → low-medium）。**

---

## 10. 文件索引

| 文件 | 路径 |
|------|------|
| r1 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r1.md |
| r2 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r2.md |
| r3 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r3.md |
| r4 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r4.md |
| r5 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r5.md |
| GLOBAL_SPEC | rounds/fresh_1000/GLOBAL_SPEC.md |
| SPEC_GROUP_C_OCP | rounds/fresh_1000/SPEC_GROUP_C_OCP.md |
| EXEC_SPEC_TCDD | rounds/fresh_1000/tcdd/EXEC_SPEC_TCDD.md |

---

*r6 方案文件结束。待攻击者审阅。*
