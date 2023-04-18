def look_and_say(nums: list[int]) -> list[int]:
    new_nums = []
    start = 0
    for i in range(len(nums)):
        if nums[i] != nums[start]:
            new_nums.append(i - start)
            new_nums.append(nums[start])
            start = i
    new_nums.append(len(nums) - start)
    new_nums.append(nums[start])
    return new_nums


number = [int(d) for d in input()]
for _ in range(40):
    number = look_and_say(number)
print("Part One:", len(number))
for _ in range(10):
    number = look_and_say(number)
print("Part Two:", len(number))
