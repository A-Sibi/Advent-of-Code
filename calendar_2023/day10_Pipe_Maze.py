with open('calendar_2023/data/day10_example.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

dirs : dict[str, ((int, int), (int, int))] = {
    '|' : ((-1,0), (1,0)),
    '-' : ((0,-1), (0,1)),
    'L' : ((-1,0), (0,1)),
    'J' : ((-1,0), (0,-1)),
    '7' : ((0,-1), (1,0)),
    'F' : ((0,1), (1,0)),
    '.' : ((None, None), (None, None))
}

# find 'S'
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            start_i, start_j = i, j
            break

connected_positions = [(start_i, start_j)]

if lines[start_i-1][start_j] == '|' or \
    lines[start_i-1][start_j] == '7' or \
    lines[start_i-1][start_j] == 'F':
    next_i = start_i - 1
    next_j = start_j
elif lines[start_i][start_j+1] == '-' or \
    lines[start_i][start_j+1] == 'J' or \
    lines[start_i][start_j+1] == '7':
    next_i = start_i
    next_j = start_j + 1
elif lines[start_i+1][start_j] == '|' or \
    lines[start_i+1][start_j] == 'L' or \
    lines[start_i+1][start_j] == 'J':
    next_i = start_i + 1
    next_j = start_j
elif lines[start_i][start_j-1] == '-' or \
    lines[start_i][start_j-1] == 'L' or \
    lines[start_i][start_j-1] == 'F':
    next_i = start_i
    next_j = start_j - 1
else:
    print('Error')

while not (next_i == start_i and next_j == start_j):

    connected_positions.append((next_i, next_j))

    curr_i = next_i
    curr_j = next_j

    ways = dirs[lines[curr_i][curr_j]]

    if (len(connected_positions) > 2) and \
    ((curr_i + ways[0][0], curr_j + ways[0][1]) == connected_positions[0] or \
        (curr_i + ways[1][0], curr_j + ways[1][1]) == connected_positions[0]):
        break

    if (curr_i + ways[0][0], curr_j + ways[0][1]) in connected_positions:
        new_way = ways[1]
    else:
        new_way = ways[0]
    
    next_i = curr_i + new_way[0]
    next_j = curr_j + new_way[1]

# print(connected_positions)
print(f"Part 1 : {len(connected_positions) // 2}")

# part 2

matrix = [[0] * len(lines[0]) for _ in lines]

for i, j in connected_positions:
    matrix[i][j] = 1

def m_print(matrix):
    for row in matrix:
        print(row)

m_print(matrix)