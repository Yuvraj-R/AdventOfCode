with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

grid, moves = [], []
i = 0
while lines[i] != "":
    grid.append(list(lines[i]))
    i += 1

i += 1  # Skip the blank line
moves = "".join(lines[i:])

# Grid dimensions
GRID_HEIGHT, GRID_WIDTH = len(grid), len(grid[0])

# inital robot position
robot_pos = next(
    (y, x) for y in range(GRID_HEIGHT)
    for x in range(GRID_WIDTH) if grid[y][x] == "@"
)

DIRECTIONS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def in_bounds(y, x):
    return 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH


def process_move(pos_y, pos_x, move):
    dy, dx = DIRECTIONS[move]
    new_y, new_x = pos_y + dy, pos_x + dx

    # If the move is blocked by a wall, stay in place
    if grid[new_y][new_x] == "#":
        return pos_y, pos_x

    # If moving to an empty space, update the robot's position
    if grid[new_y][new_x] == ".":
        grid[pos_y][pos_x] = "."
        grid[new_y][new_x] = "@"
        return new_y, new_x

    # Handle box pushing
    while grid[new_y][new_x] not in (".", "#"):
        new_y += dy
        new_x += dx

    if grid[new_y][new_x] == ".":
        # Push boxes
        while (new_y - dy, new_x - dx) != (pos_y, pos_x):
            grid[new_y][new_x] = "O"
            new_y -= dy
            new_x -= dx

        grid[new_y][new_x] = "@"
        grid[pos_y][pos_x] = "."
        return new_y, new_x

    # If blocked, stay in place
    return pos_y, pos_x


# Simulate all moves
for move in moves:
    robot_pos = process_move(robot_pos[0], robot_pos[1], move)

# Calculate the total GPS coordinates sum
total_gps = sum(
    100 * y + x
    for y in range(GRID_HEIGHT)
    for x in range(GRID_WIDTH)
    if grid[y][x] == "O"
)

# Print the result
print(total_gps)
