from collections import defaultdict
page_rules = defaultdict(list)
sum = 0
with open('calendar_2024/data/day5.txt') as file:
    for line in file:
        if line == "\n":
            break
        l, r = map(int,line.split("|"))
        page_rules[l].append(r)
    for line in file:
        valid = True
        arr = [int(x) for x in line.split(",")]
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] in page_rules.keys() and arr[i] in page_rules[arr[j]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:

            sum += int(arr[len(arr)//2])
print(sum)

# Part 2

sum = 0
with open('calendar_2024/data/day5.txt') as file:
    for line in file:
        if line == "\n":
            break
        l, r = map(int,line.split("|"))
        page_rules[l].append(r)
    for line in file:
        valid = True
        arr = [int(x) for x in line.split(",")]
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] in page_rules.keys() and arr[i] in page_rules[arr[j]]:
                    valid = False
                    arr[i], arr[j] = arr[j], arr[i]
        if not valid:

            sum += int(arr[len(arr)//2])
# < 5784
print(sum)