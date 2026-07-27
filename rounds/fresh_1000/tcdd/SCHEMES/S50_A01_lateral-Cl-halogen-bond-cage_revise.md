# S50 · TCDD · A01 · 侧位氯图式卤键/σ-空穴位点读取有机笼

- 污染物：2,3,7,8-四氯二苯并-p-二噁英 TCDD（C12H4Cl4O2，logKow~6.8，pg/L 级）
- 角度：A01 侧位氯图式卤键/σ-空穴位点读取有机笼
- 状态：**revise_with_phase0_prerequisite**（r1=70/100；卤键强度为物理化学根本性限制，天花板 ~78-82，85 为极窄路径；DFT 预筛为唯一 Go/No-Go 门）
- r1 工作流：设计 72→攻击 0c/3h→裁决 70/revise

## 关键发现

### H1 · 卤键强度根本性限制
水相中性碘代三唑对中性缺电子芳基氯（TCDD）的卤键强度为物理化学根本性限制——单位点可能 <1 kJ/mol，四位点协同性惩罚后 ΔΔG_XB 可能 <2 kJ/mol。核心创新维度（卤键位型读取）面临退化为纯形状筛分（A03 变体）的风险。

### H2 · PeCDD 检验缺失
2,3,7,8-TCDD 对 1,2,3,4-TCDD 的卤键增量不可独立验证（无 PeCDD 判据化），使卤键贡献与形状贡献不可解耦。

### H3 · 供体选择逻辑不自洽
主路线碘代三唑供体选择逻辑存在不自洽（σ-空穴深度 vs 水相稳定性权衡未定量）。

## 裁决六维评分

| 维度 | 得分 | 说明 |
|---|---|---|
| 因果闭环 | 15/20 | 形状+卤键分层因果链自洽，pg/L 极端 Kd 可行性仍悬 |
| 选择性吸附机制 | 17/25 | 双维度正交 logKow，但卤键增量诚实降为 α_XB≥2 |
| 人工材料可转译性 | 14/20 | 中性碘代三唑 POC 合成可行，pg/L 床层仍难 |
| 原创性 | 11/15 | POC×中性卤键阵列×二噁英三交集空白 |
| 实验可证伪与对照 | 8/10 | C1-C4 + 卤素梯度 + 同位素稀释完备 |
| 证据完整性 | 7/10 | 全部 DOI 核验通过，无全文读取 |
| **合计** | **70/100** | **revise_with_phase0_prerequisite** |

## Phase 0 门控
S1 DFT 预筛（M06-2X/def2-TZVP，碘代三唑-氯苯 σ-空穴复合物）：ΔΔG_XB ≥ 2 kJ/mol → GO（进入台架）；< 2 kJ/mol → TERMINATE（退化为 A03 形状筛分变体，无独立创新）。

## 证据引用
- Bunge 2003 Nature, DOI 10.1038/nature01237（CBDB1 区域选择性脱卤，metadata_verified）
- Cavallo 2016 Chem Rev, DOI 10.1021/acs.chemrev.5b00484（卤键综述，metadata_verified）
- Dai 2022 Nat Commun, DOI 10.1038/s41467-022-33858-w（AHR PAS-B 结构，metadata_verified）
- Barkovskii 1996 AEM, DOI 10.1128/aem.62.12.4556-4562.1996（TCDD 级脱氯，metadata_verified）
