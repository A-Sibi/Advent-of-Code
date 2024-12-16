from collections import defaultdict
page_rules = defaultdict(list)
no_of_correct = 0
with open('calendar_2024/data/day5.txt') as file:
    for line in file:
        if line == "\n":
            break
        l, r = map(int,line.split("|"))
        page_rules[l].append(r)
    for line in file:
        valid = True
        arr = line.split(",")
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if j in page_rules.keys() and i in page_rules[j]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            no_of_correct += 1
print(no_of_correct)