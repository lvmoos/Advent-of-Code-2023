#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=3, year=2019)
print(input_lst)

#%% Parsing
paths = [path.split(',') for path in input_str.split('\n')]

#%%
class GridPath:
    def __init__(self, movements_raw, movement_type):
        self.movement_type = movement_type
        self.movements_raw = movements_raw
        self.movements = self._split_movement()
        self.movement_map = self._set_movement_axis()
        self.path = []
        self.path_nodes = None

    def _split_movement(self):
        self.movements = [(move[0], int(move[1:])) for move in self.movements_raw]
        return self.movements 


    def _set_movement_axis(self):
        if self.movement_type=='UPLR':
            self.movement_map = {'U':(0,1), 'D':(0,-1),'L':(-1,0),'R':(1,0)}
        elif self.movement_type=='NSEW':
            self.movement_map = {'N':(0,1), 'S':(0,-1),'E':(-1,0),'W':(1,0)}
        else:
            raise ValueError(f"'movement_type' needs to be 'UPLR', or 'NSEW'")
        return self.movement_map
    
    def get_path(self):
        moves = [(np.array(self.movement_map[move[0]]), move[1]) for move in self.movements]
        position = np.array((0,0))
        self.path = [tuple(position)]

        for move in moves:
            ax = move[0]
            steps = move[1]
            for s in range(1,steps+1):
                position = position + ax
                self.path.append(tuple(position))

        return self.path
    
    def path_node_count(self):
        return len(self.path)
    
    def get_unique_path_nodes(self):
        self.path_nodes = set(self.path)
        return self.path_nodes 

# %% Test 1
# test_path1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# test_path2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
test_path1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
test_path2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

path_test1 = GridPath(movements_raw=test_path1, movement_type='UPLR')
path_test1.get_path()
nodes_path1 = path_test1.get_unique_path_nodes()

path_test2 = GridPath(movements_raw=test_path2, movement_type='UPLR')
path_test2.get_path()
nodes_path2 = path_test2.get_unique_path_nodes()

crossings = nodes_path1.intersection(nodes_path2)
crossings.remove((0,0))
min_distance = min([abs(c[0])+abs(c[1]) for c in crossings])
print(f"{min_distance} is the distance to the closests crossing")

#%% Part 1
movement1 = paths[0]
movement2 = paths[1]
path1 = GridPath(movements_raw=movement1, movement_type='UPLR')
path1.get_path()
nodes_path1 = path1.get_unique_path_nodes()

path2 = GridPath(movements_raw=movement2, movement_type='UPLR')
path2.get_path()
nodes_path2 = path2.get_unique_path_nodes()

crossings = nodes_path1.intersection(nodes_path2)
crossings.remove((0,0))
min_distance = min([abs(c[0])+abs(c[1]) for c in crossings])
print(f"{min_distance} is the distance to the closests crossing")

# %% Part 2
cross_signal_distances = []
for cross in crossings:
    path1_signal_distance = path1.path.index(cross)
    path2_signal_distance = path2.path.index(cross)
    total_signal_distance = path1_signal_distance + path2_signal_distance
    cross_signal_distances.append(total_signal_distance)

print(f"{min(cross_signal_distances)} is the smallest signal distance crossing")
