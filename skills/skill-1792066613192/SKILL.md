---
name: 短片导演分镜
description: 当要把寓言剧本拆成 60–90 秒竖屏分镜表（景别、情绪、必保镜、节奏）时使用。
---
# 短片导演分镜

## 产出
竖屏 9:16 镜头表：镜号、时长、景别、画面、旁白/对白归属、音效、情绪；总时长对准 **60～90 秒**；标必保三镜与中段刺激点。

## 借鉴来源
| 仓库 | 约 Stars | 吸收什么 |
|---|---|---|
| [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | ~6747 | 短剧端到端：剧本→分镜字段齐全、镜头可执行 |
| [liangdabiao/Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | ~2613 | 分镜可生成性：单镜动作闭合、时长片 |
| [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder)（若可及） | — | 视频规格书：画幅/时长/镜头语言字段化 |
| [henjicc/Storyboard-Copilot](https://github.com/henjicc/Storyboard-Copilot) | ~713 | 节点化分镜：前后镜衔接状态 |

## 原则
- 前 **3 秒**必须有钩子画面（冲突/反常/疑问），禁止先空镜铺环境。
- 时钟节奏：开场钩 → 中段刺激① → 中段刺激②/转折 → 收束点题；空白段=划走风险。
- 远中近与正反打要有理由；关键动作完整可读。
- 叙事依赖的手机/UI：**规划为真 UI 叠层或可读合成**，禁止指望模型「生成可读汉字」。
- 点题用空镜或结果画面，禁止真人说教硬念。
- 人脸特写占比克制；UI/物件特写可抬高（故事需要时）。

## 步骤
1. 读剧本 + 三锁卡。
2. 按钩子/加压/转折/点题切成约 8～14 镜，标秒数，总和 60～90s。
3. 每镜写清：谁说话、画面主体、结束状态（供下镜衔接）、情绪目标。
4. 标「必保三镜」+「中段刺激镜」；标哪些镜需要后期真 UI 叠层。
5. 交付：镜头表 + 情绪曲线一句 + 衔接风险一句。

## 打回时
按审片/HKRR 指出的镜号改表，不擅自改寓意落点。
