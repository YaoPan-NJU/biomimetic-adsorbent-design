# `<scheme_id>` 可视化解释提示词包

## 1. 版本锁

```yaml
scheme_id:
material_embodiment:
release_status:
prompt_package_version: 1.0
prompt_status: content_locked
generated_on:
repository_base_commit:
source_design_file:
source_design_sha256:
evidence_ids: []
reference_figure_role: style_reference_only
```

`prompt_status` 只允许 `draft`、`content_locked`、`rendered_unreviewed`、`visual_qc_passed` 或 `stale`。

## 2. 这张图要让专家判断什么

- 生物证据实际支持了什么；
- 从生物证据抽象出的 TR 是什么；
- 当前材料在哪些位置实现了 TR，哪些仍是假说；
- 合成流程能否产生所画结构；
- 哪个对照最先推翻核心映射。

## 3. 可视化主张账本

| ID | 面板 | 要画的对象或关系 | 身份 | 证据或设计定位 | 允许画法 | 禁止外推 |
|---|---|---|---|---|---|---|
| V01 | A |  | `OBSERVED` |  |  |  |
| V02 | B |  | `ABSTRACTED` |  |  |  |
| V03 | C |  | `PROPOSED` |  |  |  |
| V04 | C |  | `UNKNOWN_OMITTED` |  |  |  |

## 4. 参考资产清单

### 必须先提供，否则使用安全示意降级

- `Image 1:` 受控生成并已核对的结构、分子式、曲线或截面；用途和必须保留项。

### 可选

- `Image 2:` 版式或风格参考；不得复制其中的科学内容。

### 禁止模型自行补全

- 未附资产的原子坐标、精确键线、数值距离、真实显微形貌或定量图。

## 5. ImageGen 主提示词

复制下方完整代码块；若提供参考图，在 `Input images` 中按编号说明用途。

```text
Use case: scientific-educational, publication-quality mechanism figure for expert review
Audience: environmental materials scientists, chemists, and biological-domain reviewers
Asset type: one landscape three-panel scientific figure with a compact bottom legend
Primary request: [one sentence]

Input images:
- Image 1: [exact role, or write "none; use safe schematic mode"]

Scene/backdrop: clean white background, generous whitespace, thin separators, no decorative background
Style/medium: restrained scientific vector illustration; crisp typography; schematic where exact structural assets are absent
Composition/framing:
- Panel A: biological evidence
- Panel B: transferable functional abstraction
- Panel C: proposed material mapping plus a compact synthesis inset
- Left-to-right arrows indicate translation, not equal evidential certainty
- Bottom legend explains evidence status and visual grammar

Panel A requirements:
[source-bounded contents]

Panel B requirements:
[material-independent transfer rule]

Panel C requirements:
[candidate material, synthesis sequence, and decisive controls]

Text (verbatim, no other text):
"A"
"B"
"C"
[exact whitelist]

Color and line grammar:
- black or dark grey solid/dashed marks: directly source-supported biological evidence
- blue shapes/arrows: functional abstraction
- orange dashed marks with question marks: proposed artificial interactions or spatial relations
- red banner: proposed design, not experimentally validated

Constraints:
- preserve the distinction between evidence, abstraction, and design hypothesis
- do not invent facts, chemical connectivity, residue positions, dimensions, performance, or validation
- use only the exact labels listed above
- keep all text readable at publication scale
- no logo, no watermark

Avoid:
[scheme-specific failure modes]

Final output: one complete landscape figure suitable for expert scientific review; visually clear but explicitly non-evidentiary for the proposed material.
```

## 6. 成图复核清单

- [ ] A 栏直接目标、类似物、生物结构或过程与来源一致。
- [ ] B 栏没有加入材料名称或未支持的功能。
- [ ] C 栏有醒目的未验证状态，当前释放状态准确。
- [ ] 所有精确化学结构与受控参考资产一致；无资产时没有伪精确结构。
- [ ] 材料组分、空间位置、模板和合成顺序与来源设计一致。
- [ ] 假说接触均为橙色虚线或问号，未与生物证据共用线型。
- [ ] 因果对照和停止点可见且含义正确。
- [ ] 没有新增选择性、容量、再生、抗污、水稳定或尺度主张。
- [ ] 所有文字逐字正确，无多余文本、乱码或错误缩写。

## 7. 定向修正提示词

```text
Edit only [panel/region and exact error]. Replace [wrong content] with [correct content]. Keep the canvas, panel sizes, all other graphics, colors, labels, arrows, and legend unchanged. Preserve the red unvalidated-status banner. Do not add any new claim, molecule, interaction, number, or label.
```
