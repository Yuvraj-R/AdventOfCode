### PART 1 ###

import sys

sys.set_int_max_str_digits(20000)

with open("input.txt", "r") as file:
    nums = [int(num) for num in file.readline().strip()]

ordering, is_file, id = [], True, 0
for num in nums:
    if is_file:
        ordering.extend([id] * num)
        id += 1
    else:
        ordering.extend(["."] * num)
    is_file = not is_file

left, right = 0, len(ordering)-1
while left < right:
    while left < right and ordering[left] != ".":
        left += 1
    while left < right and ordering[right] == ".":
        right -= 1
    if left < right:
        ordering[left], ordering[right] = ordering[right], ordering[left]

checksum = sum(idx * num for idx, num in enumerate(ordering) if num != ".")
print(checksum)

### PART 2 ###
