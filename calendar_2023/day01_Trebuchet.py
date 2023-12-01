with open('2023/data/day1.txt') as file:
    lines = file.readlines()

# lines = ['two1nine']

# sum = 0
# for line in lines:
#     val = ''
#     for ch in line:
#         if ch.isnumeric():
#             val += ch
#             break
#     line_rev = line[::-1]
#     for ch in line_rev:
#         if ch.isnumeric():
#             val += ch
#             break
#     sum += int(val)

# print(sum)

# part 2

reg_nums = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

sum = 0
for line in lines:
    val = ''
    for i in range(0,len(line)):
        if line[i].isnumeric():
            val += line[i]
            break
        elif line[i:i+3] in reg_nums.keys():
            val += reg_nums[line[i:i+3]]
            break
        elif line[i:i+4] in reg_nums.keys():
            val += reg_nums[line[i:i+4]]
            break
        elif line[i:i+5] in reg_nums.keys():
            val += reg_nums[line[i:i+5]]
            break

    # line_rev = line[::-1]

    for i in range(len(line)-1,-1,-1):
        if line[i].isnumeric():
            val += line[i]
            break
        elif line[i-2:i+1] in reg_nums.keys():
            val += reg_nums[line[i-2:i+1]]
            break
        elif line[i-3:i+1] in reg_nums.keys():
            val += reg_nums[line[i-3:i+1]]
            break
        elif line[i-4:i+1] in reg_nums.keys():
            val += reg_nums[line[i-4:i+1]]
            break

    sum += int(val)

print(sum)

