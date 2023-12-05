#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=2, year=2023)
print(input_lst)

input_test = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

# %% Parsing
def parser(input):
    games = [game.split(':')[1].split(';') for game in input]
    games_dct=[]

    for game in games:
        games_sets = []

        for sets in game:
            set_dct = {}
            set = sets[1:].replace(',','').split(' ')
            set_dct[set[1]]=int(set[0])
            if len(set)>=4:
                set_dct[set[3]]=int(set[2])
            if len(set)==6:
                set_dct[set[5]]=int(set[4])
            games_sets.append(set_dct)
        
        games_dct.append(games_sets)
    return games_dct

# %% Part 1
def run_part1(input):
    max_red = 12
    max_green = 13
    max_blue = 14
    games_success = []
    for game_num, game in enumerate(input, 1):
        game_failed = False
        for game_sets in game:
            reds = game_sets.get('red', 0)
            greens = game_sets.get('green', 0)
            blues = game_sets.get('blue', 0)
            if (reds > max_red) or (greens > max_green) or (blues> max_blue):
                game_failed = True
                break 
            
        if not game_failed:
            games_success.append(game_num)

    return sum(games_success)

input_test = parser(input_test)
input_1 = parser(input_lst)
print(f"Part 1:", run_part1(input_1))
#%% Part 2
# %% Part 1
def run_part2(input):
    game_power = []
    for game in input:
        max_red = 0
        max_green = 0
        max_blue = 0
            
        for game_sets in game:
            reds = game_sets.get('red', 0)
            greens = game_sets.get('green', 0)
            blues = game_sets.get('blue', 0)

            if reds > max_red:
                max_red = reds
            if greens > max_green:
                max_green = greens
            if blues > max_blue:
                max_blue = blues
        
        game_power.append(max_red*max_green*max_blue)

    return sum(game_power)

print(f"Part 2:", run_part2(input_1))