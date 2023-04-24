import math
import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Ingredient:
    capacity: int
    durability: int
    flavour: int
    texture: int
    calories: int


def calculate_score(
    ingredients: list[Ingredient], spoons: tuple[int], check_callories: bool = False
) -> int:
    properties = [0] * 5
    for ingredient, spoon_number in zip(ingredients, spoons):
        properties[0] += ingredient.capacity * spoon_number
        properties[1] += ingredient.durability * spoon_number
        properties[2] += ingredient.flavour * spoon_number
        properties[3] += ingredient.texture * spoon_number
        properties[4] += ingredient.calories * spoon_number
    if any(p < 0 for p in properties):
        return 0
    if check_callories and properties[4] != 500:
        return 0
    return math.prod(properties[:-1])


ingredients = []
for line in sys.stdin:
    properties = map(int, re.findall(r"-?\d+", line))
    ingredients.append(Ingredient(*properties))

p1, p2 = 0, 0
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c
            p1 = max(p1, calculate_score(ingredients, (a, b, c, d)))
            p2 = max(p2, calculate_score(ingredients, (a, b, c, d), True))
print("Part One:", p1)
print("Part Two:", p2)
