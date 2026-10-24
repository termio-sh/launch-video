# Termio landing — See which agent needs you (2026-10-24)

A 7-second silent loop for the first feature panel on termio.sh. The camera glides from
the whole window into the sidebar. One agent stops and its dot turns orange because it
needs you; three more finish and turn green. The camera pulls back and the dots clear, so
the last frame meets the first.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/landing-status-v1-1080p.mp4` | 1920×1080, 60 fps | Master |
| `renders/landing-status-v1-720p-web.mp4` | 1280×720, no audio | termio.sh |

## Source

- `index.html` is the whole composition.
- Derived from `20261020-agent-tower`: the same capture, lens and camera, with the captions,
  end card, roll call and audio removed, and the frame moved onto the sidebar so the dots
  stay legible at the panel's 650 px width.
- `assets/cap/window.png` is a real capture of the app (2218×1634). The status overlays
  follow `SidebarView.swift`: the spinner replaces the mark while working, and `StatusDot`
  is 7 pt with a 1.5 pt ring in the window colour.

## Not included

- `assets/fonts/` — SF Pro Display. The film draws no text, so it renders without them.

## Render

```sh
npx hyperframes@0.8.169 render . -o renders/landing-status-v1-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/landing-status-v1-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/landing-status-v1-720p-web.mp4
```

The 720p copy is the one termio.sh serves, as `web/landing/public/videos/session-status.mp4`.
Its poster is a frame of it at 5.4 s.
