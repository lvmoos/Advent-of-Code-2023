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

# Part 2
def run_part2(input):
    values = []
    number_map = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9' }

test_input = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
run_part2(test_input)