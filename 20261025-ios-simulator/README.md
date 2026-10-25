# Termio — the Simulator pane (2026-10-25)

A 13.8-second launch film for the Simulator pane, shipped in v0.63.0, and a 12.75-second
silent loop cut from it for termio.sh.

Claude Code launches TermioMobile on iPhone 17 with `termio sim launch`, then taps
"Connect a Mac" and "Enter Address Manually" with `termio sim tap --label`. The camera
pushes in, and the person clicks the address field and types `ws://studio.local:8787` on
the Mac keyboard. The camera pulls back out, and the agent runs `termio sim screenshot` and
reports what the field shows. The camera stays level, and every move is timed by its
distance, with a peak under about 28 px a frame.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/ios-simulator-v3-4k.mp4` | 3840×2160, 60 fps, 13.8 s, music | Launch film, with the end card |
| `renders/ios-simulator-v3-1080p.mp4` | 1920×1080, under 10 MB | Upload copy |
| `site/renders/ios-simulator-site-v1-1080p.mp4` | 1920×1080, 60 fps, 12.75 s | Site loop master |
| `site/renders/ios-simulator-site-v1-720p-web.mp4` | 1280×720, no audio | termio.sh (`ios-simulator.mp4`) |
| `site/renders/ios-simulator-site-v1-poster.jpg` | 1280×720 | termio.sh poster, the frame at 10.6 s |

## Source

- `index.html` is the launch film. `site/index.html` is the same composition without the
  end card and audio. It returns to the wide shot and the first state, so it loops.
  `site/assets` is a symlink to `../assets`.
- The window, terminal and sidebar row are real captures taken by the Codex CLI's Computer
  Use from the release app (`BRIEF-codex-v2.md`, `BRIEF-codex-v3.md`; v1 captured nothing):
  - `captures-v2`: the clean window and the launch turn.
  - `captures-v3`: the tap and screenshot turns.
- In v2 the first `tap --label` after `launch` timed out (termio-sh/termio#773).
- In v3 another process typed into the demo session before the run, so its first two
  frames are not used.
- The device screen is `assets/phone/`: real `xcrun simctl io screenshot` captures of
  iPhone 17, driven by `termio sim` through the same flow.
  - The status bar was set to 9:41 for the captures.
  - There is one frame per typed key, `t01`–`t22`.
- `prep.py` builds every layer:
  - It erases the Computer Use pointer from the sidebar.
  - It stacks real terminal lines from v2 and v3 on their shared 34 px line grid into one
    state per turn (`term-A*.png`). The tap prompt comes from v2 and the tap output from v3.
  - It cuts the idle and done sidebar rows and a blank tile for the spinner.
  - It scales each screenshot into the pane's screen rect (2006, 197, 746×1622). That rect
    was found by matching a screenshot against the capture.
- Rebuilt in HTML: the arrow pointer, the WorkingIndicator, the sheet slide, and the alert
  fade.
- `STORYBOARD.md` is the plan written before capture. The film differs from it:
  - It ends on the agent's reply beside the phone, not on the sidebar dot.
  - The soft keyboard is not shown, because the real device hides it once the Mac
    keyboard types.

## Not included

- `assets/fonts/` — SF Pro Display, for the end card. Copy it from a sibling film.
- `assets/sfx/` — Pixabay sound effects. Copy them from `20261020-vertical-tabs`.
- `codex-v*.log` and `snaps/`.

## Render

```sh
python3 prep.py
npx hyperframes@0.8.169 render . --resolution 4k --fps 60 --quality delivery -o renders/ios-simulator-v3-4k.mp4
ffmpeg -i renders/ios-simulator-v3-4k.mp4 -vf scale=1920:1080 -c:v libx264 -crf 20 -maxrate 5M \
  -bufsize 10M -c:a aac -b:a 128k -movflags +faststart renders/ios-simulator-v3-1080p.mp4
cd site
npx hyperframes@0.8.169 render . -o renders/ios-simulator-site-v1-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/ios-simulator-site-v1-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/ios-simulator-site-v1-720p-web.mp4
```
