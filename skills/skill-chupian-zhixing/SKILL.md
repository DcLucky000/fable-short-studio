---
name: 短片出片执行
description: 当提示与三锁已齐、授权后要按镜调用即梦/Seedance（或等价工具）生成底片并做失败重试时使用。
---
# 短片出片执行

## 产出
按镜底片文件（或手动粘贴清单）+ 失败镜记录 + 交给剪辑的素材索引；**默认不自动烧额度**，须协调者/用户授权。

## 借鉴来源
| 仓库 | 约 Stars | 吸收什么 |
|---|---|---|
| [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) | ~4324 | 输入上限、@引用角色、单段时长、失败重试策略 |
| [songguoxs/seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill) | ~2931 | 分段延长、衔接点、禁止真人脸参考上传（平台规则） |
| [FireRedTeam/StoryMaker](https://github.com/FireRedTeam/StoryMaker) | ~720 | 角色参考图锚定跨镜 |
| [lybx-leyw/shortdrama-workplace](https://github.com/lybx-leyw/shortdrama-workplace) | — | 生成后 vision 抽检：乱码/伪影 fail 则重出不交脏片 |

## 铁律
1. **无授权不出片**（不调收费 API）。
2. 严格粘贴提示师提示 + 三锁前缀；不擅自删负面禁止项。
3. 生成后对本镜抽 1～2 帧自检：乱码 UI、多指、错脸 → **本镜重出或标记废弃**，禁止把红线脏片标「已交付」。
4. 叙事汉字 UI：底片保持无字或不可读占位，等剪辑叠真 UI。
5. 必保镜优先；额度紧时先保钩子/转折/点题。

## 步骤
1. 确认授权与额度预算；读提示清单与生成顺序。
2. 按序生成；记录种子/参数/耗时（若平台提供）。
3. 镜级自检；fail → 重掷最多 N 次（默认 2）→ 仍 fail 则改回提示师。
4. 交付：素材路径表（镜号|文件|自检pass/fail|备注）。

## 不做
不替代审片终检；不发布；不改剧本寓意。
