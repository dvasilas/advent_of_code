#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    return [line.strip() for line in lines]

def main():
    pb_input = parse_input(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()
