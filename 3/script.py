import re

### PART 1 ###

with open("input.txt", "r") as file:
    matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", file.read())

print(sum(int(match[0]) * int(match[1]) for match in matches))

### PART 2 ###
