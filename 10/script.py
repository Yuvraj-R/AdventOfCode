### PART 1 ###

with open("input.txt", "r") as file:
    topography = [list(map(int, line.strip())) for line in file.readlines()]

num_rows, num_cols = len(topography), len(topography[0])


def in_bounds(y, x):
    return 0 <= y < num_rows and 0 <= x < num_cols


def dfs(y, x, found):
    if (y, x) in found or not in_bounds(y, x):
        return 0

    cur = topography[y][x]
    if cur == 9:
        found.add((y, x))
        return 1

    # Up Down Left Right coordinates
    nearby = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    return sum(dfs(ny, nx, found) for ny, nx in nearby if in_bounds(ny, nx) and topography[ny][nx] == cur + 1)


total_score = sum(
    dfs(y, x, set())
    for y, row in enumerate(topography) for x, val in enumerate(row) if val == 0
)
print(total_score)

### PART 2 ###


def rating_dfs(y, x):
    if not in_bounds(y, x):
        return 0

    cur = topography[y][x]
    if cur == 9:
        return 1

    # Up, Down, Left, Right coordinates
    nearby = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    return sum(rating_dfs(ny, nx) for ny, nx in nearby if in_bounds(ny, nx) and topography[ny][nx] == cur + 1)


total_rating = sum(
    rating_dfs(y, x)
    for y, row in enumerate(topography) for x, val in enumerate(row) if val == 0
)
print(total_rating)
