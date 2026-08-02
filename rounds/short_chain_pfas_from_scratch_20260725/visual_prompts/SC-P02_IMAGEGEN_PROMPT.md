# SC-P02 / PG-PMO 可视化解释提示词包

## 1. 版本锁

```yaml
scheme_id: SC-P02
lineage_id: L-SCPFAS-01
material_embodiment: PG-PMO_pore-mouth-urea-gradient_phenylene-channel
release_status: E1_mechanism_validation_ready_performance_unproven_owner_review_pending
prompt_package_version: 1.0
prompt_status: content_locked
generated_on: 2026-08-02
repository_base_commit: 9ded13b7a4071c0a7b5e1535da9abde0ff43985c
source_design_file: rounds/short_chain_pfas_from_scratch_20260725/DEEP_RESEARCH_AND_E1_DESIGN.md
source_design_sha256: 590e20f0ebb8a698a9b18d9a856291b15413daefd7415d8a5b826d67ad9b08cb
evidence_ids: [E162, E163, E164]
```

本图用于检查“天然含水头基定位与第二占位区”是否被诚实地转译成孔口脲富集与相邻苯桥通道。不能用图证明 SC-P02 已制得、已吸附 PFAS 或已优于对照。

## 2. 可视化主张账本

| ID | 面板 | 对象或关系 | 身份 | 证据或设计定位 | 允许画法 | 禁止外推 |
|---|---|---|---|---|---|---|
| V01 | A | SsuA 参与天然烷基磺酸盐营养摄取，含水极性环境定位磺酸头基 | `OBSERVED` | E162 | 生物溶质结合蛋白的功能示意；显示结构水和多重中性极性接触 | 不画 PFBS 已结合 SsuA；不画人工材料 |
| V02 | A | Bug/TRAP 先固定羧酸头基，第二结构域影响生产性整体占位 | `OBSERVED` | E163，支持原型 | 小型支持示意，明确不是 PFAS 实验 | 不声称 Bug 对 PFBA、PFHxA 或 GenX 有亲和力 |
| V03 | A/B | TauA 显示相似头基配位仍受水合与去溶剂代价影响 | `OBSERVED` | E164 | 水分子保留与去溶剂代价的警示标识 | 不给出 PFAS 结合常数或方向性预测 |
| V04 | B | 含水中性头基夹口后接相邻低极性占位区 | `ABSTRACTED` | SC-P02 TR | 两个相邻而非混匀的功能区；蓝色头基区、棕色低极性区 | 不复制蛋白折叠；不画精确纳米距离 |
| V05 | C | BTPU 脲桥在开放孔端相对富集，BTEB 苯桥构成后方通道 | `PROPOSED` | SC-P02 ME | 概念性介孔剖面；橙色虚线表示候选相互作用 | 不暗示梯度已制造或局部夹口已表征 |
| V06 | C | 先制备 BTPU 前体，再加入 BTEB，20 min 后延迟加入 BTPU，随后水热缩合和模板提取 | `PROPOSED` | SC-P02 SR | 五步合成嵌图和 `M0-STOP` QC | 不画成已经获得合格批次 |
| V07 | C | 同组成均匀体、去脲体和去苯体是主因果对照 | `PROPOSED` | SC-P01、SC-P04、SC-P05 | 三个简洁对照缩略图 | 不显示任何对照结果 |
| V08 | C | PFAS 的局部取向、氢键数和孔内构象 | `UNKNOWN_OMITTED` | 尚无实验结构 | 不画原子级姿态 | 不自行补全分子对接 |

## 3. 参考资产清单

当前主提示词使用安全示意模式，可直接生成。若要升级为论文终稿，优先附加：

- `Image 1:` 经受控分子绘图核对的 PFBA、PFHxA、PFBS 和 HFPO-DA 二维结构；仅用于分子身份，不得改变连接。
- `Image 2:` 来自来源论文、经许可且已核对的 SsuA 结构渲染；仅在需要残基级 Panel A 时使用。
- `Image 3:` BTEB 与 BTPU 的受控二维结构；仅用于合成嵌图。

没有这些资产时，不画具体残基、完整键线、距离或确定的孔内构象。

## 4. ImageGen 主提示词

```text
Use case: scientific-educational, publication-quality mechanism figure for expert review
Audience: environmental materials scientists, adsorption chemists, and protein-transport reviewers
Asset type: one landscape three-panel scientific figure with a compact bottom legend
Primary request: explain how evidence from natural hydrated solute-binding systems is abstracted into the proposed SC-P02 PG-PMO short-chain-PFAS-class adsorbent and its minimum synthesis logic, while making every unvalidated material claim visually explicit

Input images:
- none; use safe schematic mode and do not invent atomically exact structures

Scene/backdrop: clean white background, generous whitespace, thin grey panel separators, no decorative texture
Style/medium: restrained high-quality scientific vector illustration; clear hierarchy; schematic rather than photorealistic; readable at journal-figure scale
Composition/framing:
- horizontal panels A, B, and C connected by narrow left-to-right arrows
- Panel A occupies about 31 percent width, Panel B 27 percent, Panel C 42 percent
- Panel C contains a main pore cutaway and a small four-step synthesis strip along its bottom
- a single compact legend spans the bottom
- the arrows mean evidence-to-abstraction-to-proposal, not equal certainty

Panel A requirements:
- title it exactly "Biological evidence: hydrated solute capture"
- show a simplified cutaway of a natural solute-binding protein pocket, not a specific atomically exact structure
- show a generic natural alkanesulfonate-like solute with its sulfonate headgroup retained in a partly hydrated polar region by several neutral polar contacts and structural water
- add a small supporting inset showing a carboxylate headgroup fixed first and a second protein domain checking productive whole-solute occupancy
- include a water-droplet warning icon showing that similar headgroup geometry can still have different hydration and desolvation costs
- make clear that these are natural nutrient-transport analogues and not PFAS-binding experiments
- use black or dark-grey marks only for source-supported biological statements

Panel B requirements:
- title it exactly "Transfer rule: hydrated headgroup zone plus adjacent low-polarity zone"
- remove all protein folds and show only two adjacent functional regions
- region 1: a blue water-containing neutral donor environment around a generic anionic oxygen headgroup
- region 2: a muted brown low-polarity occupancy region directly behind the headgroup zone
- show PFBA, PFHxA, PFBS, and GenX only as four labeled class-member silhouettes with a polar head and short tail or branched-ether body; do not draw exact chemical connectivity
- emphasize that hydration remains part of the recognition problem rather than being fully removed
- add a boxed statement: "Translate functional organization, not the protein structure"

Panel C requirements:
- title it exactly "SC-P02 / PG-PMO candidate mapping"
- place a red banner directly below the title: "Proposed design — not experimentally validated"
- show a conceptual water-accessible mesoporous organosilica channel cutaway
- at the open pore mouth, show a higher density of labelled BTPU urea bridges in blue; deeper in the channel, show labelled BTEB phenylene bridges in muted brown
- depict a generic short-chain PFAS-class silhouette approaching the pore; use only orange dashed lines with a question mark for proposed headgroup contacts and proposed tail occupancy
- do not show a precise preorganized molecular cavity, exact hydrogen-bond number, exact molecular pose, or proven gradient
- include three small causal-control thumbnails: same-composition uniform distribution, urea-deletion control, and phenylene-deletion control
- include a five-step synthesis strip: prepare the BTPU precursor; BTEB first; wait 20 min; delayed BTPU feed; hydrothermal condensation and template extraction
- end the synthesis strip with a stop-sign icon labelled "M0-STOP: gradient or matching control fails"
- add a small status box: "E1 mechanism-validation ready; performance unproven"

Text (verbatim, no other text):
"A"
"B"
"C"
"Biological evidence: hydrated solute capture"
"Natural nutrient-transport analogues — no PFAS binding test"
"Partly hydrated polar region"
"Headgroup fixed first"
"Second-domain occupancy check"
"Hydration and desolvation still matter"
"Transfer rule: hydrated headgroup zone plus adjacent low-polarity zone"
"Neutral hydrated headgroup zone"
"Adjacent low-polarity occupancy zone"
"PFBA"
"PFHxA"
"PFBS"
"GenX"
"Translate functional organization, not the protein structure"
"SC-P02 / PG-PMO candidate mapping"
"Proposed design — not experimentally validated"
"BTPU urea-rich pore mouth"
"BTEB phenylene channel"
"Hypothesized class capture"
"Same composition, uniform"
"Urea deletion"
"Phenylene deletion"
"Prepare BTPU precursor"
"BTEB first"
"Wait 20 min"
"Delayed BTPU feed"
"Condense and extract template"
"M0-STOP: gradient or matching control fails"
"E1 mechanism-validation ready; performance unproven"
"Source-supported biological evidence"
"Functional abstraction"
"Proposed artificial relation"

Color and line grammar:
- black or dark grey: source-supported biological evidence
- blue: hydrated polar function and functional abstraction
- muted brown: low-polarity occupancy function
- orange dashed lines with question marks: proposed artificial interactions or spatial relations
- red: unvalidated-status banner and stop point only

Constraints:
- keep the biological evidence, transfer rule, and proposed material visually distinct
- use only the listed text and spell every material code exactly
- show water in all three panels
- keep all labels readable and avoid dense paragraphs
- no exact chemical structure, residue identity, distance, binding constant, adsorption value, or performance result
- no logo and no watermark

Avoid:
- showing PFBS, PFBA, PFHxA, or GenX bound inside SsuA, Bug, or TauA
- portraying neutral urea contacts as proven in the material
- positive-charge icons, permanent cations, fluorinated polymer domains, protein components, metal cages, or PFAS templates
- a uniformly mixed PMO labelled as the proposed gradient material
- a precise cavity or fixed molecular pose not established by structural measurement
- any claim of PFAS selectivity, matrix resistance, regeneration, scale-up, or successful synthesis

Final output: one complete landscape scientific figure suitable for expert review, with Panel A evidentiary, Panel B abstract, and Panel C explicitly hypothetical and non-evidentiary.
```

## 5. 成图复核清单

- [ ] A 栏没有把 PFAS 画进 SsuA、Bug 或 TauA。
- [ ] A 栏把 SsuA 作为主原型，Bug/TauA 只作支持和边界。
- [ ] B 栏只有“含水头基区加相邻低极性区”，没有 PMO、BTPU 或 BTEB。
- [ ] C 栏孔口 BTPU 和后方 BTEB 的方向没有颠倒。
- [ ] 合成顺序为先制备 BTPU 前体、BTEB 先行、20 min、BTPU 延迟、缩合与模板提取。
- [ ] 同组成均匀、去脲、去苯三个对照都出现且没有虚构结果。
- [ ] 没有永久正电、含氟材料、PFAS 模板、蛋白或金属笼。
- [ ] 所有人工接触为橙色虚线或问号，且红色未验证横幅清楚。
- [ ] 图中没有选择性、容量、真实水、再生或制造成功主张。
- [ ] 文字逐字正确。

## 6. 定向修正提示词

```text
Edit only the incorrect panel or label identified by the reviewer. Correct the SC-P02 content to match this rule: BTPU urea bridges are proposed to be enriched at the open pore mouth, BTEB phenylene bridges form the adjacent inner channel, and every artificial interaction remains an orange dashed hypothesis with a question mark. Keep all other panels, spacing, colors, labels, arrows, and legend unchanged. Preserve the red "Proposed design — not experimentally validated" banner. Add no new molecule, contact, result, or claim.
```
