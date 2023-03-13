line = input()
floor, basement = 0, 0
for i, ch in enumerate(line, start=1):
    floor += 1 if ch == '(' else -1
    if basement == 0 and floor == -1:
        basement = i
print("Part One:", floor)
print("Part Two:", basement)
