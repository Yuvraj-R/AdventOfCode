### PART 1 ###

import sys

sys.set_int_max_str_digits(20000)
with open("input.txt", "r") as file:
    nums = [int(num) for num in file.readline().strip()]

ordering, id, is_file = [], 0, True
for i in range(0, len(nums), 1):
    if is_file:
        for j in range(0, nums[i]):
            ordering.append(id)
    else:
        id += 1
        for k in range(0, nums[i]):
            ordering.append(".")
    is_file = not is_file

left, right = 0, len(ordering)-1
while left < right:
    while ordering[left] != ".":
        left += 1
    while ordering[right] == ".":
        right -= 1

    ordering[left], ordering[right] = ordering[right], ordering[left]

ordering[left], ordering[right] = ordering[right], ordering[left]

left, checksum = 0, 0
while ordering[left] != ".":
    checksum += (left * ordering[left])
    left += 1

print(checksum)

### PART 2 ###
