#!/usr/bin/python3

import sys
import copy

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

def parse_input(pb_input):
    stacks_description = []
    moves_description = []

    mode = 0
    for line in pb_input:
        if len(line) == 1:
            continue

        if line[1] == '1':
            mode = 1
            continue

        if mode == 0:
            stacks_description.append(line)

        else:
            moves_description.append(line)

    return(stacks_description, moves_description)

def build_stacks(stacks_description):
    n = int(len(stacks_description[0]) / 4)

    stacks = []
    for i in range(n):
        stacks.append([])

    for line in stacks_description:
        p = 1
        for stack in stacks:
            if line[p] != ' ':
                stack.append(line[p])

            p += 4

    for stack in stacks:
        stack.reverse()

    return stacks

def do_moves_one_by_one(stacks, moves_description):
    for line in moves_description:
        line = line.split(' ')

        amount = int(line[1])
        from_stack = int(line[3])
        to_stack = int(line[5])

        for i in range(amount):
            elem = stacks[from_stack - 1].pop(len(stacks[from_stack - 1])-1)
            stacks[to_stack - 1].append(elem)

def do_moves_batch(stacks, moves_description):
    for line in moves_description:
        line = line.split(' ')

        amount = int(line[1])
        from_stack = int(line[3])
        to_stack = int(line[5])

        stay = stacks[from_stack - 1][:len(stacks[from_stack - 1]) - amount]
        go = stacks[from_stack - 1][(len(stacks[from_stack - 1]) - amount):]

        for i in range(amount):
            elem = stacks[from_stack - 1].pop(len(stacks[from_stack - 1])-1)

        stacks[to_stack - 1] += go

def print_top(stacks):
    string = ""

    for stack in stacks:
        string += stack[-1]

    print(string)

def main():
    pb_input = read_input(sys.argv[1])

    (stacks_description, moves_description) = parse_input(pb_input)

    stacks = build_stacks(stacks_description)
    stacks_copy = copy.deepcopy(stacks)
    do_moves_one_by_one(stacks, moves_description)
    print_top(stacks)

    do_moves_batch(stacks_copy, moves_description)
    print_top(stacks_copy)



if __name__ == "__main__":
    main()
