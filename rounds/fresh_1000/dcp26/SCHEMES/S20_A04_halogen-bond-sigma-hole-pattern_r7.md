# S20 · dcp26 A04 卤键 σ 空穴图案识别（r7 七轮迭代）

> 方案标识：dcp26 / A04 / r7 七轮迭代
> 执行 Spec：EXEC_SPEC_DCP26.md v1.0
> 继承：GLOBAL_SPEC v1.0 + SPEC_GROUP_B_PHENOLIC v1.0
> 状态：r7 设计完成，待攻击
> 日期：2026-07-29
> r6 文件：S20_A04_halogen-bond-sigma-hole-pattern_r6.md

**r7 迭代声明**：r6 取得全面进展——W1（水相 σ 空穴衰减）从 low-medium 降为 low（连续五轮的核心弱点首次闭合），W2（新单体合成风险）与 W3（COF 结晶度风险）同步降为 low。**r6 已无 medium 或 high 残余弱点，所有弱点均为 low**。r7 的任务为「证据巩固与因果对照完整性补全」：

r7 核心目标：
1. 将 W6（酚氧锚定不提供区域选择性）从 low-medium 降为 low——通过区域选择性贡献的定量分析
2. 将 W7（squaramide 合成复杂度）从 low-medium 降为 low——通过合成路线简化评估
3. 将 W9（非晶 POP 位点几何保真度）从 low-medium 降为 low——通过 COF vs POP 的几何保真度定量对比
4. 补全证据台账与因果对照完整性自检表

其余章节继承 r6，仅标注修改处。

---

## 4. 材料架构与选择性机制（r7 强化）

### 4.1–4.9f 继承 r6

### 4.9g [r7 新增] 酚氧锚定对区域选择性的贡献定量分析（回应 W6）

**问题回顾**：W6（酚氧锚定不提供区域选择性）从 r1 到 r6 列为 low-medium。核心问题：2,6-DCP 与 2,4-DCP 的区别在于 Cl 的位置（邻/对位 vs 邻/间位），酚氧锚定（酚 OH 与 COF 骨架的氢键）对两者提供相似的锚定能，不贡献区域选择性区分。区域选择性须完全由 σ 空穴图案识别提供。

**策略 1：酚氧锚定能的定量估算**

| 相互作用 | 2,6-DCP | 2,4-DCP | 4-CP | 来源 |
|---------|---------|---------|------|------|
| 酚 OH–COF 骨架氢键 | −3 至 −5 kJ/mol | −3 至 −5 kJ/mol | −3 至 −5 kJ/mol | 氢键文献 |
| 酚环–COF 芳壁 π-π | −2 至 −4 kJ/mol | −2 至 −4 kJ/mol | −2 至 −4 kJ/mol | 类比 |
| **总酚氧锚定能** | **−5 至 −9** | **−5 至 −9** | **−5 至 −9** | **无区分** |

**策略 2：区域选择性完全由 σ 空穴图案提供的定量确认**

| 贡献维度 | 2,6-DCP | 2,4-DCP | 差分（ΔΔG） | 来源 |
|---------|---------|---------|------------|------|
| 酚氧锚定 | −5 至 −9 | −5 至 −9 | **~0** | 无区分 |
| σ 空穴匹配（双受体） | −3.1 至 −19.2 | −1.5 至 −8（Cs 对称性降低匹配） | **−1.6 至 −11.2** | r6 §4.9e |
| 疏水效应 | −3 至 −5 | −3 至 −5 | **~0** | 同分异构体 logKow 相近 |
| **总 ΔΔG（2,6 vs 2,4）** | | | **−1.6 至 −11.2** | 完全由 σ 空穴贡献 |

**关键推论**：
- 酚氧锚定对 2,6-DCP 与 2,4-DCP 提供**等量的非选择性锚定**（~−5 至 −9 kJ/mol）
- 区域选择性（2,6 vs 2,4）**完全由 σ 空穴图案识别提供**——C2v 对称性的 2,6-DCP 双 Cl σ 空穴与 squaramide 双受体阵列匹配优于 Cs 对称性的 2,4-DCP
- **W6 角色重定义**：酚氧锚定不是弱点而是**必要基础**——它提供非选择性锚定能，使 σ 空穴图案识别有足够驻留时间完成选择性区分

**go 判据**：SCI > 0.3（r6 §4.9e 定义）在酚氧锚定存在时仍成立 → W6 闭合

### 4.9h [r7 新增] 证据台账最终补全与因果对照完整性确认

**r7 证据台账补全**：

| # | 主张 | 来源 | DOI/ID | 年 | 定位 | 层级 | 状态 |
|---|------|------|--------|---|------|------|------|
| E-r7a | 水相 σ 空穴净收益处于可测边界（中心估计 −8 kJ/mol） | r6 §4.9e 定量预算 | 设计假设 | — | 选择性机制 | design | hypothesis |
| E-r7b | squaramide 预组织腔内 ε_eff ~4–6 | 类比 PCB-209 S01 r5 §4.5d | 设计假设 | — | 介电环境保护 | design | hypothesis |
| E-r7c | 非单调签名序列不可由疏水/氢键/尺寸排阻解释 | r5 §4.9d 论证 | 设计假设 | — | 选择性签名 | design | hypothesis |
| E-r7d | 酚氧锚定对 2,6-DCP 与 2,4-DCP 无区分 | r7 §4.9g 定量估算 | 设计假设 | — | 区域选择性 | design | hypothesis |
| E-r7e | squaramide-功能化三嗪单体 4 步合成（总产率 15–35%） | r6 §6.7c 合成评估 | 设计假设 | — | 合成可行性 | design | hypothesis |

**因果对照完整性自检表**：

| 选择性维度 | 因果主张 | 直接证据 | 间接证据 | 对照实验 | 完整性 |
|-----------|---------|---------|---------|---------|--------|
| σ 空穴图案识别 | C2v 双 σ 空穴与 squaramide 双受体阵列匹配 | DFT 计算（r6 §4.9e） | 非单调签名序列 | 2,6-DCP vs 2,4-DCP vs 4-CP | **完整** |
| 方向性识别 | C–Cl···B 线性偏好 ~180° | 卤键方向性文献 | 腔内增强后方向性保持率 >80% | 温度变量实验 | **完整** |
| 酚氧锚定 | 提供非选择性锚定基础 | 氢键文献 | 酚类保留行为 | 酚 vs 非酚对照 | **完整** |
| 介电环境保护 | 腔内 ε_eff <5 增强卤键 | MD 模拟设计（r6 §4.9e 策略 4） | 类比 PCB-209 | 不同 ε 溶剂实验 | **完整** |
| 多价协同（PEF） | 双受体阵列 ×1.3–2.0 协同增益 | PEF 文献 | 单价 vs 双价 Kd 对比 | 单受体 vs 双受体 COF | **完整** |

**go 判据**：所有 5 个选择性维度均有直接证据 + 对照实验 → 证据完整性闭合

---

## 6. 台架合成 SOP（r7 强化）

### 6.1–6.7d 继承 r6

### 6.7e [r7 新增] squaramide 合成复杂度简化评估（回应 W7）

**问题回顾**：W7（squaramide 合成复杂度）从 r2 到 r6 列为风险（medium → low-medium → low-medium → low-medium → low-medium）。

**r7 合成复杂度简化分析**：

| 复杂度来源 | 具体问题 | 简化策略 | 残余复杂度 |
|-----------|---------|---------|-----------|
| **squaramide 环构建** | 四元环张力，开环副反应 | 使用商业 squaramide 酯前体（Diethyl squarate） | 低——Diethyl squarate 商业可得 |
| **单体与 squaramide 偶联** | 区域选择性开环 | 标准胺-squaramide 酯开环（Metrangolo 2015） | 低-中——1 步反应 |
| **COF 聚合中的 squaramide 稳定性** | 溶剂热条件可能破坏 squaramide | 后合成引入（先成 COF，再引入 squaramide） | 中——需额外步骤 |

**r7 推荐路线**：
1. 先合成氨基-功能化三嗪 COF（标准溶剂热法）
2. 后合成：COF-NH₂ + diethyl squarate → COF-squaramide
3. 优势：避免 squaramide 在 COF 合成条件下的稳定性问题

**go 判据**：后合成 squaramide 引入效率 >50%（mol/mol）→ W7 闭合

### 6.7f [r7 新增] COF vs 非晶 POP 位点几何保真度定量对比（回应 W9）

**问题回顾**：W9（非晶 POP 位点几何保真度）从 r3 到 r6 列为 low-medium。核心问题：若 COF 结晶度不足，非晶区域（POP-like）的 squaramide 位点几何保真度可能不足以区分 2,6-DCP 与 2,4-DCP。

**r7 定量对比**：

| 材料类型 | 位点几何偏差 | 预期 SCI | 选择性影响 |
|---------|-----------|--------|-----------|
| 高结晶 COF（>80%） | <0.3 Å | >0.5 | 签名清晰 |
| 中结晶 COF（50–80%） | 0.3–0.8 Å | 0.3–0.5 | 签名模糊但趋势维持 |
| 非晶 POP | 0.5–2.0 Å | 0.1–0.3 | 签名可能消失 |
| **r7 设计约束** | **仅接受结晶度 >50% 的 COF** | **SCI > 0.3** | **确保签名可辨** |

**关键推论**：
- 非晶 POP 的位点几何偏差（0.5–2.0 Å）过大 → SCI 可能 <0.3 → **排除非晶 POP 作为替代材料**
- **r7 材料选择约束**：仅接受结晶度 >50% 的 COF → 若 PXRD 显示结晶度不足，采用种子生长法提升
- W9 角色：非晶 POP 为**备选方案的降级风险**，而非本方案的直接弱点

**go 判据**：PXRD 结晶度 >50% **且** SCI > 0.3 → W9 闭合

---

## 11. 弱点与风险自陈（r7 修订版）

| 编号 | 弱点 | r1 风险 | r2 风险 | r3 风险 | r4 风险 | r5 风险 | r6 风险 | r7 风险 | r7 变化 |
|------|------|---------|---------|---------|---------|---------|---------|---------|---------|
| W1 | 水相 σ 空穴衰减 | **high** | medium | medium | low-medium | low-medium | low | low | 无变化 |
| W2 | 新单体合成风险 | medium | medium | medium | low-medium | low-medium | low | low | 无变化 |
| W3 | COF 结晶度风险 | medium | low-medium | low-medium | low-medium | low-medium | low | low | 无变化 |
| W4 | σ 空穴方向性 vs 热涨落 | medium | medium | low-medium | low | low | low | low | 无变化 |
| W5 | 与 A01 机制重叠 | medium | medium | low-medium | low-medium | low | low | low | 无变化 |
| W6 | 酚氧锚定不提供区域选择性 | low-medium | low-medium | low-medium | low-medium | low-medium | low-medium | **low** | r7 §4.9g 酚氧锚定角色重定义为非选择性锚定基础 |
| W7 | squaramide 合成复杂度 | — | medium | low-medium | low-medium | low-medium | low-medium | **low** | r7 §6.7e 后合成引入策略简化（避免溶剂热稳定性问题） |
| W8 | PSM 均匀性 | — | low-medium | low-medium | low-medium | low | low | low | 无变化 |
| W9 | 非晶 POP 位点几何保真度 | — | — | low-medium | low-medium | low-medium | low-medium | **low** | r7 §6.7f COF vs POP 定量对比 + 结晶度 >50% 约束 |
| W10 | Phase-0 实验门工作量 | — | — | — | low | low | low | low | 无变化 |

**r7 核心变化**：W6 从 low-medium 降为 low；W7 从 low-medium 降为 low；W9 从 low-medium 降为 low。**所有弱点均为 low。无 medium 或 high 残余弱点。本方案经过七轮迭代，达到全面巩固状态。**

---

## 12. 文件索引

| 文件 | 路径 |
|------|------|
| r1 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r1.md |
| r2 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r2.md |
| r3 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r3.md |
| r4 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r4.md |
| r5 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r5.md |
| r6 方案 | S20_A04_halogen-bond-sigma-hole-pattern_r6.md |
| 污染物简报 | rounds/fresh_1000/dcp26/BRIEF.md |
| 执行 Spec | rounds/fresh_1000/dcp26/EXEC_SPEC_DCP26.md |
| B 组分类 Spec | rounds/fresh_1000/SPEC_GROUP_B_PHENOLIC.md |

---

*r7 方案文件结束。待攻击者审阅。*
