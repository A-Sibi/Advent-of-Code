with open('calendar_2023/data/day7.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

from functools import cmp_to_key
from collections import defaultdict 

games = [(line.split()[0], int(line.split()[1])) for line in lines]

card_values = {
    'A': 15, 'K': 14, 'Q': 13, 'J': 12, 'T': 10,
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
    '4': 4, '3': 3, '2': 2
}
card_values_joker = dict(card_values, J=1)

def hand_class(hand: str, jokers=True) -> int:
    """
    Class 6: Five of a kind
    Class 5: Four of a kind
    Class 4: Full house (3+2)
    Class 3: Three of a kind
    Class 2: Two pairs
    Class 1: One pair
    Class 0: High card
    """
    occurances = defaultdict(int)
    for card in hand:
        occurances[card] += 1

    if jokers and 'J' in occurances.keys():
        j_num = occurances.pop('J')

        if j_num == 5:
            return 6
        if max(val for val in occurances.values()) + j_num == 5:
            return 6
        if max(val for val in occurances.values()) + j_num == 4:
            return 5
        if max(val for val in occurances.values()) + j_num == 3:
            if sum(1 for val in occurances.values() if val == 2) == 2:
                return 4
            return 3
        # no return 2: impossible to have 2 pairs with joker(s) in hand
        if max(val for val in occurances.values()) + j_num == 2:
            return 1
        
        return 0
    else:
        if any(val == 5 for val in occurances.values()):
            return 6
        if any(val == 4 for val in occurances.values()):
            return 5
        if any(val == 3 for val in occurances.values()):
            if any(val == 2 for val in occurances.values()):
                return 4
            return 3
        if sum(1 for val in occurances.values() if val == 2) == 2:
            return 2
        if any(val == 2 for val in occurances.values()):
            return 1
        return 0


def compare_hands(hand1: str, hand2: str, jokers=True) -> bool:
    class1, class2 = hand_class(hand1, jokers), hand_class(hand2, jokers)
    if class1 != class2:
        return class1 > class2

    values = card_values_joker if jokers else card_values

    for card1, card2 in zip(hand1, hand2):
        if values[card1] != values[card2]:
            return values[card1] > values[card2]

    return False


# Timsort O(n log n)
games.sort(key=cmp_to_key(lambda x, y: -1 if compare_hands(x[0], y[0], False) else 1))
total_winnings = sum(bid * (len(games) - i) for i, (_, bid) in enumerate(games))
print(f"Part 1: {total_winnings}")

games.sort(key=cmp_to_key(lambda x, y: -1 if compare_hands(x[0], y[0]) else 1))
total_winnings = sum(bid * (len(games) - i) for i, (_, bid) in enumerate(games))
print(f"Part 2: {total_winnings}")
