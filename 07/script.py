### PART 1 ###
with open("input.txt", "r") as file:
    data = [
        [int(part[0]), list(map(int, part[1].strip().split()))]
        for line in file
        for part in [line.strip().split(":")]
    ]


def equation_value_part1(target, curr, rest):
    if not rest:
        return target if curr == target else 0
    return (
        equation_value_part1(target, curr + rest[0], rest[1:])
        or equation_value_part1(target, curr * rest[0], rest[1:])
    )


calibration_sum_part1 = sum(
    equation_value_part1(target, nums[0], nums[1:]) for target, nums in data
)
print(calibration_sum_part1)


### PART 2 ###
def equation_value_part2(target, curr, rest):
    if not rest:
        return target if curr == target else 0
    return (
        equation_value_part2(target, curr + rest[0], rest[1:])
        or equation_value_part2(target, curr * rest[0], rest[1:])
        or equation_value_part2(target, int(str(curr) + str(rest[0])), rest[1:])
    )


calibration_sum_part2 = sum(
    equation_value_part2(target, nums[0], nums[1:]) for target, nums in data
)
print(calibration_sum_part2)
