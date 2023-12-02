with open('2023/data/day1.txt') as file:
    lines = file.readlines()

# part 1

valid_ids = []

for line in lines:
    games, game_data = line.split(":")
    _, game_id = games.split()
    vals = game_data.split(" ")[1::]
    vals = [val.rstrip(";.") for val in vals]

    valid = True
    for i in range(0, len(vals), 2):
        score, color = int(vals[i], vals[i+1])
        if (score > 14) or \
           (score > 13 and color != "blue") or \
           (score > 12 and color not in ["green", "blue"]):
            valid = False
            break
    if valid:
        valid_ids.append(int(game_id))

print(sum(valid_ids))

# part 2

from collections import defaultdict 
powers_sum = 0

for line in lines:
    max_vals = defaultdict(int)

    games, game_data = line.split(":")
    vals = game_data.split(" ")[1::]

    for i in range(0, len(vals), 2):
        color = vals[i+1].rstrip(";,\n")
        value = int(vals[i])
        max_vals = max(max_vals[color], value)
    powers_sum += max["blue"] * max["green"] * max["red"]

print(powers_sum)
