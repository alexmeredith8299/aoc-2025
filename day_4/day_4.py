import os
import numpy as np

def parse_rolls():
    with open('input.txt', 'r') as file:
        grid = []
        for line in file.readlines():
            row_raw = line.strip()
            row = []
            for c in row_raw:
                if c == '.':
                    row.append(0)
                else:
                    row.append(1)
            grid.append(row)
    grid = np.array(grid)
    return grid

def shift_grid_up(grid):
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[0]):
        new_grid[i-1, :] = grid[i, :]
    return new_grid

def shift_grid_down(grid):
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[0]):
        new_grid[i, :] = grid[i-1, :]
    return new_grid

def shift_grid_left(grid):
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[1]):
        new_grid[:, i-1] = grid[:, i]
    return new_grid

def shift_grid_right(grid):
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[1]):
        new_grid[:, i] = grid[:, i-1]
    return new_grid

def part_1(grid):
    lgrid = shift_grid_left(grid)
    rgrid = shift_grid_right(grid)
    ugrid = shift_grid_up(grid)
    dgrid = shift_grid_down(grid)
    urgrid = shift_grid_up(rgrid)
    ulgrid = shift_grid_up(lgrid)
    drgrid = shift_grid_down(rgrid)
    dlgrid = shift_grid_down(lgrid)
    blockers = lgrid + rgrid + ugrid + dgrid + urgrid + ulgrid + drgrid + dlgrid
    good_cells = np.where(np.logical_and(blockers < 4, grid == 1))
    return good_cells[0].shape[0]

def remove_paper(grid):
    lgrid = shift_grid_left(grid)
    rgrid = shift_grid_right(grid)
    ugrid = shift_grid_up(grid)
    dgrid = shift_grid_down(grid)
    urgrid = shift_grid_up(rgrid)
    ulgrid = shift_grid_up(lgrid)
    drgrid = shift_grid_down(rgrid)
    dlgrid = shift_grid_down(lgrid)
    blockers = lgrid + rgrid + ugrid + dgrid + urgrid + ulgrid + drgrid + dlgrid
    removed_rolls = np.where(np.logical_and(blockers < 4, grid == 1))
    n_removed = removed_rolls[0].shape[0]
    for r, c in zip(removed_rolls[0], removed_rolls[1]):
        grid[r, c] = 0
    return grid, n_removed

def part_2(grid):
    n_removed = np.inf
    n_removed_total = 0
    while n_removed > 0:
        grid, n_removed = remove_paper(grid)
        n_removed_total += n_removed
    return n_removed_total

grid = parse_rolls()
ans_1 = part_1(grid)
ans_2 = part_2(grid)
print(ans_2)
