import heapq

left_heap, right_heap = [], []

for line in open("input.txt", "r"):
    # split line into left and right and update heaps
    [left, right] = line.split()
    heapq.heappush(left_heap, left)
    heapq.heappush(right_heap, right)

# track total difference
total = 0

while left_heap:
    total += abs(int(heapq.heappop(left_heap)) - int(heapq.heappop(right_heap)))

print(total)
