from collections import defaultdict

# Read and parse the input
with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

# Split lines into rules and updates based on the first empty line
split_index = lines.index("")
rules = [list(map(int, line.split("|"))) for line in lines[:split_index]]
updates = [list(map(int, line.split(","))) for line in lines[split_index + 1 :]]

# Process rules into a dictionary
rules_map = defaultdict(set)
for key, value in rules:
    rules_map[key].add(value)


# Validate updates
def validate_updates(updates):
    invalid_updates = []
    total_sum = 0

    for update in updates:
        seen = set()
        valid = True
        for page in update:
            if any(successor in seen for successor in rules_map[page]):
                invalid_updates.append(update)
                valid = False
                break
            seen.add(page)
        if valid:
            total_sum += update[len(update) // 2]

    return total_sum, invalid_updates


# Correct invalid updates
def correct_update(update):
    # Create (page, count) pairs
    result = [
        (page, sum(1 for successor in rules_map[page] if successor in update))
        for page in update
    ]

    # Sort by count and return the middle page
    result.sort(key=lambda x: x[1])
    return result[len(result) // 2][0]


# Calculate totals
total_sum, invalid_updates = validate_updates(updates)
print(total_sum)

total_corrected_sum = sum(correct_update(update) for update in invalid_updates)
print(total_corrected_sum)
