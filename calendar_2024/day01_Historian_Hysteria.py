with open('calendar_2024/data/day1.txt') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

a, b = zip(*pairs)
a = sorted(a)
b = sorted(b)

total_diff = sum(abs(x-y) for x, y in zip(a,b))

print("Part 1 : " + str(total_diff))

#  Part 2
from collections import Counter

b_count = Counter(b)
sim_score = sum(x * b_count[x] for x in a)

print("Part 2 : " + str(sim_score))

