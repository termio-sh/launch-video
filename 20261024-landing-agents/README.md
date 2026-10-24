# Termio landing — Every agent, one switch (2026-10-24)

A 7-second silent loop for the second feature panel on termio.sh. The camera glides into
Settings ▸ Agents, and the switches for OpenCode, Amp, Droid, Copilot, Kimi and Qwen Code
turn on one by one. The camera pulls back and the switches reset for the next loop.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/landing-agents-v1-1080p.mp4` | 1920×1080, 60 fps | Master |
| `renders/landing-agents-v1-720p-web.mp4` | 1280×720, no audio | termio.sh |

## Source

- `index.html` is the whole composition.
- `assets/cap/agents.png` is the docs capture `17-agents-settings.png` (1964×1614) with the
  Computer Use pointer painted out.
- The switches are drawn in HTML over the captured ones, measured off the capture: a 72×32
  track and a 40×24 capsule knob, 4 px inset, off grey `rgb(65,68,73)`, on blue
  `rgb(56,123,242)`.

## Not included

None. The film draws no text.

## Render

```sh
npx hyperframes@0.8.169 render . -o renders/landing-agents-v1-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/landing-agents-v1-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/landing-agents-v1-720p-web.mp4
```

The 720p copy is the one termio.sh serves, as `web/landing/public/videos/agents.mp4`.
Its poster is a frame of it at 4.8 s.
