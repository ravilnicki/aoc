import itertools
import math
import sys

distances = {}
locations = set()

for line in sys.stdin:
    start, _, end, _, distance = line.split()
    distance = int(distance)
    distances[(start, end)] = distance
    distances[(end, start)] = distance
    locations.add(start)
    locations.add(end)

p1 = float("inf")
p2 = float("-inf")
end = math.factorial(len(locations)) // 2
for i, perm in enumerate(itertools.permutations(locations, 8)):
    if i >= end:
        break
    perm_sum = sum(distances[location_pair] for location_pair in itertools.pairwise(perm))
    p1 = min(p1, perm_sum)
    p2 = max(p2, perm_sum)

print("Part One:", p1)
print("Part Two:", p2)
