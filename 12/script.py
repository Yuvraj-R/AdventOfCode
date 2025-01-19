### PART 1 ###
with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


def in_bounds(y, x):
    """Check if the given coordinates are within matrix bounds."""
    return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])


def dfs(y, x, plant_type):
    if not in_bounds(y, x) or matrix[y][x] != plant_type:
        return (0, 1)
    if visited[y][x] == 1:
        return (0, 0)

    visited[y][x] = 1

    area, perimeter = 1, 0

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_area, next_perimeter = dfs(y + dy, x + dx, plant_type)
        area += next_area
        perimeter += next_perimeter

    return (area, perimeter)


def calculate_region_cost(y, x):
    """ Calculate the fencing cost for a region starting at (y, x). """
    area, perimeter = dfs(y, x, matrix[y][x])
    return area * perimeter


total_cost = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if visited[i][j] == 0:
            total_cost += calculate_region_cost(i, j)

print(total_cost)
