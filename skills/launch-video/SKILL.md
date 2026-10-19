---
name: launch-video
description: Make a short Termio feature launch video (15–20 s, 4K 60 fps) with HyperFrames — capture the app through the Codex desktop app's Computer Use, rebuild interactive UI in HTML from the Swift source, direct camera and pointer by attention, render, and archive to termio-sh/launch-video. Use when the user asks for a launch/feature/demo video or animation of a Termio UI change, or to revise one. Load together with general-video and hyperframes; this skill holds the lessons those generic skills do not.
---

# Termio launch video

Two films were made with this process: `20261018-ui-2` (session cards, 16 versions)
and `20261019-horizontal-tabs` (11 versions). Almost every version after the first
fixed something a rule below now forbids. Read the rules before the first draft,
not after the first complaint.

Source of truth for working code: the two folders in
https://github.com/termio-sh/launch-video, cloned at `~/Documents/GitHub/launch-video`.
Start a new film by copying the closest folder, not from a blank composition. Build
in that clone, not in the scratchpad: the scratchpad is wiped.

- `references/craft.md` — technique catalogue with the exact parameters that shipped
- `references/capture.md` — capture pipeline and the Codex brief template
- `references/corrections.md` — every user correction, its root cause, and its rule
- `scripts/camera.js` — camera, pointer, easing, motion-blur core
- `scripts/patch_pointer.py` — erase a baked pointer with a diff gate

## The limit you must state

You cannot watch motion. Stills prove layout, never motion. Every motion defect
in both films (flicker, pacing, gaze, bobbing, jumpy speed) was found by the user.
Say so in every review hand-off. Before asking the user to watch, run the motion
checks in `references/craft.md` § Motion checks: peak px/frame, rest time after
each action, and a 12 fps contact sheet around every interaction.

## Story rules

1. **Open on the product.** No intro slide. The first second shows the app.
   "Introducing <Feature>" goes on the end card, with termio.sh and the GitHub URL.
2. **One story, not a feature checklist.** Motivate actions with Termio's own
   agent status: an agent finishes, its dot pulls the eye, the pointer acts on it.
3. **Every action has a visible cause.** Clicks and drags need a pointer. A film
   without a pointer only works when the UI changes by itself (OpenCode's tabs film).
   Ask why a reference works before copying it.
4. **Land on density.** The one full-window frame is where viewers stop. End it on an
   agent conversation, never an empty pane or a file list.
5. **Behaviour comes from source.** Read the Swift before animating a state change:
   selection after a move, status dots, indicator timing, strings, menu items. Do not
   animate from memory (the dropped tab does NOT become selected: `moveTab`).
6. **Content swaps in place.** One stage; panels change inside it, as the app does.

## Attention rules

The five beats for every interaction:

| beat | what moves | time |
|---|---|---|
| Arrive | camera glides, then settles | 0.6–1.1 s + 0.2–0.3 s settle |
| Ready | hover state appears | 0.3 s |
| Act | click or drag; camera still | instant / ≤ 1 s |
| Result | focus opens on what changed; camera still | 0.5 s |
| Rest | nothing | ≥ 0.8 s (≥ 1 s after a drop) |

- Never click while the camera moves. Never move the camera during a click or drag.
- The pointer leads; the camera follows a beat behind.
- The camera travels one way (or zooms in place). No vertical dip to show a result —
  open the focus band instead.
- Choose the subject first, then frame it. Centre the subject, not the geometry
  ("fit three tabs" centred git log between the two agents).
- Hold the payoff ≥ 1.2 s. The end card is shorter than the payoff.

## Motion rules

- Camera ease `cubic-bezier(0.4,0,0.1,1)`, pointer `(0.3,0,0.15,1)`. No chains of
  short `power3.inOut` tweens: velocity spikes between them.
- Pan speed ≤ about half a screen width per second. Over ~30 px/frame needs
  horizontal motion blur in proportion to speed.
- Zoom in log space.
- Depth of field is a tilt-shift band that rotates with the window, three layers
  (0 / 2.5 / 5.5 px), blur inside the clipped window content, one shadow.
- Glow breathes slowly (4.5 s) and visibly (opacity 0.4→1). Never flicker.
- Backgrounds move: aurora layers on yoyo loops, 4.9–7.3 s periods, 250–450 px.

## Look rules

- Frame 0 is sharp: platforms use it as the cover. Start blur ≤ 6 px.
- No text inside a 3D (`preserve-3d`) subtree: Chrome rasterises it blurry. Labels
  go in a flat 2D overlay.
- One type family per card. SF Pro Display 600, −0.02em titles; sentence-case kicker
  in #86868b. URLs are in SF Pro, not mono.
- One glass pill style for every chip and caption.
- Margins: ≥ 90 px top, ≥ 130 px right at 1920×1080. Tilt ≤ 32°/14°.
- Window corners: real alpha at the real radius (33 px at 2×); replace the 2-row
  light rim with the window background colour. Same radius on shadow and overlays.
- Small captions (34–42 px). The product is the subject, not the copy.
- Hide the sidebar unless the feature is the sidebar.

## Process

1. **Echo the request as imperatives** before building, one per noun. Two films lost a
   version each to a misread ("keep the intro, merge it into one slide").
2. **Read the source** for the feature: views, store methods, strings
   (`Sources/termio/Resources/Localizable.xcstrings`).
3. **Find the reference film** if the user names one; download and analyse its beats.
4. **Capture** via `references/capture.md`. Plan an HTML rebuild for anything that
   needs hover, drag, or a menu: Computer Use cannot capture those.
5. **Build** from the closest launch-video folder. Write `STORYBOARD.md` with the
   gaze path per beat before keyframes.
6. **Check:** `npx hyperframes lint`; snapshots at every beat with
   `--zoom "x,y,w,h" --zoom-scale 2`; the motion checks; first and last frame of the
   final MP4.
7. **Render:** `npx hyperframes render --resolution 4k --fps 60 --quality delivery
   -o <slug>-vN-4k.mp4`. Version every file name. Tell the user to close the old
   player window: QuickTime keeps playing an overwritten file.
8. **1080p copy** under 10 MB for browser upload:
   `ffmpeg -i in.mp4 -vf scale=1920:1080 -c:v libx264 -crf 20 -maxrate 5M -bufsize 10M
   -c:a aac -b:a 128k -movflags +faststart out.mp4`.
9. **Cover** for Xiaohongshu: see `social-publish`. Rebuild it whenever the video changes.
10. **Archive** (only when asked to save/commit): `termio-sh/launch-video/YYYYMMDD-slug/`
    with `index.html`, `hyperframes.json`, `package.json`, `assets/`, `cover/` (source),
    `renders/` (4K, 1080p, cover or thumbnail), and a README (story, source mapping,
    renders table, "Not included", render command). Add a row to the root README table.
    Leave out SF Pro fonts and Pixabay SFX (licences); say how to restore them.
    Commit `feat: add the Termio <feature> video (YYYY-MM-DD)`, no Co-Authored-By.
    The scratchpad is wiped; anything not in the repo is lost.
