### PART 2 ###

from collections import defaultdict


def read_initial_stones(file_path):
    with open(file_path, "r") as file:
        return list(map(int, file.readline().strip().split()))


def process_stones(counts):
    new_counts = defaultdict(int)
    for num, cnt in counts.items():
        if num == 0:
            new_counts[1] += cnt
        elif len(str(num)) % 2 == 0:
            digits = str(num)
            mid = len(digits) // 2
            left = int(digits[:mid])
            # Handle cases like '1000' -> '10' and '00' which becomes '0'
            right = int(digits[mid:]) if digits[mid:] else 0
            new_counts[left] += cnt
            new_counts[right] += cnt
        else:
            new_num = num * 2024
            new_counts[new_num] += cnt
    return new_counts


def main():
    initial_nums = read_initial_stones("input.txt")

    # Initialize counts
    counts = defaultdict(int)
    for num in initial_nums:
        counts[num] += 1

    iterations = 75  # Change to 25 for Part 1

    for i in range(iterations):
        counts = process_stones(counts)
        if (i + 1) % 10 == 0 or i == 0 or i == iterations - 1:
            print(f"After {i+1} blinks: {sum(counts.values())} stones")

    total_stones = sum(counts.values())
    print(f"Total number of stones after {iterations} blinks: {total_stones}")


if __name__ == "__main__":
    main()
