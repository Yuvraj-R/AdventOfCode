from collections import deque


class Day18:
    def __init__(self, num_falls, grid_width, grid_height):
        self.num_falls = num_falls
        self.grid_width = grid_width
        self.grid_height = grid_height

    def solution1(self):
        # Read and parse coordinates from the input file
        with open("input.txt", "r") as file:
            coordinates = [tuple(map(int, line.strip().split(",")))
                           for line in file]

        # Initialize the grid
        grid = [["."] * self.grid_width for _ in range(self.grid_height)]
        for x, y in coordinates[:self.num_falls]:
            grid[y][x] = "#"

        def in_bounds(y, x):
            return 0 <= y < self.grid_height and 0 <= x < self.grid_width

        # Breadth-first search setup
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = 0

        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                y, x = queue.popleft()
                if grid[y][x] == "#":
                    continue
                if (y, x) == (self.grid_height - 1, self.grid_width - 1):
                    return distance
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if in_bounds(ny, nx) and (ny, nx) not in visited:
                        visited.add((ny, nx))
                        queue.append((ny, nx))
            distance += 1

        # If no path is found, return -1
        return -1

    def solution2(self):
        # Read and parse coordinates from the input file
        with open("input.txt", "r") as file:
            coordinates = [tuple(map(int, line.strip().split(",")))
                           for line in file]

        # Initialize the grid
        grid = [["."] * self.grid_width for _ in range(self.grid_height)]

        def in_bounds(y, x):
            return 0 <= y < self.grid_height and 0 <= x < self.grid_width

        def bfs():
            """Perform BFS to determine if there is a path from (0, 0) to (self.grid_height-1, self.grid_width-1)."""
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                y, x = queue.popleft()
                if (y, x) == (self.grid_height - 1, self.grid_width - 1):
                    return True
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if in_bounds(ny, nx) and (ny, nx) not in visited and grid[ny][nx] == ".":
                        visited.add((ny, nx))
                        queue.append((ny, nx))
            return False

        # Simulate bytes falling and check connectivity
        for x, y in coordinates:
            grid[y][x] = "#"
            if not bfs():
                # Return the coordinates of the byte that caused the cut-off
                return f"{x},{y}"

        # If the path is never blocked, return None (this case should not occur in valid inputs)
        return None

    # Example usage
if __name__ == "__main__":
    day18 = Day18(1024, 71, 71)
    print(day18.solution1())
    print(day18.solution2())
