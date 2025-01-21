### PART 1 ###

import re

with open("input.txt", "r") as file:
    As, Bs, Prizes = [], [], []
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line[0] == "B":
            match = re.search(r"Button (A|B): X\+(\d+), Y\+(\d+)", line)
            button, x, y = match.groups()
            As.append((int(x), int(y))) if button == "A" else Bs.append(
                (int(x), int(y)))
        else:
            match = re.search(r"Prize: X=(\d+), Y=(\d+)", line)
            x, y = match.groups()
            Prizes.append((int(x), int(y)))

total_tokens = 0
for i, (b_x, b_y) in enumerate(Bs):
    prize_x, prize_y = Prizes[i]
    a_x, a_y = As[i]

    iteration = 100
    while iteration >= 0:
        x_x2 = (prize_x - (b_x * iteration)) / a_x
        y_x2 = (prize_y - (b_y * iteration)) / a_y

        if x_x2.is_integer() and x_x2 == y_x2:
            total_tokens += (3 * int(x_x2) + iteration)
            break

        iteration -= 1

print(total_tokens)
