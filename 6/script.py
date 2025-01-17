### PART 1 ###

with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

pos = next(
    [r, c] for r, row in enumerate(matrix) for c, val in enumerate(row) if val == "^"
)

offset = (-1, 0)  # Store the direction of the guard as an offset
mappings = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

while (0 <= pos[0] < len(matrix) - 1) and (0 <= pos[1] < len(matrix[0]) - 1):
    # base case: move forwards with no obstructions
    if matrix[pos[0] + offset[0]][pos[1] + offset[1]] != "#":
        matrix[pos[0]][pos[1]] = "X"
        pos = [pos[0] + offset[0], pos[1] + offset[1]]
    else:
        offset = mappings[offset]

matrix[pos[0]][pos[1]] = "X"

total_moves = sum(line.count("X") for line in matrix)
print(total_moves)
