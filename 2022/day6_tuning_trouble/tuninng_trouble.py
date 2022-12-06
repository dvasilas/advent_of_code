#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()

    return lines

def parse_input(lines):
    return [line.strip() for line in lines][0]

def all_chars_are_different(string):

    chars_in_string = {}
    for c in string:
        if c in chars_in_string:
            return False
        chars_in_string[c] = True

    return True

def find_first_unique_char_subtring(signal, n_unique_chars):
    p_start = 0
    p_end = n_unique_chars-1

    while p_end < len(signal):
        window = signal[p_start:p_end+1]

        p_start += 1
        p_end += 1

        if all_chars_are_different(window):
            break

    print(p_end)


def main():
    signal = parse_input(read_input(sys.argv[1]))

    find_first_unique_char_subtring(signal, 4)
    find_first_unique_char_subtring(signal, 14)


if __name__ == "__main__":
    main()
