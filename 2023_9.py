#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=9, year=2023)
print(input_lst)
#%% Parser
def parser(input_lst):

    return [list(map(int, row.split(' '))) for row in input_lst]

# %% Recursion
def get_recursive_difference(row):
    row_diff = np.diff(row)
    if all(row_diff == 0):
        return 0
    else:
        diff = get_recursive_difference(row=row_diff)
        # return row_diff[-1] + diff    # Part 1
        return row_diff[0] - diff       # Part 2

def run_row_predictor(row):
    diff = get_recursive_difference(row=row)
    # prediction = row[-1] + diff   # Part 1
    prediction = row[0] - diff      # Part 2
    return prediction

test_lst = ['0 3 6 9 12 15',
'1 3 6 10 15 21',
'10 13 16 21 30 45']

rows = parser(input_lst)
predictions = []
for row in rows:
    prediction = run_row_predictor(row=row)
    predictions.append(prediction)

print("Part 1:", sum(predictions))

#%%

    