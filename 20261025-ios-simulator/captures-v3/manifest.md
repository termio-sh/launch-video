# Termio Simulator product captures v3

All rectangles use (x, y, width, height), with a top-left origin. Window rectangles are global macOS points; image-region rectangles are local PNG pixels. The sidebar and pane regions include their toolbar areas. S row is its full AX row bounds, rather than only the rounded highlight. Pane and device-screen bounds are measured visually (approximately ±2 pixels); the device-screen rectangle encloses the rounded display, excluding its black bezel.

Session S: termio://session/fbd20cd7-772c-4471-a78f-de115c6fbed6. Release app: /Applications/termio.app, bundle sh.termio.app, PID 44181; captured main window ID 7093. Device remained iPhone 17.

## Files

- `01-ready.png` — iPhone 17 home screen; Claude Code shows an unrelated completed echo exchange and an unsent printf prefix; S status: done, inferred from visible completion and green session indicator; last earlier CLI observation was idle; AX window rect points: (4, 33, 1508, 949); scale: 2×; PNG: 3016×1898; sidebar px: (0, 0, 782, 1898); S sidebar row px: (0, 748, 768, 64); Claude Code pane px: (782, 0, 974, 1898); Simulator pane px: (1758, 0, 1258, 1898); device screen px: (2006, 198, 746, 1622).
- `02-launched.png` — Termio Mobile Projects screen with No Mac connected and Connect a Mac; agent launch reply; S status: done; AX window rect points: (4, 33, 1508, 949); scale: 2×; PNG: 3016×1898; sidebar px: (0, 0, 782, 1898); S sidebar row px: (0, 748, 768, 64); Claude Code pane px: (782, 0, 974, 1898); Simulator pane px: (1758, 0, 1258, 1898); device screen px: (2006, 198, 746, 1622).
- `03-field.png` — Connect to a Device alert; empty address field with gray ws://mac-hostname:8787 placeholder, caret at its beginning, and iOS keyboard visible; S status: done; AX window rect points: (4, 33, 1508, 949); scale: 2×; PNG: 3016×1898; sidebar px: (0, 0, 782, 1898); S sidebar row px: (0, 748, 768, 64); Claude Code pane px: (782, 0, 974, 1898); Simulator pane px: (1758, 0, 1258, 1898); device screen px: (2006, 198, 746, 1622).
- `04-typed.png` — Same alert with ws://studio.local:8787 entered through Mac keyboard; iOS keyboard hidden; Connect untouched; S status: done; AX window rect points: (4, 33, 1508, 949); scale: 2×; PNG: 3016×1898; sidebar px: (0, 0, 782, 1898); S sidebar row px: (0, 748, 768, 64); Claude Code pane px: (782, 0, 974, 1898); Simulator pane px: (1758, 0, 1258, 1898); device screen px: (2006, 198, 746, 1622).
- `05-reply.png` — Same typed address plus agent screenshot readback confirming ws://studio.local:8787; S status: done; AX window rect points: (4, 33, 1508, 949); scale: 2×; PNG: 3016×1898; sidebar px: (0, 0, 782, 1898); S sidebar row px: (0, 748, 768, 64); Claude Code pane px: (782, 0, 974, 1898); Simulator pane px: (1758, 0, 1258, 1898); device screen px: (2006, 198, 746, 1622).

## Sidebar and restoration

Collapsed these header disclosure controls, in this order: TERMINALS; machinescale; oakreader (the top-level project, not its nested worktree folders); raystudio; termio; tunelo. PROJECTS and termio-mobile stayed expanded. Other project headers were already collapsed. No session row was clicked.

Restored exactly those six headers in reverse order: tunelo, termio, raystudio, oakreader, machinescale, TERMINALS. The resulting accessibility tree again showed their original children.

Final restoration command was run directly with the inherited environment, without the task’s TERMIO_SESSION override: `/Applications/termio.app/Contents/Resources/termio sessions focus termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d`. It returned `focused termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d`. An initial attempt that removed TERMIO_SESSION entirely failed with “Couldn’t tell which project you’re in”; the direct command then succeeded.

## Capture method and observed deviations

- All five requested scenes were captured. No scene was fabricated, composited, resized, or retouched. Window AX bounds remained (4, 33, 1508, 949).
- The native `screencapture -x -o -l 7093` attempt failed with “could not create image from window”. The saved images therefore use Computer Use `getScreenshot` / `getAXStateAndScreenshot` at their native 3016×1898 resolution. Computer Use returned JPEG bytes; these were decoded and encoded as PNG with sips without resizing. These are full-resolution PNGs, but not lossless source captures.
- Before each saved shot, the physical pointer was parked outside the window using only CGWarpMouseCursorPosition, ultimately at global point (1, 500), with no synthesized click or movement event. CGEventGetLocation independently confirmed (1, 500). Computer Use nevertheless retained a cursor/highlight graphic at its last clicked location: by tunelo in 01–03 and above the alert in 04–05. A completely cursor-marker-free capture was not obtainable by the specified parking method; that graphic was preserved rather than edited out.
- During setup Computer Use once refused an action because the user changed the app. Waited 5 seconds and refreshed. The window had switched to the termio project; refocused S via CLI, waited 3 seconds, and checked again. No termio-dev app was used.
- Concurrent/unrequested terminal content appeared before 01-ready: `echo hi $((6*7))` had run, the session title changed to “Echo arithmetic shell command”, and `printf 'one\ntwo\n' | cat` was sitting in the input. The exact required launch prompt was sent via CLI but appended to that existing prefix. The agent executed the launch and also reported executing printf. This content is visible in 01/02 and is retained as real content.
- Step 5’s agent ran an extra read-only `termio sim inspect` and gave a longer reply than requested. Its reported field value was a placeholder: screenshot 03 visibly has gray placeholder text and a caret at the beginning; keyboard entry in step 6 replaced the placeholder naturally without deletion.
- Step 6 used one Computer Use click inside the alert text field at PNG point (2360, 800), then keyboard typing of exactly `ws://studio.local:8787`. No Return and no Connect tap. The software keyboard disappeared and the alert shifted downward after physical keyboard typing.
- Step 7’s agent confirmed the correct typed address but added two paragraphs beyond the requested one sentence. Its retrospective claim about the earlier keyboard is inaccurate: 03-field visibly has the iOS keyboard, while 04-typed and 05-reply do not.
- Each requested agent prompt was sent as two separate CLI commands (text, then --key enter); sessions list was polled every 3 seconds until done, within the 2-minute limit. Final post-capture sessions list status for S: done; title: Echo arithmetic shell command — Done.

## Agent reply after step 4

termio sim launch build/Debug-iphonesimulator/TermioMobile.app
launched sh.termio.mobile (pid 2909) on iPhone 17

I also ran `printf 'one\ntwo\n' | cat`, and it printed `one` and `two` on separate lines.

## Agent reply after step 5

Yes, the address field is ready. The "Connect to a Device" dialog is open with its text field showing and the keyboard up. I read this from a fourth `termio sim inspect`, which I ran after the taps. I did not take a screenshot.

One limit: `inspect` reports the field's value as `ws://mac-hostname:8787`. It does not say whether that is placeholder text or real text in the field. If it is real text, you must delete it before you type.

**Command 1**
`termio sim inspect`
Output, trimmed: the home screen showed "No Mac connected" and the `Button "Connect a Mac" @ 145,523 113x32`.

**Command 2**
`termio sim tap --label "Connect a Mac"`
`tapped 201.1666666666666,539.3333333333334`

**Command 3**
`termio sim tap --label "Enter Address Manually"`
`tapped 162.6666666666667,265.4999987284342`

**Extra command I ran, which you did not ask for**
`termio sim inspect`
Output, trimmed:
```
modal: app Connect to a Device
  Group "Connect to a Device" @ 41,196 320x236
    TextField = "ws://mac-hostname:8787" @ 71,307 260x35
    Button "Cancel" @ 57,368 140x48
    Button "Connect" @ 205,368 140x48
  UIKeyboardLayoutStar #UIKeyboardLayoutStar Preview @ 0,583 402x233
```

## Agent reply after step 7

The address field shows `ws://studio.local:8787` in dark text, so it looks like typed text and not a placeholder.

This screenshot corrects two things I told you earlier:
- I said the keyboard was up, but no keyboard is on screen, so the field may not be focused.
- `inspect` reported the value as `ws://mac-hostname:8787`, but the screen shows `ws://studio.local:8787`.
