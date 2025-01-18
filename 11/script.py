### PART 1 ###

with open("input.txt", "r") as file:
    nums = list(map(int, file.readline().strip().split()))


def process(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        res = [int(str(num)[0:len(str(num))//2]),
               int(str(num)[len(str(num))//2:])]
        return res
    else:
        return [num*2024]


for i in range(0, 25):
    j = 0
    while j < len(nums):
        res = process(nums[j])
        del nums[j]
        for val in res[::-1]:
            nums.insert(j, val)
        j += len(res)

print(len(nums))

### PART 2 ###
