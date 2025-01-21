import re
from collections import defaultdict

robots = []
AREA_WIDTH = 101
AREA_HEIGHT = 103

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        m = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        x, y, vx, vy = m.group(1), m.group(2), m.group(3), m.group(4)
        robots.append(((int(x), int(y)), (int(vx), int(vy))))


def process(robot):
    """ Simulates one robot's motion for one second """
    (x, y), (vx, vy) = robot
    new_position = ((x + vx) % AREA_WIDTH, (y + vy) % AREA_HEIGHT)
    return new_position


for _ in range(100):
    for i, robot in enumerate(robots):
        robots[i] = (process(robots[i]), robots[i][1])

robot_positions = defaultdict(int)
for robot in robots:
    robot_positions[robot[0]] += 1

x_middle = AREA_WIDTH // 2
y_middle = AREA_HEIGHT // 2
quadrant_ranges = [
    (range(0, x_middle), range(0, y_middle)),
    (range(x_middle+1, AREA_WIDTH), range(0, y_middle)),
    (range(0, x_middle), range(y_middle+1, AREA_HEIGHT)),
    (range(x_middle+1, AREA_WIDTH), range(y_middle+1, AREA_HEIGHT))
]
product = 1

for x_range, y_range in quadrant_ranges:
    count = 0
    for x in x_range:
        for y in y_range:
            count += robot_positions[(x, y)]
    if count > 0:
        product *= count

print(product)

### PART 2 ###
robots = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        m = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        x, y, vx, vy = m.group(1), m.group(2), m.group(3), m.group(4)
        robots.append(((int(x), int(y)), (int(vx), int(vy))))


def print_robots(file):
    for y in range(AREA_HEIGHT):
        line = ''.join(str(robot_positions[(x, y)]) if robot_positions[(
            x, y)] > 0 else '.' for x in range(AREA_WIDTH))
        file.write(line + '\n')


def check():
    for y in range(AREA_HEIGHT):
        consecutive = 0
        for x in range(AREA_WIDTH):
            if robot_positions[(x, y)] > 0:
                consecutive += 1
                if consecutive >= 10:
                    return True
            else:
                consecutive = 0
    return False


robot_positions = defaultdict(int)
for robot in robots:
    robot_positions[robot[0]] += 1

with open("output.txt", "w") as out_file:
    for j in range(10403):
        if check():
            out_file.write(f"---------- {j} ----------\n")
            print_robots(out_file)
        for i, robot in enumerate(robots):
            old_position = robot[0]
            new_position = process(robot)
            robots[i] = (new_position, robot[1])
            robot_positions[old_position] -= 1
            robot_positions[new_position] += 1
