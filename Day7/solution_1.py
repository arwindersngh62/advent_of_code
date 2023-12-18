# types
# 1. Five of a kind
# 2. Four of a kind
# 3. Full house
# 4. Three of a kind
# 5. Two pairs
# 6. One Pair
# 7. High Card
from collections import Counter
from functools import cmp_to_key
def get_type(hand_string):
    count_dict = dict(Counter(hand_string))
    count_values = count_dict.values()
    if 5 in count_values:
        return 6 
    elif 4 in count_values:
        return 5
    elif 3 in count_values and 2 in count_values:
        return 4 
    elif 3 in count_values:
        return 3
    elif 2 in count_values:
        pair_count = Counter(list(count_values))
        if pair_count[2] == 2:
            return 2
        else:
            return 1     
    return 0

card_strenght = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}
def compare_cards(card1, card2):

    return card_strenght[card2] -card_strenght[card1]

        
def compare_high_card_order(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        compare_value = compare_cards(card1, card2)
        if compare_value == 0:
            continue
        return compare_value
    
                
        

def compare_two_hands(hand1, hand2):
    hand_one_type = get_type(hand1)
    hand_two_type = get_type(hand2)
    if hand_two_type==hand_one_type:
        return compare_high_card_order(hand1, hand2)
    return hand_two_type-hand_one_type

from pathlib import Path

data_file_path = Path(__file__).parent.resolve()/"data_test.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
all_dict = {}
for data in all_data:
    split_data= data.split(" ")
    all_dict[split_data[0]] = int(split_data[1])

all_hands = list(all_dict.keys())
sorted_hands = sorted(all_hands, key = cmp_to_key(compare_two_hands))
highest_rank = len(sorted_hands)
print(highest_rank)
bid_value = 0
print(sorted_hands)
for hand in sorted_hands:
    bid_value+=(highest_rank*all_dict[hand])
    highest_rank-=1
print(bid_value)