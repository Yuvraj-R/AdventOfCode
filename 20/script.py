from collections import defaultdict
import sys

sys.setrecursionlimit(10000)


class Day20:

    def solution(self):
        with open("input.txt", "r") as file:
            grid = [list(line.strip()) for line in file]

        GRID_WIDTH, GRID_HEIGHT = len(grid[0]), len(grid)
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_bounds(y, x):
            return 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH

        path = {}

        def dfs(y, x, i):
            if (y, x) in path or not in_bounds(y, x) or grid[y][x] == "#":
                return False

            path[(y, x)] = i

            if grid[y][x] == "E":
                grid[y][x] = "."
                return True

            for dy, dx in offsets:
                if dfs(y + dy, x + dx, i+1):
                    return True

            del path[(y, x)]
            return False

        start_y, start_x = next(((y, x) for y in range(GRID_HEIGHT)
                                 for x in range(GRID_WIDTH) if grid[y][x] == "S"))

        dfs(start_y, start_x, 0)

        cheats = defaultdict(int)  # time saved -> count
        calculated = set()

        def calculate_cheat(y, x):
            if (y, x) in calculated:
                return

            calculated.add((y, x))

            # Check all possible entry/exit combinations
            # Up, Down, Left, Right
            for (dy1, dx1), (dy2, dx2) in ((d1, d2) for i, d1 in enumerate(offsets) for d2 in offsets[i + 1:]):
                first, second = (y + dy1, x + dx1), (y + dy2, x + dx2)
                if first in path and second in path:
                    time_saved = abs(path[first] - path[second]) - 2
                    if time_saved > 0:
                        cheats[time_saved] += 1

        # Iterate over every wall cell and calculate cheats
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid[y][x] == "#":
                    calculate_cheat(y, x)

        return sum(count for cheat, count in cheats.items() if cheat >= 100)


day20 = Day20()
print(day20.solution())
