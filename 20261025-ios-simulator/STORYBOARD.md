---
domd-id: 11a98a17-d513-4413-b800-48e6db451583
---

# Termio — Simulator pane (storyboard, not yet captured)

Waits on PR #758 (termio-sh/termio, `feat/ios-simulator`) merging and shipping in a release.
Capture from `/Applications/termio.app` only. Rename this folder to `YYYYMMDD-ios-simulator`
on the day it is captured.

Behaviour comes from c18f6b11: `Sources/termio/Simulator/SimulatorPane.swift`,
`TermioStore+Simulator.swift`, and `termio sim` in `termiod/src/bin/termio.rs`. Re-read them
on the merged commit before animating: the pane is still changing on `feat/ios-simulator-panel`.

## Story (about 17 s, 4K 60 fps)

One agent builds an iOS app and checks it on the simulator while the person watches the
same device. The cause of every change on the phone is a visible `termio sim` line in the
agent's pane, or the person's finger pointer.

| # | time | what happens | gaze |
|---|---|---|---|
| 1 | 0–2 s | Wide: Claude Code on the left, the Simulator pane on the right with an iPhone in its bezel on the home screen. No intro slide. | whole window |
| 2 | 2–5 s | The agent runs `termio sim launch …/TermioMobile.app`. The app opens in the pane. | terminal line → pane |
| 3 | 5–9 s | `termio sim tap --label "…"`: the screen in the pane moves to the next view. Focus band moves from the command to the phone. | terminal line → pane |
| 4 | 9–12 s | The person takes over: the finger pointer taps a field and the Mac keyboard types into it. | pointer → field |
| 5 | 12–15 s | `termio sim screenshot`, then the agent writes its check. Its sidebar dot turns green. Hold ≥ 1.2 s on the agent's reply. | reply → dot |
| 6 | 15–17 s | End card: "Introducing the Simulator pane", termio.sh, github.com/termio-sh/termio. | centre |

Also cut a 7 s silent landing loop from beats 2–3 for termio.sh.

## Strings to use verbatim

- Pane header help: "Home", "Rotate Right", "Save Screenshot to Desktop"
- Device menu placeholder: "Choose a Simulator"; booting: "Booting <name>…"
- Agent reply lines: "launched <bundle id> (pid N) on <device>", "tapped X,Y",
  "attached <device> (W×H points)"

## Capture plan (Codex CLI Computer Use, brief to be written from the v5 brief)

- A clean demo project with one Claude Code session and the Simulator pane open on one
  iPhone (shut down every other booted simulator first: six were booted on 2026-10-24).
- The agent asks once per device before it drives it. Allow it before the capture.
- Captures: before launch, after launch, after the tap, after typing, after the reply.
  Hover and the finger pointer cannot be captured; rebuild them in HTML.
