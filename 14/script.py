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
