with open('calendar_2023/data/day7.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

from collections import defaultdict 

games = []

for line in lines:
    hand, bid = line.split()
    games.append((hand, int(bid)))

ranks = len(games)

card_values = {
    'A': 15,
    'K': 14,
    'Q': 13,
    'J': 12, # jack
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
card_values_joker = {
    'A': 15,
    'K': 14,
    'Q': 13,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1 # joker
}

# sort the games by rank

def hand_class(hand: str) -> int:
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

def hand_class_jokers(hand: str) -> int:
    occurances = defaultdict(int)
    for card in hand:
        occurances[card] += 1

    if 'J' not in occurances.keys():
        return hand_class(hand)
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
        

def compare_hands(hand1: str, hand2: str, jokers=True) -> bool:
    """
    Returns True, if first hand's class is of greater value, else False.
    Decider: higer value of card compared left to right.
    """
    if jokers:
        if hand_class_jokers(hand1) > hand_class_jokers(hand2):
            return True
        
        if hand_class_jokers(hand1) < hand_class_jokers(hand2):
            return False
        for card1, card2 in zip(hand1, hand2):
            if card_values_joker[card1] > card_values_joker[card2]:
                return True
            if card_values_joker[card1] < card_values_joker[card2]:
                return False
    else:
        if hand_class(hand1) > hand_class(hand2):
            return True
        
        if hand_class(hand1) < hand_class(hand2):
            return False
        for card1, card2 in zip(hand1, hand2):
            if card_values[card1] > card_values[card2]:
                return True
            if card_values[card1] < card_values[card2]:
                return False
        
    return False

# sorting
for i in range(ranks):
    for j in range(i, ranks):
        if compare_hands(games[j][0], games[i][0]):
            games[i], games[j] = games[j], games[i]

total_winnings = 0

for i, game in enumerate(games):
    total_winnings += game[1] * (ranks - i)

print(total_winnings)
