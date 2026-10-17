---
name: 剪映成片装配
description: 当素材齐了要用剪映草案/FFmpeg/字幕工具装配 60–90 秒竖屏成片时使用。
---
# 剪映成片装配

## 产出
成片装配说明或可执行草案：时间轴、字幕轨、TTS 对齐、BGM 曲线、导出规格；优先可导入剪映草稿或 FFmpeg 脚本说明。

## 借鉴来源
| 仓库 | 约 Stars | 吸收什么 |
|---|---|---|
| [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) | ~4580 | 程序化生成剪映草稿：轨道/素材/字幕时间码 |
| [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) | ~16267 | 字幕断句、校正、烧录前质检 |
| [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | ~1980 | Agent 可用的裁切、混音、抽帧、导出参数 |

## 约束
- 成片竖屏 **1080×1920**；目标时长 **60～90 秒**（实测）
- 人声优先：BGM 不得压过人声
- 字幕准确；不挡脸/不挡关键动作
- **真 UI 叠层**：机内乱码底片必须覆盖可读层，禁止裸 AI 字上屏交审
- 切点跟情绪或动作；高潮/反转前留半拍
- 畸变/双机穿帮段：直接删或换镜，不「凑合切」

## 步骤
1. 收齐：分镜、画面、配音 cue/WAV、三锁、提示师叠层备注。
2. 排时间轴；标必保三镜；砍红线脏段。
3. 叠真 UI / 字幕轨；对白标说话人。
4. BGM 音量曲线；轻触控/环境底噪可补，勿砸乐。
5. 自检：`ffprobe` 时长画幅；抽 3 帧看 UI 是否可读。
6. 交付：成片路径或装配说明 + 时间轴表 + 给审片的变更摘要。

## 打回时
只改装配与叠层；不擅自改剧本。
