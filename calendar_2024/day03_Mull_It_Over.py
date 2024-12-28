import re
with open('calendar_2024/data/day3.txt') as file:
    t = file.read()

l = re.findall( "mul\(\d{1,3},\d{1,3}\)",t)
sum = 0
for el in l:
    nums = re.findall("\d+", el)
    sum += int(nums[0]) * int(nums[1])
print(sum)

# part 2

l2 = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",t)

is_on = True
s2 = 0
for el in l2:
    if "don't" in el:
        is_on = False
    elif "do" in el:
        is_on = True
    elif is_on:
        nums = re.findall("\d+", el)
        s2 += int(nums[0]) * int(nums[1])

print(s2)
