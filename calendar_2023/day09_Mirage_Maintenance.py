with open('calendar_2023/data/day9.txt') as file:
    histories = [[int(val) for val in line.split()] for line in file]


def get_rows(history):
    rows = [history]
    while any(val != 0 for val in rows[-1]):
        new_row = [rows[-1][i + 1] - rows[-1][i] for i in range(len(rows[-1]) - 1)]
        rows.append(new_row)
    return rows

def extrapolate(rows, front=True):
    for i in range(len(rows) - 2, -1, -1):
        next_val = rows[i][-1] + rows[i + 1][-1] if front else rows[i][0] - rows[i + 1][0]
        rows[i].append(next_val) if front else rows[i].insert(0, next_val)
    return rows[0][-1] if front else rows[0][0]

extrapolated_sum = sum(extrapolate(get_rows(history)) for history in histories)
backwards_sum = sum(extrapolate(get_rows(history), False) for history in histories)

print(f"Part 1: {extrapolated_sum}")
print(f"Part 2: {backwards_sum}")
