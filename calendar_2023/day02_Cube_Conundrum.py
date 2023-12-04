with open('calendar_2023/data/day2.txt') as file:
    lines = file.readlines()

# part 1

valid_ids = []

for line in lines:
    games, game_data = line.split(":")
    _, game_id = games.split()
    vals = [val.rstrip(";,") for val in game_data.split(" ")[1::]]

    valid = True
    for i in range(0, len(vals), 2):
        score, color = int(vals[i]), vals[i+1]
        if (score > 14) or \
           (score > 13 and color != "blue") or \
           (score > 12 and color not in ["green", "blue"]):
            valid = False
            break
    if valid:
        valid_ids.append(int(game_id))

print(f"Part 1: {sum(valid_ids)}")

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
        max_vals[color] = max(max_vals[color], value)
    powers_sum += max_vals["blue"] * max_vals["green"] * max_vals["red"]

print(f"Part 2: {powers_sum}")
