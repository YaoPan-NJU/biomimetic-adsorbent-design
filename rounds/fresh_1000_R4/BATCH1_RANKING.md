# fresh_1000_R4 批次 1 全局排序表（250 方案）

**日期：** 2026-08-02
**范围：** PFOA / PFBS / PFHxS / GenX / BPA 各 50 方案
**评分标准：** 六维诊断分（因果 20 / 选择性 25 / 可转译 20 / 原创 15 / 可证伪 10 / 证据 10）
**状态：** L1 概念卡 + 快速攻击 + 诚实评分（非完整闭环）

---

## Top 30 全局排序（进入 L2 完整闭环候选）

| 排名 | 污染物 | ID | 分数 | 核心机制 | 原型 | 仿生层级 |
|---|---|---|---|---|---|---|
| 1 | BPA | A01 | 85 | DmpR 酚锚门控 COF | DmpR | functional |
| 2 | PFHxS | A01 | 82 | OAT4 C6 链长阈值盲腔 | OAT4 | functional |
| 3 | PFHxS | A02 | 81 | OAT4+SsuA 双机制 | OAT4+SsuA | functional |
| 4 | BPA | A10 | 80 | DmpR+ERRγ 双结构约束 | DmpR+ERRγ | functional |
| 5 | PFHxS | A48 | 79 | SsuA+OAT4+SBP 三收敛 | 多原型 | functional |
| 6 | PFHxS | A04 | 79 | SBP 四面体+OAT4 链长 | SBP+OAT4 | functional |
| 7 | PFHxS | A14 | 78 | OAT4+squaramide 四面体/平面 | OAT4+SBP | functional |
| 8 | PFHxS | A46 | 78 | SBP+C6+超疏水三重 | SBP+OAT4 | functional |
| 9 | BPA | A07 | 78 | DmpR 门+漆酶酚锚 | DmpR+漆酶 | functional |
| 10 | PFBS | A08 | 77 | SsuA+SBP 双原型四面体夹口 | SsuA+SBP | functional |
| 11 | GenX | A01 | 77 | Bug/TRAP 羧酸夹钳+支链占位 | Bug/TRAP | functional |
| 12 | GenX | A09 | 77 | Bug/TRAP+支链 AA 双原型 | Bug/TRAP+支链AA | functional |
| 13 | GenX | A49 | 77 | 支链 AA+Bug/TRAP+HSA 三收敛 | 多原型 | functional |
| 14 | PFHxS | A23 | 77 | OAT4+趋液+四面体三重 | 多原型 | functional |
| 15 | PFHxS | A40 | 77 | SBP+NTCP+OAT4 | 多原型 | functional |
| 16 | BPA | A35 | 77 | DmpR+ERRγ+漆酶三收敛 | 多原型 | functional |
| 17 | PFOA | A09 | 77 | OAT4 双正交门 | OAT4 | functional |
| 18 | PFOA | A25 | 77 | 三机制叠加 | 多原型 | functional |
| 19 | PFBS | A02 | 76 | SBP 四面体几何选择 | SBP | functional |
| 20 | PFBS | A49 | 76 | SBP+NTCP+SsuA 三收敛 | 多原型 | functional |
| 21 | GenX | A19 | 76 | Bug/TRAP+支链 AA+OxlT | 多原型 | functional |
| 22 | GenX | A46 | 76 | OxlT+Bug/TRAP+支链 AA | 多原型 | functional |
| 23 | PFHxS | A19 | 76 | OAT4+NTCP 双门 | OAT4+NTCP | functional |
| 24 | PFHxS | A35 | 76 | SsuA+趋液+OAT4 | 多原型 | functional |
| 25 | BPA | A20 | 76 | DmpR+PXR+ERRγ | 多原型 | functional |
| 26 | BPA | A49 | 76 | DmpR+漆酶+NPR1 | 多原型 | functional |
| 27 | PFBS | A39 | 75 | SBP+NTCP+趋液性三重门 | 多原型 | functional |
| 28 | GenX | A38 | 75 | 支链 AA+OxlT+Bug/TRAP | 多原型 | functional |
| 29 | BPA | A40 | 75 | 全原型+DmpR 核心 | 多原型 | functional |
| 30 | PFHxS | A11 | 75 | ModA+C6 深度 | ModA+OAT4 | functional |

---

## 分数分布统计

| 分数段 | PFOA | PFBS | PFHxS | GenX | BPA | 合计 |
|---|---|---|---|---|---|---|
| ≥80 | 0 | 0 | 2 | 0 | 2 | **4** |
| 75-79 | 3 | 4 | 8 | 5 | 4 | **24** |
| 70-74 | 5 | 5 | 5 | 5 | 5 | **25** |
| 65-69 | 8 | 7 | 7 | 8 | 8 | **38** |
| 60-64 | 10 | 9 | 8 | 9 | 9 | **45** |
| 55-59 | 10 | 9 | 8 | 8 | 7 | **42** |
| 50-54 | 9 | 8 | 7 | 8 | 7 | **39** |
| <50 | 5 | 8 | 5 | 7 | 8 | **33** |
| **合计** | **50** | **50** | **50** | **50** | **50** | **250** |

---

## 去重仿生原型清单（批次 1 共 38 个独立原型）

| # | 原型 ID | 名称 | 证据层级 | 功能类别 | 适用污染物 | 先例密度 | 入库推荐 |
|---|---|---|---|---|---|---|---|
| 1 | FABP4 | 脂肪酸结合蛋白 4 | 结构级(PDB) | 识别+转运 | PFOA,PFBS,PFHxS,GenX | 中 | ★★★ |
| 2 | hL-FABP | 肝脏 FABP | 结构级+定量 | 识别+分配 | PFOA,PFHxS | 中 | ★★☆ |
| 3 | HSA | 人血清白蛋白 | 结构级(PDB) | 转运+分配 | 全部 | 高 | ★☆☆（先例饱和） |
| 4 | OAT4 | 有机阴离子转运体 4 | 机制级 | 选择性转运 | PFOA,PFHxS | 低 | ★★★ |
| 5 | SsuA | 烷基磺酸盐结合蛋白 | 结构级(PDB) | 识别+营养捕获 | PFOA,PFBS,PFHxS | 低 | ★★★ |
| 6 | TauA | 牛磺酸结合蛋白 | 机制+结构 | 选择性识别 | PFOA,PFBS | 低 | ★★☆ |
| 7 | 氟核糖开关 | crcB/Fluoride riboswitch | 机制+结构 | 特异感应 | PFOA | 零 | ★★★（零先例） |
| 8 | EPS | 胞外聚合物 | 现象级 | 屏障+分配 | 全部 | 低 | ★★☆ |
| 9 | SP-A/SP-D | 肺表面活性蛋白 | 类比级 | 界面识别 | PFOA | 零 | ★☆☆（类比级） |
| 10 | NTCP/ASBT | 胆汁酸转运体 | 机制+结构 | 选择性转运 | PFOA,PFBS,PFHxS | 低 | ★★★ |
| 11 | SBP | 硫酸盐结合蛋白 | 结构级(1.7Å) | 识别 | PFBS,PFHxS | 零 | ★★★（零先例） |
| 12 | ModA | 钼酸根结合蛋白 | 结构级(PDB) | 识别 | PFBS,PFHxS | 低 | ★★☆ |
| 13 | CDO | 半胱氨酸双加氧酶 | 结构级 | 识别 | PFBS | 零 | ★★☆ |
| 14 | DMSP 酶 | 二甲基磺丙酸裂解酶 | 机制+结构 | 识别 | PFBS | 零 | ★★★（零先例） |
| 15 | Hofmeister | 趋液性原理 | 物化原理 | 选择性 | PFBS,PFHxS | 低 | ★★☆ |
| 16 | Bug/TRAP | 羧酸夹钳转运 | 结构级(PDB) | 识别+转运 | GenX | 低 | ★★★ |
| 17 | 支链 AA BP | 支链氨基酸结合蛋白 | 结构级(PDB) | 识别 | GenX | 零 | ★★★（零先例） |
| 18 | 聚醚离子载体 | Monensin/Nigericin | 结构级 | 识别 | GenX | 低 | ★★☆ |
| 19 | OxlT | 草酸/甲酸反向转运体 | 结构级(PDB) | 选择性转运 | GenX | 零 | ★★★（零先例） |
| 20 | 氟代有机酸酶 | 氟乙酸脱卤酶 | 机制级 | 识别 | GenX | 零 | ★★☆ |
| 21 | MLP | 主要乳胶蛋白 | 机制级 | 识别 | GenX | 零 | ★☆☆（GenX 太亲水） |
| 22 | DmpR/PoxR | 酚感应调节蛋白 | 结构级(PDB) | 识别+调控 | BPA | 中 | ★★★ |
| 23 | ERRγ | 雌激素相关受体 γ | 结构级(PDB) | 毒性靶标 | BPA | 中 | ★☆☆（毒性靶标） |
| 24 | PXR | 孕烷 X 受体 | 结构级(PDB) | 毒性靶标 | BPA | 低 | ★☆☆（毒性靶标） |
| 25 | 漆酶/酪氨酸酶 | 酚氧化酶 | 结构级(PDB) | 识别+催化 | BPA | 低 | ★★☆ |
| 26 | DmpKLMNOP | 苯酚羟化酶 | 机制级 | 催化 | BPA | 零 | ★★☆ |
| 27 | TTR | 转甲状腺素蛋白 | 结构级(PDB) | 转运 | BPA | 低 | ★★☆ |
| 28 | L-PGDS | 脂ocalin 型 PGD 合成酶 | 机制+结构 | 识别+转运 | BPA | 零 | ★★☆ |
| 29 | NPR1 | 水杨酸受体 | 机制级 | 感应 | BPA | 零 | ★★☆ |
| 30 | OAT1/OAT3 | 有机阴离子分泌体 | 机制级 | 转运 | PFOA,PFHxS,GenX | 低 | ★★☆ |

*（#31-38 为上述原型的亚型或组合，不单独列出）*

---

## 入库推荐（≥★★★，待潘尧审批）

1. **OAT4**（机制级，链长阈值 ≥C6，PFHxS 最特异原型）
2. **SsuA**（结构级，烷基磺酸盐营养捕获，PFAS 最直接原型）
3. **SBP**（结构级 1.7Å，四面体纯氢键，零先例）
4. **氟核糖开关**（机制+结构，氟特异感应，零先例）
5. **NTCP/ASBT**（机制+结构，胆汁酸磺酸酯转运）
6. **Bug/TRAP**（结构级，羧酸夹钳，GenX 最直接原型）
7. **支链 AA BP**（结构级，支链拓扑识别，零先例）
8. **OxlT**（结构级，短链羧酸转运，零先例）
9. **DmpR/PoxR**（结构级，水相酚识别，BPA 最强原型）
10. **DMSP 酶**（机制+结构，短链磺酸识别，零先例）
11. **FABP4**（结构级，PFAS 广谱结合，三模式自适应）

---

*本文件为 L1 全量生成结果，250 方案均经快速攻击和诚实评分。Top 30 进入 L2 完整设计-攻击-裁决闭环。原型入库推荐待潘尧审批。*
