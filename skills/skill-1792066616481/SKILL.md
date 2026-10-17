---
name: 即梦出片提示
description: 当要为即梦/Seedance 2.0 按镜写可复制提示（含@引用、时间戳分镜、禁乱码）时使用。
---
# 即梦出片提示

## 产出
按镜号可复制提示：三锁前缀 + 本镜动作/构图/光线 + 9:16；超长则分段+衔接点；附负面禁止项（乱码/多指/错脸）。

## 借鉴来源
| 仓库 | 约 Stars | 吸收什么 |
|---|---|---|
| [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) | ~4324 | @Image/@Video 角色分配；时间戳分段；运镜词表；短剧对白模板 |
| [songguoxs/seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill) | ~2931 | 中文提示结构；禁止项声明；>15s 分段延长+衔接点 |
| [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | ~2146 | 提示词素材库作参考，不整段抄袭成片 |

## 铁律
- **禁止指望模型生成可读屏内汉字/复杂 UI。** 叙事 UI 在提示里写「blank/generic phone UI, no legible text」，并注明「后期叠真 UI」。
- 每镜复用角色锁与画风锁全文；一次只改一个主变量（动作或机位）。
- 负面写死：`extra fingers, face morph, on-screen gibberish text, watermark, wrong character name, fused dual phones`
- 单段按时长能力拆（常 4～15s）；多段写衔接点（结束状态→下段开头）。

## 提示公式（吸收 Seedance Skill）
`[画幅9:16] + [三锁前缀] + [主体动作] + [场景] + [运镜] + [时段光] + [音效氛围可选] + [禁止项]`

短剧对白镜：画面与台词分行；台词标角色+情绪。

## 步骤
1. 读分镜 + 三锁；标出「需真 UI 叠层」镜。
2. 组装全局前缀；按镜输出（中文主提示优先，平台吃中文时）。
3. >15s 故事段：拆多段并写衔接点。
4. 失败镜建议：保留 / 重掷 / 改写（改写优先砍乱码源）。
5. 交付：提示清单 + 推荐生成顺序（必保镜优先）+ 叠层备注。

## 不做
不擅自调用收费 API 出片；出片由出片执行岗/协调者授权。
