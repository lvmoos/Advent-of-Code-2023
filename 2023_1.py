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
    num_lst = ('1', '2', '3', '4', '5', '6', '7', '8', '9',
                'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    num_lst_rev = [s[::-1] for s in num_lst]
    rep_value = np.inf
    values = []

    for line in input:
        # First digit
        num_idx = [line.index(num) if num in line else rep_value for num in num_lst]
        digit_1 = np.argmin(num_idx)%9 +1

        # Second digit, reversed string
        line_rev = line[::-1]
        num_idx_rev = [line_rev.index(num) if num in line_rev else rep_value for num in num_lst_rev]
        digit_2 = np.argmin(num_idx_rev)%9 + 1

        values.append(int(str(digit_1) + str(digit_2)))

    return sum(values)

test_input = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
print(run_part2(test_input))
# %% Part 2
part2 = run_part2(input_lst)
print(f"{part2} is the answer to part 2.")