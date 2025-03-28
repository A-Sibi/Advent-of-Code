import copy
with open('calendar_2024/data/day6.txt') as file:
    M = file.read().splitlines()
    for i in range(len(M)):
        M[i] = [ch for ch in M[i]]

M1 = copy.deepcopy(M)
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
dir = 0
# guard = [-1,-1]

for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == '^':
            start_guard = [i,j]
            M[i][j] = '.'
            break

guard = copy.deepcopy(start_guard)
while True:
    M[guard[0]][guard[1]] = 'X'
    new_row = guard[0] + dirs[dir][0]
    new_col = guard[1] + dirs[dir][1]
    if not(0 <= new_row < len(M) and 0 <= new_col < len(M[0])):
        break
    elif M[new_row][new_col] == '#':
        dir = (dir + 1) % 4
        continue
    else:
        guard[0] = new_row
        guard[1] = new_col


print(sum(1 for row in M for el in row if el == 'X'))

# part 2
c2 = 0

# bruteforce
for i in range(len(M1)):
    for j in range(len(M1[0])):
        if M1[i][j] == '#':
            continue
        M1[i][j] = '#'

        guard = copy.deepcopy(start_guard)
        dir = 0
        states = set() # i,j,dir

        while True:
            if (guard[0], guard[1], dir) in states:
                c2 += 1
                break
            else:
                states.add((guard[0], guard[1], dir))
            new_row = guard[0] + dirs[dir][0]
            new_col = guard[1] + dirs[dir][1]
            if not(0 <= new_row < len(M1) and 0 <= new_col < len(M1[0])):
                break
            elif M1[new_row][new_col] == '#':
                dir = (dir + 1) % 4
                continue
            else:
                guard[0] = new_row
                guard[1] = new_col

        M1[i][j] = '.'

print(c2)