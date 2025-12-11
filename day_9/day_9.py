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

def get_corner_types(tiles):
    ul, ur, dl, dr = np.zeros(tiles.shape[0]), np.zeros(tiles.shape[0]), np.zeros(tiles.shape[0]), np.zeros(tiles.shape[0])
    for i in range(tiles.shape[0]):
        tile = tiles[i, :]
        if i == 0:
            neighbor_0 = tiles[-1, :]
        else:
            neighbor_0 = tiles[i-1, :]
        if i == tiles.shape[0]-1:
            neighbor_1 = tiles[0, :]
        else:
            neighbor_1 = tiles[i+1, :]
        if tile[0] > neighbor_0[0]:
            if tile[1] < neighbor_1[1]:
                # Right, then down
                ur[i] = 1
            else:
                # Right, then up
                dl[i] = 1
                ul[i] = 1
                ur[i] = 1
        if tile[0] < neighbor_0[0]:
            if tile[1] > neighbor_1[1]:
                # Left, then up
                dl[i] = 1
            else:
                # Left, then down
                ur[i] = 1
                dr[i] = 1
                dl[i] = 1
        if tile[1] > neighbor_0[1]:
            if tile[0] > neighbor_1[0]:
                # Down, then left
                dr[i] = 1 
            else:
                # Down, then right
                dr[i] = 1 
                ur[i] = 1 
                ul[i] = 1 
        if tile[1] < neighbor_0[1]:
            if tile[0] < neighbor_1[0]:
                # Up, then right
                ul[i] = 1
            else:
                # Up, then left
                dl[i] = 1
                dr[i] = 1
                ul[i] = 1
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

def get_areas_part_2(ul_all, dl_all, ur_all, dr_all, tiles):
    max_area = 0
    max_ul, max_dl, max_dr, max_ur = None, None, None, None
    for ul in tiles[np.where(ul_all==1)]:
        dr_ind = np.where(np.logical_and(np.logical_and(tiles[:, 1] >= ul[1], tiles[:, 0] >= ul[0]), dr_all==1))
        dr_tiles = tiles[dr_ind[0], :]
        for dr in dr_tiles:
            ur_ind = np.where(np.logical_and(np.logical_and(tiles[:, 1] <= ul[1], tiles[:, 0] >= dr[0]), ur_all==1))
            dl_ind = np.where(np.logical_and(np.logical_and(tiles[:, 1] >= dr[1], tiles[:, 0] <= ul[0]), dl_all==1))
            if dl_ind[0].shape[0] > 0 and ur_ind[0].shape[0] > 0:
                height = dr[1]-ul[1] + 1
                width = dr[0]-ul[0] + 1
                max_area = max(height*width, max_area)
                if height*width==max_area:
                    max_ul = ul
                    max_dr = dr
                    max_ur = ur_ind
                    max_dl = dl_ind

    """
    for ur in tiles:
        dl_ind = np.where(np.logical_and(tiles[:, 1] >= ur[1], tiles[:, 0] <= ur[0]))
        dl_tiles = tiles[dl_ind[0], :]
        for dl in dl_tiles:
            ul_ind = np.where(np.logical_and(tiles[:, 1] <= ur[1], tiles[:, 0] <= dl[0]))
            dr_ind = np.where(np.logical_and(tiles[:, 1] >= dl[1], tiles[:, 0] >= ur[0]))
            if ul_ind[0].shape[0] > 0 and dr_ind[0].shape[0] > 0:
                height = dl[1]-ur[1]+1
                width=ur[0]-dl[0] + 1
                max_area = max(height*width, max_area)
    """
    breakpoint()
    return max_area
    

tiles = parse_red_tiles()
ul, dl, ur, dr = get_potential_corners(tiles)
#area = get_areas(ul, dl, ur, dr)
ul_all, dl_all, ur_all, dr_all = get_corner_types(tiles)
breakpoint()
area = get_areas_part_2(ul_all, dl_all, ur_all, dr_all, tiles)
breakpoint()
