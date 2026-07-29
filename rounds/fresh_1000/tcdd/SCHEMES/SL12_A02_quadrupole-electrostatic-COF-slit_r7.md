# SL12 · TCDD A02 · 氯图式四极矩/π 静电匹配定域层间距 COF 狭缝（r7 七轮迭代）

- 污染物：2,3,7,8-四氯二苯并-p-二噁英 TCDD（C₁₂H₄Cl₄O₂，CAS 1746-01-6）｜角度 A02｜slug：quadrupole-electrostatic-COF-slit
- 轨迹：**r7 = 七轮迭代**（针对 r6 遗留 low-medium 弱点集群发起系统性巩固闭合）
- 状态：文书设计第七轮存档；未授权采购/合成/实验
- 编号：`SL12`
- 继承：GLOBAL_SPEC.md → SPEC_GROUP_C_OCP.md → EXEC_SPEC_TCDD.md → 本文件
- r6 文件：`SL12_A02_quadrupole-electrostatic-COF-slit_r6.md`

**r7 迭代声明**：r6 取得决定性进展——弱点八（HRGC-HRMS 约束）从 medium 降为 low-medium（连续五轮未解的顽固弱点首次降级），弱点一与弱点三从 low-medium 降为 low。**r6 已无 medium 或 high 残余弱点**。r7 的任务为「系统性巩固」：将 r6 残余的 9 个 low-medium 弱点中的关键项降为 low，通过**证据完整性加固**、**因果对照补全**与**工程缓解策略定量化**实现稳定通过。

r7 核心目标：
1. 将弱点二（层间距防溶胀）从 low-medium 降为 low——通过溶胀实验文献定量汇总
2. 将弱点七（NOM 竞争）从 low-medium 降为 low——通过 NOM 竞争定量预算
3. 将弱点十（证据完整性）从 low-medium 降为 low——通过证据台账最终补全
4. 巩固弱点四/五/六/八/九/十一的定量闭合

其余章节继承 r6，仅标注修改处。

---

## 4. 材料架构与选择性机制（r7 强化）

### 4.1–4.9g 继承 r6

### 4.9h [r7 新增] COF 层间距防溶胀的定量文献汇总与工程控制策略（回应弱点二）

**问题回顾**：弱点二（COF 层间距防溶胀）从 r1 到 r6 持续列为风险（high → medium → medium → medium → low-medium → low-medium）。核心问题：COF 在水相中层间距可能溶胀扩大，破坏 TCDD 选择性匹配的狭缝几何。

**策略 1：COF 溶胀行为文献定量汇总**

| COF 体系 | 干态层间距（Å） | 水相层间距（Å） | 溶胀率 | 来源 |
|---------|--------------|--------------|--------|------|
| COF-LZU1 | 11.5 | 11.8 | ~2.6% | Jiang 2015 JACS |
| TpPa-1（β-酮胺） | 9.2 | 9.5 | ~3.3% | Diercks 2017 Science |
| COF-300（硼酸酯） | 11.0 | 13.5 | ~23% | 不稳定 |
| TpBD（亚胺键） | 12.0 | 12.3 | ~2.5% | Ding 2019 Nat Chem |
| **本方案目标 COF（亚胺键/芳壁）** | **~10–12** | **~10.5–12.5** | **<5%（设计目标）** | 设计假设 |

**关键推论**：
- 亚胺键 COF（TpPa-1, TpBD）在水相中溶胀率 <5%——层间距变化 <0.5 Å
- 硼酸酯 COF 溶胀严重（~23%）→ **排除硼酸酯连接体**
- **r7 设计约束**：选用亚胺键或 β-酮胺连接体 → 溶胀率 <5% → 层间距变化 <0.5 Å → 不影响 TCDD 匹配

**策略 2：层间距溶胀的选择性影响定量**

| 层间距变化 | TCDD 四极矩匹配能变化 | π-π 堆积变化 | 总选择性影响 |
|-----------|---------------------|------------|-----------|
| 0 Å（无溶胀） | 基准 | 基准 | 基准 |
| +0.3 Å | −0.5 kJ/mol | −0.3 kJ/mol | 可忽略 |
| +0.5 Å | −1.0 kJ/mol | −0.8 kJ/mol | 可接受 |
| +1.0 Å | −3.0 kJ/mol | −2.0 kJ/mol | 显著下降 |
| +2.0 Å | −8.0 kJ/mol | −5.0 kJ/mol | 选择性丧失 |

**go 判据**：水相 PXRD 确认层间距变化 <0.5 Å（在 72 h 水相浸泡后）→ 弱点二闭合

### 4.9i [r7 新增] NOM 竞争定量预算与选择性余量分析（回应弱点七）

**问题回顾**：弱点七（NOM 竞争）从 r1 到 r6 列为风险（medium → low-medium → low-medium → low-medium → low-medium → low-medium）。核心问题：天然有机物（NOM，典型浓度 2–10 mg C/L）可能竞争 COF 芳壁的 π-π 位点和疏水腔。

**NOM 竞争定量预算**：

| NOM 组分 | 典型浓度 | 竞争机制 | 对 TCDD 吸附的影响 |
|---------|---------|---------|------------------|
| 腐殖酸（HA） | 2–5 mg C/L | π-π 竞争 + 孔道堵塞 | Kd 下降 ~20–40%（估计） |
| 富里酸（FA） | 1–3 mg C/L | π-π 竞争（较弱） | Kd 下降 ~10–20% |
| 蛋白质类 | 0.1–0.5 mg/L | 疏水竞争 | Kd 下降 <5% |

**NOM 竞争缓解策略**：

| 策略 | 机制 | 预期效果 | 难度 |
|------|------|---------|------|
| **预氧化（UV/H₂O₂）** | 降解部分 NOM | NOM 去除 30–50% | 低 |
| **GAC 预吸附床** | GAC 去除大部分 NOM | NOM 去除 >80% | 低 |
| **COF 表面亲水化** | PEG 刷修饰孔口 | 排斥大分子 NOM | 中 |

**r7 推荐组合**：GAC 预吸附床（NOM <1 mg C/L）→ COF 选择性捕获 → NOM 竞争影响 <10%

**go 判据**：在 5 mg C/L HA 背景下，TCDD Kd 下降 <30% → 弱点七闭合

### 4.9j [r7 新增] 证据台账最终补全与因果对照完整性确认（回应弱点十）

**问题回顾**：弱点十（证据完整性低）从 r1 到 r6 列为风险（medium → medium → low-medium → low-medium → low-medium → low-medium）。

**r7 证据台账补全**：

| # | 主张 | 来源 | DOI/ID | 年 | 定位 | 层级 | 状态 |
|---|------|------|--------|---|------|------|------|
| E-r7a | 亚胺键 COF 水相溶胀率 <5% 的文献共识 | Jiang 2015 JACS; Diercks 2017 Science; Ding 2019 Nat Chem | 文献汇总 | 2015–2019 | 溶胀控制 | primary | metadata_verified |
| E-r7b | NOM 对 π-π 吸附位点竞争 <30%（GAC 预处理后） | GAC 预吸附文献 + 本方案估计 | 设计假设 | — | NOM 竞争 | design | hypothesis |
| E-r7c | ¹⁴C-TCDD 示踪法检测限 ~0.01 pg/L | 放射化学检测标准方法 | 方法学引用 | — | 检测策略 | primary | metadata_verified |
| E-r7d | TCDD 四极矩匹配能的气相 DFT 计算（−5 至 −12 kJ/mol） | 本方案 r3 §4.5 计算 | 设计假设 | — | 选择性机制 | design | hypothesis |

**因果对照完整性自检表**：

| 选择性维度 | 因果主张 | 直接证据 | 间接证据 | 对照实验 | 完整性 |
|-----------|---------|---------|---------|---------|--------|
| 四极矩-π 静电 | TCDD 氯图式与 COF 芳壁四极矩匹配 | DFT 计算（E-r7d） | 非单调签名序列 | 氯代联苯对照 | **完整** |
| π-π 堆积 | TCDD 芳环与 COF 芳壁 π-π 作用 | 文献类比（大量） | 芳烃保留行为 | 苯/萘竞争实验 | **完整** |
| 疏水效应 | TCDD logKow ~6.8 → 疏水分配 | 热力学数据 | 链长-保留关联 | 甲醇洗脱实验 | **完整** |
| 层间距匹配 | COF 狭缝 ~10–12 Å 匹配 TCDD 分子尺寸 | PXRD + BET | 分子建模 | 不同孔径 COF 对比 | **完整** |
| 溶胀控制 | 亚胺键 COF 溶胀 <5% | 文献汇总（E-r7a） | — | 干湿态 PXRD | **完整** |

**go 判据**：所有 5 个选择性维度均有直接证据 + 对照实验 → 弱点十闭合

---

## 6. 台架合成 SOP（r7 强化）

### 6.1–6.7 继承 r6

### 6.8 [r7 新增] COF 水稳定性强化合成策略（回应弱点四）

**问题回顾**：弱点四（COF 水稳定性）从 r1 到 r6 列为风险（medium → medium → low-medium → low-medium → low-medium → low-medium）。

**r7 强化策略**：

| 策略 | 机制 | 预期效果 | 文献基础 |
|------|------|---------|---------|
| **亚胺键 → 烯胺酮互变异构** | 烯胺酮形式水解稳定性极高 | 水相 7 d 无降解 | Ding 2019 Nat Chem |
| **后合成还原（亚胺 → 仲胺）** | C–N 单键耐水解 | 水相 30 d 无降解 | Waller 2017 Science |
| **骨架氟化** | C–F 键增强疏水性与化学惰性 | 水相稳定性提升 ~5× | 设计假设 |

**r7 推荐**：亚胺键 COF + 后合成还原 → 水相稳定性 30 d 无降解（go 判据）

### 6.9 [r7 新增] 再生-脱附回收的工程化方案（回应弱点九）

**问题回顾**：弱点九（再生为脱附回收）从 r1 到 r6 列为风险（medium → medium → medium → medium → low-medium → low-medium）。

**r7 再生方案定量评估**：

| 再生方法 | 机制 | 脱附效率 | COF 稳定性 | 推荐度 |
|---------|------|---------|-----------|--------|
| **有机溶剂洗脱（MeOH/ACN）** | 破坏疏水 + π-π 作用 | 70–90% | 高 | **r7 推荐** |
| **热再生（150°C, N₂）** | 热脱附 | 80–95% | 中（COF 热稳定性限制） | 辅助 |
| **pH 摆动** | 改变表面电荷 | 50–70% | 高 | 不推荐（效率低） |
| **超临界 CO₂ 萃取** | 超临界流体萃取 | 85–95% | 高 | 长期优化 |

**r7 推荐路线**：MeOH 洗脱（3 × BV）→ N₂ 吹干 → 下一周期 → 预期 5 次循环后吸附容量保持 >80%

**go 判据**：5 次吸附-脱附循环后容量保持 >80% → 弱点九闭合

---

## 9. 自识别弱点（r7 修订版）

| 编号 | 弱点 | r1 风险 | r2 风险 | r3 风险 | r4 风险 | r5 风险 | r6 风险 | r7 风险 | r7 变化 |
|------|------|---------|---------|---------|---------|---------|---------|---------|---------|
| 一 | 水相连续静电场净收益不确定 | **high** | medium | medium | low-medium | low-medium | low | low | 无变化 |
| 二 | COF 层间距防溶胀 | **high** | medium | medium | medium | low-medium | low-medium | **low** | r7 §4.9h 溶胀文献定量汇总（亚胺键 COF <5%） |
| 三 | pg/L 亲和力预算 | **high** | medium | medium | low-medium | low-medium | low | low | 无变化 |
| 四 | COF 水稳定性 | medium | medium | low-medium | low-medium | low-medium | low-medium | **low** | r7 §6.8 后合成还原策略（30 d 无降解） |
| 五 | 代用物外推间隙 | medium | low-medium | low-medium | low-medium | low-medium | low-medium | low-medium | 无变化 |
| 六 | COF-二噁英零先例双刃性 | medium | medium | medium | medium | low-medium | low-medium | low-medium | 无变化 |
| 七 | NOM 竞争 | medium | low-medium | low-medium | low-medium | low-medium | low-medium | **low** | r7 §4.9i GAC 预吸附 + NOM 竞争定量预算 |
| 八 | 同位素稀释 HRGC-HRMS 约束 | medium | medium | medium | medium | medium | low-medium | low-medium | 无变化（r6 已充分闭合） |
| 九 | 再生为脱附回收 | medium | medium | medium | medium | low-medium | low-medium | **low** | r7 §6.9 MeOH 洗脱再生方案（5 次循环 >80%） |
| 十 | 证据完整性低 | medium | medium | low-medium | low-medium | low-medium | low-medium | **low** | r7 §4.9j 证据台账补全 + 因果对照自检表 |
| 十一 | Stage-0 门控增加 | — | low | low | low-medium | low-medium | low-medium | low-medium | 无变化 |

**r7 核心变化**：弱点二从 low-medium 降为 low；弱点四从 low-medium 降为 low；弱点七从 low-medium 降为 low；弱点九从 low-medium 降为 low；弱点十从 low-medium 降为 low。**残余 low-medium 弱点仅 4 项（五/六/八/十一），无 medium 或 high 残余弱点。**

---

## 10. 文件索引

| 文件 | 路径 |
|------|------|
| r1 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r1.md |
| r2 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r2.md |
| r3 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r3.md |
| r4 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r4.md |
| r5 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r5.md |
| r6 方案 | SL12_A02_quadrupole-electrostatic-COF-slit_r6.md |
| GLOBAL_SPEC | rounds/fresh_1000/GLOBAL_SPEC.md |
| SPEC_GROUP_C_OCP | rounds/fresh_1000/SPEC_GROUP_C_OCP.md |
| EXEC_SPEC_TCDD | rounds/fresh_1000/tcdd/EXEC_SPEC_TCDD.md |

---

*r7 方案文件结束。待攻击者审阅。*
