#%%
import numpy as np

import utilities.helper_functions as utils

#%%
input_lst, text = utils.aoc_input_fetch(day=1, year=2019)
print(input_lst)
#%%
module_mass = utils.list_str_to_num(input_lst, 'int')
#%%
def get_fuel_req(mass):
    limit = 3*(0 + 2 + 1)
    return  [int(m/3)-2 for m in mass if m >= limit]

fuel_total = get_fuel_req(mass=module_mass)
print(f"Part 1: {sum(fuel_total)}")

# %% Part 2
def calculate_total_fuel_iteratively(module_mass):
    fuel = get_fuel_req(mass=module_mass)
    total_fuel = 0
    while fuel:
        total_fuel += sum(fuel)
        fuel = get_fuel_req(mass=fuel)

    return total_fuel

print(f"Part 2: {calculate_total_fuel_iteratively(module_mass)}")
#%% REcursive fuel
def calculate_total_fuel_recursively(mass):
    fuel = get_fuel_req(mass)
    #print(f"{mass}->{fuel}")
    if not fuel:
        #print('last_call - 0')
        return 0
    
    total_fuel = sum(fuel)
    additional_fuel = calculate_total_fuel_recursively(mass=fuel)
    #print(f"{total_fuel} + {additional_fuel} = {total_fuel+additional_fuel}")
    return total_fuel + additional_fuel

print("Part 2:" ,calculate_total_fuel_recursively(mass=module_mass))
# %%
utils.timer_function(calculate_total_fuel_iteratively, module_mass, n_run=1000)

# %%
utils.timer_function(calculate_total_fuel_recursively, module_mass, n_run=1000)
# %%
