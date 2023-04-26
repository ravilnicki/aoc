import re
import sys


def find_aunt(
    aunts: list[dict[str, int]],
    ticker_tape: dict[str, int],
    outdated_retroencabulator: bool = False,
) -> int:
    for aunt, compounds in enumerate(aunts, start=1):
        for compound, value in compounds.items():
            if outdated_retroencabulator:
                if compound in ("cats", "trees"):
                    if value > ticker_tape[compound]:
                        continue
                    else:
                        break
                elif compound in ("pomeranians", "goldfish"):
                    if value < ticker_tape[compound]:
                        continue
                    else:
                        break
            if value != ticker_tape[compound]:
                break
        else:
            return aunt


ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
aunts = []
for line in sys.stdin:
    compounds = dict(re.findall(r"(\w+): (\d+)", line))
    for k, v in compounds.items():
        compounds[k] = int(v)
    aunts.append(compounds)

print("Part One:", find_aunt(aunts, ticker_tape))
print("Part Two:", find_aunt(aunts, ticker_tape, outdated_retroencabulator=True))
