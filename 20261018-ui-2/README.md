# Termio UI 2.0 — launch video (2026-10-18)

A 20-second launch video for Termio UI 2.0: each agent session is a card.
Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/termio-ui-2-4k.mp4` | 3840×2160, 60 fps | Master |
| `renders/termio-ui-2-1080p.mp4` | 1920×1080, 60 fps, under 10 MB | Social uploads |
| `renders/thumbnail.jpg` | 1920×1080 | Video thumbnail |

## Source

- `index.html` is the whole composition: the title slide, the tiled-cards scene, the panel walkthrough and the end card.
- `assets/cap/` holds real captures of the running app (2802×1714). The Computer Use pointer was removed from them, and the window corners were made transparent.
- `assets/bgm/track.wav` is the music bed, generated locally with MusicGen.

## Not included

These files are referenced by `index.html` but are not in the repo, because their licenses do not allow redistribution:

- `assets/fonts/` — SF Pro Display (Bold, Semibold, Medium, Regular) and `SFNSMono.ttf`. Copy them from a Mac: `/Library/Fonts` after installing SF Pro from developer.apple.com/fonts, and `/System/Library/Fonts/SFNSMono.ttf`.
- `assets/sfx/` — `click.mp3`, `click-soft.mp3`, `impact-bass-1.mp3`, `whoosh.mp3`, `whoosh-short.mp3`, from Pixabay's free sound library. Any short click, whoosh and bass hit with those names will work.

## Render

```sh
npx hyperframes@0.8.169 render . -o termio-ui-2-4k.mp4 --fps 60 --quality delivery --resolution 4k
```
