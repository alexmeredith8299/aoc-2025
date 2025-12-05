import os
import numpy as np

def load_ranges_and_ingredients():
    with open('input.txt', 'r') as file:
        ranges = []
        ingredients = []
        for line in file.readlines():
            line = line.strip()
            if '-' in line:
                vals = line.split('-')
                ranges.append((int(vals[0]), int(vals[1])))
            elif line =='':
                pass
            else:
                ingredients.append(int(line))
    return ranges, ingredients

def part_1(ranges, ingredients):
    ingredients = np.array(ingredients)
    fresh = np.zeros_like(ingredients)
    for (range_start, range_end) in ranges:
        fresh_range = np.logical_and(ingredients <= range_end, ingredients >= range_start)
        fresh += fresh_range
    return len(np.where(fresh > 0)[0])

def add_range(new_range, new_ranges):
    insert_start_ind = 0
    insert_end_ind = 0
    for i in range(len(new_ranges)):
        if new_ranges[i][0] < new_range[0]:
            insert_start_ind = i+1
        if new_ranges[i][1] < new_range[1]:
            insert_end_ind = i + 1

    # Need to adjust range
    if insert_start_ind > 0:
        new_range_start = max(new_range[0], new_ranges[insert_start_ind-1][1]+1)
    else:
        new_range_start = new_range[0]
    if insert_end_ind < len(new_ranges):
        new_range_end = min(new_range[1], new_ranges[insert_end_ind][0]-1)
    else:
        new_range_end = new_range[1]

    # If an existing range falls within this range, delete
    for i in range(insert_start_ind, insert_end_ind):
        del new_ranges[i]

    # If this range doesn't fall within existing range, add
    if new_range_end >= new_range_start:
        new_ranges.insert(insert_start_ind, (new_range_start, new_range_end))

def part_2(ranges):
    new_ranges = [ranges[0]]
    for (range_start, range_end) in ranges[1:]:
        add_range((range_start, range_end), new_ranges)
    n_fresh = 0
    for (range_start, range_end) in new_ranges:
        n_fresh += (range_end-range_start)+1
    return n_fresh

ranges, ingredients = load_ranges_and_ingredients()
ans_1 = part_1(ranges, ingredients)
ans_2 = part_2(ranges)

