import numpy as np

def parse_red_tiles():
    tiles = np.genfromtxt('input.txt', delimiter=',')
    return tiles

def get_potential_corners(tiles):
    ul = [tiles[0, :]]
    dl = [tiles[0, :]]
    ur = [tiles[0, :]]
    dr = [tiles[0, :]]
    for i in range(1, tiles.shape[0]):
        tile = tiles[i, :]
        is_ul, is_dl, is_ur, is_dr = True, True, True, True
        dominated_ul_tiles, dominated_dl_tiles, dominated_ur_tiles, dominated_dr_tiles = [], [], [], []
        for j, ul_tile in enumerate(ul):
            if ul_tile[0] <= tile[0] and ul_tile[1] <= tile[1]:
               is_ul = False 
            elif ul_tile[0] >= tile[0] and ul_tile[1] >= tile[1]:
               dominated_ul_tiles.append(j)
        if is_ul:
            ul.append(tile)
        for j in reversed(sorted(dominated_ul_tiles)):
            del ul[j]
        for j, dl_tile in enumerate(dl):
            if dl_tile[0] <= tile[0] and dl_tile[1] >= tile[1]:
                is_dl = False
            elif dl_tile[0] >= tile[0] and dl_tile[1] <= tile[1]:
                dominated_dl_tiles.append(j)
        if is_dl:
            dl.append(tile)
        for j in reversed(sorted(dominated_dl_tiles)):
            del dl[j]
        for j, ur_tile in enumerate(ur):
            if ur_tile[0] >= tile[0] and ur_tile[1] <= tile[1]:
                is_ur = False
            elif ur_tile[0] <= tile[0] and ur_tile[1] >= tile[1]:
                dominated_ur_tiles.append(j)
        if is_ur:
            ur.append(tile)
        for j in reversed(sorted(dominated_ur_tiles)):
            del ur[j]
        for j, dr_tile in enumerate(dr):
            if dr_tile[0] >= tile[0] and dr_tile[1] >= tile[1]:
                is_dr = False
            elif dr_tile[0] <= tile[0] and dr_tile[1] <= tile[1]:
                dominated_dr_tiles.append(j)
        if is_dr:
            dr.append(tile)
        for j in reversed(sorted(dominated_dr_tiles)):
            del dr[j]
    return ul, dl, ur, dr

def get_areas(ul, dl, ur, dr):
    max_area = 0
    for ul_tile in ul:
        for dr_tile in dr:
            if dr_tile[0] >= ul_tile[0] and dr_tile[1] >= ul_tile[1]:
                area = ((dr_tile[0]-ul_tile[0])+1)*((dr_tile[1]-ul_tile[1])+1)
                max_area = max(max_area, area)
    for ur_tile in ur:
        for dl_tile in dl:
            if ur_tile[0] >= dl_tile[0] and ur_tile[1] <= dl_tile[1]:
                area = ((ur_tile[0]-dl_tile[0])+1)*((dl_tile[1]-ur_tile[1])+1)
                max_area = max(max_area, area)
    return max_area

tiles = parse_red_tiles()
ul, dl, ur, dr = get_potential_corners(tiles)
area = get_areas(ul, dl, ur, dr)
breakpoint()
