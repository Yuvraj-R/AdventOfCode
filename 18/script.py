from collections import deque


class Day18:

    def __init__(self, num_falls, GRID_WIDTH, GRID_HEIGHT):
        self.num_falls = num_falls
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT

    def solution(self):
        with open("input.txt", "r") as file:
            coordinates = [list(map(int, line.strip().split(",")))
                           for line in file]

        grid = [["."] * self.GRID_WIDTH for _ in range(self.GRID_HEIGHT)]

        for i in range(self.num_falls):
            x, y = coordinates[i]
            grid[y][x] = "#"

        def in_bounds(y, x):
            return 0 <= y < self.GRID_HEIGHT and 0 <= x < self.GRID_WIDTH

        queue = deque()
        queue.append((0, 0))
        distance = 0
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        while queue:
            iterations = len(queue)
            for i in range(iterations):
                y, x = queue.popleft()
                if (y, x) in visited or not in_bounds(y, x) or grid[y][x] == "#":
                    continue

                visited.add((y, x))

                if y == self.GRID_HEIGHT - 1 and x == self.GRID_WIDTH - 1:
                    return distance

                for dy, dx in offsets:
                    queue.append((y + dy, x + dx))
            distance += 1


day18 = Day18(1024, 71, 71)
print(day18.solution())
