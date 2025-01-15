### PART 1 ###
def strict_is_safe(nums):
    if nums[1] > nums[0]:
        return all(nums[i - 1] < nums[i] < nums[i - 1] + 4 for i in range(1, len(nums)))
    else:
        return all(nums[i - 1] > nums[i] > nums[i - 1] - 4 for i in range(1, len(nums)))


count = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        if strict_is_safe(nums):
            count += 1

print(count)


### PART 2 ###
def is_safe(nums):
    if not strict_is_safe(nums):
        for i in range(0, len(nums)):
            if strict_is_safe(nums[:i] + nums[i + 1 :]):
                return True
        return False
    return True


count = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        if is_safe(nums):
            count += 1

print(count)
