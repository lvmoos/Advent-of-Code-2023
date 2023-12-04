#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=3, year=2023)
print(input_lst)

input_test = ['467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']
test_str = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
# %% Parsing
symbols = [sym for sym in np.unique(list(input_str)) if sym not in ('0', '1', '2',
       '3', '4', '5', '6', '7', '8', '9','.','\n')]

# %% Part 1
i = 0
str_len = len(test_str)
row_len = test_str.index('\n')
n_rows = str_len/row_len
while i<str_len:
    char = test_str[i]

    if char.isdigit():
        num_len = 1
        while test_str[i+num_len].isdigit():
            num_len += 1
        num = test_str[i:i+num_len]
        row_prev = (i//row_len - 1) if i > row_len else 0
        row_next = (i//row_len + 1) if i > row_len else 0
        i_left = i - 1 if i > 0 else i
        i_right = i + num_len if i + num_len < str_len else i
        i_top_min = row_prev + i_left
        i_top_max = row_prev + i_right
        i_bot_min = row_next + i_left
        i_bot_max = row_next + i_right
        print(num)
        print(i_left, i_right, i_top_min, i_top_max, i_bot_min, i_bot_max)
        i += num_len
    i+=1