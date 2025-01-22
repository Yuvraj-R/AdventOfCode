import sys


class Solution:
    def solution(self):
        with open("input.txt", "r") as file:
            grid = [list(line.strip()) for line in file]

        start, end = (len(grid) - 2, 1), (1, len(grid[0]) - 2)

        offsets = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
        opposites = {"^": "v", "v": "^", "<": ">", ">": "<"}

        lowest_score = float('inf')

        # best_score[(y, x, direction)] = minimal cost found so far
        # for being at (y, x) *while facing `direction`*
        best_score = {}

        def in_bounds(y, x):
            return 0 <= y < len(grid) and 0 <= x < len(grid[0])

        def dfs(y, x, score, direction):
            nonlocal lowest_score

            if not in_bounds(y, x) or grid[y][x] == "#":
                return

            if (y, x, direction) in best_score and best_score[(y, x, direction)] <= score:
                return

            best_score[(y, x, direction)] = score

            if (y, x) == end:
                lowest_score = min(lowest_score, score)
                return

            dy, dx = offsets[direction]
            dfs(y + dy, x + dx, score + 1, direction)

            for new_dir, (ny, nx) in offsets.items():
                if new_dir in (direction, opposites[direction]):
                    continue
                dfs(y + ny, x + nx, score + 1001, new_dir)

        dfs(start[0], start[1], 0, ">")
        print(lowest_score)


sys.setrecursionlimit(50000)
instance = Solution()
instance.solution()
