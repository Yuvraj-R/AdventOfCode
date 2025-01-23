import sys
from collections import defaultdict


class Solution:
    def solution(self):
        ### PART 1 ###
        with open("input.txt", "r") as file:
            grid = [list(line.strip()) for line in file]

        start, end = (len(grid) - 2, 1), (1, len(grid[0]) - 2)

        offsets = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
        opposites = {"^": "v", "v": "^", "<": ">", ">": "<"}

        lowest_score = float('inf')

        # best_score[(y, x, direction)] = minimal cost found so far
        # for being at (y, x) *while facing `direction`*
        best_score = {}
        score_paths = defaultdict(set)
        current_path = []

        def in_bounds(y, x):
            return 0 <= y < len(grid) and 0 <= x < len(grid[0])

        def dfs(y, x, score, direction):
            nonlocal lowest_score

            current_path.append((y, x))

            if not in_bounds(y, x) or grid[y][x] == "#":
                current_path.pop()
                return

            if (y, x, direction) in best_score and best_score[(y, x, direction)] < score:
                current_path.pop()
                return

            best_score[(y, x, direction)] = score

            if (y, x) == end:
                # -- Compare with the global lowest_score --
                if score < lowest_score:
                    # Found a NEW best cost: discard old best-path sets
                    score_paths.clear()
                    score_paths[score].update(current_path)
                    lowest_score = score
                elif score == lowest_score:
                    # Found ANOTHER path with the SAME best cost: union its cells
                    score_paths[score].update(current_path)

                current_path.pop()
                return

            # Move forward
            dy, dx = offsets[direction]
            dfs(y + dy, x + dx, score + 1, direction)

            # Turn left/right (skipping 180° and same direction)
            for new_dir, (ny, nx) in offsets.items():
                if new_dir in (direction, opposites[direction]):
                    continue
                dfs(y + ny, x + nx, score + 1001, new_dir)

            current_path.pop()

        dfs(start[0], start[1], 0, ">")
        print(lowest_score)

        ### PART 2 ###
        print(len(score_paths[lowest_score]))


sys.setrecursionlimit(1000)
instance = Solution()
instance.solution()
