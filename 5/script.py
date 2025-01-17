### PART 1 ###
from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

# Split lines into rules and updates based on the first empty line
split_index = lines.index("")
rules = [list(map(int, line.split("|"))) for line in lines[:split_index]]
updates = [list(map(int, line.split(","))) for line in lines[split_index + 1 :]]

# process rules into dictionary
rules_map = defaultdict(set)
for key, value in rules:
    rules_map[key].add(value)


# validate each update and keep track of running sum and invalid updates
invalid_updates = []  # for part 2


def validate_update(update):
    seen = set()
    for page in update:
        if any(successor in seen for successor in rules_map[page]):
            invalid_updates.append(set(update))
            return 0
        seen.add(page)

    return update[len(update) // 2]


total_sum = sum(validate_update(update) for update in updates)
print(total_sum)


### PART 2 ###
def correct_update(update):
    result = []

    for page in update:
        count = sum(1 if successor in update else 0 for successor in rules_map[page])
        result.append((page, count))

    result.sort(key=lambda x: x[1])
    return result[len(result) // 2][0]


total_corrected_sum = sum(correct_update(update) for update in invalid_updates)
print(total_corrected_sum)
