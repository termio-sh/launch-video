# Capture pipeline

## What is blocked

- This agent's `screencapture`: TCC denies it ("could not create image from display").
- Codex `screencapture -x -R …`: "could not create image from rect".
- osascript: no Accessibility. Computer Use refuses Terminal.app.
- Computer Use has click/drag/scroll but no hover and no held drag. Drags are atomic.
  Context menus did not open reliably.

## What works

Drive the **Codex desktop app** (not the Codex CLI) with Computer Use, through Termio:

1. `termio sessions spawn --agent codex "<brief>"` with the brief below.
2. Background: `termio sessions watch --json --no-snapshot --state done,needs-you`.
3. Codex asks `QUESTION:` lines. Answer with `termio sessions send <link> "<answer>"`.
4. The user must not touch the Mac during the run. Typing in Termio stalls Codex.
   Ask the user to confirm the machine is idle before sending.

## Failures and their fixes

| failure | fix |
|---|---|
| Codex clicked the macOS menu bar to park the pointer; CUA wedged | Never click menus to park. Warp with `CGWarpMouseCursorPosition` only (no click, no events). The user had to press Esc. |
| Codex resized the user's window | Record the original rect first; restore it exactly at the end. |
| Computer Use pointer marker stays in every capture | Patch it: `scripts/patch_pointer.py`, from the ORIGINAL capture, tight box, row-matched fill or a clean neighbouring shot. Then look at a 2× crop. |
| Over-wide auto-detected patch box erased a prompt line | Tight hand-measured box; the script fails if anything outside changes. |
| Patch with a flat dark block cut a separator line | `--from-col`: each row filled from its own background pixel. |
| Menu-highlight shot needs a hover | Down-arrow key gives the real highlight without a pointer. |
| Hover, drag-in-progress, context menu not capturable | Rebuild that UI in HTML from the Swift source metrics. Use the captures only as content behind it. |
| CUA returned JPEG bytes | Convert to PNG; check dimensions match the rect × scale. |

## Rebuilding UI from source

The horizontal-tabs strip was rebuilt from `Sources/termio/Terminal/SessionTabStrip.swift`,
`Shared/Sources/TermioShared/SessionStatus.swift` (WorkingIndicator),
`Sources/termio/Sidebar/SidebarView.swift` (StatusDot), and `TermioStore` (markSeen,
moveTab). Brand SVGs came from the BrandLogo paths in `Sources/termio/App/Models.swift`.
Measure the rebuilt UI against a capture at 2× before animating it.

## Brief template for the Codex desktop app

```
Use Computer Use to capture screenshots of the running Termio app for a 4K product
video about <feature>. Save every PNG into: <absolute captures dir>

Rules:
- Use the Termio app that is already running. Do not build or launch a second app.
- Before anything else, record the window's current rect in points. Restore it at the end.
- Set the window to <rect> points and do not move or resize it between shots.
- Hide the sidebar unless a shot needs it.
- Park the pointer outside the window with a cursor warp only. Never click the menu bar
  or a menu to park it.
- Dark appearance, Atom One Dark theme.
- Real content only. No secrets, tokens, emails, or private paths beyond the repo.
- Do not commit, push, or edit repo files.
- Note any setting you change (e.g. Settings ▸ Appearance) and set it back at the end.
- If a shot needs hover, a held drag, or a context menu and you cannot do it, skip it
  and say so. Do not fake it.

Setup: <sessions, order, what each shows — each must look clearly different;
agents mid-conversation, not empty>

Shots (file: content):
1. 01-<name>.png: …

Finally write captures/manifest.md: one line per file, what it shows, the window rect
in points, the scale factor, and pixel rects of the elements the video will point at.
Reply with the file list and any shot you could not make and why.
```
