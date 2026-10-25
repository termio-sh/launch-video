Use Computer Use to capture screenshots of the running Termio app for two short product videos:
(A) live agent status in the sidebar, (B) agent sessions survive quitting Termio.
Save every PNG into: /Users/yuanjiwei/Documents/GitHub/launch-video/20261024-landing-v2/captures-v4
(create that folder).

Rules:
- Use the Termio app that is already running (/Applications/termio.app). Other termio-dev.app builds are also running; ignore them, never quit or touch them.
- Before anything else, record the Termio window's current rect in points. Do not move or resize it.
- Never click the macOS menu bar or any menu. Park the pointer outside the window with CGWarpMouseCursorPosition only (no click, no events).
- Do not type into any terminal pane with the keyboard. Drive sessions only with the termio CLI below. The only keystroke you may send is Command-Q in step 6.
- Do not click any sidebar session row. Change selection only with the termio CLI.
- Every termio CLI command must run with this environment variable, so it targets the demo project:
  export TERMIO_SESSION=F46CDB83-DB0D-44A6-A649-423D5487319C
- If Computer Use refuses an action because "the user changed" the app, wait 5 s, take a fresh screenshot, and try again. Retry up to 5 times before giving up on that step.
- Real content only. Do not commit, push, or edit repo files.
- Each PNG must be the Termio window only, at native 2x scale, saved as PNG at full resolution.
- If a shot is impossible, skip it and say why. Do not fake it.

The demo project is "ky" (~/Documents/termio-demo/ky). Its sessions (S = termio://session/):
- LONG  = S a37e9a81-fb43-40aa-b29d-4d9e91360394  Claude Code
- ASK   = S e68fb41c-7fb0-4fde-b8f2-0b8ac438f4a3  Claude Code
- CODEX = S df735c84-d599-440a-b09a-06934ba83570  Codex CLI
- OPTS  = S 08642efa-b20e-49b0-91d8-22e5eb0c842b  Claude Code
- TERM  = S f46cdb83-db0d-44a6-a649-423d5487319c  plain terminal showing git log

Steps:
1. Set the scene with the CLI only:
   a. termio sessions send <LONG> --key ctrl-u
      termio sessions send <LONG> "Read every file under source/ and test/ one at a time. After each file, write a three-line summary of it. Do not stop until you have read all of them."
   b. termio sessions send <OPTS> "In one sentence, what does the throwHttpErrors option do?"
      termio sessions send <CODEX> "In one sentence, what does ky's timeout option default to?"
   c. Poll `termio sessions list` every 5 s until OPTS and CODEX show done and LONG shows working (max 3 min).
   d. termio sessions send <ASK> "Use AskUserQuestion to ask me one question: should ky's default retry limit stay at 2 or become 3? Give the two options. Then wait for my answer and do nothing else."
   e. Poll `termio sessions list` every 3 s until ASK shows needs-you (max 2 min). From now on, never answer ASK.
   f. termio sessions focus <LONG>
2. Bring Termio to the front with: open -a /Applications/termio.app . Look at the window. The selected sidebar row must be LONG and the panes must be the ky group.
3. Tidy the sidebar so only the ky project's sessions show: collapse every other section and project (the TERMINALS section and each other project folder) by clicking its header row's disclosure chevron, never a session row. Write down exactly which headers you collapsed. If the ky project is collapsed, expand it.
4. Run `termio sessions list` and note each status. ASK must be needs-you, OPTS and CODEX done, LONG working. Park the pointer. Save 01-status.png at once.
5. Wait 20 s. Save 02-before-quit.png (LONG must still be working; note its last visible line).
6. Make sure Termio is frontmost, then press Command-Q once. Wait 25 s. Confirm the release app process is gone (pgrep -f "/Applications/termio.app/Contents/MacOS"). Do not quit anything else.
7. Relaunch: open -a /Applications/termio.app . Wait about 8 s until the window is drawn and stable, park the pointer, and save 03-reopened.png without changing anything. Note whether the same session is selected, whether the sidebar is still tidied, and whether LONG's pane shows more output than in 02.
8. Restore: expand exactly the headers you collapsed in step 3. Then, WITHOUT the TERMIO_SESSION override, run: termio sessions focus termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d

Finally write captures-v4/manifest.md: one line per file with what it shows, the statuses from `termio sessions list` at that moment, the window rect in points, the scale factor, and the pixel rects (in the PNG) of the sidebar, each ky session's sidebar row, and each terminal pane. Reply with the file list and any shot you could not make and why.
