### PART 1 ###

with open("input.txt", "r") as file:
    topography = [list(map(int, line.strip())) for line in file.readlines()]

num_rows, num_cols = len(topography), len(topography[0])


def in_bounds(y, x):
    return 0 <= y < num_rows and 0 <= x < num_cols


def dfs(y, x, found):
    if not (0 <= y < num_rows and 0 <= x < num_cols):
        return 0

    cur = topography[y][x]

    print("VALUE: ", cur, "COORDS: ", y+1, x+1)

    if cur == 9 and (y, x) not in found:
        print("9 FOUND: ", y, x)
        found.add((y, x))
        return 1

    # Up Down Left Right coordinates
    nearby = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    return sum(dfs(c[0], c[1], found) for c in nearby if in_bounds(c[0], c[1]) and topography[c[0]][c[1]] == cur+1)


total_score = sum(dfs(y, x, set())
                  for y, y_val in enumerate(topography) for x, x_val in enumerate(y_val) if x_val == 0)
print(total_score)

### PART 2 ###
