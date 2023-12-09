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
def range_mapper_part2(input_str):
    mapper_tmp = {map.split(':')[0]: map.split(':')[1].lstrip().rstrip().split('\n') for map in input_str.split('\n\n')}
    range_map = {}
    for mapping, entries in mapper_tmp.items():
        if mapping == 'seeds':
            seed_ranges = []
            seed_lst = [int(e) for e in entries[0].split(' ')]
            for i in range(len(seed_lst))[::2]:
                seed_ranges.append((seed_lst[i], seed_lst[i] + seed_lst[i+1]))
            seed_ranges = sorted(seed_ranges, key=lambda x: x[0])
        else:
            src_ranges = []
            trg_ranges = []
            for entry in entries:
                entry_lst = [int(e) for e in entry.split(' ')]
                trg_start, src_start = entry_lst[0:2]
                range_len = entry_lst[2] - 1

                src_ranges.append((src_start, src_start + range_len))
                trg_ranges.append((trg_start, trg_start + range_len))

            src_ranges, trg_ranges = zip(*sorted(zip(src_ranges, trg_ranges), key=lambda x: x[0][0]))
            src_ranges, trg_ranges = list(src_ranges), list(trg_ranges)
            
            # Assign missing ranges
            min_src = min([i[0] for i in src_ranges])
            max_src = max([i[1] for i in src_ranges])
            min_range = [(-np.inf, min_src - 1)]

            max_range = [(max_src + 1, np.inf)]
            src_ranges = min_range + src_ranges + max_range
            trg_ranges = min_range + trg_ranges + max_range
            src_ranges = src_ranges
            range_map[mapping] = {'src':src_ranges, 'trg':trg_ranges}

    return seed_ranges, range_map

def range_splitter(inc_ranges, src_trg_range_map):
    out_ranges = []
    for inc_range in inc_ranges:
        inc_min_val = inc_range[0]
        inc_max_val = inc_range[1]
        for src_range, trg_range in zip(src_trg_range_map['src'],src_trg_range_map['trg']):
            src_bucket_min = src_range[0]
            src_bucket_max = src_range[1]
            range_transform = trg_range[0] - src_range[0] if src_bucket_min != -np.inf else trg_range[1] - src_range[1]

            min_val_in_bucket = (inc_min_val >= src_bucket_min) & (inc_min_val <= src_bucket_max)
            max_val_in_bucket = (inc_max_val >= src_bucket_min) & (inc_max_val <= src_bucket_max)

            if (not min_val_in_bucket) & max_val_in_bucket:
                out_ranges.append((src_bucket_min + range_transform, inc_max_val + range_transform))
                # print(f'{inc_range} max only in {src_range}: {trg_range} -> ', out_ranges)
            elif min_val_in_bucket & max_val_in_bucket:
                out_ranges.append((inc_min_val + range_transform, inc_max_val + range_transform))
                # print(f'{inc_range} both in {src_range}: {trg_range} -> ', out_ranges)
            elif min_val_in_bucket & (not max_val_in_bucket):
                out_ranges.append((inc_min_val + range_transform, src_bucket_max + range_transform))
                # print(f'{inc_range} min only in {src_range}: {trg_range} -> ', out_ranges)

    return out_ranges

# Find all ranges
seed_ranges, range_maps = range_mapper_part2(input_str)
inc_range = seed_ranges
for src_trg_mapper in range_maps:
    print(src_trg_mapper)
    inc_range = range_splitter(inc_ranges=inc_range, src_trg_range_map=range_maps[src_trg_mapper])

print("Part 2:", min(inc_range, key=lambda x: x[0])[0])

