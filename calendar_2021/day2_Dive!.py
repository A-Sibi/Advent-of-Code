with open('data/day2.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
# print(lines)
for i in range(len(lines)):
    lines[i]= lines[i].split()
horizontal = 0
depth = 0
aim = 0
for i in range(len(lines)):
    komanda = lines[i][0]
    vrednost = int(lines[i][1])
    if lines[i][0] == 'forward':
        horizontal += vrednost
        depth += aim * vrednost
    if lines[i][0] == 'down':
        # depth += vrednost
        aim += vrednost
    if lines[i][0] == 'up':
        # depth -= vrednost
        aim -= vrednost
print(horizontal*depth)
# 1593951287 not right