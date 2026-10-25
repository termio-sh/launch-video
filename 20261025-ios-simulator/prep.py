# Build the film's layers from the Codex CLI captures (window, terminal, sidebar row)
# and from simctl screenshots of iPhone 17 (the device screen, clean and one per key).
import os
from PIL import Image, ImageDraw

V2, V3 = "captures-v2", "captures-v3"
os.makedirs("assets/cap", exist_ok=True)
os.makedirs("assets/screen", exist_ok=True)

base = Image.open(f"{V2}/01-ready.png").convert("RGB")
src = base.copy()

# The Computer Use pointer and its halo sit on the sandboxbench folder icon: copy the
# icon column from the ky row, four rows up, then return the halo to the background.
BG = src.getpixel((300, 1300))
base.paste(src.crop((0, 300, 62, 364)), (0, 556))
for y in range(540, 650):
    for x in range(0, 300):
        if max(base.getpixel((x, y))) < 95:
            base.putpixel((x, y), BG)
base.save("assets/cap/window.png")

# Terminal: every capture keeps one line every 34px, so lines move between captures
# whole. Target grid: line k of the clean window starts at 290 + 34k.
def line(path, origin, k):
    return Image.open(path).convert("RGB").crop((790, origin + 34 * k - 7, 1746, origin + 34 * k + 27))

SOURCES = {
    "launch": (f"{V2}/02-launched.png", 290),
    "tapask": (f"{V2}/03-field.png", 222),
    "taps": (f"{V3}/04-typed.png", 86),
    "shot": (f"{V3}/05-reply.png", 86),
}
# (target line, source, source line), in the order they appear.
STEPS = [
    ("A1", [(k, "launch", k) for k in range(2, 6)]),
    ("A2", [(k, "launch", k) for k in range(6, 14)]),
    ("A3", [(k, "tapask", k) for k in range(15, 20)]),
    ("A4", [(21, "taps", 6), (23, "taps", 26), (24, "taps", 27), (26, "taps", 30), (27, "taps", 31), (29, "taps", 45)]),
    ("A6", [(k + 4, "shot", k) for k in range(27, 30)]),
    ("A7", [(35, "shot", 31), (37, "shot", 33), (38, "shot", 34), (39, "shot", 35)]),
]
TOP = 270
term = base.crop((790, TOP, 1746, 1645))
for name, lines in STEPS:
    for k, source, j in lines:
        path, origin = SOURCES[source]
        term.paste(line(path, origin, j), (0, 290 + 34 * k - 7 - TOP))
    term.save(f"assets/cap/term-{name}.png")

# Sidebar row: idle before the first turn, titled with its done dot after it.
ROW = (0, 744, 768, 816)
base.crop(ROW).save("assets/cap/row-idle.png")
Image.open(f"{V2}/02-launched.png").convert("RGB").crop(ROW).save("assets/cap/row-done.png")
# A working row: the tile with its mark removed, under the spinner.
tile = base.crop((43, 754, 95, 806))
for y in range(14, 38):
    tile.paste(tile.getpixel((12, y)), (11, y, 41, y + 1))
tile.save("assets/cap/tile-blank.png")

# Device screen: where the pane draws it, found by matching a simctl screenshot.
SCREEN = (2006, 197, 746, 1622)
RADIUS = 116
SS = 4
mask = Image.new("L", (SCREEN[2] * SS, SCREEN[3] * SS), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, SCREEN[2] * SS - 1, SCREEN[3] * SS - 1), RADIUS * SS, fill=255)
mask = mask.resize(SCREEN[2:], Image.LANCZOS)
for name in sorted(os.listdir("assets/phone")):
    shot = Image.open(f"assets/phone/{name}").convert("RGB").resize(SCREEN[2:], Image.LANCZOS)
    shot.putalpha(mask)
    shot.save(f"assets/screen/{name}")
print("ok", BG)
