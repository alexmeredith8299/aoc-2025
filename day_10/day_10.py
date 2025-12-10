import os
import numpy as np

def parse_data():
    with open('input.txt', 'r') as file:
        indicator_lights = []
        buttons = []
        joltages = []
        for line in file.readlines():
            line = line.strip()
            lbracket_ind = line.find('[')
            rbracket_ind = line.find(']')
            ljoltage_ind = line.find('{')
            rjoltage_ind = line.find('}')
            indicator_light = line[lbracket_ind+1:rbracket_ind]
            indicator_light = indicator_light.replace('#', '1')
            indicator_light = indicator_light.replace('.', '0')
            indicator_light = list(indicator_light)
            indicator_light = [int(lt) for lt in indicator_light]
            indicator_lights.append(indicator_light)
            button = line[rbracket_ind+1:ljoltage_ind].strip()
            button = button.split(' ')
            for i, btn in enumerate(button):
                btn = btn[1:-1].split(',')
                button[i] = [int(b) for b in btn]
            buttons.append(button)
            joltage = line[ljoltage_ind+1:rjoltage_ind]
            joltage = joltage.split(',')
            joltage = [int(j) for j in joltage]
            joltages.append(joltage)
    return indicator_lights, buttons, joltages

def min_presses(current_lights, indicator_lights, buttons):
    if (current_lights == indicator_lights).all():
        return 0
    current_configs = [current_lights,]
    all_configs = set(tuple(current_lights))
    i = 1
    while True:
        new_configs = []
        for config in current_configs:
            for button in buttons:
                new_config = (config + button)%2
                if (new_config == indicator_lights).all():
                    return i
                elif tuple(new_config) not in all_configs:
                    all_configs.add(tuple(new_config))
                    new_configs.append(new_config)
        current_configs = new_configs
        i += 1

def part_1(indicator_lights, buttons):
    total_cost = 0
    for i in range(len(buttons)):
        ind_lights_i = np.array(indicator_lights[i])
        buttons_i = buttons[i]
        new_buttons = []
        for btn in buttons_i:
            new_btn = np.zeros_like(ind_lights_i)
            new_btn[btn] = 1
            new_buttons.append(new_btn)
        cost = min_presses(np.zeros_like(ind_lights_i), ind_lights_i, new_buttons)
        total_cost += cost
    return total_cost

def min_presses_joltage(current_joltage, goal_joltage, buttons):
    if (current_joltage == goal_joltage).all():
        return 0
    current_joltages = [current_joltage,]
    all_joltages = set(tuple(current_joltage))
    i = 1
    while True:
        new_joltages = []
        for joltage in current_joltages:
            for button in buttons:
                new_joltage = joltage + button
                if (new_joltage == goal_joltage).all():
                    return i
                elif tuple(new_joltage) not in all_joltages and (new_joltage <= goal_joltage).all():
                    all_joltages.add(tuple(new_joltage))
                    new_joltages.append(new_joltage)
        current_joltages = new_joltages
        i += 1

def part_2(indicator_lights, buttons):
    total_cost = 0
    for i in range(len(buttons)):
        print(i)
        ind_lights_i = np.array(indicator_lights[i])
        buttons_i = buttons[i]
        new_buttons = []
        for btn in buttons_i:
            new_btn = np.zeros_like(ind_lights_i)
            new_btn[btn] = 1
            new_buttons.append(new_btn)
        cost = min_presses_joltage(np.zeros_like(ind_lights_i), ind_lights_i, new_buttons)
        total_cost += cost
    return total_cost


indicator_lights, buttons, joltages = parse_data()
total_cost = part_1(indicator_lights, buttons)
joltage_cost = part_2(joltages, buttons)
breakpoint()
