with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

    grid = []
    moves = []

    i = 0
    while lines[i] != "":
        grid.append(list(lines[i]))
        i += 1

    i += 1
    while i < len(lines):
        moves.extend(lines[i])
        i += 1

# Grid dimensions
GRID_HEIGHT = len(grid)
GRID_WIDTH = len(grid[0])

# inital robot position
robot_pos = [(y, x) for y in range(GRID_HEIGHT)
             for x in range(GRID_WIDTH) if grid[y][x] == "@"][0]

offsets = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)
}


def in_bounds(y, x):
    return 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH


def process_move(pos_y, pos_x, move):
    move_y = pos_y + offsets[move][0]
    move_x = pos_x + offsets[move][1]

    move_element = grid[move_y][move_x]

    if move_element == "#":
        return (pos_y, pos_x)
    elif move_element == ".":
        grid[pos_y][pos_x] = "."
        return (move_y, move_x)
    else:
        while move_element not in (".", "#"):
            move_y += offsets[move][0]
            move_x += offsets[move][1]
            move_element = grid[move_y][move_x]

        if grid[move_y][move_x] == ".":
            print("valid shift")
        else:
            print("invalid shift")
        return (pos_y, pos_x)


print(robot_pos)
for move in moves:
    robot_pos = process_move(robot_pos[0], robot_pos[1], move)
    print(move, robot_pos)
