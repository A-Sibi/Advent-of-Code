with open('data/day1.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]
counter = 0
for i in range(len(lines[:-3])):
    if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]:
        counter += 1
print(counter)
