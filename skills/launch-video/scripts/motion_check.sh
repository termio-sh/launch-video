#!/bin/sh
# Measurable stand-in for watching a render. Not a substitute for the user's eyes.
# usage: motion_check.sh VIDEO.mp4 OUTDIR [from_s to_s]
#   OUTDIR/motion.csv   per-frame mean luma change (0-255) between consecutive frames
#   OUTDIR/jumps.txt    frames whose change is > 2.5x the median of its 9-frame window
#                       (a jerk: velocity spike, pop, flicker)
#   OUTDIR/rests.txt    still spans >= 0.3 s (where clicks belong) and their lengths
#   OUTDIR/sheet.png    12 fps contact sheet of the range (default: whole video)
set -e
v="$1"; out="$2"; from="${3:-0}"; to="${4:-}"
mkdir -p "$out"
fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$v" | awk -F/ '{print $1/($2?$2:1)}')
ffmpeg -v error -i "$v" -vf "scale=480:-2,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=$out/raw.txt" -f null -
grep -o 'YAVG=[0-9.]*' "$out/raw.txt" | cut -d= -f2 | awk -v fps="$fps" '{printf "%d,%.3f,%s\n", NR, NR/fps, $1}' > "$out/motion.csv"
python3 -I - "$out" "$fps" <<'PY'
import sys, statistics
out, fps = sys.argv[1], float(sys.argv[2])
rows = [l.split(",") for l in open(f"{out}/motion.csv")]
d = [float(r[2]) for r in rows]
jumps = []
for i in range(len(d)):
    w = d[max(0, i-4):i+5]
    m = statistics.median(w)
    if d[i] > 0.4 and d[i] > 2.5 * max(m, 0.05):
        jumps.append(f"{i/fps:7.3f}s  change {d[i]:.2f}  window median {m:.2f}")
open(f"{out}/jumps.txt", "w").write("\n".join(jumps) + "\n")
rests, start = [], None
for i, x in enumerate(d + [99]):
    if x < 0.15 and start is None: start = i
    if x >= 0.15 and start is not None:
        if (i - start) / fps >= 0.3: rests.append(f"{start/fps:7.3f}s - {i/fps:7.3f}s  ({(i-start)/fps:.2f}s still)")
        start = None
open(f"{out}/rests.txt", "w").write("\n".join(rests) + "\n")
print(f"{len(jumps)} jump frames, {len(rests)} rests >= 0.3s, peak change {max(d):.2f}")
PY
range="-ss $from"; [ -n "$to" ] && range="$range -to $to"
ffmpeg -v error $range -i "$v" -vf "fps=12,scale=320:-2,tile=8x6" -frames:v 1 -y "$out/sheet.png"
echo "wrote $out/{motion.csv,jumps.txt,rests.txt,sheet.png}"
