#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=10, year=2023)
print(input_lst)
# %% Test set
test_lst = ['.....',
'.S-7.',
'.|.|.',
'.L-J.',
'.....']

test_lst = ['..F7.',
'.FJ|.',
'SJ.L7',
'|F--J',
'LJ...']

def scan_valid_neighbours(coordinate, prev_coordinate, pipe_type):
    valid_connection_points = {
    '|': ((0,1), (0,-1)),
    '-': ((-1,0), (1,0)),
    'L': ((1,0), (0,-1)),
    'J': ((-1,0), (0,-1)),
    '7': ((-1,0), (0,1)),
    'F': ((1,0), (0,1)),
}
    potential_neigbors = valid_connection_points[pipe_type]
    x = coordinate[0]
    y = coordinate[1]
    x_diff = prev_coordinate[0] - x
    y_diff = prev_coordinate[1] - y
    neighbor_1 = potential_neigbors[0]
    neighbor_2 = potential_neigbors[1]
    # print(f"{prev_coordinate}->{coordinate} = {(x_diff, y_diff)}, {pipe_type}:{potential_neigbors}")
    if neighbor_1 == (x_diff, y_diff):
        next_coordinate =  (x + neighbor_2[0], y + neighbor_2[1])
    elif neighbor_2 == (x_diff, y_diff):
        next_coordinate =  (x + neighbor_1[0], y + neighbor_1[1])
    else:
        raise ValueError("Wrong input direction")
    
    return next_coordinate

    
#%%
def print_grid(grid):
    # Just for visuals
    for row in grid:
        print(row)

def assign_step_to_grid(grid, position, step):
    # Just for visuals
    x, y = position
    grid[y] = grid[y][:x] + str(step) + grid[y][x + 1:]
    return grid

def find_origin(grid):
    for y, row in enumerate(grid):
        x = row.find('S')
        if x != -1:
            return (x, y)

def find_valid_starting_direction(origin, grid):
    valid_neighbours= [(origin[0]+a, origin[1]+b) for a,b in ((0,1), (0,-1), (1,0), (-1,0))
                        if origin[0]+a>=0 and origin[1]+b>=0]
    for neighbor in valid_neighbours:
        try:
            pipe = grid[neighbor[1]][neighbor[0]]
            if pipe != '.':
                scan_valid_neighbours(coordinate=(neighbor[0], neighbor[1]),
                                                        prev_coordinate=origin,
                                                        pipe_type=pipe)
                valid_neighbor = neighbor
        except ValueError:
            print(f'{pipe_type} not a valid directional neigbor')
    return valid_neighbor

grid = test_lst.copy()
grid_steps = grid.copy()
origin = find_origin(grid=grid)
current_position = find_valid_starting_direction(origin, grid)
prev_position = origin
step_count = 1

while current_position != origin:
    x = current_position[0]
    y = current_position[1]
    pipe_type = grid[y][x]
    next_position = scan_valid_neighbours(coordinate=current_position,
                                          prev_coordinate=prev_position,
                                          pipe_type=pipe_type)
    
    # grid_steps = assign_step_to_grid(grid=grid_steps, position=current_position, step='*')
    # print(f'\nStep: {step_count}')
    # print_grid(grid_steps)
    prev_position = current_position
    current_position = next_position
    step_count += 1
    

print('Part 1:', int(step_count / 2))

    