### PART 1 ###
with open("input.txt", "r") as file:
    data = [
        [int(part[0]), list(map(int, part[1].strip().split()))]
        for line in file
        for part in [line.strip().split(":")]
    ]


def equation_value(target, curr, rest):
    if not rest:
        return target if curr == target else 0
    else:
        if equation_value(target, curr + rest[0], rest[1:]) != 0:
            return target
        elif equation_value(target, curr * rest[0], rest[1:]) != 0:
            return target
        return 0


calibration_sum = sum(
    equation_value(target, nums[0], nums[1:]) for [target, nums] in data
)

print(calibration_sum)
