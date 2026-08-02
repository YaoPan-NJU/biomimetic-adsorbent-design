# DDT50-01 / LPO-SIP 可视化解释提示词包

## 1. 版本锁

```yaml
scheme_id: DDT50-01
lineage_id: L-DDT-01
material_embodiment: LPO-SIP_C12-soft-domain_shallow-dummy-imprinted_hydrated-shell_bead
release_status: E1_mechanism_validation_ready_performance_unproven_owner_review_pending
prompt_package_version: 1.0
prompt_status: content_locked
generated_on: 2026-08-02
repository_base_commit: 9ded13b7a4071c0a7b5e1535da9abde0ff43985c
source_design_file: rounds/genx_ddt_50x2_deep_design_20260725/DEEP_DESIGN_AND_SCORECARD.md
source_design_sha256: 64da36ad7b7c6babab63aaef349cb6129b1d2f370a2b5f1c7481c0272791eacc
evidence_ids: [E195, E196]
```

本图用于检查“膜链有序度和界面可达软相，而非总疏水量”是否被正确转译为 C12 浅壳软域；同时把浅印迹姿态和 HEMA 水化屏障明确标为待独立验证的附加模块。

## 2. 可视化主张账本

| ID | 面板 | 对象或关系 | 身份 | 证据或设计定位 | 允许画法 | 禁止外推 |
|---|---|---|---|---|---|---|
| V01 | A | DDT 膜分配随脂链长度、相态和胆固醇有序度发生大幅非单调变化 | `OBSERVED` | E195 | 三种膜软相与定性非单调趋势；胆固醇降低分配的注释 | 不把膜画成 DDT 专一结合位点 |
| V02 | A | DDT 从乳糜微粒向组织转移快于并区别于胆固醇酯核心转移 | `OBSERVED` | E196 | 界面释放快于核心脂质转移的功能示意 | 不画特异生物结合位点或组织选择性机制 |
| V03 | B | 可达浅层软相的有序度比总疏水体积更接近功能变量 | `ABSTRACTED` | DDT50-01 TR | 水界面、浅软域、非单调 C8/C12/C18 比较 | 不预设 C12 已在人工材料胜出 |
| V04 | B/C | 软相分配、浅腔形状记忆和水化屏障是三个可分离模块 | `ABSTRACTED` / `PROPOSED` | PACKING、POSE、BARRIER | 三层功能块与各自对照 | 不把三者画成已证实协同 |
| V05 | C | St/DVB 芯外为 1–3 µm HEMA/LMA/EGDMA/4-VBP 候选浅壳 | `PROPOSED` | DDT50-01 ME | 概念性核壳珠截面；无精确纳米形貌 | 不暗示壳层已成功制造 |
| V06 | C | 4,4'-二氯二苯甲烷是假模板，目标 DDT 不作模板 | `PROPOSED` | DDT50-01 SR | 假模板进入和洗脱流程标签 | 不画 DDT 直接模板或模板残留已合格 |
| V07 | C | 同锅种珠、延迟壳料、固化、假模板提取和截面 QC | `PROPOSED` | DDT50-01 SR | 五步流程与 MFG-STOP | 不声称独立成核、壳质量和富集已通过 |
| V08 | C | C8/C18、无 LMA、无 HEMA、NIP、错位 dummy 为同批因果对照 | `PROPOSED` | E1 控制组 | 六个小对照图标 | 不显示任何吸附排序 |
| V09 | C | DDT 家族在浅腔中的精确姿态和氯特异作用 | `UNKNOWN_OMITTED` | 尚无结构证据 | 不画原子级接触 | 不自行生成氯特异结合位点 |

## 3. 参考资产清单

当前主提示词使用安全示意模式，可直接生成。论文级精确版建议附加：

- `Image 1:` p,p'-DDT、o,p'-DDT、p,p'-DDE、p,p'-DDD 与 4,4'-二氯二苯甲烷的受控二维结构。
- `Image 2:` E195 来源数据重绘的定量分配曲线；只有人工复核数值后才能加入 Panel A。
- `Image 3:` DDT50-01 壳层单体和投料流程的受控化学图。

没有资产时只画命名轮廓、膜相和材料截面，不画具体键线或定量曲线。

## 4. ImageGen 主提示词

```text
Use case: scientific-educational, publication-quality mechanism figure for expert review
Audience: environmental materials scientists, polymer chemists, and membrane-partition reviewers
Asset type: one landscape three-panel scientific figure with a compact bottom legend
Primary request: explain how biological evidence for phase- and chain-order-dependent DDT membrane partition is abstracted into the proposed DDT50-01 LPO-SIP shallow-shell bead, including separate packing, pose, and hydration-barrier hypotheses and the minimum synthesis and control logic

Input images:
- none; use safe schematic mode and do not invent exact chemical structures or quantitative curves

Scene/backdrop: clean white background, generous whitespace, thin grey separators, no decorative background
Style/medium: restrained membrane-biophysics and polymer-materials vector illustration; clear, publication-scale labels; conceptual rather than photorealistic
Composition/framing:
- three horizontal panels A, B, and C connected by small arrows
- Panel A shows biological membrane-partition evidence
- Panel B shows the material-independent transfer rule
- Panel C shows the candidate core-shell bead, a compact synthesis strip, and causal controls
- a bottom legend explains evidence status

Panel A requirements:
- title it exactly "Biological evidence: phase-dependent DDT partition"
- show three simplified hydrated phospholipid membrane strips with different chain length or phase order, with DDT silhouettes partitioning to different extents in a visibly non-monotonic qualitative pattern
- add a separate cholesterol-rich membrane strip with fewer DDT silhouettes and the label that 50 mol% cholesterol lowered partition in the reported system
- add a small chylomicron-to-tissue transfer inset showing DDT leaving an accessible interfacial soft phase faster than a core cholesterol-ester marker
- clearly state that this is biological partition evidence, not a DDT-specific binding pocket
- use black or dark grey for directly source-supported relationships

Panel B requirements:
- title it exactly "Transfer rule: accessible shallow soft phase, not maximum hydrophobicity"
- show water above a shallow soft domain at an interface and a deep bulk-hydrophobic domain crossed out
- show a qualitative C8, C12, and C18 sequence with a question mark over the middle as the proposed non-monotonic test; do not show a result
- separate three labelled functions: soft-phase packing, shallow shape memory, and hydrated entrance barrier
- add a boxed statement: "PACKING, POSE, and BARRIER must be tested separately"

Panel C requirements:
- title it exactly "DDT50-01 / LPO-SIP candidate mapping"
- place a red banner: "Proposed design — not experimentally validated"
- show a 150–300 µm conceptual St/DVB macroporous bead in cross-section
- show only the outer 1–3 µm as a proposed HEMA/LMA/EGDMA/4-VBP shell; label LMA as the C12 soft-domain component, HEMA as the hydrated entrance component, and 4-VBP as a rigid aromatic interface component
- show a shallow cavity left by the non-target dummy 4,4'-dichlorodiphenylmethane; all proposed DDT interactions must use orange dashed lines with question marks
- explicitly state that target DDT is not used as the template
- include a five-step synthesis strip: St/DVB seed bead to 35–45% conversion; delayed shell feed over 30–45 min; cure at 70 then 80 degrees Celsius; extract non-target dummy; cross-section and phase-order QC
- end the synthesis strip with "MFG-STOP if shell localization fails"
- show six causal-control thumbnails: C8, C18, no LMA, no HEMA, NIP, and wrong-position dummy
- add a status box: "E1 mechanism-validation ready; performance unproven"

Text (verbatim, no other text):
"A"
"B"
"C"
"Biological evidence: phase-dependent DDT partition"
"Chain length and phase order change partition non-monotonically"
"50 mol% cholesterol lowered partition in the reported system"
"Accessible interfacial release"
"Biological partition evidence — not a DDT-specific binding pocket"
"Transfer rule: accessible shallow soft phase, not maximum hydrophobicity"
"C8"
"C12"
"C18"
"Soft-phase packing"
"Shallow shape memory"
"Hydrated entrance barrier"
"PACKING, POSE, and BARRIER must be tested separately"
"DDT50-01 / LPO-SIP candidate mapping"
"Proposed design — not experimentally validated"
"St/DVB macroporous core"
"Proposed 1–3 µm shallow shell"
"LMA: C12 soft domain"
"HEMA: hydrated entrance"
"4-VBP: rigid aromatic interface"
"Non-target dummy: 4,4'-dichlorodiphenylmethane"
"Target DDT is not the template"
"St/DVB seed, 35–45% conversion"
"Delayed shell feed, 30–45 min"
"Cure at 70 then 80 °C"
"Extract non-target dummy"
"Cross-section and phase-order QC"
"MFG-STOP if shell localization fails"
"No LMA"
"No HEMA"
"NIP"
"Wrong-position dummy"
"E1 mechanism-validation ready; performance unproven"
"Source-supported biological evidence"
"Functional abstraction"
"Proposed artificial relation"

Color and line grammar:
- black or dark grey: source-supported biological partition evidence
- blue-green: hydrated interface and abstraction
- muted amber: proposed soft-domain packing
- orange dashed lines with question marks: proposed artificial interactions or cavity relations
- red: unvalidated banner and stop point only

Constraints:
- distinguish membrane-partition evidence from the proposed polymer material
- use only the listed text and spell all material codes and monomers exactly
- keep C8, C12, and C18 as a testable question, not a result
- preserve the separation of PACKING, POSE, and BARRIER
- show the shell as a proposed conceptual region, not a measured micrograph
- no exact molecule connectivity, numerical partition curve, adsorption value, selectivity result, or validated performance
- no logo and no watermark

Avoid:
- a protein receptor, enzyme pocket, or DDT-specific biological binding site
- a monotonic more-carbon-means-more-uptake story
- showing C12 as already proven superior
- using DDT itself as the imprinting template
- chlorine-specific artificial contacts or an atomically exact cavity
- a bulk LMA bead without a shallow hydrated interface
- omitting the NIP, wrong-position dummy, no-LMA, or no-HEMA controls
- claiming successful shell synthesis, matrix resistance, regeneration, family selectivity, or superiority to GAC

Final output: one complete landscape scientific figure for expert review, with Panel A evidence-bounded, Panel B material-independent, and Panel C explicitly hypothetical.
```

## 5. 成图复核清单

- [ ] A 栏表达非单调膜分配与胆固醇降低分配，没有画专一生物位点。
- [ ] 乳糜微粒示意只支持界面释放，不声称特异生物结合位点或组织选择性。
- [ ] B 栏把浅层可达软相与最大疏水体积区分开。
- [ ] C8/C12/C18 是待检验问号，没有预画 C12 胜出。
- [ ] PACKING、POSE、BARRIER 三个模块分开，未画成已证实协同。
- [ ] C 栏芯、1–3 µm 壳和 HEMA/LMA/EGDMA/4-VBP 位置正确。
- [ ] 假模板是 4,4'-二氯二苯甲烷，且明确 DDT 不作模板。
- [ ] 合成顺序、温度阶段和截面/相态 QC 没有颠倒。
- [ ] 六类因果对照齐全且没有虚构结果。
- [ ] 没有性能、选择性、再生、GAC 优势或成功制备主张，文字逐字正确。

## 6. 定向修正提示词

```text
Edit only the incorrect DDT50-01 region. Preserve the St/DVB core and the proposed outer 1–3 µm HEMA/LMA/EGDMA/4-VBP shell. Keep C8, C12, and C18 as an unresolved non-monotonic test, not a result. Keep the non-target dummy as 4,4'-dichlorodiphenylmethane and state that target DDT is not the template. Use orange dashed question-mark lines for every artificial interaction. Keep all other layout, colors, labels, arrows, and legend unchanged and preserve the red unvalidated-status banner. Add no new claim or result.
```
