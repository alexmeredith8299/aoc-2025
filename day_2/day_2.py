import os

def load_ranges():
    with open('input.txt', 'r') as file:
        raw_ranges = file.read().strip().split(',')
    ranges = []
    for id_range in raw_ranges:
        split_range = id_range.split('-')
        lower = int(split_range[0])
        upper = int(split_range[1])
        ranges.append((lower, upper))
    return ranges

def part_1(ranges):
    sum_ids = 0
    for (lower, upper) in ranges:
        for num in range(lower, upper+1):
            str_num = str(num)
            if len(str_num)%2 == 0:
                first_half = str_num[0:len(str_num)//2]
                second_half = str_num[len(str_num)//2:]
                if first_half == second_half:
                    sum_ids += num
    return sum_ids

def part_2(ranges):
    sum_ids = 0
    for (lower, upper) in ranges:
        for num in range(lower, upper+1):
            str_num = str(num)
            already_match = False
            for div in range(1, len(str_num)//2+1):
                if not already_match:
                    if len(str_num)%div == 0:
                        first_chunk = str_num[0:div]
                        match = True
                        for i in range(len(str_num)//div):
                            chunk = str_num[i*div:(i+1)*div]
                            if chunk != first_chunk:
                                match = False
                                break
                        if match:
                            sum_ids += num
                            already_match = True
    return sum_ids


ranges = load_ranges()
#part_1_sum = part_1(ranges)
part_2_sum = part_2(ranges)
breakpoint()
