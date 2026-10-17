# 寓言短片工作室 · 各岗高星 Skill / 工具调研

数据来源：GitHub search_repositories / get_repository / get_file_contents，2026-10-17（UTC+8）。  
**同日晚**：按用户要求「全部 Skill 大改」，已把可复用做法写入 `skills/*/SKILL.md` 与 sand-data workflows；本表为索引。

| 岗位 | 仓库 | Star（约） | 吸收进 Skill 的做法 | Skill id |
|---|---|---|---|---|
| 编剧 | [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | 7680 | 冲突颗粒、可转述落点、结构自检 | skill-1792066607676 |
| 编剧 | [liangdabiao/Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | 2613 | 一句话→可拍剧本、时长锚定 | 同上 |
| 三锁 | [FireRedTeam/StoryMaker](https://github.com/FireRedTeam/StoryMaker) | 720 | 角色参考锚定 | skill-1792066610615 |
| 三锁 | [Murray-Wang/CharaConsist](https://github.com/Murray-Wang/CharaConsist) | 166 | 发型/服装/五官/体型/风格分维 | 同上 |
| 三锁/审片 | [lybx-leyw/shortdrama-workplace](https://github.com/lybx-leyw/shortdrama-workplace) | 0（方法完整） | vision.json：AI伪影/乱码/一致性/穿帮；时长画幅实测 | 三锁+审片+HKRR+出片执行 |
| 导演 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | 6747 | 短剧分镜可执行字段 | skill-1792066613192 |
| 导演 | [henjicc/Storyboard-Copilot](https://github.com/henjicc/Storyboard-Copilot) | 713 | 镜头衔接状态 | 同上 |
| 出片提示 | [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) | 4324 | @引用、时间戳分段、运镜词、短剧模板 | skill-1792066616481 |
| 出片提示 | [songguoxs/seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill) | 2931 | 中文提示、禁止项、>15s 衔接点 | 同上 |
| 出片提示 | [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | 2146 | 提示素材库（参考不整抄） | 同上 |
| 出片执行 | 同上 dexhunter/songguoxs + StoryMaker | — | 授权出片、镜级自检、必保优先 | skill-chupian-zhixing（新建） |
| 剪辑 | [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) | 4580 | 程序化剪映草稿 | skill-1792066778141 |
| 剪辑 | [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) | 16267 | 字幕断句校正 | 同上 |
| 剪辑 | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 1980 | 抽帧/混音/导出 | 同上 |
| **审片** | [Netflix/vmaf](https://github.com/Netflix/vmaf) | 5533 | 感知画质参考 | skill-1792066788314 |
| **审片** | [VQAssessment/DOVER](https://github.com/VQAssessment/DOVER) | 531 | UGC 美学+技术双通道 | 同上 |
| **审片** | shortdrama-workplace vision.json | — | **抽帧红线：乱码/伪影/劝退；禁止硬字幕万能放行** | 同上 |
| 配音 | [rany2/edge-tts](https://github.com/rany2/edge-tts) | 12305 | 免费中文 TTS 兜底 | skill-1792077049837 |
| 配音 | CosyVoice 生态 | 高 | 固定角色音色 | 同上 |
| 配音 | [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1535 | 有 Key 时高质感 | 同上 |
| 选题 | oh-story + 公开页拆解法 | — | 10 字段卡、60–90s 可拍过滤 | skill-1792235005393 |
| HKRR | 影视飓风公开 HKRR + vision 硬门槛衔接 | — | 禁止「可发·弱项」掩盖劝退画面 | hkrr |
| 发布 | 各平台公开规范 + 封面安全区惯例 | — | 标题/封面/AI 标识 | skill-1792235658500 |

## 关键条款变更（相对自制空壳 v1）
1. 默认时长 **30–60 → 60–90 秒**。
2. 审片：**视觉抽帧强制**；机内乱码/畸变/错脸 = 红线；不得因硬字幕能懂标 40。
3. 提示/出片：**禁止指望模型生成可读汉字 UI**；后期真叠层。
4. HKRR：成片先过视觉硬门槛再谈可发话术。
5. 新建 **出片执行** Skill。

## 仍缺 / 需装工具（未擅自安装、未烧 Seedance）
- [ ] `ffmpeg`/`ffprobe`（抽帧与实测时长；多数环境已有）
- [ ] Netflix VMAF 二进制或 Docker（可选，手检可暂代）
- [ ] DOVER 环境（可选 GPU）
- [ ] edge-tts（配音岗首装推荐）
- [ ] pyJianYingDraft（剪辑程序化草稿，可选）
- [ ] 将 `skill-chupian-zhixing` 用 UpdateSkill **write 无 id** 注册为全局 Skill（本执行环境无 cursor UpdateSkill MCP）

## 副本位置
- 仓内：`/workspace/fable-short-studio/skills/<id>/SKILL.md`
- 运行时：`/home/box/sand-data/workflows/<id>/SKILL.md` 与 `agent-data/workflows/` 已同步写入

- 出片执行正式 id：`skill-1792243815568`（原临时 skill-chupian-zhixing）

