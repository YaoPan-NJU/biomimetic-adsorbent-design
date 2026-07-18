# main近期提交与推送归属审计

审计时间：2026-07-18 17:23（Asia/Shanghai）

审计范围：`main`截至`5ea8e4e7a3d39a332814d64c9142197819e4dcc4`。

## 1. 能够从Git数据确认什么

- 最近30个`main`提交的Git作者和提交者均记录为`Yao Pan <yaopan@nju.edu.cn>`。这是当前Git配置身份，不等于能够识别具体操作者是潘尧本人、某台电脑上的Codex或其他代理。
- GitHub Repository Events API显示，近期`main` PushEvent的actor均为`YaoPan-NJU`。两台电脑和Codex使用同一个GitHub账号或凭据时，GitHub事件只能确认账号，不能区分设备或实际执行者。
- 当前工作目录的本地reflog可以确认哪些提交在这份本地检出中被创建或拉取，但它同样不会给出“由哪个Codex任务发起”的可靠身份字段。

因此，提交作者、提交者和PushEvent账号不能单独用于认定实际推送人。可靠归属需要结合具体任务中的命令执行记录。

## 2. 本任务可直接确认由当前Codex执行的近期推送

| 本地时间 | 提交 | 内容 | 归属依据 |
|---|---|---|---|
| 2026-07-18 14:35 | `e60a1e0` | broaden ROX biomimetic design tournament | 当前任务成功执行`git push origin main` |
| 2026-07-18 14:36 | `7d7350d` | record ROX checkpoint continuity | 当前任务成功执行`git push origin main` |
| 2026-07-18 17:02 | `f86910d` | reframe ROX as low-cost macrolide adsorption | 当前任务成功执行`git push origin main` |
| 2026-07-18 17:04 | `77e143c` | record macrolide replan continuity | 当前任务成功执行`git push origin main` |
| 2026-07-18 17:22 | `5ea8e4e` | complete MAC-BI1 narrative and audit pushes | 当前任务成功执行`git push origin main`；GitHub PushEvent actor为`YaoPan-NJU` |

上述五次GitHub PushEvent的actor均为`YaoPan-NJU`，时间与本地提交链一致。

## 3. 不能仅凭当前证据归到本任务的提交

`9ac60dc`及更早提交虽然同样显示作者、提交者为Yao Pan，GitHub actor为YaoPan-NJU，但这些字段不能区分办公室电脑、当前电脑或其他Codex任务。本审计不把它们武断归到当前Codex名下。

## 4. 后续改进

为减少跨设备归属歧义，后续每个检查点可在提交说明或状态文件中记录非敏感执行标签，例如`executor: codex_home`、`executor: codex_office`或人工确认的设备别名。该标签只用于项目审计，不包含令牌、机器用户名或绝对路径。
