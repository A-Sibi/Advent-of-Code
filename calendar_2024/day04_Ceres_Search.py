with open('calendar_2024/data/day4.txt') as file:
    M = file.read().splitlines()

# Part 1

count = 0
for r in range(len(M)):
    for c in range(len(M[0])):
        if M[r][c] != "X": continue
        for dr in [-1, 0, 1]: # directions
            for dc in [-1, 0, 1]:
                if dr == dc == 0: continue
                if not (0 <= r + 3 * dr < len(M) and 0 <= c + 3 * dc < len(M[0])): continue
                if M[r + dr][c + dc] == "M" and M[r + 2 * dr][c + 2 * dc] == "A" and M[r + 3 * dr][c + 3 * dc] == "S":
                    count += 1
print(count)

# Part 2

count = 0
for r in range(1, len(M)-1):
    for c in range(1, len(M[0])-1):
        if M[r][c] != "A": continue
        corners = [M[r-1][c-1], M[r-1][c+1], M[r+1][c+1], M[r+1][c-1]] # clockwise order of corners
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            count += 1
print(count)
