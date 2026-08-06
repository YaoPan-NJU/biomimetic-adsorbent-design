# 审阅工作流交接 Handoff（2026-08-06）

本文件交接 2026-08-05~06 "高质量方案 HTML 审阅 + 选择性价值判据（Q1/Q2）"工作流的当前状态。新窗口继续前先读本文件，并读记忆：`selectivity-value-criterion.md`、`biomimetic-adsorbent-branch-map.md`（自动注入或手动读 `C:\Users\15995\.claude\projects\C--Users-15995-biomimetic-adsorbent-design\memory\`）。

## 一、分支与提交状态

- 当前分支：`dsreview`，本地 HEAD = **ed7a307**（提级 BPA20-12 审阅卡 + 附录 Q2）
- ⚠️ **ed7a307 已提交但未推送**（本次会话 shell 分类器故障，推送未完成）。新窗口第一步：`git push origin dsreview`
- 已推送基线：main@9877115、Qwen@65b21c3、Ultimate@1abcae0、dsreview@64b8ea4；kimi-k3 冻结未动
- 工作树仅剩 `deliverables/attachments/` 七个未跟踪审阅附件（评审底稿，非本次产物，正常不提交）

## 二、权威文档位置

| 文档 | 分支 | 说明 |
|---|---|---|
| `HIGH_QUALITY_SCHEMES_HTML_REVIEW_2026-08-05.html` | dsreview | 审阅卷主交付物，现 25 卡（新增卡片 1b） |
| `docs/SELECTIVITY_VALUE_CRITERION_2026-08-05.md` | 全部分支 | Q1 判据规范文本（§4 逐方案审计表、§5 整改要求） |
| `rounds/bpa_dcp_20x2_deep_design_20260725/DEEP_DESIGN_AND_SCORECARD.md` | main/dsreview | BPA20-01/DCP20-01 源文件，含附录 Q1（2026-08-05）与 Q2（2026-08-06） |
| `rounds/fresh_1000/bpa/BRIEF.md` | dsreview（含） | BPA 简报，§2/§3 带了 BPF/BPS/BPAF 检出频率与风险证据（Q2 依据） |
| `deliverables/attachments/` | dsreview | 07-31 评审底稿（独立技术审查、裁决底稿、各方案评审） |

## 三、已完成（本工作流）

1. **Q1 选择性价值判据全分支整改**（commit 64b8ea4）：规范文本 + 总纲第五节 + 框架 §6.2/§十二/§10 + SPEC 第 10 条 + GLOBAL_SPEC G9.1 + 各分支 CLAUDE.md 锚点 + 17 方案审计附录。PAN 质询 Q1 共识化：同系物选择性须先证检出频率 + PNEC 风险格局；基质选择性是底线；等摩尔混合物只作机制探针。
2. **HTML 审阅卷**：24 卡九章节，经 10 智能体提取 + 对抗核验（35+ 承重声明回源）。
3. **BPA20-01 审计落地**（2026-08-06）：从 BRIEF.md §2/§3 挖出 BPF/BPS/BPAF 检出频率（上海水源 17/19 种、四川地表水 13–14/14 种、四川盆地 100% 检出率）与风险证据（BPS/BPF 雌激素活性与 BPA 同量级、BPS 小鼠 LOEL 100 nM 低于 BPA 1000 nM），判定命中决策矩阵第三格（风险不低于目标物 → 类级共捕），选择性主张终止。
4. **附录 Q2 + 卡片 1b**（commit ed7a307）：矩阵区分缺口审计（BPA20-01 只设 G1/MATRIX-STOP 耐受性门，无 DOM 因果对照/盐分层/再生，锚失效即矩阵失效）；BPA20-12（HEMA 水化薄壳·AG-COF，79 concept_valid）由负责人提级审阅。

## 四、BPA 线当前立场（负责人质询后，待 U-019 讨论确认）

- **同系物**：BPF/BPS/BPAF 检出高频 + 风险不低于 BPA → **类级共捕**，不区分；四元等摩尔竞争改为环境比例臂
- **BPA20-01**：价值收窄为**机制探针**（锚—门解耦、门谱移动、去锚因果、逆 logKow 四元竞争的可证伪设计）；S2 硬门降为机制探针判据
- **BPA20-12**：提级审阅（卡片 1b）。补矩阵防线（借调 DCP20-01 的 M2 屏障因果/M1 盐分层/M3 再生）；**COF 微晶包壳合成路线是立项前置最大缺口**
- 讨论焦点：机制探针单独立项 vs 与 BPA20-12 合并为"类级共捕 + 抗 DOM 屏障"复合线

## 五、待办（未完成）

1. **推送 dsreview@ed7a307**
2. **Ultimate fresh_1000_R4 新增 150 方案的选择性判据审计**（R4 方案早于判据 2026-08-05，尚未审计；已向负责人提出，未获指令）
3. **台账修复**：Ultimate `STATUS.yaml` 汇总 9 vs 逐项 10（S51 消失）、BDE-209 A07 文件错指
4. **开放问题清单 8 条**（HTML 第八章）待负责人逐条裁决，尤其 #1 "BPA 线整体重组"（a 类级共捕确认 / b BPA20-01 机制探针 vs 复合线 / c 惰性壳必要性 + 包壳路线立项 / d C1-B 电中性对照）
5. 卡片 1 的"独立审查 A 级科学价值最高"徽章与 Q2 后"价值收窄"的口径差异，下一步可考虑在 HTML 卡片 1 头加一行 Q2 注记（本次未改卡片 1 本体，避免冻结文件被改）

## 六、新窗口继续的下一步建议

1. `git push origin dsreview`（清除 §五.1）
2. 打开 HTML 审阅卷，重点看新增卡片 1b 与开放问题 #1
3. 若负责人要推进 BPA 线：先做 BPA20-12 的 COF 微晶包壳可行性纸面设计 + 独立技术审查（79 分未进过裁决底稿）
4. 若负责人批准：启动 Ultimate R4 150 方案选择性审计（§五.2）

## 七、纪律提醒

- 冻结文件只追加不改写（附录式）；kimi-k3 冻结；BMDL 数据库严格只读
- 事实/线索/推断分层标注；证据未全文核验不得标 verified
- 中文书面语遵 SOUL.md 去 AI 腔规则