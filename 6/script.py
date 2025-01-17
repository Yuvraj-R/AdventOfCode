### PART 1 ###

with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

pos = next(
    [r, c] for r, row in enumerate(matrix) for c, val in enumerate(row) if val == "^"
)

offset = (-1, 0)  # Store the direction of the guard as an offset
mappings = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

while 0 <= pos[0] + offset[0] < len(matrix) and 0 <= pos[1] + offset[1] < len(matrix[0]):
    # base case: move forwards with no obstructions
    if matrix[pos[0] + offset[0]][pos[1] + offset[1]] != "#":
        matrix[pos[0]][pos[1]] = "X"
        pos = [pos[0] + offset[0], pos[1] + offset[1]]
    else:
        offset = mappings[offset]

matrix[pos[0]][pos[1]] = "X"

total_moves = sum(line.count("X") for line in matrix)
print(total_moves)

### PART 2 ###
with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]


def is_loop(matrix, start_pos, offset):
    visited = set()

    while 0 <= start_pos[0] + offset[0] < len(matrix) and 0 <= start_pos[1] + offset[1] < len(matrix[0]):
        state = (start_pos[0], start_pos[1], offset)
        if state in visited:
            return True
        visited.add(state)

        if matrix[start_pos[0] + offset[0]][start_pos[1] + offset[1]] != "#":
            start_pos = (start_pos[0] + offset[0], start_pos[1] + offset[1])
        else:
            offset = mappings[offset]

    return False


total_positions = 0

for r, row in enumerate(matrix):
    for c, col in enumerate(row):
        if col == ".":
            matrix[r][c] = "#"
            if is_loop(matrix, [53, 89], (-1, 0)):
                total_positions += 1
            matrix[r][c] = "."

print(total_positions)
