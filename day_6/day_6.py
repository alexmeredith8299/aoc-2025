import os
import numpy as np

def extract_rows():
    rows = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            row = []
            raw_row = line.strip().split(' ')
            for elt in raw_row:
                if elt != '':
                    if elt == '+' or elt == '*':
                        row.append(elt)
                    else:
                        row.append(int(elt))
            rows.append(row)
    return rows

def extract_cephalopod_form():
    num_rows = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            raw_row = list(line[:-1])
            row = []
            for elt in raw_row:
                if elt != ' ' and elt != '+' and elt != '*':
                    row.append(int(elt))
                elif elt == ' ':
                    row.append(0)
                else:
                    row.append(elt)
            num_rows.append(row)
        raw_elt_line = list(lines[-1])
        elt_line = []
        for elt in raw_elt_line:
            if elt == '*' or elt == '+':
                elt_line.append(elt)
    num_arr = np.array(num_rows)
    fixed_num_arr = transform_num_arr(num_arr)
    fixed_num_arr.append(elt_line)
    return fixed_num_arr

def parse_num_from_col(col):
    lsd = 0
    for i in range(1, col.shape[0]):
        if col[i] != 0:
            lsd = i
    num = 0
    for i in reversed(range(lsd+1)):
        num += col[i] * 10**(lsd-i)
    return num

def transform_num_arr(num_arr):
    nums = []
    for i in range(num_arr.shape[1]):
        num = parse_num_from_col(num_arr[:, i])
        nums.append(num)
    new_nums = []
    current_row = []
    for num in nums:
        if num == 0:
            while len(current_row) < num_arr.shape[0]:
                current_row.append(0)
            new_nums.append(current_row)
            current_row = []
        else:
            current_row.append(num)
    if len(current_row) > 0:
        while len(current_row) < num_arr.shape[0]:
            current_row.append(0)
        new_nums.append(current_row)
    return np.array(new_nums).T.tolist()

def extract_mult_rows_and_add_rows(rows):
    symbols = np.array(rows[-1])
    nums = np.array(rows[:-1])
    mult_nums = nums[:, np.where(symbols=='*')]
    mult_nums[mult_nums==0] = 1
    add_nums = nums[:, np.where(symbols=='+')]
    return mult_nums[:, 0, :], add_nums[:, 0, :]

def part_1(rows):
    mult_nums, add_nums = extract_mult_rows_and_add_rows(rows)
    mult_row = mult_nums[0]
    for i in range(1, mult_nums.shape[0]):
        mult_row = mult_row*mult_nums[i]
    return mult_row.sum() + add_nums.sum()

rows = extract_rows()
#ans_1 = part_1(rows)
new_rows = extract_cephalopod_form()
ans_2 = part_1(new_rows)
breakpoint()
#breakpoint()
