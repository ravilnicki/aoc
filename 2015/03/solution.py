def next_house(house: tuple[int], move: str) -> tuple:
    x, y = house
    match move:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1
    return x, y


line = input()
robo_house = santa2_house = santa1_house = 0, 0
year1 = {santa1_house}
year2 = year1.copy()
for i, move in enumerate(line):
    santa1_house = next_house(santa1_house, move)
    year1.add(santa1_house)
    if i % 2 == 0:
        santa2_house = next_house(santa2_house, move)
        year2.add(santa2_house)
    else:
        robo_house = next_house(robo_house, move)
        year2.add(robo_house)
print("Part One:", len(year1))
print("Part Two:", len(year2))
