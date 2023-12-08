with open('calendar_2023/data/day8.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

directions = lines[0]
paths: dict[str, (str, str)] = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

# part 1

curr_loc = 'AAA'
step_count = 0
i = 0

while curr_loc != 'ZZZ':
    curr_loc = paths[curr_loc][0 if directions[i] == 'L' else 1]
    step_count += 1
    i = (i+1) % len(directions) # list cycling

print(f"Part 1: {step_count}")

# part 2

import math
from functools import reduce

starting_locs = [key for key in paths if key.endswith('A')]
steps_to_Z = []

for loc in starting_locs:
    step_count = 0
    i = 0
    while not loc.endswith('Z'):

        loc = paths[loc][0 if directions[i] == 'L' else 1]
        step_count += 1

        i = (i+1) % len(directions)

    steps_to_Z.append(step_count)

lcm = reduce(lambda x,y: (x*y) // math.gcd(x,y), steps_to_Z) # lcm(list[int])

print(f"Part 2: {lcm}")