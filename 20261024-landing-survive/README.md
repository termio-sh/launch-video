# Termio landing — Sessions survive quit (2026-10-24)

A 7.5-second silent loop for termio.sh. The camera glides into an agent reading ky's tests.
⌘Q quits Termio and the window goes. The app reopens on the same window and session, and
the agent is further down the file list: it kept working while Termio was closed.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/landing-survive-v1-1080p.mp4` | 1920×1080, 60 fps | Master |
| `renders/landing-survive-v1-720p-web.mp4` | 1280×720, no audio | termio.sh |

## Source

- `index.html` is the whole composition. Lens, camera and backdrop come from
  `20261024-landing-status-v2`.
- `assets/cap/before-raw.png` and `after-raw.png` are real captures taken by the Codex CLI's
  Computer Use, 1 min 36 s apart, either side of a real ⌘Q and reopen
  (`20261024-landing-v2/BRIEF-codex-v5.md`). The agent went from `test/bytes.ts` at 1m 13s
  to `test/helpers/create-large-file.ts` at 2m 48s.
- `prep.py` erases the Computer Use pointer, the stray `quote>` prompt and the capture
  folder's own project row, and writes `before.png` and `after.png`.

## Not included

- `assets/fonts/` — SF Pro Display, for the ⌘Q chip. Copy it from a sibling film to render
  with the same face.

## Render

```sh
python3 prep.py
npx hyperframes@0.8.169 render . -o renders/landing-survive-v1-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/landing-survive-v1-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/landing-survive-v1-720p-web.mp4
```
