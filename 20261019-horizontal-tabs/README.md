# Termio Horizontal Tabs — launch video (2026-10-19)

A 17-second video for Termio's horizontal tabs. Claude Code and Codex work side by side; Codex finishes, its tab lights up, the pointer opens it and drags it to the front.
Built with [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.169.

## Renders

| File | Size | Use |
|---|---|---|
| `renders/termio-horizontal-tabs-4k.mp4` | 3840×2160, 60 fps | Master |
| `renders/termio-horizontal-tabs-1080p.mp4` | 1920×1080, 60 fps, under 10 MB | Social uploads |
| `renders/cover.jpg` | 2880×2160 | Xiaohongshu cover |

## Source

- `index.html` is the whole composition.
- The tab strip is rebuilt in HTML from `Sources/termio/Terminal/SessionTabStrip.swift`, so it stays sharp in 4K and can move: the selected pill, dividers, hover fill, the 0.2 s reorder curve, and the rule that dropping a tab keeps the selection.
- The working comet and the done dot follow `WorkingIndicator` and `StatusDot`. Opening a finished session clears its dot, as `TermioStore.markSeen` does.
- `assets/cap/` holds real captures of the running app (1654×1122) for the content under the strip. The Computer Use pointer was removed from them.
- `assets/img/` holds the Claude and Codex marks from Termio's source, a terminal glyph, and toolbar icons cropped from the captures.
- `assets/bgm/track.wav` is the music bed, generated locally with MusicGen.

## Not included

These files are referenced by `index.html` but are not in the repo, because their licenses do not allow redistribution:

- `assets/fonts/` — SF Pro Display (Semibold, Medium, Regular). Install SF Pro from developer.apple.com/fonts and copy them from `/Library/Fonts`.
- `assets/sfx/` — `click.mp3`, `click-soft.mp3`, `whoosh.mp3`, `whoosh-short.mp3`, from Pixabay's free sound library. Any short click and whoosh with those names will work.

## Render

```sh
npx hyperframes@0.8.169 render . -o termio-horizontal-tabs-4k.mp4 --fps 60 --quality delivery --resolution 4k
```
