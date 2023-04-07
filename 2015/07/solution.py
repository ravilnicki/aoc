import sys


def get_signal(k: str, d: dict) -> str:
    if k.isdigit():
        return k
    fields = d[k].split()
    match fields:
        case [x]:
            signal = get_signal(x, d)
        case ["NOT", x]:
            signal = 65536 + ~int(get_signal(x, d))
        case [x, op, y]:
            x = int(get_signal(x, d))
            y = int(get_signal(y, d))
            match op:
                case "OR":
                    signal = x | y
                case "AND":
                    signal = x & y
                case "RSHIFT":
                    signal = x >> y
                case "LSHIFT":
                    signal = x << y
    d[k] = str(signal)
    return d[k]


d = {}
for line in sys.stdin:
    v, k = line.strip().split(" -> ")
    d[k] = v
d2 = d.copy()

p1 = get_signal("a", d)
d2["b"] = p1
p2 = get_signal("a", d2)

print("Part One:", p1)
print("Part Two:", p2)
