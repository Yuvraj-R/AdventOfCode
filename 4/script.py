### PART 1 ###

with open("input.txt", "r") as file:
    lines = file.readlines()


# Function to check a specific direction with explicit bounds
def check_direction(row, col, row_step, col_step):
    for i in range(4):
        new_row = row + i * row_step
        new_col = col + i * col_step
        # Ensure the new position is within bounds
        if (
            new_row < 0
            or new_row >= len(lines)
            or new_col < 0
            or new_col >= len(lines[0]) - 1
        ):
            return False
        if lines[new_row][new_col] != "XMAS"[i]:
            return False
    return True


def is_root(row, col):
    directions = [
        (-1, 0),  # Up
        (1, 0),  # Down
        (0, -1),  # Left
        (0, 1),  # Right
        (-1, -1),  # Top-left to bottom-right (diagonal down)
        (1, 1),  # Bottom-left to top-right (diagonal up)
        (-1, 1),  # Top-right to bottom-left (diagonal down-back)
        (1, -1),  # Bottom-right to top-left (diagonal up-back)
    ]

    return sum(
        check_direction(row, col, row_step, col_step)
        for row_step, col_step in directions
    )


res = 0
for row in range(len(lines)):
    for col in range(len(lines[0]) - 1):
        if lines[row][col] == "X":
            res += is_root(row, col)

print(res)

### PART 2 ###


def is_middle(row, col):
    if 0 < row < len(lines) - 1 and 0 < col < len(lines[0]) - 1:
        diagonals = (
            lines[row - 1][col - 1]
            + lines[row - 1][col + 1]
            + lines[row + 1][col - 1]
            + lines[row + 1][col + 1]
        )
        return diagonals in {"MMSS", "MSMS", "SSMM", "SMSM"}
    return False


res = sum(
    is_middle(row, col)
    for row in range(len(lines))
    for col in range(len(lines[0]) - 1)
    if lines[row][col] == "A"
)

print(res)
