#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=3, year=2023)
print(input_lst)

input_test = [
'467..114..',
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
def run_part1(input_str):
    valid_numbers = []
    i = 0
    row_len = input_str.index('\n')
    input_str = input_str.replace('\n', '')
    str_len = len(input_str)

    # Run through flat string
    while i < str_len:
        char = input_str[i]

        if char.isdigit():
            # Scan whole number
            num_len = 1
            while input_str[i+num_len].isdigit():
                num_len += 1
            num = input_str[i:i+num_len]

            i_left = i - 1
            i_right = i + num_len
            idx_left = [i_left] if i_left >= 0 else []
            idx_right = [i_right] if i_right < str_len else []

            indicies = idx_left \
                + idx_right \
                + [i for i in range(i_left - row_len, i_right - row_len + 1) if i >= 0] \
                + [i for i in range(i_left + row_len, i_right + row_len + 1) if i < str_len]

            boundaries = [input_str[i] for i in indicies]
            # Check for symbols around number
            for sym in symbols:
                if sym in boundaries:
                    valid_numbers.append(int(num))
            i += num_len
        i+=1
    return sum(valid_numbers)

run_part1(input_str=test_str)
print("Part 1:", run_part1(input_str=input_str))

#%% Part 2
def run_part2(input_str):
    gears = {} 
    i = 0
    row_len = input_str.index('\n')
    input_str = input_str.replace('\n', '')
    str_len = len(input_str)

    while i < str_len:
        char = input_str[i]

        if char.isdigit():
            # Scan whole number
            num_len = 1
            while input_str[i+num_len].isdigit():
                num_len += 1
            num = input_str[i:i+num_len]

            i_left = i - 1
            i_right = i + num_len
            idx_left = [i_left] if i_left >= 0 else []
            idx_right = [i_right] if i_right < str_len else []

            indicies = idx_left \
                + idx_right \
                + [i for i in range(i_left - row_len, i_right - row_len + 1) if i >= 0] \
                + [i for i in range(i_left + row_len, i_right + row_len + 1) if i < str_len]

            # Check for symbols around number
            for gear in [i for i in indicies if input_str[i] == '*']:
                if gear in gears:
                    gears[gear] += [int(num)]
                else:
                    gears[gear] = [int(num)]
            i += num_len
        i += 1

    gear_ratios = sum([gear_values[0]*gear_values[1] for gear_values in gears.values() if len(gear_values)==2])
    return gears,gear_ratios

run_part2(input_str=test_str)
gears,gear_ratios = run_part2(input_str=input_str)
print("Part 2:", gear_ratios)