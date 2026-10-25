# Capture manifest

No PNGs were saved. Capture stopped at step 1 because the required Simulator pane was not visible.

- `01-ready.png` — SKIPPED: release Termio showed the Claude Code terminal across the main content area, with no right-hand inspector or Simulator pane; iPhone 17 and its home screen were not visible. S status: `idle` on the subsequent CLI check. Observed AX window rect in points: `(x=4, y=33, width=1508, height=949)`. Native capture scale was not measured. PNG pixel rects for the sidebar, S row, Claude Code pane, Simulator pane, and device screen: N/A (no PNG).
- `02-launched.png` — SKIPPED: step 1 prerequisite failed; launch prompt not sent. S last observed status: `idle`. Window rect: `(4, 33, 1508, 949)` points, observed during the step 1 check only. Scale and all requested PNG pixel rects: N/A.
- `03-field.png` — SKIPPED: step 1 prerequisite failed; tap prompt not sent. S last observed status: `idle`. Window rect: `(4, 33, 1508, 949)` points, observed during the step 1 check only. Scale and all requested PNG pixel rects: N/A.
- `04-typed.png` — SKIPPED: step 1 prerequisite failed; no simulator field was clicked and no keyboard text was typed. S last observed status: `idle`. Window rect: `(4, 33, 1508, 949)` points, observed during the step 1 check only. Scale and all requested PNG pixel rects: N/A.
- `05-reply.png` — SKIPPED: step 1 prerequisite failed; screenshot prompt not sent. S last observed status: `idle`. Window rect: `(4, 33, 1508, 949)` points, observed during the step 1 check only. Scale and all requested PNG pixel rects: N/A.

## Observations

Release app: `/Applications/termio.app`, bundle ID `sh.termio.app`, PID `44181`.

The specified CLI focus command returned success. The first Computer Use screenshot had window title `~/Documents/termio-demo/termio-mobile` and the Claude Code welcome screen, but no Simulator inspector. The highlighted visible sidebar row was `Landing page redesign with Mobbin references` under `termio`, rather than the requested session S. After a 3-second wait, a fresh Computer Use screenshot showed window title `~/Documents/GitHub/termio`, the same highlighted sidebar row, and a Claude Code conversation across the main area. No inspector pane was visible in either screenshot. The cause of the selection change was not established.

CLI status check: `termio://session/fbd20cd7-772c-4471-a78f-de115c6fbed6`, agent `claude`, status `idle`, title `Claude Code`.

Headers collapsed in step 2: none. Headers expanded during restoration: none.

Agent replies after steps 4, 5, and 7: none; these prompts were not sent.

Restoration: an initial attempt with `TERMIO_SESSION` removed failed with “Couldn’t tell which project you’re in. Run this from inside a Termio session.” Then ran the exact requested focus command for `termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d` using the inherited environment without the demo-session override; CLI reported success.

No menus, sidebar rows, terminal panes, or simulator controls were clicked. No keyboard input was sent. The window was not moved or resized. No development app was targeted. Only this manifest was written.
