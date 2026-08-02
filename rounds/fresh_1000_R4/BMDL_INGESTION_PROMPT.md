# 任务：审阅、优化并入库 fresh_1000_R4 仿生原型

## 背景与目标

biomimetic-adsorbent-design 项目 Ultimate 分支完成了 1000 个仿生吸附材料概念设计（20 污染物 × 50 方案），产生了约 90 个独立仿生原型（分布在 20 个污染物目录的 PROTOTYPE_REGISTRY 和 CONCEPT_CARDS 文件中）。

你的任务不是原样搬运这些原型，而是：
1. **逐个审阅**所有 ~90 个原型，评估其是否达到 BMDL 入库质量
2. **主动联网搜索验证 + 深度研究思考**，确认原型的科学准确性和转译价值
3. **分析、优化、补全**不到位的地方（因果链不完整、转译原则模糊、边界规则缺失、证据层级标注不准确等）
4. **只将优化后达到 BMDL 质量标准的原型入库**——不达标的宁可不入，也不降标凑数

## 工作分支

在 `massive` 分支操作（从 main 创建）。完成后推送至 origin/massive，待我审阅后并入 main。

## 源数据位置

biomimetic-adsorbent-design 项目 Ultimate 分支（`https://github.com/YaoPan-NJU/biomimetic-adsorbent-design.git`）：
- `rounds/fresh_1000_R4/pfoa/PROTOTYPE_REGISTRY.md`（最详细的 10 原型格式，含证据层级、转译原则、先例密度）
- `rounds/fresh_1000_R4/[pollutant]/SCHEMES/CONCEPT_CARDS_FULL.md`（各污染物原型注册表节，20 个文件）
- `rounds/fresh_1000_R4/GLOBAL_RANKING_1000.md`（总览 + 18 个 ★★★ 推荐）
- `rounds/fresh_1000_R4/L2/`（L2 深度闭环中的原型评估和材料实体合并图谱）

20 个污染物目录：pfoa, pfbs, pfhxs, genx, bpa, np, rox, octocrylene, ddt, dieldrin, pcp, betahch, hcbd, bde209, pcb209, dcp26, chloroform, dde, endosulfan, tcdd

## 审阅流程

### Step 1: 去重检查

与 BMDL 现有 ~100 个原型（`prototypes_db/*.json`）逐一对比。判断标准：
- 如果自然功能、作用机制和可转译原则实质相同 → 标记为"已有，跳过"
- 如果仅是名称不同但机制相同 → 跳过
- 如果是已有原型的新亚型/新应用场景（如 P450BisD 已在库中，但 CYP3A4 大环内酯代谢是新机制）→ 视为新原型，继续评估

### Step 2: 质量评估（联网验证 + 深度研究）

对每个通过去重的原型，不是被动检查已有描述是否"看起来完整"，而是**主动验证和深度思考**：

#### 联网搜索验证（必须执行，每个原型至少一次搜索）

- 搜索该生物原型的原始文献，确认其自然功能描述是否准确（不依赖概念卡中的转述）
- 验证引用的 PDB/DOI/PMID 是否真实存在且支持所声称的结论
- 搜索是否有更新的文献修正或补充了该原型的机制理解
- 搜索该原型在吸附材料领域是否已有应用先例（判断先例密度和原创性）
- 对关键数据（结合常数、选择性比值、突变效应量级）进行交叉验证

#### 深度研究思考（必须执行）

- **独立推理因果链**：从生物结构到可转译原则，每一步逻辑是否有实验/理论支撑，还是有跳跃？
- **独立判断转译原则**：这个原则是否足够具体到可以指导材料设计，还是只是泛泛而谈？
- **独立思考边界条件**：在什么水化学条件（pH/离子强度/DOM/浓度）下该原理会失效？
- **独立评估与已有原型的差异**：是真正的新机制，还是已有原型的表面改写？
- **对毒性靶标/催化酶**：独立思考是否存在非毒性/非催化的功能抽象视角

#### 评估结论标记

- ✅ **达标**：联网验证通过 + 因果链逻辑自洽 + 转译原则可操作 + 边界清晰
- ⚠️ **需优化**：指出具体缺陷（如"因果链第 3 步跳跃：从 X 到 Y 缺少 Z 证据"）和优化方向
- ❌ **不达标**：指出根本性问题（如"自然功能描述错误：该蛋白实际功能是 A 而非 B"或"转译原则不可操作：'做一个腔'不是原则"）

#### 关键要求

每个原型的评估必须附带至少一次联网搜索的证据（搜索了什么、找到了什么、是否支持/否定了概念卡中的描述）。不允许仅凭内部知识下结论。

### Step 3: 优化（对 ⚠️ 类）

- 补全因果链（从文献中补充缺失的逻辑环节）
- 明确转译原则（从模糊描述提炼为可操作规则）
- 添加边界规则（标注不适用条件）
- 修正证据层级（降级膨胀的标注）
- 补充来源（联网搜索验证）
- 添加 failure_modes（什么情况下转译会失败）

### Step 4: 入库（对 ✅ 和优化后的 ⚠️）

创建 `prototypes_db/<kebab-case-id>.json`，完整 BMDL 数据模型：

```json
{
  "id": "kebab-case-id",
  "name": "原型名称",
  "organism": "来源生物",
  "biomimetic_dimension": "static/dynamic/both",
  "features": ["分子特征列表"],
  "tested_conditions": {"pH": "...", "temperature": "...", "relevant_pollutants": [...]},
  "mechanisms": [
    {
      "mechanism_id": "MECH_XXX_001",
      "name": "机制名称",
      "基本原理": "...",
      "causal_chain": ["步骤1", "步骤2", "..."],
      "functional_groups": ["..."],
      "key_structures": ["..."],
      "transferable_principle": "可转译原则（不依赖材料名称）",
      "evidence_tier": "fact/lead/exploratory",
      "sources": [{"doi": "...", "title": "...", "year": 2020, "claim_supported": "..."}]
    }
  ],
  "design_translation": [
    {
      "idea": "材料设计思路",
      "material_handle": "材料实现把手",
      "target_interaction": "目标相互作用",
      "constraints": ["约束条件"],
      "failure_modes": ["失效模式"],
      "material_realization_examples": ["示例"]
    }
  ],
  "boundary_rules": [
    {
      "rule": "不适用条件/禁止外推",
      "source_mechanism": "MECH_XXX_001",
      "gate_level": "hard/soft",
      "basis": "依据"
    }
  ],
  "honesty_ledger": {
    "facts": ["已接地事实"],
    "leads": ["待核验线索"],
    "inferences": ["推断"],
    "do_not": ["禁止外推"]
  },
  "sources": [{"doi": "...", "title": "...", "year": 2020, "locator": "..."}]
}
```

### Step 5: 产出审阅报告

输出一份 `MASSIVE_INGESTION_REVIEW_REPORT.md`，包含：
- 审阅总数 / 去重跳过数 / 达标数 / 优化后达标数 / 不达标数
- 每个原型的审阅结论（✅/⚠️/❌ + 一句话理由 + 联网搜索证据摘要）
- 不达标原型的具体原因
- 入库原型清单（含证据层级）
- 与已有 BMDL 原型的关联说明

## 入库质量门（必须全部满足）

### 必须有的（缺一不入）
- [ ] **清晰的自然功能描述**：该生物体系在自然中执行什么功能（不是"与某污染物有关"，而是"在什么生物过程中做什么"）
- [ ] **完整的因果链（causal_chain）**：从生物结构→相互作用机制→为什么有效→可迁移原则，逻辑链完整无跳跃
- [ ] **明确的可转译原则（transferable_principle）**：不依赖特定材料名称的、可操作的功能规则
- [ ] **至少一条边界规则（boundary_rule）**：什么条件下不适用、什么外推是禁止的
- [ ] **诚实的证据层级标注**：fact/lead/exploratory 准确，不膨胀
- [ ] **可追溯的来源**：至少一个经验证的 DOI/PMID/PDB/URL

### 质量加分项
- 有 PDB 结构证据
- 有突变/结合/转运实验数据
- 有明确的 failure_modes
- 有与已有原型的区分说明
- 有跨污染物适用性说明

### 不入库的情况
- 自然功能描述模糊（"与某污染物结合"但说不清生物功能）
- 因果链有跳跃（"因为蛋白结合 X，所以材料也能吸附 X"）
- 转译原则只是重复材料设计（"做一个腔"不是转译原则）
- 纯类比无机制（"因为形状像所以能用"）
- 与已有 BMDL 原型实质重复
- 毒性靶标且无法提供非毒性转译视角
- 联网搜索发现概念卡中的描述与原始文献不符

## 特殊类型处理规则

### 毒性靶标（ERRγ/AhR/Rdl/ER 等）
- 可以入库，但必须在 boundary_rules 中标注 `"toxicity_target_not_primary_biomimetic_source"`
- 转译原则必须是非毒性的功能抽象（如"刚性疏水腔内单一极性接触的调制"而非"模拟毒性结合"）
- 如果无法找到非毒性转译视角 → 不入库

### 催化酶（漆酶/P450/脱氯化氢酶/环氧化物水解酶等）
- 可以入库，但转译原则必须标注 `"catalytic_function_translated_as_recognition_only"`
- 只转译识别几何/底物选择性，不转译催化功能
- 如果该酶的价值仅在于催化（无独立识别价值）→ 不入库

### 物化原理（Hofmeister/卤键/膜分配/偶极矩等）
- 可以作为原型入库（BMDL 接受非生物原型）
- 必须标注 `"physicochemical_principle_not_biological_function"`
- boundary_rules 中说明"非生物功能，无进化优化，无特异性"
- 如果该原理过于泛化（如"疏水作用"）→ 不入库（太泛，无设计指导价值）

### 已有 BMDL 原型的新应用场景
- 如果机制相同但适用污染物不同 → 不新建原型，而是在已有原型的 tested_conditions 中补充（但这需要修改已有文件，本次不做，仅在报告中标注"建议补充"）
- 如果机制不同（如 P450BisD 是 BPA 双酚氧化，CYP3A4 是大环内酯 N-脱甲基）→ 视为新原型

## 禁止事项

- 不修改 BMDL 已有原型文件（只新增）
- 不填 performance_data（无实验数据）
- 不自动并入 main（等我审阅）
- 不降标凑数（质量优先于数量）
- 不把"某蛋白结合某污染物"直接当作入库理由
- 不跳过联网搜索验证（每个原型至少一次搜索）
- 不凭内部知识下结论（必须有搜索证据支撑判断）

## 质量门控脚本

每批入库后运行：
```bash
python -X utf8 tools/validate_consistency.py --strict
python -X utf8 tools/check_source_authenticity.py
python -X utf8 tools/check_causal_chain.py
python -X utf8 tools/check_repo_hygiene.py
```

全部通过后提交推送至 origin/massive。
