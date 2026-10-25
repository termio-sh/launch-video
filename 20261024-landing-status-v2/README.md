# Termio landing — See which agent needs you, v2 (2026-10-24)

A 7-second silent loop for the first feature panel on termio.sh, rebuilt on a fresh
capture of a clean demo project (ky). The camera glides from the whole window into the
sidebar. One agent stops and its dot turns orange because it needs you; two more finish
and turn green while the selected agent keeps reading. The camera pulls back and the dots clear, so
the last frame meets the first.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/landing-status-v2-1080p.mp4` | 1920×1080, 60 fps | Master |
| `renders/landing-status-v2-720p-web.mp4` | 1280×720, no audio | termio.sh |

## Source

- `index.html` is the whole composition.
- Derived from `20261024-landing-status`: the same lens, camera and status overlays, moved
  onto the new capture.
- `assets/cap/window.png` is cleaned from `assets/cap/capture-raw.png`, taken
  by the Codex CLI's Computer Use. `prep.py` erases the Computer Use pointer, the stray
  `quote>` prompt and the capture folder's own project row, and cuts the blank tiles and the
  dot patch from the capture itself.

## Not included

- `assets/fonts/` — SF Pro Display. The film draws no text, so it renders without them.

## Render

```sh
npx hyperframes@0.8.169 render . -o renders/landing-status-v2-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/landing-status-v2-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/landing-status-v2-720p-web.mp4
```

The 720p copy is the one termio.sh serves, as `web/landing/public/videos/session-status.mp4`.
Its poster is a frame of it at 5.4 s.
