with open('calendar_2023/data/day5.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

# part 1

seeds = [int(seed) for seed in lines[0].split(":")[1].split()]

# 50 98 2    input
# 98 99 -48  map
# 50 51 48   reverse map

mapings, reverse_mappings = [], []

i = 3
while i < len(lines):
    this_mapping, this_reverse = [], []
    while i < len(lines) and lines[i] != '':
        temp_val = tuple(map(int, lines[i].split()))
        this_mapping.append((temp_val[1], temp_val[1] + temp_val[2] - 1, temp_val[0] - temp_val[1]))
        this_reverse.append((temp_val[0], temp_val[0] + temp_val[2] - 1, temp_val[1] - temp_val[0]))
        i += 1
    mapings.append(this_mapping)
    reverse_mappings.append(this_reverse)
    i += 2 # skip empty and description line

reverse_mappings = reverse_mappings[::-1]

seeds_mapped = []

for x in seeds:
    for mapping in mapings:
        for a, b, c in mapping:
            if x >= a and x <= b:
                x += c
                break
    seeds_mapped.append(x)

print(f"Part 1: {min(seeds_mapped)}")

# part 2

seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0,len(seeds),2)]

min_location = 0
terminate_flag = False

while not terminate_flag:
    
    # if min_location % 100_000 == 0:
    #     print(min_location) # just for checking the progress, algorithm is very slow

    x = min_location
    for mapping in reverse_mappings:
        for a,b,c in mapping:
            if x >= a and x <= b:
                x += c
                break
    
    for down_lim, up_lim in seed_ranges:
        if x >= down_lim and x <= up_lim:
            terminate_flag = True
            break
    
    # if any(down_lim <= x <= up_lim for down_lim, up_lim in seed_ranges): # better written

    min_location += 1

print(f"Part 2: {min_location-1}")
