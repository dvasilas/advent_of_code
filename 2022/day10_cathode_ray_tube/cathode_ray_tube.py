#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    return [line.strip() for line in lines]

def next_cycle(cycle, x_register, strength):
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        strength += (cycle * x_register)
    return (cycle, strength)

def parse_instructions_signal_strength(lines):
    cycle = 0
    strength = 0
    x_register = 1
    for line in lines:
        if line == "noop":
            (cycle, strength) = next_cycle(cycle, x_register, strength)
        else:
            (cycle, strength) = next_cycle(cycle, x_register, strength)
            (cycle, strength) = next_cycle(cycle, x_register, strength)
            line = line.split(' ')
            assert line[0] == 'addx'
            x_register += int(line[1])

    print(strength)

def draw_pixel(screen, cycle, x_register):
    draw_pos = cycle % 40
    if draw_pos in [x_register - 1, x_register, x_register + 1]:
        screen[cycle] = '#'


def parse_instructions_draw(lines):
    screen = ['*']*240
    cycle = 0
    strength = 0
    x_register = 1
    for line in lines:
        if line == "noop":
            draw_pixel(screen, cycle, x_register)
            (cycle, strength) = next_cycle(cycle, x_register, strength)
        else:
            draw_pixel(screen, cycle, x_register)
            (cycle, strength) = next_cycle(cycle, x_register, strength)
            draw_pixel(screen, cycle, x_register)
            (cycle, strength) = next_cycle(cycle, x_register, strength)
            line = line.split(' ')
            assert line[0] == 'addx'
            x_register += int(line[1])

    for (p0, p1) in [(0, 40), (40,80), (80, 120), (120, 160), (160, 200), (200, 240)]:
        print(' '.join(screen[p0:p1]))

def main():
    pb_input = parse_input(read_input(sys.argv[1]))

    parse_instructions_signal_strength(pb_input)
    parse_instructions_draw(pb_input)

if __name__ == "__main__":
    main()
