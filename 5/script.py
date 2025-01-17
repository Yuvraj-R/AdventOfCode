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


# validate each update and keep a running sum
def validate_update(update):
    seen = set()
    for page in update:
        if any(successor in seen for successor in rules_map[page]):
            return 0
        seen.add(page)

    return update[len(update) // 2]


total_sum = sum(validate_update(update) for update in updates)
print(total_sum)
