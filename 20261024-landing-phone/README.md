# Termio landing — Your sessions, on your phone (2026-10-24)

A 7-second silent loop for the third feature panel on termio.sh. The camera glides in to
the iPhone. A tap on the `home` project pushes Claude Code's live terminal in from the
right; a tap on the prompt raises the keyboard and the key bar. The camera pulls back and
the phone returns to the project list.

Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/landing-phone-v1-1080p.mp4` | 1920×1080, 60 fps | Master |
| `renders/landing-phone-v1-720p-web.mp4` | 1280×720, no audio | termio.sh |

## Source

- `index.html` is the whole composition.
- `assets/cap/` holds three real captures of the iOS app (662×1440): the project list, the
  Claude Code mirror, and the same session with the keyboard up.
- The push is the UINavigationController slide; the keyboard rises by sliding the lower
  half of the keys capture over the mirror. Touches are drawn as iOS screen recordings show
  them.
- In the app, tapping a project opens its session list first. The film skips that step to
  stay at 7 seconds.

## Not included

None. The film draws no text.

## Render

```sh
npx hyperframes@0.8.169 render . -o renders/landing-phone-v1-1080p.mp4 --fps 60 --quality delivery
ffmpeg -i renders/landing-phone-v1-1080p.mp4 -an -vf scale=1280:720 -c:v libx264 -preset slow \
  -crf 23 -pix_fmt yuv420p -movflags +faststart renders/landing-phone-v1-720p-web.mp4
```

The 720p copy is the one termio.sh serves, as `web/landing/public/videos/phone.mp4`.
Its poster is a frame of it at 5.0 s.
