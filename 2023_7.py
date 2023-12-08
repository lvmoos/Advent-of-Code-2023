#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=7, year=2023)
print(input_lst)
test_lst = ['32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483']

# %%Part1

class CamelHand:
    def __init__(self, hand_bid_str, use_joker=False):
        self.hand_numbers = None
        self.card_values = None
        self.hand_rank = None
        self.hand_value = None
        self.card_ranking = None
        
        self.joker = use_joker
        self.hand, self.bid = hand_bid_str.split(' ')
        self.bid = int(self.bid)

    def assign_hand_rank(self):
        self.hand_rank = str(5 + max([self.hand.count(card) for card in set(self.hand)])  - len(set(self.hand)))

    def assign_card_value(self):
        if self.joker:
            self.card_ranking = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
        else:
            self.card_ranking = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]

        # Unique monotonic value based on cards in hand
        self.card_values = ''.join([str(self.card_ranking.index(card) + 12) for card in list(self.hand)])

    def assign_hand_value(self):
        self.assign_card_value()
        if self.joker and ('J' in self.hand):
            self.replace_joker()
        self.assign_hand_rank()
        self.hand_value = int(str(self.hand_rank) + str(self.card_values))
    
    def replace_joker(self):
        most_frequent_card = max(self.hand, key=lambda x: str(self.hand.count(x))+str(self.card_ranking.index(x)+12))
        most_high_card = max(self.hand, key=lambda x: self.card_ranking.index(x))

        if most_frequent_card != 'J':
                replace_card = most_frequent_card
        else:
            is_five_of_a_kind = self.hand_rank == 9
            if is_five_of_a_kind:
                replace_card = self.card_ranking[-1]             
            else:
                replace_card = most_high_card

        # Replace Joker
        self.hand = self.hand.replace('J', replace_card)


# %% Part 1 test
def run_through_hands(hands, use_joker=False):
    hand_values = []
    hand_bids = []

    for hand in hands:
        h = CamelHand(hand_bid_str=hand, use_joker=use_joker)
        h.assign_hand_value()
        hand_values.append(h.hand_value)
        hand_bids.append(h.bid)

    ranked_index = np.argsort(hand_values)
    winnings = [rank*hand_bids[idx] for rank, idx in enumerate(ranked_index,1)]
    return sum(winnings)

print("Part 1:", run_through_hands(hands=input_lst, use_joker=False))
print("Part 2:", run_through_hands(hands=input_lst, use_joker=True))