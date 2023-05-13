import sys
from itertools import combinations

containers = [int(x) for x in sys.stdin]
p1, p2 = 0, 0
min_number_of_containers = len(containers)
for i in range(1, len(containers) + 1):
    for combination in combinations(containers, i):
        if sum(combination) == 150:
            p1 += 1
            l = len(combination)
            if l < min_number_of_containers:
                min_number_of_containers = l
                p2 = 1
            elif l == min_number_of_containers:
                p2 += 1

print("Part One:", p1)
print("Part Two:", p2)
