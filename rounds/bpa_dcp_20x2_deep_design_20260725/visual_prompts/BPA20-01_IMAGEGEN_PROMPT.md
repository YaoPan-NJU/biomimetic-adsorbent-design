# BPA20-01 / AG-COF 可视化解释提示词包

## 1. 版本锁

```yaml
scheme_id: BPA20-01
lineage_id: L-BPA-01
material_embodiment: AG-COF_fixed-single-phenol-anchor_interchangeable-wall-gate
release_status: E1_mechanism_validation_ready_performance_unproven_owner_review_pending
prompt_package_version: 1.0
prompt_status: content_locked
generated_on: 2026-08-02
repository_base_commit: 9ded13b7a4071c0a7b5e1535da9abde0ff43985c
source_design_file: rounds/bpa_dcp_20x2_deep_design_20260725/DEEP_DESIGN_AND_SCORECARD.md
source_design_sha256: bb80da5e66096ca8cd065cf86bbb050e48d872c678563a87632dc26944fcdd7f
evidence_ids: [E145, E156, E157]
```

本图用于检查“天然水相酚效应物识别中的固定单酚锚与邻近壁身份”是否被诚实地转译为 AG-COF 的内向吡啶 N 和可换门。不得恢复历史上已否定的对称双端夹持叙事。

## 2. 可视化主张账本

| ID | 面板 | 对象或关系 | 身份 | 证据或设计定位 | 允许画法 | 禁止外推 |
|---|---|---|---|---|---|---|
| V01 | A | DmpR/PoxR 在水相识别酚类效应物并调控降解相关功能 | `OBSERVED` | E156、E157 | 细菌酚感知与调控的功能示意 | 不画成天然 BPA 去除系统 |
| V02 | A | DmpR 6IY8 提供 His100 型固定酚 OH 锚的结构约束 | `OBSERVED` | E157 | 无原子坐标的简化标签或附受控 PDB 资产 | 不自行画残基坐标、距离或 BPA 复合物 |
| V03 | B | 固定单酚锚与邻近桥连区门共同改变效应物谱 | `ABSTRACTED` | E145、E156、E157 与 BPA20-01 TR | 一端锚定、中央桥区读取、第二酚端可选 | 不画成两个酚 OH 都必须被夹持 |
| V04 | C | 内向吡啶 N 与甲基门位于同一 β-酮烯胺 COF 孔壁 | `PROPOSED` | BPA20-01 ME | 同拓扑概念孔段；橙色假说接触 | 不暗示湿态几何或选择性已经证明 |
| V05 | C | G0/G1/G2/C1 以同晶格门交换和去锚分离因果 | `PROPOSED` | E1 对照 | 四个同拓扑缩略图 | 不显示预设排序结果 |
| V06 | C | 微晶制备、彻底洗涤、结构匹配 QC 与可选低粘结相造粒 | `PROPOSED` | BPA20-01 SR | 四步合成与 QC 嵌图 | 不声称已得到 2–5 µm 合格晶体 |
| V07 | C | BPA 与吡啶 N 的净水相锚、门对 BPA/BPAF 的逆疏水增益 | `UNKNOWN_OMITTED` | E1 待测 medium 风险 | 橙色问号和停止点 | 不显示已通过 α 或真实水门 |

## 3. 参考资产清单

当前主提示词可在安全示意模式下直接使用。论文级精确版建议附加：

- `Image 1:` 从 PDB 6IY8 受控渲染并人工核对的 DmpR 酚结合区域；不得由 ImageGen 重排残基。
- `Image 2:` BPA、BPF、BPS、BPAF 的受控二维结构；必须保持正确连接。
- `Image 3:` AG-COF 单体与孔壁重复单元的受控化学图；当前设计文件未给足键线时不得让 ImageGen发明。

没有资产时，只用功能轮廓和名称标签，不画具体键线、残基距离或精确孔径。

## 4. ImageGen 主提示词

```text
Use case: scientific-educational, publication-quality mechanism figure for expert review
Audience: environmental chemists, porous-materials scientists, and bacterial-sensing reviewers
Asset type: one landscape three-panel scientific figure with a compact bottom legend
Primary request: explain the evidence-bounded translation from natural bacterial phenolic-effector sensing to the proposed BPA20-01 anchor-gate COF, including the candidate material, minimum synthesis logic, and decisive causal controls without presenting any artificial interaction as validated

Input images:
- none; use safe schematic mode and do not invent atomically exact protein or COF structures

Scene/backdrop: clean white background, generous whitespace, thin grey dividers, no decorative texture
Style/medium: restrained chemical-biology and materials-science vector illustration; crisp typography; conceptual where exact assets are absent
Composition/framing:
- three horizontal panels A, B, and C connected by small arrows
- Panel A: biological function and structural constraint
- Panel B: material-independent transfer rule
- Panel C: proposed AG-COF mapping plus a compact synthesis and control inset
- one bottom legend explains evidence status

Panel A requirements:
- title it exactly "Biological evidence: aqueous phenolic-effector sensing"
- show a bacterial cell with a phenolic-effector sensor controlling a degradation-pathway gene response in water
- add a simplified pocket inset containing a generic phenol, with one labelled His100-associated phenol anchor; keep it explicitly schematic and do not show exact atomic coordinates
- label the system as a natural phenolic-effector sensing function, not a BPA-removal system
- do not place BPA inside the biological pocket
- use black or dark grey for source-supported content

Panel B requirements:
- title it exactly "Transfer rule: fixed single-phenol anchor plus an interchangeable wall gate"
- show a simplified BPA silhouette in a twisted, non-coplanar presentation, but not an exact chemical structure
- anchor only one phenolic end in a blue polar zone
- place a separate muted-gold wall-gate zone next to the central bridge region
- leave the second phenolic end unanchored and label it as optional, not required
- show four small bridge-type silhouettes labelled BPA, BPF, BPS, and BPAF to express that wall identity should change the response spectrum
- include the statement "Functional mapping does not require a symmetric two-ended clamp"

Panel C requirements:
- title it exactly "BPA20-01 / AG-COF candidate mapping"
- place a red banner: "Proposed design — not experimentally validated"
- show a conceptual beta-ketoenamine COF pore segment in water, without exact covalent connectivity
- mark one inward pyridine-N site as the candidate single-phenol anchor and one adjacent methyl-facing wall feature as the candidate bridge gate
- show one BPA silhouette approaching the pore; all artificial contacts must be orange dashed lines with question marks
- show four same-topology control thumbnails: G0 no methyl gate, G1 methyl gate, G2 fluoro gate, and C1 anchor deletion
- add a four-step process strip: 50–100 mg microcrystal synthesis; wash monomers below LOQ; match topology and pore metrics; optional granulation with no more than 15 wt% porous binder
- place a stop-sign icon labelled "STOP if pore mismatch explains the spectrum"
- add a status box: "E1 mechanism-validation ready; performance unproven"

Text (verbatim, no other text):
"A"
"B"
"C"
"Biological evidence: aqueous phenolic-effector sensing"
"Natural sensing and regulation — not a BPA-removal system"
"Phenolic effector"
"His100-associated phenol anchor"
"Degradation-pathway response"
"Transfer rule: fixed single-phenol anchor plus an interchangeable wall gate"
"Single-phenol anchor"
"Bridge-facing wall gate"
"Second phenol: optional, not required"
"BPA"
"BPF"
"BPS"
"BPAF"
"Functional mapping does not require a symmetric two-ended clamp"
"BPA20-01 / AG-COF candidate mapping"
"Proposed design — not experimentally validated"
"Candidate inward pyridine-N anchor"
"Candidate methyl wall gate"
"G0: no methyl gate"
"G1: methyl gate"
"G2: fluoro gate"
"C1: anchor deletion"
"50–100 mg microcrystals"
"Wash monomers below LOQ"
"Match topology and pore metrics"
"Optional granulation, binder ≤15 wt%"
"STOP if pore mismatch explains the spectrum"
"E1 mechanism-validation ready; performance unproven"
"Source-supported biological evidence"
"Functional abstraction"
"Proposed artificial relation"

Color and line grammar:
- black or dark grey: source-supported biological function
- blue: single-phenol anchoring abstraction
- muted gold: bridge-facing wall-gate abstraction
- orange dashed lines with question marks: proposed artificial contacts
- red: unvalidated banner and stop icon only

Constraints:
- make the evidence, abstraction, and proposed material visibly different in certainty
- use only the listed text, with exact spelling
- preserve the one-anchor asymmetry and keep the second phenol unanchored
- keep the COF conceptual unless a validated structure asset is supplied
- no exact residue geometry, bond lengths, pore size, binding energy, selectivity result, or adsorption performance
- no logo and no watermark

Avoid:
- placing BPA inside DmpR or PoxR as if direct natural BPA sensing were the project evidence
- a symmetric two-ended BPA clamp
- showing both BPA hydroxyls as required anchors
- atomically precise COF connectivity invented by the image model
- portraying pyridine-N to phenol interaction or methyl-gate discrimination as proven
- implying G1 has already outperformed G0, G2, C1, BPAF, BPF, or BPS
- permanent charge, direct BPA imprinting, protein material components, or successful synthesis and performance claims

Final output: one complete landscape scientific figure for expert review, with a clearly evidentiary Panel A, an abstract Panel B, and an explicitly hypothetical Panel C.
```

## 5. 成图复核清单

- [ ] A 栏没有把 BPA 画成 DmpR/PoxR 的已证实天然效应物。
- [ ] A 栏只把 His100 作为示意性结构约束，没有伪造坐标、距离或残基网络。
- [ ] B 栏只有一个固定酚锚，第二酚端明确为可选。
- [ ] B 栏的门读取中央桥区，没有恢复对称双端夹持。
- [ ] C 栏为内向吡啶 N 与邻近甲基门，且都标为候选。
- [ ] G0、G1、G2、C1 四个同拓扑对照齐全，没有画结果排名。
- [ ] 合成嵌图包含微晶、洗涤、同拓扑/同孔 QC 和 ≤15 wt% 粘结相边界。
- [ ] 没有虚构 COF 键线、孔径、选择性、性能或实验成功。
- [ ] 红色未验证横幅和 E1 性能未证实状态清楚。
- [ ] 文字逐字正确。

## 6. 定向修正提示词

```text
Edit only the incorrect BPA20-01 panel region. Preserve one and only one candidate phenol anchor, keep the second phenolic end explicitly unanchored and optional, and place the candidate wall gate next to the central bridge region. Use orange dashed question-mark lines for every artificial contact. Keep all other graphics, labels, colors, panel sizes, arrows, and legend unchanged. Preserve the red "Proposed design — not experimentally validated" banner. Add no new structural or performance claim.
```
