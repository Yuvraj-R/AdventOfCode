with open("input.txt", "r") as file:
    lines = file.readlines()


def is_root(row, col):
    res = 0

    # check up
    if row > 3 and ("".join(lines[x][col] for x in range(row, row - 4, -1))) == "XMAS":
        res += 1

    # check down
    if row < 137 and ("".join(lines[x][col] for x in range(row, row + 4, 1))) == "XMAS":
        res += 1

    # check left
    if col > 3 and ("".join(lines[row][x] for x in range(col, col - 4, -1))) == "XMAS":
        res += 1

    # check right
    if col < 137 and ("".join(lines[row][x] for x in range(col, col + 4, 1))) == "XMAS":
        res += 1

    # check top-left to bottom-right (diagonal down)
    if (
        row <= len(lines) - 4
        and col <= len(lines[0]) - 5
        and ("".join(lines[row + i][col + i] for i in range(4))) == "XMAS"
    ):
        res += 1

    # check bottom-left to top-right (diagonal up)
    if (
        row >= 3
        and col <= len(lines[0]) - 5
        and ("".join(lines[row - i][col + i] for i in range(4))) == "XMAS"
    ):
        res += 1

    # check top-right to bottom-left (diagonal down-back)
    if (
        row <= len(lines) - 4
        and col >= 3
        and ("".join(lines[row + i][col - i] for i in range(4))) == "XMAS"
    ):
        res += 1

    # check bottom-right to top-left (diagonal up-back)
    if (
        row >= 3
        and col >= 3
        and ("".join(lines[row - i][col - i] for i in range(4))) == "XMAS"
    ):
        res += 1

    return res


res = 0
for row in range(len(lines)):
    for col in range(len(lines[0]) - 1):
        if lines[row][col] == "X":
            res += is_root(row, col)

print(res)
