
#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=4, year=2023)
print(input_lst)
input_test = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
# %% Parsing
def parser(input_lst):
    input_parsed = [(
        set(card.replace('  ', ' ').split(': ')[1].replace('  ', ' ').split(' | ')[0].replace('  ', ' ').split(' ')),
        set(card.replace('  ', ' ').split(': ')[1].replace('  ', ' ').split(' | ')[1].replace('  ', ' ').split(' ')))
        for card in input_lst]

    return input_parsed


input_parsed = parser(input_lst=input_test)

#%% Part 1
input_parsed = parser(input_lst=input_lst)
points = 0

for num, card in enumerate(input_parsed):
    winning_numbers = card[0].intersection(card[1])
    card_points = 2 ** (len(winning_numbers) - 1) if len(winning_numbers) >= 1 else 0
    points += card_points

print(f"Part 1:", points)

# %% Part 2
def parser_part2(input_lst):
    input_parsed = {num:(
        set(card.replace('  ', ' ').split(': ')[1].replace('  ', ' ').split(' | ')[0].replace('  ', ' ').split(' ')),
        set(card.replace('  ', ' ').split(': ')[1].replace('  ', ' ').split(' | ')[1].replace('  ', ' ').split(' ')))
        for num, card in enumerate(input_lst,1)}

    return input_parsed

new_hand = parser_part2(input_lst=input_test)
#%%
def run_through_hand(hand, orginal_hand):
    won_cards = []
    for card in hand:
        winning_numbers = len(orginal_hand[card][0].intersection(orginal_hand[card][1]))
        if winning_numbers:
            for won_card in range(card + 1, card + 1 + winning_numbers):
                won_cards.append(won_card)

    return won_cards

original_hand = parser_part2(input_lst=input_lst)
new_hand = [card for card in original_hand]
hand_count = len(new_hand)
while new_hand:
    new_hand = run_through_hand(hand=new_hand, orginal_hand=original_hand)
    hand_count += len(new_hand)

print(f"Part 2:", hand_count)
# %% Part 2 - Better implementation
def check_hand(card, orginal_hand):
    won_cards = []
    winning_numbers = len(orginal_hand[card][0].intersection(orginal_hand[card][1]))
    if winning_numbers:
        for won_card in range(card + 1, card + 1 + winning_numbers):
            won_cards.append(won_card)

    return won_cards

def assign_card_winnings(original_hand):
    hand_winning_map = {} 
    hand_win_count = {card:0 for card in original_hand}
    starting_hand = [card for card in original_hand]
    for card in starting_hand:
        hand_win_count = {card:0 for card in original_hand}
        won_cards = check_hand(card=card, orginal_hand=original_hand)
        for won_card in won_cards:
            hand_win_count[won_card] += 1
    
        hand_winning_map[card] = hand_win_count

    return hand_winning_map


original_hand = parser_part2(input_lst=input_lst)
card_win_map = assign_card_winnings(original_hand)

accumulated_cards = {card:1 for card in original_hand}
starting_hand = {card:1 for card in original_hand}
for card_played in accumulated_cards:
    for card, win_count in card_win_map[card_played].items():
        accumulated_cards[card] += win_count*accumulated_cards[card_played]

cards_gained = sum(accumulated_cards.values())
print(f"Part 2:", cards_gained)