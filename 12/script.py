### PART 1 ###
with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

coordinates = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


def in_bounds(y, x):
    return 0 <= y < len(coordinates) and 0 <= x < len(coordinates[0])


def dfs(y, x, last):
    if not in_bounds(y, x) or matrix[y][x] != last:
        return (0, 1)
    elif coordinates[y][x] == 1:
        return (0, 0)

    coordinates[y][x] = 1
    area, perimeter = 1, 0

    adjacents = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    for adj_y, adj_x in adjacents:
        next_area, next_perimeter = dfs(adj_y, adj_x, matrix[y][x])
        area += next_area
        perimeter += next_perimeter

    return (area, perimeter)


def processRegion(y, x):
    """ Returns the price for fencing around a region """
    area, perimeter = dfs(y, x, matrix[y][x])
    return area * perimeter


total_price = 0
for i, row in enumerate(coordinates):
    for j, val in enumerate(row):
        if val == 0:
            total_price += processRegion(i, j)

print(total_price)
