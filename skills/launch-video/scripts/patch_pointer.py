"""Erase a baked-in pointer from a capture, then prove nothing else changed.

usage: python3 -I patch_pointer.py IN.png OUT.png x0 y0 x1 y1 [--from-col C | --from OTHER.png]

  --from-col C   fill each row of the box with that row's pixel at column C
                 (row-matched background: keeps separator lines and gradients intact)
  --from OTHER   copy the same box from a neighbouring capture where it is clean

Always patch from the ORIGINAL capture, never from an earlier patched file.
Exits 1 if any pixel outside the box differs from IN.
"""
import sys
import numpy as np
from PIL import Image

args = sys.argv[1:]
src, out = args[0], args[1]
x0, y0, x1, y1 = map(int, args[2:6])
a = np.asarray(Image.open(src).convert("RGBA")).copy()
orig = a.copy()
if "--from-col" in args:
    c = int(args[args.index("--from-col") + 1])
    a[y0:y1, x0:x1] = a[y0:y1, c:c + 1]
elif "--from" in args:
    b = np.asarray(Image.open(args[args.index("--from") + 1]).convert("RGBA"))
    a[y0:y1, x0:x1] = b[y0:y1, x0:x1]
else:
    sys.exit("give --from-col C or --from OTHER.png")

mask = np.ones(a.shape[:2], bool)
mask[y0:y1, x0:x1] = False
outside = int((a != orig).any(axis=2)[mask].sum())
inside = int((a != orig).any(axis=2)[~mask].sum())
print(f"changed inside box: {inside} px; changed outside box: {outside} px")
if outside:
    sys.exit(1)
Image.fromarray(a).save(out)
print(f"wrote {out}. Now LOOK at a 2x crop of the box: no cut lines, no erased text.")
