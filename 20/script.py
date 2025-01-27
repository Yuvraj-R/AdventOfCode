from collections import defaultdict, Counter, deque
import sys

sys.setrecursionlimit(10000)


class Day20:

    def solution(self):
        with open("input.txt", "r") as file:
            grid = [list(line.strip()) for line in file]

        GRID_HEIGHT, GRID_WIDTH = len(grid), len(grid[0])
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
                if dfs(y + dy, x + dx, i + 1):
                    return True

            del path[(y, x)]
            return False

        start_y, start_x = next((y, x) for y in range(GRID_HEIGHT)
                                for x in range(GRID_WIDTH) if grid[y][x] == "S")
        dfs(start_y, start_x, 0)

        cheats = defaultdict(int)

        def calculate_cheat(y, x):
            for i, (dy1, dx1) in enumerate(offsets):
                for (dy2, dx2) in offsets[i + 1:]:
                    first, second = (y + dy1, x + dx1), (y + dy2, x + dx2)
                    if first in path and second in path:
                        time_saved = abs(path[first] - path[second]) - 2
                        if time_saved > 0:
                            cheats[time_saved] += 1

        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid[y][x] == "#":
                    calculate_cheat(y, x)

        part1_answer = sum(count for cheat_val,
                           count in cheats.items() if cheat_val >= 100)

        # --------------------
        # PART 2:
        # --------------------

        best_cheats = {}  # key = (start_idx, end_idx), value = max time_saved

        for (sy, sx), start_idx in path.items():
            queue = deque([(sy, sx, 0)])  # (current_y, current_x, steps_used)
            visited = set([(sy, sx)])
            best_dist = {}  # key = end_idx, value = min steps_used to reach it

            while queue:
                cy, cx, dist = queue.popleft()
                if dist >= 20:
                    continue

                for dy, dx in offsets:
                    ny, nx = cy + dy, cx + dx
                    if not in_bounds(ny, nx):
                        continue

                    if (ny, nx) in visited:
                        continue

                    visited.add((ny, nx))
                    new_dist = dist + 1

                    if (ny, nx) in path:
                        end_idx = path[(ny, nx)]
                        if end_idx != start_idx:
                            if end_idx not in best_dist or new_dist < best_dist[end_idx]:
                                best_dist[end_idx] = new_dist

                    queue.append((ny, nx, new_dist))

            for end_idx, steps_used in best_dist.items():
                time_saved = abs(start_idx - end_idx) - steps_used
                if time_saved > 0:
                    pair = (start_idx, end_idx)
                    if pair not in best_cheats or time_saved > best_cheats[pair]:
                        best_cheats[pair] = time_saved

        part2_answer = sum(
            1 for time_saved in best_cheats.values() if time_saved >= 100)//2

        return part1_answer, part2_answer


day20 = Day20()
print(day20.solution())
