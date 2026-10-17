# 寓言短片工作室 · 各岗高星 Skill / 工具调研

数据来源：GitHub search_repositories 实时查询，2026-10-17 14:40（UTC+8）。star 为当时实数。本次未在本机安装任何东西。

| 岗位 | 仓库 | Star | 做什么 | 是否建议装 |
|---|---|---|---|---|
| 编剧 | [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | 7680 | Claude Code/Codex 中文网文写作 Skill（扫榜、拆文、写作） | ✅ 拆文/结构参考 |
| 编剧 | [liangdabiao/Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | 2613 | 剧情剧本 Skill，一句话→剧本/分镜 | ✅ |
| 三锁 | [FireRedTeam/StoryMaker](https://github.com/FireRedTeam/StoryMaker) | 720 | 文生图角色一致性模型 | ⚠️ 需 GPU，作方法参考 |
| 三锁 | [Murray-Wang/CharaConsist](https://github.com/Murray-Wang/CharaConsist) | 166 | ICCV 2025 细粒度角色一致性 | ⚠️ 研究代码，不装 |
| 导演 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | 6747 | AI 短剧端到端：剧本→分镜→成片 | ✅ 流程参考 |
| 导演 | [waooAI/waoowaoo](https://github.com/waooAI/waoowaoo) | 14571 | 全流程 AI 影视生产 Agent 平台 | ⚠️ 平台较重，参考 |
| 导演 | [henjicc/Storyboard-Copilot](https://github.com/henjicc/Storyboard-Copilot) | 713 | 节点画布分镜工作台 | 可选 |
| 出片提示师 | [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) | 4324 | Seedance 2.0 提示词 Skill | ✅ 首选 |
| 出片提示师 | [songguoxs/seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill) | 2931 | 中文 Seedance 2.0 提示词 Skill | ✅ |
| 出片提示师 | [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | 2146 | 2000+ 精选 Seedance 提示词库 | ✅ 当素材库 |
| **配音** | [rany2/edge-tts](https://github.com/rany2/edge-tts) | 12305 | 免费微软 Edge TTS（晓晓/云希等中文音色） | ✅ **首装**：免费，40 分兜底版必备 |
| **配音** | [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) | 24014 | 多语种语音大模型，可声音克隆、情感 | ✅ 固定角色音色（需 GPU/云端） |
| **配音** | [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1535 | ElevenLabs 官方 MCP | ✅ 有 API Key 时装，90 分版质感 |
| 剪辑 | [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) | 4580 | Python 生成/导出剪映草稿 | ✅ 首选 |
| 剪辑 | [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) | 16267 | LLM 自动字幕：生成、断句、校正 | ✅ |
| 剪辑 | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 1980 | 给 Agent 的 42 个 FFmpeg 工具 Skill | ✅ |
| 审片 | [Netflix/vmaf](https://github.com/Netflix/vmaf) | 5533 | 感知视频质量评分（技术画质） | ✅ 画质红线 |
| 审片 | [VQAssessment/DOVER](https://github.com/VQAssessment/DOVER) | 531 | UGC 视频美学+技术质量评估 | 可选 |
| 逆向分析 | [morluto/rea](https://github.com/morluto/rea) | 294676 | Reverse Engineer Anything：Skill+MCP，应用到二进制逆向 | ✅ REA 岗主装 |
| 逆向分析 | [aicodeking/leanrea](https://github.com/aicodeking/leanrea) | 20 | 8KB 轻量版 REA Skill（纯 CLI） | 可选 |

## 配音岗推荐设定
- 首装 edge-tts（免费、零门槛，保证日更不断）；需要固定角色音色时上 CosyVoice；拿到 ElevenLabs Key 后加 elevenlabs-mcp。
- 职责：按剧本出旁白+角色台词音轨，交 wav + SRT 时间轴给剪辑；当天交不出 90 分音色就用 edge-tts 出 40 分版，不挡发布。

## 我们自己的 7 个 Skill
`skills/` 下 7 个 SKILL.md 均为本仓新发布，目前 **0 star**。
