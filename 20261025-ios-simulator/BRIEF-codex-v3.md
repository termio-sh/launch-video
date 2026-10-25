Use Computer Use to capture screenshots of the running Termio app for a short product video:
an agent drives the iOS Simulator inside Termio's Simulator pane, and the person takes over the
same device with the Mac keyboard.
Save every PNG into: /Users/yuanjiwei/Documents/GitHub/launch-video/pending-ios-simulator/captures-v3
(the folder exists).

Rules:
- Use the release Termio app, /Applications/termio.app. Other termio-dev.app builds may be running; ignore them, never quit or touch them.
- Never run `open` with a directory argument. Front the app only with: open -a /Applications/termio.app
- Never click the macOS menu bar or any menu. Park the pointer outside the window with CGWarpMouseCursorPosition only (no click, no events).
- Do not resize or move the Termio window.
- Do not type into any terminal pane with the keyboard. Drive the agent only with the termio CLI below.
  The only keyboard typing allowed is in step 6, into the simulator screen inside the Simulator pane.
- Do not click any sidebar session row. Change selection only with the termio CLI.
- Use this CLI path and environment for every termio command:
  export TERMIO_SESSION=FBD20CD7-772C-4471-A78F-DE115C6FBED6
  T=/Applications/termio.app/Contents/Resources/termio
  S=termio://session/fbd20cd7-772c-4471-a78f-de115c6fbed6
- Send each prompt as two commands: `$T sessions send $S "<prompt>"`, then `$T sessions send $S --key enter`.
  After each prompt, poll `$T sessions list` every 3 s until S shows done (max 2 min).
- If the selected sidebar row is not S at any step, run `$T sessions focus $S`, wait 3 s, and look again. Retry up to 5 times before stopping.
- If Computer Use refuses an action because "the user changed" the app, wait 5 s, take a fresh screenshot, and try again. Retry up to 5 times.
- Real content only. Do not commit, push, or edit any file other than the PNGs and the manifest.
- Each PNG must be the Termio window only, at native 2x scale, saved as PNG at full resolution.
- If a shot is impossible, skip it and say why. Do not fake it.

The demo project is "termio-mobile" (~/Documents/termio-demo/termio-mobile) with one Claude Code session, S.
The Simulator pane in the right-hand inspector shows the device "iPhone 17". Do not change the device.

Steps:
1. $T sessions focus $S. Then: open -a /Applications/termio.app . Look at the window. The selected sidebar row
   must be S, the left side must show the Claude Code pane, and the right inspector must show the Simulator pane
   with iPhone 17 on its home screen. If the inspector shows another pane, write down what it shows and stop.
2. Tidy the sidebar so only the termio-mobile project shows its sessions: collapse every other expanded section and
   project folder by clicking its header row's disclosure chevron, never a session row. Write down exactly which
   headers you collapsed. If termio-mobile is collapsed, expand it.
3. Record the window rect in points (AX position and size). Park the pointer. Wait 3 s. Save 01-ready.png.
4. Prompt: Launch the app with exactly: termio sim launch build/Debug-iphonesimulator/TermioMobile.app — then reply with the command on one line and its output on the next.
   When done, wait 3 s, park the pointer, save 02-launched.png. Note the agent's reply lines.
5. Prompt: First read the screen with exactly: termio sim inspect — then tap the button with exactly: termio sim tap --label "Connect a Mac" — then tap with exactly: termio sim tap --label "Enter Address Manually" — then reply with each command and its output, and tell me the address field is ready for me to type in.
   When done, wait 3 s, park the pointer, save 03-field.png. The phone must show the "Connect to a Device" alert with an empty field.
   If the alert is not shown, write down what the phone shows.
6. The person takes over. Click once inside the alert's text field on the simulator screen in the Simulator pane.
   Then type with the keyboard: ws://studio.local:8787
   Do not press Return and do not tap Connect. Park the pointer. Wait 2 s. Save 04-typed.png.
7. Prompt: Take a screenshot with exactly: termio sim screenshot — then look at it and reply in one sentence with what the address field shows.
   When done, wait 3 s, park the pointer, save 05-reply.png. Run `$T sessions list` and note S's status.
8. Restore: expand exactly the headers you collapsed in step 2. Then, WITHOUT the TERMIO_SESSION override, run:
   /Applications/termio.app/Contents/Resources/termio sessions focus termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d

Finally write captures-v3/manifest.md: one line per file with what it shows, S's status at that moment, the window rect
in points, the scale factor, and the pixel rects (in the PNG) of the sidebar, S's sidebar row, the Claude Code pane,
the Simulator pane, and the device screen inside it. Also note the agent's reply text after steps 4, 5 and 7.
Reply with the file list and any shot you could not make and why.
