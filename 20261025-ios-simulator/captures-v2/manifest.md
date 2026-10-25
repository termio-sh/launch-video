# Capture manifest

All rectangles use (x,y,width,height), origin at upper-left. Window coordinates are desktop points. Other coordinates are pixels within the PNG. Sidebar and S row use AX bounds; Claude pane uses the visible pane boundary; Simulator pane uses its AX group bounds. The rounded device screen is represented by its approximate rectangular bounding box (±2 px).

- `01-ready.png` — Claude Code ready; iPhone 17 home screen; S=idle; window points=(4,33,1508,949); scale=2; PNG=3016x1898; sidebar px=(0,0,768,1898); S row px=(0,748,768,64); Claude Code pane px=(780,0,976,1898); Simulator pane px=(1756,76,1246,1808); device screen bounding box px≈(2006,197,746,1623).
- `02-launched.png` — Successful launch reply; TermioMobile Projects screen with No Mac connected and Connect a Mac; S=done; window points=(4,33,1508,949); scale=2; PNG=3016x1898; sidebar px=(0,0,768,1898); S row px=(0,748,768,64); Claude Code pane px=(780,0,976,1898); Simulator pane px=(1756,76,1246,1808); device screen bounding box px≈(2006,197,746,1623).
- `03-field.png` — FAILED field shot: agent reports accessibility timeout; phone display is black; no Connect to a Device alert or field; S=done; window points=(4,33,1508,949); scale=2; PNG=3016x1898; sidebar px=(0,0,768,1898); S row px=(0,748,768,64); Claude Code pane px=(780,0,976,1898); Simulator pane px=(1756,76,1246,1808); device screen bounding box px≈(2006,197,746,1623).
- `05-reply.png` — Agent says its screenshot shows Projects and no address field; embedded phone remains mostly black with white status strip showing 07:28; S=done; window points=(4,33,1508,949); scale=2; PNG=3016x1898; sidebar px=(0,0,768,1898); S row px=(0,748,768,64); Claude Code pane px=(780,0,976,1898); Simulator pane px=(1756,76,1246,1808); device screen bounding box px≈(2006,197,746,1623).

- `04-typed.png` — NOT CREATED: step 5 never opened the address alert. No keyboard input was sent and Connect was never tapped. S was done when this shot was skipped.

## Capture provenance and limitations

- Release app only: /Applications/termio.app, bundle sh.termio.app, PID 44181. Device remained iPhone 17.
- Computer Use returned native 3016×1898 JPEG window images. These were converted to PNG without resizing, cropping, compositing, or content retouching. They are full-resolution PNGs but not lossless source captures. Native screencapture window and rectangle attempts failed with “could not create image”; neither created a file.
- Pointer parking used only CGWarpMouseCursorPosition at desktop point (0,500), outside the window, with success return 0. Computer Use nonetheless retained its blue pointer indicator over the sandboxbench header in the captured images. It was not removed or faked. These images therefore retain that capture-tool overlay.
- Window AX position and size were (4,33) and (1508,949). No move or resize action was performed. Early observations showed the sidebar/pane split change before capture, during external app changes; all saved frames share the recorded geometry.
- The requested successful alert, handoff typing, and typed-address confirmation sequence could not be made. 03-field.png and 05-reply.png document the real failure, not the intended successful shots.
- Computer Use reported “the user changed” three times before successful sidebar operations. Each refusal was followed by a five-second wait and fresh screenshot. Selection moved to other sessions during setup and was restored only through the prescribed CLI focus command. No sidebar session row or macOS menu was clicked.

## Sidebar restoration

Collapsed in step 2, in order: termio; tunelo; raystudio; oakreader (top-level project); machinescale; TERMINALS; 20261024-landing-v2; ky; sandboxbench. PROJECTS and termio-mobile remained expanded. No nested project folders needed separate collapse after their parent project was collapsed.

Expanded exactly those nine headers afterward. The accessibility tree again showed the original project/session groups. Final focus succeeded with the exact release CLI command and no TERMIO_SESSION override: `/Applications/termio.app/Contents/Resources/termio sessions focus termio://session/ca34d40b-7d58-4308-9e9c-08542c95d70d`. An earlier attempt with TERMIO_SESSION entirely removed failed because the CLI could not determine the caller project; the successful command used the inherited original session environment.

## Agent replies

### Step 4

```
termio sim launch build/Debug-iphonesimulator/TermioMobile.app
launched sh.termio.mobile (pid 82510) on iPhone 17
```

### Step 5

The address field is not ready. The first tap failed, so I did not run the second tap.

```
termio sim tap --label "Connect a Mac"
error: The application with pid 82510 did not respond to an accessibility request before it timed out. Pid 82510 is sh.termio.mobile.
```

`termio sim tap --label "Enter Address Manually"` was not run. It needs the screen that "Connect a Mac" opens, and that tap never happened.

The app (pid 82510) did not answer the accessibility request before it timed out. I did not check if the app is still running or frozen. I can retry the first tap, or relaunch the app and then run both taps again.

### Step 7

No address field is on screen: the app still shows the Projects screen with "No Mac connected" and the "Connect a Mac" button, because the first tap failed and the address screen never opened.

Final post-step-7 `sessions list`: S = done; agent = claude; title = TermioMobile app in simulator — Done.

Prompts were each sent as the specified text command followed by a separate --key enter command. sessions list was polled every three seconds until done for each prompt; none exceeded two minutes.
