### PART 1 ###

from math import gcd
from collections import deque
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

solutions = {}
total_tokens = 0
for i, (b_x, b_y) in enumerate(Bs):
    prize_x, prize_y = Prizes[i]
    a_x, a_y = As[i]

    iteration = 100
    while iteration >= 0:
        x_x2 = (prize_x - (b_x * iteration)) / a_x
        y_x2 = (prize_y - (b_y * iteration)) / a_y

        if x_x2.is_integer() and x_x2 == y_x2:
            cost = (3 * int(x_x2) + iteration)
            total_tokens += cost
            solutions[Prizes[i]] = cost
            break

        iteration -= 1

print(total_tokens)

### PART 2 ###

offset = 10000000000000
new_total_tokens = 0

# Define the button costs
cost_A = 3
cost_B = 1

for i, (b_x, b_y) in enumerate(Bs):

    # Adjust the prize coordinates by the offset
    prize_x, prize_y = Prizes[i]
    prize_x += offset
    prize_y += offset
    a_x, a_y = As[i]

    # Compute the determinant of the matrix
    det = a_x * b_y - a_y * b_x
    if det == 0:
        continue  # No unique solution exists

    # Compute the numerators for a and b using Cramer's Rule
    a_num = b_y * prize_x - b_x * prize_y
    b_num = a_x * prize_y - a_y * prize_x

    # Check if the solutions are integers
    if a_num % det != 0 or b_num % det != 0:
        continue  # Solutions are not integers

    # Compute the actual number of button presses
    a = a_num // det
    b = b_num // det

    # Ensure that the number of presses is non-negative
    if a < 0 or b < 0:
        continue  # Negative button presses are invalid

    # Calculate the cost for this machine
    cost = (cost_A * a) + (cost_B * b)
    new_total_tokens += cost

print(new_total_tokens)
