import os

def parse_graph():
    with open('input.txt', 'r') as file:
        device_map = {}
        for line in file.readlines():
            line = line.strip()
            line = line.split(':')
            device_key = line[0]
            device_vals = tuple(line[1].strip().split(' '))
            device_map[device_key] = device_vals
        return device_map

def get_n_paths(loc, n_paths, device_map):
    if device_map[loc] == ('out',):
        return n_paths
    if loc == 'out':
        return n_paths
    next_locs = device_map[loc]
    total_paths = 0
    for next_loc in next_locs:
        total_paths += n_paths*get_n_paths(next_loc, n_paths, device_map)
    return total_paths

def get_n_paths_to_exits(loc, n_paths, device_map, exits, memoized):
    if loc in memoized:
        return memoized[loc]
    for j, exit_opt in enumerate(exits):
        if loc == exit_opt:
            exit_paths = [0 for i in range(len(exits))]
            exit_paths[j] = n_paths
            memo_paths = [0 for i in range(len(exits))]
            memo_paths[j] = 1
            memoized[loc] = memo_paths
            return exit_paths
    next_locs = device_map[loc]
    total_paths = [0 for i in range(len(exits))]
    for next_loc in next_locs:
        next_paths = get_n_paths_to_exits(next_loc, 1, device_map, exits, memoized)
        memoized[next_loc] = next_paths
        for i in range(len(next_paths)):
            total_paths[i] += next_paths[i]*n_paths
    return total_paths

def get_descendants(loc, device_map, loc_children):
    children = device_map[loc]
    for child in children:
        if child != 'out' and child not in loc_children:
            desc = get_descendants(child, device_map, loc_children)
            loc_children = loc_children.union(desc)
            loc_children.add(child)
    return loc_children

def part_1(device_map):
    return get_n_paths('you', 1, device_map)

def part_2(device_map):
    dac_to_fft, dac_to_out = get_n_paths_to_exits('dac', 1, device_map, ['fft', 'out'], {})
    fft_to_dac, fft_to_out = get_n_paths_to_exits('fft', 1, device_map, ['dac', 'out'], {})
    svr_to_fft, svr_to_out = get_n_paths_to_exits('svr', 1, device_map, ['fft', 'out'], {})
    return svr_to_fft*fft_to_dac*dac_to_out

device_map = parse_graph()
ans_1 = part_1(device_map)
ans_2 = part_2(device_map)
breakpoint()

