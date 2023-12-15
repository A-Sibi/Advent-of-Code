with open('calendar_2023/data/day15.txt') as file:
    data = file.readline().rstrip().split(",")

def hash_val(label : str) -> int:
    seq_sum = 0
    for c in label:
        seq_sum = 17 * (seq_sum + ord(c)) % 256
    return seq_sum

print(f"Part 1: {sum(hash_val(lens) for lens in data)}")

# part 2

import re

boxes = [[] for _ in range(256)]

for lens in data:
    label, foc_len = re.split("-|=", lens)
    box_id = hash_val(label)

    if lens[-1] == "-":
        for i, (len_id, _) in enumerate(boxes[box_id]):
            if len_id == label:
                boxes[box_id].pop(i)
                break
    else:
        for i, (len_id, val) in enumerate(boxes[box_id]):
            if len_id == label:
                boxes[box_id][i][1] = foc_len
                break
        else:
            boxes[box_id].append([label, foc_len])


focus_sum = 0

for i, box in enumerate(boxes, start=1):
    for j, (_, fl) in enumerate(box, start=1):
        focus_sum += i * j * int(fl)

print(f"Part 2: {focus_sum}")