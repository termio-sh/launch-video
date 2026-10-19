# User corrections, 2026-10-17 to 10-19

Each row: what the user said, the root cause, the rule. The rules are folded into
SKILL.md; this file keeps the evidence so a rule can be re-argued from facts.

## UI 2.0 / session cards (16 versions)

| user | root cause | rule |
|---|---|---|
| "一点创意都没有…跟做 PPT 似的，特别老土…文案也没有那么打动人心" | stock template: icon → cards → push-in → logo; no concept | study current launch films first; one concept sentence; one focal point per shot |
| "从第七秒之后的反而是比较合适的…前几秒的没有什么用处…可以更大一点，文字再变小一点…没有抓住为什么这种用法比较好" | 6.9 s of copy before product; 120–180 px captions | product in second one; small captions; say *why* with the PR's own claims |
| "6.3 到 9.5 有点太少了…先显示 plan 文档…Codex…GitHub list…另外一个 Agent…起个名字" | too few use cases | one beat per use case; name the feature; label placeholders honestly, never fake content |
| "后面展示那些 Git 之类的东西，应该直接在上面原地替换" | cover-flow broke spatial continuity | one stage, swap in place |
| "要像苹果的这种入场动画" | — | masked whole words rising, light blur, expo.out, no bounce |
| "首帧为什么感觉不太清晰？感觉会有光晕…字体选择和排版是比较合适的吗" | frame 0 mid-tween at 14 px blur; radial glow; banding; 700 weight, mono caps kicker | frame 0 sharp; blur ≤ 6 px; `--quality delivery`; 600 −0.02em; sentence-case grey kicker |
| "为什么截图的时候不顺便处理一下？感觉很多图片都是重复的…" | near-duplicate captures with baked cursors | capture distinct, purpose-built states; clean at source |
| "花了接近 5 秒的时间介绍一个概念，用户可能就跑了，你的 Hook 不够啊" | 2 intro slides | one intro slide ≤ 2.2 s (later: none) |
| "感觉你误会我的意思了…还是要保留入场动画，只是入场动画要合并成一个整体" | acted on an ambiguous request without restating it | echo multi-noun requests as imperatives first |
| End card: "GitHub 地址的字体要和其他字体保持一致…字间距…padding" | mono URL looked like another system | one family per card; URL 30 px SF Pro 0.02em; gaps 44/20 px |
| "倾斜的角度是不是有点大？…字体注释的风格好像有点不太一致…玻璃质感边框" | tilt 46°/22°; mixed label styles | tilt ≤ 32°/14°; one glass pill style |
| "为什么这里感觉配置 label 和其他地方不一样呢？感觉有点失真、有点模糊" | text inside `preserve-3d` rasterised at pre-zoom size | no text in 3D; flat overlay labels |
| "你的这个背景应该都是动的呀…它不应该是个静态图片的" | 140 px drift over 20 s is invisible | yoyo loops, 250–450 px, 4.9–7.3 s |
| "上边距和右边距应该稍大一点，特别是上边距" | 32 px top, 87 px right | ≥ 90 top, ≥ 130 right |
| "图片的上边缘有点白光…radius…不太一致，会露出一点白边" | white desktop behind capture; 28 vs 33 px radius; light rim rows | real alpha at real radius; replace rim rows |

## Horizontal tabs (11 versions)

| user | root cause | rule |
|---|---|---|
| "你可以没有开场页，直接是动画，最后再介绍" | intro slide habit | open on product; title on end card |
| "你截图的时候应该把侧边栏关掉" | captured what was on screen | frame only the feature |
| "前景里那个边缘散景有点晃眼睛，而不是那种优雅、丝滑" | screen-fixed ellipse mask; text crossed it while panning; 2 layers | tilt-shift band rotating with window; 3 layers |
| "为什么第一秒和第二秒还是有点闪？就是你的图片和那个背景之间的边缘" | blur on whole window copies; 3 stacked shadows | blur inside clipped content; one shadow |
| "不需要有抖动的光，但是需要有点光。你可以更慢一点，呼吸光更强一点" | — | 4.5 s breath, opacity 0.4→1 |
| "用那个 file 结尾的话…信息密度有点少。起码你是需要有个对话的" | ended on the last tab in order | land on a conversation |
| "file 挪动之后，再点 …这个时间节奏不太对，有点太快了" | drag before settle; hover 0.23 s after drop; payoff 0.4 s | settle 0.3 s before acting; rest 1 s after drop; payoff ≥ 1.2 s |
| "用户的注意力刚一聚焦，镜头就移开了…正确的动画设计应该是什么样的？" | keyframes on a 1.1 s clock grid | five beats; camera moves only in Arrive/Rest |
| "为什么要上下晃呢？…移动的时候不要点击，点击的时候不要移动" | RESULT beat dipped the camera | one direction; reveal by focus band |
| "移动速度的算法是有问题的，感觉会跳一下，一跳一跳的" | chained 0.7 s power3.inOut; > 2000 px/s; linear scale | GLIDE curve; ≤ half screen/s; motion blur; log zoom |
| "整个交互逻辑…还是不够自然。你觉得最大的问题是什么？" | copied OpenCode's pointer-free style; checklist not story | visible cause for every action; agent-status story |
| "居中位置是不太对的。用户注意力会放到给 log，但是实际上你是想展示 explain split" | framed by geometry | subject first, then frame; reorder content |
| (found in source, v6) dropped tab became selected | animated from memory | behaviour from source (`moveTab` keeps selection) |

## Process failures

- Motion was only ever judged from stills; the user found every motion defect.
- A stale CSS block later in the file overrode new rules; the last frame was never
  checked. QuickTime replayed an overwritten file, so the user saw an old render.
- An over-wide pixel patch erased real text. Patch from the original, tight box, diff gate.
- Requirements arrived one at a time; most were already implied by the first film.
