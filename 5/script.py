### PART 1 ###
from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if not lines[i].strip():
            j = i
            break

    rules = [list(map(int, x.strip().split("|"))) for x in lines[0:j]]
    updates = [list(map(int, x.strip().split(","))) for x in lines[j + 1 :]]

# process rules into dictionary
rules_map = defaultdict(set)
for rule in rules:
    rules_map[rule[0]].add(rule[1])


# validate each update and keep a running sum
def validate_update(update):
    seen = set()
    for page in update:
        for successor in rules_map[page]:
            if successor in seen:
                return 0

        seen.add(page)

    return update[len(update) // 2]


total_sum = 0
for update in updates:
    total_sum += validate_update(update)
print(total_sum)
