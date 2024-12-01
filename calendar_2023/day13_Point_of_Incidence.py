import numpy as np
import math

with open('calendar_2023/data/day13.txt', 'r') as file:
    content = file.read().strip()

temp_arr = content.split('\n\n')
patterns = [np.array([[1 if char == '#' else 0 for char in line] for line in pattern.split('\n')]) for pattern in temp_arr]


def test_symerty(pattern : np.ndarray, horizontal = False) -> int:
    if horizontal:
        pattern = pattern.T
    as_first = []
    as_last = []

    for i in range(pattern.shape[0]-1):
        if np.array_equal(pattern[i], pattern[-1]):
            as_last.append(i)

    if as_last != []:
        as_last = [idx for idx in as_last if all(np.array_equal(pattern[idx + i], pattern[-1-i]) for i in range(idx, math.ceil((pattern.shape[0] - idx)/2)+1))]


    for i in range(pattern.shape[0]-1, 0, -1):
        if np.array_equal(pattern[0], pattern[i]):
            as_first.append(i)

    if as_first != []:
        as_first = [idx for idx in as_first if all(np.array_equal(pattern[i], pattern[idx - i]) for i in range(math.ceil(idx/2)+1))]


    if as_first != [] and as_last != []:
        print(f"No {'horizontal' if horizontal else 'vertical'} symetry detected.")
        return -1
    if len(as_first) > 1 or len(as_last) > 1:
        print(f"Multiple {'horizontal' if horizontal else 'vertical'} symetry detected.")
        return -1
    elif as_first != []:
        idx = (pattern.shape[0] - as_first[0]) // 2 + 1
        return idx
    elif as_last != []:
        idx = as_last[0] // 2 + 1
        return idx
    else:
        return -1


sum = 0
for p in patterns:
    print("Pattern:")
    if test_symerty(p, horizontal=True) != -1:
        sum +=  test_symerty(p, horizontal=True)
    elif test_symerty(p) != -1:
        sum += 100 *test_symerty(p)
    else:
        print(p)
        print("\nError, no symetry detected in previous pattern.\n\n-----\n")

print(f"Part 1: {sum}")
# > 18102