import os

def load_tokens():
    tokens = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            tokens.append(line.strip())
    return tokens
     
def part_1():
    # Load input
    tokens = load_tokens()
    password = 0
    num = 50
    for token in tokens:
        if token[0] == 'L':
            num_add = -1*int(token[1:])
        else:
            num_add = int(token[1:])
        num += num_add
        num = num%100
        if num == 0:
            password += 1
    return password

def part_2():
    # Load input
    tokens = load_tokens()
    password = 0
    num = 50
    for token in tokens:
        if token[0] == 'L':
            num_add = -1*int(token[1:])
        else:
            num_add = int(token[1:])
        num_orig = num
        num += num_add
        num_mod = num%100
        if num_mod != num:
            password += (abs(num)//100)
            if num < 0 and num_orig > 0:
                password += 1
            #if num_orig == 0 and num < 0:
            #    password -= 1
        elif num == 0:
            password += 1
        print(num_orig, num, num_mod, token, password)
        num = num_mod
    return password

print(part_1())
print(part_2())
