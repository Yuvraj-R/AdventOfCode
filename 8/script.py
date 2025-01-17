### PART 1 ###
from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.readlines()

dim_y, dim_x = len(lines), len(lines[0].strip())
antennas = defaultdict(list)
for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if char != ".":
            antennas[char].append((i, j))


def is_valid_coordinate(coordinate):
    return (0 <= coordinate[0] < dim_y) and (0 <= coordinate[1] < dim_x)


def generate_antinodes(coord1, coord2):
    dy, dx = coord1[1] - coord2[1], coord1[0] - coord2[0]
    possible_antinodes = [
        (coord1[0]+dx, coord1[1]+dy),
        (coord2[0]-dx, coord2[1]-dy)
    ]
    result = []
    for c in possible_antinodes:
        if is_valid_coordinate(c):
            result.append(c)

    return result


antinode_coordinates = set()
for antenna, coordinates in antennas.items():
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            antinode_coordinates.update(
                generate_antinodes(coordinates[i], coordinates[j])
            )

print(len(antinode_coordinates))
