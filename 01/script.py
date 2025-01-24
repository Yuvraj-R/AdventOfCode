from collections import Counter
import heapq

left_heap, right_heap = [], []
left_list, right_list = [], []

for line in open("input.txt", "r"):
    # split line into left and right and update heaps
    [left, right] = map(int, line.split())
    heapq.heappush(left_heap, left)
    heapq.heappush(right_heap, right)
    left_list.append(left)
    right_list.append(right)

### PART 1 ###

total_diff = sum(
    abs(heapq.heappop(left_heap) - heapq.heappop(right_heap))
    for _ in range(len(left_heap))
)

print(total_diff)

### PART 2 ###

right_counts = Counter(right_list)

similarity_score = sum(left * right_counts[left] for left in left_list)

print(similarity_score)
