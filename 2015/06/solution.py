import re
import sys

import numpy

grid1 = numpy.zeros(shape=(1000, 1000), dtype="int8")
grid2 = grid1.copy()

for line in sys.stdin:
    r1, c1, r2, c2 = map(int, re.findall(r"\d+", line))
    r2 += 1
    c2 += 1
    op =line.split()[1]
    if op == "on":
        grid1[r1:r2, c1:c2] = 1
        grid2[r1:r2, c1:c2] += 1
    elif op == "off":
        grid1[r1:r2, c1:c2] = 0
        positive = grid2[r1:r2, c1:c2] > 0
        grid2[r1:r2, c1:c2][positive] -= 1
    else:
        zeros = grid1[r1:r2, c1:c2] == 0
        ones = grid1[r1:r2, c1:c2] == 1
        grid1[r1:r2, c1:c2][zeros] = 1
        grid1[r1:r2, c1:c2][ones] = 0
        grid2[r1:r2, c1:c2] += 2

print("Part One:", grid1.sum())
print("Part Two:", grid2.sum())
