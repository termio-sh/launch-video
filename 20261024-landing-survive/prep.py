# Clean the two Codex CLI captures of the ky scene, taken before Command-Q and after reopening.
from PIL import Image

BG = (47, 50, 55)
PANE = (34, 37, 42)
SIDEBAR = 772
ROW = 64

def clean(src_path, out_path):
    src = Image.open(src_path).convert("RGB")
    im = src.copy()
    # The Computer Use pointer sits on the tunelo folder icon: copy the closed-folder icon
    # from the oakreader row, then clear its halo, which is darker than any label text.
    im.paste(src.crop((0, 1005 - 256, 62, 1068 - 256)), (0, 1005))
    for y in range(975, 1105):
        for x in range(0, 300):
            if max(im.getpixel((x, y))) < 95:
                im.putpixel((x, y), BG)
    # The bare Terminal pane ends on a stray `quote>` prompt.
    im.paste(PANE, (790, 885, 940, 940))
    # Drop the capture folder's own project row: lift the sidebar from ky up by one row.
    # Stop above the window's bottom corner so its rounded edge stays where it is.
    im.paste(im.crop((0, 301, SIDEBAR, 1800)), (0, 301 - ROW))
    im.paste(BG, (0, 1800 - ROW, SIDEBAR, 1800))
    im.save(out_path)

clean("assets/cap/before-raw.png", "assets/cap/before.png")
clean("assets/cap/after-raw.png", "assets/cap/after.png")
