with open('calendar_2023/data/day9.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

histories = [[int(val) for val in line.split()] for line in lines]

extrapolated_sum = 0

for history in histories:
    curr_row = [el for el in history]
    rows = [history]
    # create rows
    while not all(val == 0 for val in curr_row):
        new_row = []
        for i in range(len(rows[-1])-1):
            new_row.append(rows[-1][i+1] - rows[-1][i])
        rows.append(new_row)
        curr_row = [el for el in new_row]
    # extrapolate
    rows[len(rows)-1].append(0)
    for i in range(len(rows) - 2, -1, -1): # [-2:0:-1]
        rows[i].append(rows[i][-1] + rows[i+1][-1])
    
    extrapolated_sum += rows[0][-1]

print(f"Part 1: {extrapolated_sum}")

backwards_sum = 0

for history in histories:
    curr_row = [el for el in history]
    rows = [history]
    # create rows
    while not all(val == 0 for val in curr_row):
        new_row = []
        for i in range(len(rows[-1])-1):
            new_row.append(rows[-1][i+1] - rows[-1][i])
        rows.append(new_row)
        curr_row = [el for el in new_row]
    # extrapolate
    rows[len(rows)-1].insert(0,0)
    for i in range(len(rows) - 2, -1, -1): # [-2:0:-1]
        rows[i].insert(0, rows[i][0] - rows[i+1][0])
    backwards_sum += rows[0][0]

print(f"Part 2: {backwards_sum}")