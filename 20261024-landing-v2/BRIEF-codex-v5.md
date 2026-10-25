Use Computer Use to capture two screenshots of the running Termio app for a short product video:
agent sessions survive quitting Termio. The shot before the quit and the shot after the reopen must
show the same window, the same selected session, and the same layout.
Save every PNG into: /Users/yuanjiwei/Documents/GitHub/launch-video/20261024-landing-v2/captures-v5
(create that folder).

Rules:
- Use the release Termio app, /Applications/termio.app. Other termio-dev.app builds may be running or relaunching; ignore them, never quit or touch them.
- Never run `open` with a directory argument. Launch or front the app only with: open -a /Applications/termio.app
- Never click the macOS menu bar or any menu. Park the pointer outside the window with CGWarpMouseCursorPosition only (no click, no events).
- Do not type into any terminal pane with the keyboard. Drive sessions only with the termio CLI. The only keystroke you may send is Command-Q in step 6.
- Do not click any sidebar session row. Change selection only with the termio CLI.
- Every termio CLI command must run with this environment variable, so it targets the demo project:
  export TERMIO_SESSION=F46CDB83-DB0D-44A6-A649-423D5487319C
- If Computer Use refuses an action because "the user changed" the app, wait 5 s, take a fresh screenshot, and try again. Retry up to 5 times before giving up on that step.
- Real content only. Do not commit, push, or edit repo files.
- Each PNG must be the Termio window only, at native 2x scale, saved as PNG at full resolution.
- If a shot is impossible, skip it and say why. Do not fake it.

The demo project is "ky" (~/Documents/termio-demo/ky). Its sessions (S = termio://session/):
- LONG  = S a37e9a81-fb43-40aa-b29d-4d9e91360394  Claude Code (selected one)
- ASK   = S e68fb41c-7fb0-4fde-b8f2-0b8ac438f4a3  Claude Code
- CODEX = S df735c84-d599-440a-b09a-06934ba83570  Codex CLI
- OPTS  = S 08642efa-b20e-49b0-91d8-22e5eb0c842b  Claude Code
- TERM  = S f46cdb83-db0d-44a6-a649-423d5487319c  plain terminal showing git log

Steps:
1. Start a long task with the CLI only:
   termio sessions send <LONG> --key ctrl-u
   termio sessions send <LONG> "Read every file under test/ one at a time. After each file, write a three-line summary of it. Do not stop until you have read all of them."
   Poll `termio sessions list` every 5 s until LONG shows working (max 2 min).
2. termio sessions focus <LONG>
   Then: open -a /Applications/termio.app . Look at the window. The selected sidebar row must be LONG and the panes must be the ky group.
3. Tidy the sidebar so only the ky project's sessions show: collapse every other expanded section and project folder (TERMINALS and each other expanded project) by clicking its header row's disclosure chevron, never a session row. Write down exactly which headers you collapsed. If ky is collapsed, expand it.
4. Record the window's rect in points (AX position and size of the Termio window). Park the pointer. Wait 3 s. Save 01-before-quit.png. Note LONG's last visible line.
5. Wait 10 s.
6. Make sure Termio is frontmost, then press Command-Q once. Wait 3 s. Check the release app process (pgrep -f "/Applications/termio.app/Contents/MacOS") and note its pid; something else may relaunch it, which is fine.
7. Wait 20 s in total since the quit, so LONG keeps working without the app. Then run: open -a /Applications/termio.app . Wait until the window is drawn.
8. Put the scene back exactly as a person would after reopening:
   a. termio sessions focus <LONG>
   b. If the window rect differs from step 4, set the window's AX position and size back to the step-4 rect with System Events (no menus, no dragging).
   c. If the sidebar is no longer tidied as in step 3, collapse the same headers again the same way.
   Write down which of a–c you had to do.
9. Wait 3 s. Park the pointer. Save 02-reopened.png. Run `termio sessions list` and note LONG's status. Note whether LONG's pane shows more output than in 01.
10. Restore: expand exactly the headers you collapsed. Then, WITHOUT the TERMIO_SESSION override, run: termio sessions focus termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d

Finally write captures-v5/manifest.md: one line per file with what it shows, the statuses at that moment, the window rect in points, the scale factor, and the pixel rects (in the PNG) of the sidebar, each ky session's sidebar row, and each terminal pane. Also write the steps 6–8 observations. Reply with the file list and any shot you could not make and why.
