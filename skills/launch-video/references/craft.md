# Craft catalogue: parameters that shipped

Working code: `termio-sh/launch-video/20261019-horizontal-tabs/index.html` (camera,
DoF, pointer, tab strip) and `20261018-ui-2/index.html` (3D exploded view, intro
title, labels, panels). `scripts/camera.js` is the extracted core.

## Composition contract (HyperFrames 0.8.169)

- One paused GSAP timeline registered as `window.__timelines["main"]`.
- Per-frame state (camera, pointer, indicators) is computed in
  `tl.eventCallback("onUpdate", render)`, from `tl.time()`. Deterministic under seek.
- Every tween is `fromTo(..., { immediateRender: false })` from a mirrored `state`
  object, so a tween never reads a value an earlier tween has not reached yet.
- Root ends with `tl.to({}, { duration: FILM }, 0)`.

## Camera

- State `{px, py, ls, r, sx, sy, far, mid}`: focus point in world px, log scale,
  rotation, screen focus spot, blur depths. `PAD = 600` around the stage so the
  rotated world never shows an edge.
- `ox = sx − s·(cos·px − sin·py)`, `oy = sy − s·(sin·px + cos·py)`;
  `.cam { x:ox, y:oy, rotation:r, scale:s }`.
- `.tilt` / `.untilt` rotate ±r about the focus spot: the focus band turns with the window.
- Durations: 1.1 s per tab hop, 1.6 s to reach the strip, 1.8 s to pull out to the window.
- Motion blur: `streak = 0.28 × panSpeed / 60 / s` px, horizontal only, applied when
  > 0.05. panSpeed sums `|dx|·slope(ease,p)/duration` over active pans.

## Depth of field

- Three lenses (far, mid, sharp), each a full window copy.
- Mid mask: linear-gradient band ±1.1…2.6×`--h1` around the strip; sharp ±1.0…1.6×`--h1`.
- Blur `depth/s` px on `.content`, clipped by `.win { border-radius:30px; overflow:hidden }`.
  Blurring the whole window copy haloes onto the backdrop and flickers.
- Shadow only on the far lens.
- Revealing a result = tween `--h1` (70→190 px), never move the camera.
- Opening: one whole-scene blur 10→0 over 0.8 s.

## Pointer

- Flat SVG arrow above the lenses (crisp at any zoom), `scale s·0.5`, `rotation r`.
- Click: scale 0.86 in 0.06 s, back in 0.16 s.
- Drag: press, then the tab moves `x` over 0.9 s; neighbours step aside on 0.2 s
  (the app's reorder curve); dividers return at drop.
- After the last action the pointer drifts off and fades (0.4 s).
- UI 2.0 variant: PNG sprite cut from the Computer Use pointer, RGBA (a black box shows
  otherwise), `mix-blend-mode: plus-lighter`; click ripple 32 px ring, 0.2→1 in 0.45 s.

## App indicators (from source)

- WorkingIndicator: 3×3 grid, 1.1 s per turn, centre dot 0.5; ring opacity
  `max(0.5, 1 − d/4)`, scale `1 + 0.2·max(0, 1 − d/2)`; dot 2.5 pt, spacing 3.6 pt.
- StatusDot: 7 pt, rgb(48,209,88) done, orange needs-you; 1.5 pt window-colour ring;
  offset (+3,−3) top-trailing. Pops in with `back.out(2.2)` 0.35 s. Clicking clears it (markSeen).
- Tab strip: 26 pt tabs, min 120 pt, equal share, 6 pt padding, 8 pt icon gap; active
  pill white 9% + hairline + rim; track white 3.5%; SF 13; dividers 1×14 pt at 14%,
  hidden beside the selected tab and during drag.

## Aurora backdrop (landing hero)

Layers navy, teal, band, violet, shade, floor, grain. Grain: SVG `feTurbulence` 0.82,
160 px tiles, opacity 0.16, overlay (stops H.264 banding). Yoyo `sine.inOut`:

| layer | period | movement |
|---|---|---|
| band | 5.3 s | x 260, y 140, rotation 24→10, scaleY 1.35 |
| navy | 6.7 s | x 320, scale 1.12 |
| teal | 4.9 s | x 420, scale 1.25 |
| violet | 7.3 s | x −440, scale 1.2 |
| shade | 6.1 s | x 340, y −220 |

Cost: 4K render went from ~1 min to ~4 min 42 s.

## Breathing glow

`.halo` blur 70 px, opacity 0.4→1, scale 0.98→1.03; `.rim` opacity 0.35→1; both
`BREATH = 4.5 s` sine yoyo.

## Typography and glass

- SF Pro Display .otf via local `@font-face` (not in the public repo).
- Intro (UI 2.0): kicker 30 px 600 #86868b; title 128 px 600 −0.02em; whole words rise
  from a mask `yPercent 125→0`, stagger 0.1, expo.out 1.0 s, blur 6→0; gradient sweep on
  the hero word only. Brand word grey, feature words white.
- End card (tabs): icon 150 px (14.15 s), kicker 30 px (14.3), title 112 px (14.4),
  links (15.2): termio.sh 36 px 600 0.01em, GitHub 30 px 500 0.02em #8e8e94, margin-top
  46 px, gap 20 px. Fade at FILM − 0.6 s.
- Glass pill: `linear-gradient(180deg, rgba(255,255,255,.16), rgba(255,255,255,.05)),
  rgba(24,24,28,.55)`, 1 px border white 22%, inset top highlight .28,
  `backdrop-filter: blur(18px) saturate(160%)`, radius 999 px.
- 3D labels: flat overlay (`#hlabels`) aligned to the 3D boxes.

## Audio

- BGM: local MusicGen, warm synth pad. Volume 0.35 → 0.8 by 0.6 s, hold, 0 over the
  last 1.2 s.
- SFX (Pixabay click, click-soft, whoosh, whoosh-short) on the exact event times, volume
  0.3–0.5: done-dot, click, lift, drop, pull-out, end card.
- You cannot hear. Measure loudness (`ffmpeg -af ebur128`) and say you did not listen.

## Lint traps

| error | fix |
|---|---|
| `className` tween does nothing | `attr: { class: … }` |
| `overlapping_gsap_tweens` on a CSS var | reset it at the start of each move, not mid-move |
| `gsap_css_transform_conflict` | move the initial transform from CSS into `tl.set` |
| `gsap_non_transform_motion` (letterSpacing) | use scale/blur |
| `tl.set` of a missing property throws | everything after it silently never runs; check late snapshots |
| unused captions visible | default `opacity: 0` on caption words |

Ignorable: `nested_structure_needs_subcomposition`, `composition_file_too_large`.

## Motion checks

Run before every hand-off; report the numbers, and still say you did not watch it.

```sh
scripts/motion_check.sh render-1080p.mp4 OUTDIR [from_s to_s]
```

- `jumps.txt`: frames whose change is > 2.5× their 9-frame median. A jump at a click
  or a cut is expected; anywhere else is a defect (velocity spike, pop, flicker).
- `rests.txt`: still spans ≥ 0.3 s. Every click must sit inside one, and a rest
  ≥ 0.8 s must follow each result.
- `sheet.png`: 12 fps contact sheet; read it for direction changes (bobbing) and for
  what is centred.
- Limit: small motion in a wide shot (a tab drag at s ≈ 1.1) stays under the stillness
  threshold, and ambient loops (WorkingIndicator) count as motion.
- Also compute from the timeline: peak pan px/frame (≤ ~16 at 1080p/60 without blur).

## Stills and the cover

- `npx hyperframes snapshot --at 0.3,3.2,… -o snaps` per beat;
  `--zoom "x,y,w,h" --zoom-scale 2` for 4K detail.
- Transparent hero still: render on black and on white, `alpha = 1 − (W − B)/255`.
- Xiaohongshu cover: composition 1440×1080 rendered at 2× → 2880×2160 JPEG q92:
  `npx hyperframes snapshot . --at 0.95 --zoom "0,0,1440,1080" --zoom-scale 2 -o out`
  (without `--zoom`, `--zoom-scale` is ignored and you get 1440×1080).
  Source: `launch-video/20261019-horizontal-tabs/cover/`.
  Background = a 4K frame with the story's key state (v11 at 3.77 s), top rows
  stretched into sky for the title. Brand row (64 px icon + "Termio" 44 px 600) above
  h1 (136 px 600). Nothing else. Top-right stays empty (play icon).
