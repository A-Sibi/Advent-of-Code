with open('calendar_2023/data/day4.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

def get_numbers(line:str) -> (set, set):
    _, vals = line.split(":")
    target_nums, nums = vals.split("|")
    target_nums = set(map(int, target_nums.split()))
    nums = set(map(int, nums.split()))
    return target_nums, nums

# part 1

wining_sum = 0

for line in lines:
    target_nums, nums = get_numbers(line)
    
    # score = 0

    # for num in nums:
    #     if num in target_nums:
    #         score = 1 if score == 0 else score * 2

    matches = sum(1 for num in nums if num in target_nums)
    score = 2 ** (matches - 1) if matches > 0 else 0   
    
    wining_sum += score

print(f"Part 1: {wining_sum}")

# part 2

amount_of_cards = [1] * len(lines)

for i, line in enumerate(lines):
    target_nums, nums = get_numbers(line)

    score = sum(num in target_nums for num in nums)

    for idx in range(1, score+1):
        try:
            amount_of_cards[i + idx] += amount_of_cards[i]
        except IndexError:
            pass

print(f"Part 2: {sum(amount_of_cards)}")

    
