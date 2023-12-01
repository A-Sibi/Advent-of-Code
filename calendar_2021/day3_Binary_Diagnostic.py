with open('data/day3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
linesO = lines
i = 0
while len(linesO) != 1:
    zeros = 0
    ones = 0
    for line in linesO:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1
    newlines = []
    if zeros <= ones :
        for line in linesO:
            if line[i] == '0':
                newlines.append(line)
    else:
        for line in linesO:
            if line[i] == '1':
                newlines.append(line)
    linesO = newlines
    i += 1
    print(linesO)
print(linesO)
a = 2783
b = 1353
print(2783*1353)