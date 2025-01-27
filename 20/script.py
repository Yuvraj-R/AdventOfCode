from collections import defaultdict
import sys

sys.setrecursionlimit(10000)


class Day20:

    def solution(self):
        with open("input.txt", "r") as file:
            grid = [[c for c in line.strip()] for line in file]

        GRID_WIDTH, GRID_HEIGHT = len(grid[0]), len(grid)

        def in_bounds(y, x):
            return 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH

        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, (dy1, dx1) in enumerate(directions):
                for j, (dy2, dx2) in enumerate(directions):
                    # Skip checking the same direction twice
                    if i >= j:
                        continue

                    # Entry point and exit point
                    first = (y + dy1, x + dx1)
                    second = (y + dy2, x + dx2)

                    # Both entry and exit points must be valid path points
                    if first in path and second in path:
                        time_saved = abs(path[first] - path[second]) - 2
                        if time_saved > 0:
                            cheats[time_saved] += 1

        # Iterate over every wall cell and calculate cheats
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid[y][x] == "#":
                    calculate_cheat(y, x)

        count = sum(count for cheat, count in cheats.items() if cheat >= 100)
        print(count)


day20 = Day20()
day20.solution()
