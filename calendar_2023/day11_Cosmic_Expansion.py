with open('calendar_2023/data/day11.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

import numpy as np

galaxy = np.array([[1 if c == '#' else 0 for c in line] for line in lines], dtype="int8")

empty_columns = np.all(galaxy == 0, axis=0)
empty_rows = np.all(galaxy == 0, axis = 1)

row_multiplier = [0] * galaxy.shape[0]
column_multiplier = [0] * galaxy.shape[1]

for i in range(len(row_multiplier)):
    if empty_rows[i]:
        for j in range(i, len(row_multiplier)):
            row_multiplier[j] += 1

for i in range(len(column_multiplier)):
    if empty_columns[i]:
        for j in range(i, len(column_multiplier)):
            column_multiplier[j] += 1

indexes = np.where(galaxy == 1)
stars = [list(pair) for pair in zip(indexes[0], indexes[1])]
# print(stars)
# print(row_multiplier)
# print(column_multiplier)
MULTIPLIER = 1_000_000

for i in range(len(stars)):
    stars[i][0] += (MULTIPLIER - 1) * row_multiplier[stars[i][0]]
    stars[i][1] += (MULTIPLIER - 1) * column_multiplier[stars[i][1]]

dist_sum = 0

for i in range(len(stars)):
    for j in range(i, len(stars)):
        dist_sum += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])

print(f"Part 2: {dist_sum}")
# > 82000210


# bruteforce part 1

# universe expansion

# temp_glx = []

# for column, duplicate in zip(galaxy.T, empty_columns):
#     temp_glx.append(column)
#     if duplicate:
#         temp_glx.append(column)

# galaxy = np.array(temp_glx).T

# temp_glx = []

# for row, duplicate in zip(galaxy, empty_rows):
#     temp_glx.append(row)
#     if duplicate:
#         temp_glx.append(row)

# galaxy = np.array(temp_glx)

# # print(galaxy)

# # paths between galaxies

# indexes = np.where(galaxy == 1)
# stars = list(zip(indexes[0], indexes[1]))
# print(stars)

# dist_sum = 0

# for i in range(len(stars)):
#     for j in range(i, len(stars)):
#         dist_sum += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])

# print(f"Part 1: {dist_sum}")

