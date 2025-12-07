import os
import numpy as np

def parse_tree():
    with open('input.txt', 'r') as file:
        lines = []
        for line in file.readlines():
            raw_line = list(line.strip())
            proc_line = []
            for elt in raw_line:
                if elt == '.':
                    proc_line.append(0)
                else:
                    proc_line.append(1)
            lines.append(proc_line)
        return np.array(lines)

def process_lines(top_line, bottom_line):
    continued_lines = np.zeros_like(top_line)
    continued_lines[np.where(np.logical_and(top_line==1, bottom_line==0))] = 1
    split_lines = np.zeros_like(top_line)
    split_lines[np.where(np.logical_and(top_line==1, bottom_line==1))] = 1
    n_splits = np.sum(split_lines)
    l_splits = np.zeros_like(split_lines)
    l_splits[:-1] = split_lines[1:]
    r_splits = np.zeros_like(split_lines)
    r_splits[1:] = split_lines[:-1]
    all_lines = np.zeros_like(top_line)
    all_lines[np.where(np.logical_or(np.logical_or(r_splits==1, l_splits==1), continued_lines==1))] = 1
    return n_splits, all_lines

def process_lines_quantum(top_line, bottom_line):
    continued_lines = np.zeros_like(top_line)
    continued_lines[np.where(np.logical_and(top_line>=1, bottom_line==0))] = 1
    continued_lines = continued_lines*top_line
    split_lines = np.zeros_like(top_line)
    split_lines[np.where(np.logical_and(top_line>=1, bottom_line==1))] = 1
    split_lines = split_lines*top_line
    l_splits = np.zeros_like(split_lines)
    l_splits[:-1] = split_lines[1:]
    r_splits = np.zeros_like(split_lines)
    r_splits[1:] = split_lines[:-1]
    all_lines = r_splits + l_splits + continued_lines
    return all_lines


def part_1(lines):
    split = 0
    current_line = lines[0, :]
    for i in range(1, lines.shape[0]):
        n_splits, current_line = process_lines(current_line, lines[i, :])
        split += n_splits
    return split 

def part_2(lines):
    current_line = lines[0, :]
    for i in range(1, lines.shape[0]):
        current_line = process_lines_quantum(current_line, lines[i, :])
    return np.sum(current_line)

lines = parse_tree()
#ans_1 = part_1(lines)
ans_2 = part_2(lines)
breakpoint()

