#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

class Tree(object):
    def __init__(self, height):
        self.height = height
        self.visible = False

def parse_row(line):
    return [Tree(int(x)) for x in line.strip()]

def row_visibility(row):
    cur_max = -1
    for tree in row:
        if tree.height > cur_max:
            cur_max = tree.height
            tree.visible = True

def columns_visibility(grid):
    for j in range(len(grid[0])):
        col = []
        for i in range(len(grid)):
            col.append(grid[i][j])

        row_visibility(col)
        row_visibility(reversed(col))

def scenic_score_up(grid, i, j):
    score_up = 0

    x = i - 1
    while x >= 0:
        score_up += 1
        if grid[x][j].height >= grid[i][j].height:
            return score_up
        x -= 1

    return score_up

def scenic_score_down(grid, nrows, i, j):
    score_down = 0

    x = i + 1
    while x < nrows:
        score_down += 1
        if grid[x][j].height >= grid[i][j].height:
            return score_down
        x += 1

    return score_down

def scenic_score_left(grid, i, j):
    score_left = 0

    y = j - 1
    while y >= 0:
        score_left += 1
        if grid[i][y].height >= grid[i][j].height:
            return score_left

        y -= 1

    return score_left

def scenic_score_right(grid, ncols, i, j):
    score_right = 0

    y = j + 1
    while y < ncols:
        score_right += 1
        if grid[i][y].height >= grid[i][j].height:
            return score_right
        y += 1

    return score_right

def place_tree_house(grid):
    max_scenic_score = 0

    count = 0
    nrows = len(grid)
    ncols = len(grid[0])
    for i in range(nrows):
        if i == 0:
            continue
        for j in range(ncols):
            if j == 0:
                continue

            scenic_score = scenic_score_up(grid, i, j) * \
                scenic_score_down(grid, nrows, i, j) * \
                scenic_score_left(grid, i, j) * \
                scenic_score_right(grid, ncols, i, j)

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(max_scenic_score)

def main():
    pb_input = read_input(sys.argv[1])

    grid = []
    for row_in in pb_input:
        row = parse_row(row_in)
        row_visibility(row)
        row_visibility(reversed(row))

        grid.append(row)

    columns_visibility(grid)

    count = 0
    for row in grid:
        for tree in row:
            if tree.visible:
                count += 1

    print(count)

    place_tree_house(grid)

if __name__ == "__main__":
    main()
