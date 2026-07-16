# PBP 构建体来源与身份记录

核验日期：2026-07-16。来源为 RCSB PDB 的公开结构记录和 FASTA，不包含数据库凭据或受限全文。

## 来源核对

- [1OIB 结构记录](https://www.rcsb.org/structure/1OIB)将实体标为 *E. coli* phosphate-binding protein mutant T141D，序列长度 321 aa。
- [1OIB FASTA](https://www.rcsb.org/fasta/entry/1OIB/display)与[1IXG FASTA](https://www.rcsb.org/fasta/entry/1IXG/display)逐字符相同，均为 321 aa。
- 源成熟链的 SHA-256 为 `78558e51049eec070b0f3249ffa8617b37a45b912436af1274ed746b57931a96`。编号 56 为 Asp，141 为 Asp，197 为 Ala。

## 项目变体

项目只在源成熟链上定义以下变体，精确序列见 `deliverables/attachments/PBP_CONSTRUCTS.fasta`：

| 构建体 | 改动 | 长度 | SHA-256 |
|---|---|---:|---|
| 主成熟链 | T141D 源链上 A197C | 321 aa | `5f90614377b9f30b131c0df1c67cbef7daf8af2be860c1fa5f78fc327a533d25` |
| D56N 对照成熟链 | 主成熟链上 D56N | 321 aa | `f77e94a790526b535c8e766b143b25377b46966bb415dc05e7336f37e96964b1` |
| 主可溶前体 | 主成熟链 + `LPETGHHHHHH` | 332 aa | `d249767e91791d500c87a84e9e95274f74b675665cf4df8c4aae747fe79312ff` |
| D56N 可溶前体 | 对照成熟链 + `LPETGHHHHHH` | 332 aa | `59c1f69bd43a776d4271b7e4dddc2b23bafbead10c69c04f9bd341e97c2f46a8` |

表达载体中的信号肽、启动子、抗性标记和经供应商密码子优化后的 DNA 不在现有结构记录中。实验开始前须冻结载体图谱和 DNA 文件；翻译产物必须与本附件的氨基酸序列一致。理论质量只能在最终化学修饰、起始 Met/信号肽加工和 sortase 产物边界确定后计算，不能用裸蛋白估算值替代 intact LC-MS 放行。

## Sortase 产物边界

前体 C 端为 `...LPETG-His6`。sortase 应在 Thr 与 Gly 之间切割并与支架上的 `GGGK` 形成 `...LPET-GGGK-support` 结点。固定产物的肽图必须检出跨结点肽；`G-His6` 不计入固定蛋白质量。该表述是工艺身份定义，不代表反应已成功。
