#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=1, year=2023)
print(input_lst)

input_test = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
#%% Part 1
def run_part1(input):
    values = []
    for line in input:
        line_digits = [i for i in line if i.isdigit()]
        values.append(int(line_digits[0] + line_digits[-1]))
    
    return sum(values)


part1 = run_part1(input_lst)
print(f"{part1} is the answer to part 1.")

#%% Part 2
def run_part2(input):
    num_lst = ('1', '2', '3', '4', '5', '6', '7', '8', '9' )
    str_lst = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    str_lst_rev = [s[::-1] for s in str_lst]

    rep_value = np.inf
    values = []
    for line in input:
        num_idx = [line.index(num) if num in line else rep_value for num in num_lst]
        str_idx = [line.index(num) if num in line else rep_value for num in str_lst]

        if min(num_idx)<min(str_idx):
            d1 = np.argmin(num_idx) +1
        else:
            d1 = np.argmin(str_idx) +1

        line_rev = line[::-1]
        num_idx = [line_rev.index(num) if num in line_rev else rep_value for num in num_lst]
        str_idx = [line_rev.index(num) if num in line_rev else rep_value for num in str_lst_rev]

        if min(num_idx)<min(str_idx):
            d2 = np.argmin(num_idx) + 1
        else:
            d2 = np.argmin(str_idx) + 1

        values.append(int(str(d1) + str(d2)))

    return sum(values)

test_input = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
run_part2(test_input)

# %% Part 2
part2 = run_part2(input_lst)
print(f"{part2} is the answer to part 2.")