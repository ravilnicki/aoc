import json
from typing import Any


def add_up_nums(d: Any, ignore_red=False) -> int:
    if isinstance(d, int):
        return d
    if isinstance(d, list):
        return sum(add_up_nums(el, ignore_red=ignore_red) for el in d)
    if isinstance(d, dict):
        if ignore_red and "red" in d.values():
            return 0
        return sum(add_up_nums(val, ignore_red=ignore_red) for val in d.values())
    return 0


d = json.loads(input())
print("Part One:", add_up_nums(d))
print("Part Two:", add_up_nums(d, ignore_red=True))
