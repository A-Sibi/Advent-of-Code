with open('calendar_2023/data/day3.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

import re

gear_sum = 0
for i in range(len(lines)):
    j = 0
    while j < len(lines[0]):
        if lines[i][j].isdigit():
            sub_start, sub_end = re.search('\d+', lines[i][j::]).span()
            
            if i > 0: # not first row

                # top left corner
                if j > 0 and not lines[i-1][j-1].isalnum() and not lines[i-1][j-1] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # left
                if j > 0 and not lines[i][j-1].isalnum() and not lines[i][j-1] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # top right corner
                elif j + sub_end < len(lines[i]) - 1 and not lines[i-1][j+sub_end].isalnum() and not lines[i-1][j+sub_end] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # right
                elif j + sub_end < len(lines[i]) - 1 and not lines[i][j+sub_end].isalnum() and not lines[i][j+sub_end] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # top
                continue_flag = False
                for idx in range(j+sub_start, j+sub_end):
                    if not lines[i-1][idx].isalnum() and lines[i-1][idx] != '.':
                        gear_sum += int(lines[i][j+sub_start:j+sub_end])
                        j += sub_end - sub_start
                        continue_flag = True
                        break
                
                if continue_flag:
                    continue

                if i == len(lines) - 1:
                    j += sub_end - sub_start
                    continue
                
            
            
            if i < len(lines) - 1: # not last row

                # bottom left corner
                if j > 0 and not lines[i+1][j-1].isalnum() and not lines[i+1][j-1] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # bottom right corner
                elif j + sub_end < len(lines[i]) - 1 and not lines[i+1][j+sub_end].isalnum() and not lines[i+1][j+sub_end] == '.':
                    gear_sum += int(lines[i][j+sub_start:j+sub_end])
                    j += sub_end - sub_start
                    continue

                # bottom
                for idx in range(j+sub_start, j+sub_end):
                    if not lines[i+1][idx].isalnum() and lines[i+1][idx] != '.':
                        gear_sum += int(lines[i][j+sub_start:j+sub_end])
                        j += sub_end - sub_start
                        break
                else:
                    j += sub_end - sub_start


        else:
            j += 1

print(f"Part 1: {gear_sum}")

# part 2

from functools import reduce
from operator import mul

gear_product = 0

for i in range(len(lines)):
    j = 0
    while j < len(lines[0]):
        if lines[i][j] == '*':
            valid_nums = set()

            #if not first row
            if i > 0:

                # check top left
                if j > 0 and lines[i-1][j-1].isnumeric():
                    num_start = j - 1
                    num_end = j - 1
                    while num_start > 0 and lines[i-1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i-1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i-1][num_start:num_end+1]))
                    
                # check top middle
                if  lines[i-1][j].isnumeric():
                    num_start = j
                    num_end = j
                    while num_start > 0 and lines[i-1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i-1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i-1][num_start:num_end+1]))
                
                # check top right
                if  j < len(lines[i])-1 and lines[i-1][j+1].isnumeric():
                    num_start = j + 1
                    num_end = j + 1
                    while num_start > 0 and lines[i-1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i-1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i-1][num_start:num_end+1]))

            # check left
            if j > 0 and lines[i][j-1].isnumeric():
                num_start = j - 1
                num_end = j - 1
                while num_start > 0 and lines[i][num_start-1].isnumeric():
                    num_start -= 1
                valid_nums.add(int(lines[i][num_start:num_end+1]))

            # check right
            if j < len(lines[i])-1 and lines[i][j+1].isnumeric():
                num_start = j + 1
                num_end = j + 1
                while num_end < len(lines[i]) - 1 and lines[i][num_end+1].isnumeric():
                    num_end += 1
                valid_nums.add(int(lines[i][num_start:num_end+1]))

            #if not last row
            if i > 0:

                # check bottom left
                if j > 0 and lines[i+1][j-1].isnumeric():
                    num_start = j - 1
                    num_end = j - 1
                    while num_start > 0 and lines[i+1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i+1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i+1][num_start:num_end+1]))
                    
                # check bottom middle
                if  lines[i+1][j].isnumeric():
                    num_start = j
                    num_end = j
                    while num_start > 0 and lines[i+1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i+1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i+1][num_start:num_end+1]))
                
                # check bottom right
                if  j < len(lines[i])-1 and lines[i+1][j+1].isnumeric():
                    num_start = j + 1
                    num_end = j + 1
                    while num_start > 0 and lines[i+1][num_start-1].isnumeric():
                        num_start -= 1
                    while num_end < len(lines[i]) - 1 and lines[i+1][num_end+1].isnumeric():
                        num_end += 1
                    valid_nums.add(int(lines[i+1][num_start:num_end+1]))

            if len(valid_nums) == 2:
                gear_product += reduce(mul, valid_nums)
           
        j += 1

print(f"Part 2: {gear_product}")
