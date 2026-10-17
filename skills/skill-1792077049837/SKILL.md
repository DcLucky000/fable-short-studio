---
name: 短片自动配音
description: 当寓言短片剧本需要 TTS 选角、旁白/角色分轨、cue sheet 与导出规格时使用。
---
# 短片自动配音

## 产出
配音 cue sheet + TTS 粘贴稿 + 声线卡；可选 WAV/SRT（授权后导出）；对齐 60～90 秒时间轴。

## 借鉴来源
| 仓库 | 约 Stars | 吸收什么 |
|---|---|---|
| [rany2/edge-tts](https://github.com/rany2/edge-tts) | ~12305 | 免费中文音色兜底（晓晓/云希/云健等）；日更不断档 |
| [QwenAudio/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 或 CosyVoice 生态 | 高 | 固定角色音色/情感（需算力时） |
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | ~1535 | 有 Key 时的高质感 MCP 导出 |

> 仓库名以当时 GitHub 实名为准；CosyVoice 组织名可能为 FunAudioLLM。

## 目标
- 旁白与角色声线可区分；同角色全片不换声
- 句级时间码可对齐分镜；核心三句标「必保」
- 默认不烧额度：可先交 cue，等协调者点头再批量 TTS

## 步骤
1. 从剧本拆旁白轨/角色轨：说话人、情绪、原文、预估秒数。
2. 声线卡：旁白中性说书；角色各 1 套（edge-tts 音色名或 CosyVoice 描述）。
3. 禁：音乐压人声；口型强绑做不到则画外音+过肩。
4. 输出：cue sheet（镜号/说话人/台词/情绪/时长）+ tts_paste + 导出规格（WAV、约 -14 LUFS、命名 `shot#_role`）。
5. 分镜变更后只改镜号列，不重写声线除非打回。

## 交付检查
- [ ] 每句有说话人
- [ ] 核心三句标必保
- [ ] 总人声时长支撑 60～90s 故事（过短回编剧加节拍）
