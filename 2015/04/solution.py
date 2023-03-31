import hashlib
from itertools import count

secret_key = input()
p1 = next(
    i
    for i in count(1)
    if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()[:5] == "00000"
)
p2 = next(
    i
    for i in count(p1)
    if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()[:6] == "000000"
)
print("Part One:", p1)
print("Part Two:", p2)
