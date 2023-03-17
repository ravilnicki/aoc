import sys

paper, ribbon = 0, 0
for line in sys.stdin:
    w, l, h = sorted(int(n) for n in line.split("x"))
    paper += 2 * (w * l + l * h + w * h) + w * l
    ribbon += 2 * (w + l) + w * l * h
sys.stdout.write(f"Part One: {paper}\n")
sys.stdout.write(f"Part Two: {ribbon}\n")
