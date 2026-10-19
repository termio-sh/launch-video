---
name: social-publish
description: Publish or schedule a Termio video post on Xiaohongshu, X, LinkedIn, WeChat Channels, Reddit, or TikTok through the user's logged-in Chrome (Claude-in-Chrome), including the cover, short copy, scheduling, and editing a post that is already scheduled. Use when the user asks to post, publish, upload, schedule, or update a video or its cover on any of these platforms. Holds each platform's working page flow, upload workarounds, and copy rules.
---

# Publishing a Termio video

`references/platforms.md` holds each platform's exact flow, quirks, and limits.
Read the section for the platform before opening the page.

## Hard rules

1. **Confirm before the irreversible click.** Fill everything, then stop and show the
   user title, body, cover, file, and schedule. Click 发布 / 发表 / Post / 定时发布 only
   after a clear yes in chat for that post. A yes for one platform is not a yes for the next.
2. **Never log in, never solve a captcha, never type a password.** The user does it.
3. **No cross-source compiling of third parties' data.** The user asked to find
   stargazers' LinkedIn profiles, then to tag or DM them, then for a script. All forms
   were refused. Offer instead: tag people the user names, a thank-you line, or a
   GitHub Discussion/Release.
4. **A blocked site stays blocked.** reddit.com is blocked by the extension. Hand off:
   copy the video to `~/Desktop`, reveal it in Finder, give title and steps.
5. **Never overwrite the user's edits.** The user edits drafts while you work. Read the
   editor back with JS before every change; keep their text; report what they changed.
6. **Report status from fully loaded evidence.** The note manager shows "全部 0" while
   it loads; a status claim made from that was wrong for two days.

## Files

- The Chrome `file_upload` tool takes ≤ 10 MB. Upload the 1080p copy:
  `ffmpeg -i master-4k.mp4 -vf scale=1920:1080 -c:v libx264 -crf 20 -maxrate 5M
  -bufsize 10M -c:a aac -b:a 128k -movflags +faststart out-1080p.mp4`.
- Squeezing 1440p or 4K under 10 MB looks worse than 1080p. If the user wants the
  master, say the user must drag it in by hand.
- Find file inputs with JS, not `find` alone:
  `[...document.querySelectorAll('input[type=file]')].map(i => i.accept)`.
  The accept list tells the video input from the image input. Walk shadow roots when
  nothing is found (WeChat Channels).

## Copy

- Short. Title = product + feature. Body = one sentence on what it does + links.
  The video carries the detail.
- Use the app's own UI words (zh from `Localizable.xcstrings`: 设置 › 外观 › 标签页 › 横向).
- No superlatives ("Best place…"). "Termio" with a capital T. Free and open source,
  never paid.
- Let the user add hashtags/topics (a `#` opens a picker on Xiaohongshu).
- Communities (Reddit): disclose "I built", lead with what the sub cares about
  (libghostty for r/Ghostty), put the GitHub link in the first comment.

Approved examples:
- Xiaohongshu: title "Termio 横向标签页"; body "Termio 横向标签页：Agent 会话排成一行，
  支持一键切换和拖动排序。/ 官网：termio.sh / GitHub：termio-sh/termio".
- LinkedIn (user's own): "Introducing Termio UI 2.0: each agent session is a card. /
  Free and open source, for macOS: termio.sh / GitHub: github.com/termio-sh/termio".

## Cover

- Never ship the first frame (it is a dark fade-in) and never a cropped screenshot.
- Xiaohongshu cover: icon + "Termio" above the feature title, nothing else. More
  elements read as AI slop. Keep the top-right empty: the play icon sits there.
- Background is a frame showing the story's key state. Build it with the
  `launch-video` skill (craft.md § Stills and the cover).
- Rebuild the cover whenever the video changes, and replace both together.

## Scheduling

- The picker's own time zone label is the truth. Xiaohongshu's "北京时间" picker is
  GMT+8 even when the browser is in London. Enter Beijing time directly.
- Check the result from the submitted request, not the UI: hook fetch/XHR and convert
  the timestamp (1792472400000 = 2026-10-20T05:00Z = 13:00 Beijing was the bug).
  Then check the note list reads the intended time.
