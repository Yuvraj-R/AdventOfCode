### PART 1 ###

import sys

sys.set_int_max_str_digits(20000)

'''
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


left, right = 0, len(ordering) - 1
while left < right:
    while left < right and ordering[left] != ".":
        left += 1
    while left < right and ordering[right] == ".":
        right -= 1
    if left < right:
        ordering[left], ordering[right] = ordering[right], ordering[left]

checksum = sum(idx * num for idx, num in enumerate(ordering) if num != ".")
print(checksum)
'''

### PART 2 ###

# Re-read the input to get the original un-compacted layout again.
with open("input.txt", "r") as file:
    nums_part2 = [int(num) for num in file.readline().strip()]

ordering_part2, is_file2, id2 = [], True, 0
for num in nums_part2:
    if is_file2:
        ordering_part2.extend([id2] * num)
        id2 += 1
    else:
        ordering_part2.extend(["."] * num)
    is_file2 = not is_file2

# Now apply the Part 2 rules:
# "Attempt to move whole files to the leftmost span of free space blocks
# that could fit the file, in order of decreasing file ID."

max_file_id = max(x for x in ordering_part2 if x != ".")

for file_id in range(max_file_id, -1, -1):
    # Find all blocks of this file
    positions = [i for i, val in enumerate(ordering_part2) if val == file_id]
    if not positions:
        # No blocks of this file present (or file size 0)
        continue

    file_size = len(positions)
    # The leftmost position occupied by this file
    leftmost_block = positions[0]

    # Scan all free-space spans strictly to the left of leftmost_block
    free_spans = []
    in_span = False
    span_start = None

    for i in range(leftmost_block):
        if ordering_part2[i] == ".":
            if not in_span:
                in_span = True
                span_start = i
        else:
            # End the free span
            if in_span:
                free_spans.append((span_start, i - 1))
            in_span = False

    # Check if we ended in a free span that goes right up to leftmost_block - 1
    if in_span:
        free_spans.append((span_start, leftmost_block - 1))

    # Find the first (leftmost) free span that can fit the entire file
    target_span = None
    for (start, end) in free_spans:
        if (end - start + 1) >= file_size:
            target_span = (start, end)
            break

    # If a suitable free span was found, move the file there as a contiguous block
    if target_span:
        (span_start, span_end) = target_span
        # Remove the file blocks from their old positions
        for pos in positions:
            ordering_part2[pos] = "."
        # Place the file contiguously, starting at span_start
        for idx in range(span_start, span_start + file_size):
            ordering_part2[idx] = file_id

# Finally, compute the checksum for Part 2
checksum_part2 = sum(
    idx * val for idx, val in enumerate(ordering_part2) if val != ".")
print(checksum_part2)
