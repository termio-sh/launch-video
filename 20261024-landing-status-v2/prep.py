# Clean the Codex CLI capture of the ky scene and cut the tiles the film animates.
from PIL import Image

src = Image.open("assets/cap/capture-raw.png").convert("RGB")
im = src.copy()

# The Computer Use pointer and its halo sit on the sandboxbench folder icon: copy the
# icon column from two rows up, which is a clean folder row.
im.paste(src.crop((0, 723, 62, 823)), (0, 850))
# Its halo spreads past the icon under the label: below the text's brightness, every
# pixel there is window background.
BG = (47, 50, 55)
for y in range(840, 975):
    for x in range(0, 260):
        if max(im.getpixel((x, y))) < 95:
            im.putpixel((x, y), BG)

# The bare Terminal pane ends on a stray `quote>` prompt.
im.paste((34, 37, 42), (722, 880, 900, 940))

# Drop the capture folder's own project row: lift the sidebar from ky down by one row.
SIDEBAR = 712
ROW = 64
im.paste(im.crop((0, 300, SIDEBAR, 1898)), (0, 300 - ROW))
im.paste((47, 50, 55), (0, 1898 - ROW, SIDEBAR, 1898))
im.save("assets/cap/window.png")

# Rows after the lift, top of each 40px tile; the tile spans x 49..89.
TILE = {"term": 312, "opts": 376, "ask": 440, "codex": 504, "long": 568}
def blank(top, out):
    tile = im.crop((44, top - 6, 96, top + 46))
    # The tile face is a vertical gradient: fill each line with its own edge colour.
    for y in range(14, 38):
        tile.paste(tile.getpixel((12, y)), (11, y, 41, y + 1))
    tile.save(out)
blank(TILE["term"], "assets/img/tile-blank.png")
blank(TILE["long"], "assets/img/tile-blank-selected.png")
# The terminal row has no status dot, so its tile corner is the clean corner.
# Its icon reaches into the bottom-left of that corner, so that part stays transparent and
# the patched row keeps its own mark there.
corner = im.crop((72, TILE["term"] - 10, 98, TILE["term"] + 16)).convert("RGBA")
corner.paste((0, 0, 0, 0), (0, 19, 8, 26))
corner.save("assets/img/corner-patch.png")
