import os
import numpy as np

def load_banks():
    with open('input.txt', 'r') as file:
        banks = file.readlines()
        for i in range(len(banks)):
            banks[i] = list(banks[i].strip())
            for j in range(len(banks[i])):
                banks[i][j] = int(banks[i][j])
    return banks

def part_1(banks):
    total_joltage = 0
    for bank in banks:
        best_first_digit = 0
        best_first_digit_ind = -1
        for i in range(len(bank)-1):
            if bank[i] > best_first_digit:
                best_first_digit = bank[i]
                best_first_digit_ind = i
        best_second_digit = 0
        for j in range(best_first_digit_ind+1, len(bank)):
            if bank[j] > best_second_digit:
                best_second_digit = bank[j]
        total_joltage += 10*best_first_digit + best_second_digit
    return total_joltage

def get_best_digit_and_rem_bank(bank, rem_digits):
    if rem_digits > 0:
        best_digit = bank[:-rem_digits].max()
    else:
        best_digit = bank.max()
    best_digit_ind = np.where(bank==best_digit)[0][0]
    rem_bank = bank[best_digit_ind+1:] if best_digit_ind < len(bank)-1 else []
    return best_digit, rem_bank

def part_2(banks):
    total_joltage = 0
    for bank in banks:
        n_digits = 12
        rem_bank = np.array(bank)
        joltage = 0
        for i in reversed(range(n_digits)):
            best_digit, rem_bank = get_best_digit_and_rem_bank(rem_bank, i)
            joltage += 10**i * best_digit
        total_joltage += joltage
    return total_joltage

banks = load_banks()
joltage = part_2(banks)
print(joltage)
