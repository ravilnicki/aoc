import sys
from itertools import permutations
from math import factorial

from more_itertools import windowed

h = {}
people = set()

for line in sys.stdin:
    person_one, _, change, happiness, *_, person_two = line.strip(".\n").split()
    happiness = int(happiness) if change == "gain" else -int(happiness)
    h.setdefault((person_one, person_two), 0)
    h.setdefault((person_two, person_one), 0)
    h[(person_one, person_two)] += happiness
    h[(person_two, person_one)] += happiness
    people.add(person_one)
    people.add(person_two)

optimal = float("-inf")
n = factorial(len(people)) // 2
for i, seating in enumerate(permutations(people)):
    seating = [*seating, seating[0]]
    optimal = max(optimal, sum(h[pair] for pair in windowed(seating, 2)))
    if i == n:
        break
print("Part One:", optimal)

for person in people:
    h[(person, "me")] = h[("me", person)] = 0

people.add("me")

optimal = float("-inf")
n = factorial(len(people)) // 2
for i, seating in enumerate(permutations(people)):
    seating = [*seating, seating[0]]
    optimal = max(optimal, sum(h[pair] for pair in windowed(seating, 2)))
    if i == n:
        break
print("Part Two:", optimal)
