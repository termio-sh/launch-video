# Platform flows (as of 2026-10-19)

All through Claude-in-Chrome in the user's logged-in Chrome. UIs change; when a step
fails, read the DOM again before retrying.

## Xiaohongshu — creator.xiaohongshu.com

**New post**
1. `https://creator.xiaohongshu.com/publish/publish?source=official`. Wait 3–8 s: the
   upload input loads late.
2. Video input: class `upload-input`, accept `.mp4,.mov,.flv,…`. Upload the 1080p file.
   The page says "检测为高清视频".
3. Title: input with placeholder "填写标题会有更多赞哦". Limit 20 characters.
4. Body: the contenteditable. Typing `#` opens the topic picker; topics are stored as
   `#name[话题]#`. Leave them to the user.
5. Links (termio.sh, GitHub) may become plain text; the user kept them.

**Cover**
1. Click 编辑封面 → "设置封面" modal.
2. The image input (`image/png, image/jpeg, image/*`, "上传封面图片") exists only when
   no uploaded cover is in the modal. To replace: click × on the old tile (sometimes
   twice), then re-run the accept-list JS until the image input appears. `find` once
   returned the VIDEO input under the cover label; the accept check caught it.
3. Upload → 完成. Expect "封面效果评估通过，未发现封面质量问题".
4. Format: 4:3, 2880×2160 JPEG q92, ~400 KB.

**Schedule**: turn on 定时发布, pick date, hour, minute in Beijing time, click 定时发布.

**Edit a scheduled note**
1. 笔记管理: `https://creator.xiaohongshu.com/new/note-manager`. Wait for the list to load.
2. Hover the note card → 编辑 → `/publish/update`.
3. 重新上传 swaps the video; the cover survives a video swap, so replace it explicitly.
4. Click 定时发布 → `/publish/editSuccess` "更新成功". The note shows 审核中 until it goes out.
5. Confirm the list line, e.g. "定时发布 2026-10-20 20:00 （GMT+8:00 北京时间）".

**Limits seen**: video ≤ 4 h and 20 GB; no chapters under 15 s; above 1080p keeps more
quality via the web uploader.

## X — x.com

1. `https://x.com/compose/post`. Two file inputs exist (dialog and timeline); use the dialog one.
2. `file_upload` the 1080p file. Text typed during the upload can vanish: click the
   "Post text" box again and retype, then read it back.
3. To swap the file: ✕ on the attached video, then upload again.
4. Outcome of the 2026-10-18 post was not confirmed. Check the profile after posting.

## LinkedIn — linkedin.com

1. `https://www.linkedin.com/feed/?shareActive=true`. If a screenshot fails with
   "Can't interact with browser-internal or unparseable URLs", wait 4 s.
2. A URL in the text becomes a link preview that hides the Media button. Remove the
   preview, then attach media.
3. No file input exists until click time, and Media opens the OS picker. Workaround:
   patch `HTMLInputElement.prototype.click` and `showPicker` so a file input is tagged,
   attached to `body`, and returns without opening the picker. Click Media, find the
   captured input (accept `image/…,video/*`), `file_upload` into it. Next.
4. Thumbnail: video pencil → "Video thumbnail" → file input by "Add video thumbnail" →
   Add → Next. Use a 16:9 1920×1080 title frame from the master, not the first frame.

## WeChat Channels — channels.weixin.qq.com

1. `https://channels.weixin.qq.com/platform/post/create`. Wait ~8 s.
2. The uploader is inside a `wujie-app` micro-frontend shadow root: `find` and
   `querySelectorAll` see nothing. Walk shadow roots recursively to find the input
   (`video/mp4,video/x-m4v,video/*`).
3. Proxy upload: create a visible `<input type=file id=proxy-video-input>` in the light
   DOM; on change copy its files through `new DataTransfer()` into the shadow input and
   dispatch `input` and `change`. `file_upload` into the proxy, then hide it.
4. Description, then 短标题. Short title rejects "." ("Termio UI 2.0 发布" failed;
   "Termio 新界面：会话即卡片" worked). The page scrolls while typing: read field values
   back from the shadow root.
5. Before 发表, check the defaults with the user: location (auto, was 伦敦), 声明原创
   (off), cover (first frame).
6. 发表 → "已发表", redirects to the post list.

## Reddit — blocked

Every reddit.com URL returns "This site is not allowed due to safety restrictions."
Hand off: video to `~/Desktop`, revealed in Finder; a title; steps; tell the user to
read the sub's self-promotion and flair rules. Title used for r/Ghostty: "I built a
free, open-source terminal on libghostty where every coding-agent session is its own card".

## TikTok

- `sig` (sigcli.ai) stores and injects credentials; it does not post.
- The Content Posting API needs a registered, audited app; unaudited apps post
  SELF_ONLY. Use TikTok Studio on the web.
- Vertical 1080×1920 video; compress under 10 MB or the user drags it in.
- Not yet decided: a dedicated dev-tools account (same handle on YouTube Shorts).

## Archive

After a video ships, it lives in `termio-sh/launch-video/YYYYMMDD-slug/` (see the
`launch-video` skill, Process step 10). Link that folder from READMEs.
