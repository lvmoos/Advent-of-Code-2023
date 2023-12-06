#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=6, year=2023)
print(input_lst)
test_lst = ['Time:      7  15   30',
    'Distance:  9  40  200']
#%% Parsing
def parser_part1(input_lst):
    times = [int(i) for i in input_lst[0].split(':')[1].lstrip().rstrip().split(' ') if i.isdigit()]
    records = [int(i) for i in input_lst[1].split(':')[1].lstrip().rstrip().split(' ') if i.isdigit()]
    return times, records

parser_part1(input_lst=test_lst)
# %% Part 1
def calculate_hold_times(race_time, record):
    # distance = hold_time * 1 ms/ms * (race_time - hold_time)
    # 0  < race_time * hold_time - hold_time**2 - prev_record
    # The +-1 and fllor/ceil are to accomodate whole numbers and rounding
    hold_time_min = int(np.floor((race_time - np.sqrt(race_time**2 - 4*record)) / 2) + 1)
    hold_time_max = int(np.ceil((race_time + np.sqrt(race_time**2 - 4*record)) / 2) - 1)
    possible_wins = hold_time_max - hold_time_min + 1

    return hold_time_min, hold_time_max, possible_wins

def run_part1(times, records):
    race_win_possibilities = []
    for time, record in zip(times, records):
        hold_time_min, hold_time_max, possible_wins = calculate_hold_times(race_time=time, record=record)
        race_win_possibilities.append(possible_wins)

    return np.prod(race_win_possibilities)

times, records = parser_part1(input_lst=input_lst)
run_part1(times, records)

# %% Part 2
def parser_part2(input_lst):
    times = int(input_lst[0].split(':')[1].replace(' ',''))
    records = int(input_lst[1].split(':')[1].replace(' ',''))
    return times, records

times, records = parser_part2(input_lst=input_lst)
run_part1([times], [records])