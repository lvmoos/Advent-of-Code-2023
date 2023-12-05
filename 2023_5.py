#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=5, year=2023)
print(input_lst)
# %% Test
test_str = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def range_mapper(input_str):
    mapper_tmp = {map.split(':')[0]: map.split(':')[1].lstrip().rstrip().split('\n') for map in input_str.split('\n\n')}
    range_map = {}
    for mapping, entries in mapper_tmp.items():
        range_map[mapping] = []
        for entry in entries:
            entry_values = tuple([int(e) for e in entry.split(' ')])
            range_map[mapping].append(entry_values)

    seeds = range_map['seeds'][0]
    del range_map['seeds']

    return seeds, range_map

def assign_new_path(location, location_map):
    src_start = location_map[1]
    src_end = location_map[1] + location_map[2] - 1
    trg_start = location_map[0]
    location_shift = trg_start - src_start

    if (location >= src_start) and (location <= src_end):
        new_location = location + location_shift
    else:
        new_location = None

    return new_location

def part1(seeds, path_mapper):
    min_location = np.inf
    for seed in seeds:
        current_path = seed
        for location_ranges in path_mapper.values():
            for location_range in location_ranges:
                new_path = assign_new_path(location=current_path, location_map=location_range)
                if new_path:
                    break
            if not new_path:
                new_path = current_path

            current_path = new_path

        if current_path < min_location:
            min_location = current_path

    return min_location

seeds, range_map = range_mapper(input_str=test_str)
part1(seeds=seeds, path_mapper=range_map)

#%% Part 2
def expand_seed_range(seed_ranges):
    for start, length in zip(seed_ranges[::2], seed_ranges[1::2]):
        for seed in range(start,start+length):
            yield seed

seeds_ranges, range_map = range_mapper(input_str=input_str)
seeds_part2 = expand_seed_range(seed_ranges=seeds_ranges)

part1(seeds=seeds_part2, path_mapper=range_map)