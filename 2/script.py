### PART 1 ###
count = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        valid = 1
        if nums[1] > nums[0]:
            if all(
                nums[i - 1] < nums[i] < nums[i - 1] + 4 for i in range(1, len(nums))
            ):
                count += 1
        else:
            if all(
                nums[i - 1] > nums[i] > nums[i - 1] - 4 for i in range(1, len(nums))
            ):
                count += 1

print(count)
