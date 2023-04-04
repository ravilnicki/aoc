import re
import sys


def part1(string: str) -> int:
    vowels = bool(re.search(r"([aeiou]\w*){2}[aeiou]", string))
    doubles = bool(re.search(r"(\w)\1", string))
    does_not_contain = not bool(re.search(r"ab|cd|pq|xy", string))
    return int(vowels and doubles and does_not_contain)


def part2(string: str) -> int:
    double_pair = bool(re.search(r"(\w\w)\w*\1", string))
    in_between = bool(re.search(r"(\w)\w\1", string))
    return int(double_pair and in_between)


p1, p2 = 0, 0
for line in sys.stdin:
    p1 += part1(line)
    p2 += part2(line)
print("Part One:", p1)
print("Part Two:", p2)
