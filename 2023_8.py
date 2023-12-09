#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=8, year=2023)
print(input_lst)
test_lst = ['RL',
'',
'AAA = (BBB, CCC)',
'BBB = (DDD, EEE)',
'CCC = (ZZZ, GGG)',
'DDD = (DDD, DDD)',
'EEE = (EEE, EEE)',
'GGG = (GGG, GGG)',
'ZZZ = (ZZZ, ZZZ)']

test_lst2 = ['LLR',
'',
'AAA = (BBB, BBB)',
'BBB = (AAA, ZZZ)',
'ZZZ = (ZZZ, ZZZ)']
test_lst3 =['LR',
'',
'11A = (11B, XXX)',
'11B = (XXX, 11Z)',
'11Z = (11B, XXX)',
'22A = (22B, XXX)',
'22B = (22C, 22C)',
'22C = (22Z, 22Z)',
'22Z = (22B, 22B)',
'XXX = (XXX, XXX)']
# %% Parsing
def parser(input_lst):
    directions = list(map(int, list(input_lst[0].replace('L', '0').replace('R', '1'))))
    nodes = {}
    for node_path in input_lst[2:]:
        tmp = node_path.split(' = ')
        node = tmp[0]
        paths = tuple([path for path in tmp[1].replace('(','').replace(')','').split(', ')])
        nodes[node] = paths

    return directions, nodes


directions, nodes = parser(input_lst=test_lst)

# %% Part 1
def take_step(nodes, step, current_node):
    next_node = nodes[current_node][step]
    return next_node

def run_through_direction(directions, nodes, current_node, end_node):
    step_count = 0
    for step in directions:
        current_node = take_step(nodes, step, current_node)
        step_count += 1

        if current_node == end_node:
            break

    return current_node, step_count

directions, nodes = parser(input_lst=input_lst)

end_node = 'ZZZ'
current_node = 'AAA'
steps_count = 0
while current_node != end_node:
    current_node, steps = run_through_direction(directions, nodes, current_node, end_node)
    steps_count += steps

print("Part 1:", steps_count)

#%% Part 2
def get_start_and_finish_nodes(nodes):
    start_nodes = [node for node in nodes if node[2]=='A']
    end_nodes = [node for node in nodes if node[2]=='Z']

    return start_nodes, end_nodes

def take_step(nodes, step, current_node):
    next_node = nodes[current_node][step]
    return next_node


directions, nodes = parser(input_lst=input_lst)
start_nodes, end_nodes = get_start_and_finish_nodes(nodes)
current_nodes = start_nodes
step_count = 0
at_endpoints = False
cycles = {}
completed_cycles = {}
while len(completed_cycles)<len(start_nodes):
    for step in directions:
        next_nodes = [take_step(nodes, step, node) for node in current_nodes]
        current_nodes = next_nodes
        step_count += 1

        check_nodes = [(idx, node) for idx, node in enumerate(current_nodes) if node in end_nodes and idx not in completed_cycles]
        for start_node, end_node in check_nodes:
            if start_node in cycles:
                prev_entry = cycles[start_node]
                prev_end_node = prev_entry[0]
                prev_count = prev_entry[1]
                cycles[start_node] = (end_node, step_count - prev_count)

                if (end_node == prev_end_node) & (prev_count == (step_count - prev_count)):
                    completed_cycles[start_node] = (end_node, step_count - prev_count)
            else:
                cycles[start_node] = (end_node, step_count)
    
check_factors = sorted([cycles[1] for cycles in completed_cycles.values()])
n = check_factors[0]
n_adder = n
for idx, entry in enumerate(check_factors[:-2]):
    next_entry = check_factors[idx+1]
    while True:
        if n%next_entry == 0:
            print(f'Least common multiple between {entry} and {next_entry}:', n)
            n_adder = n
            break
        n += n_adder

    



