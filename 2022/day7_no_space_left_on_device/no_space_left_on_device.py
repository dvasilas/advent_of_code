#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    return [line.strip() for line in lines]

class File(object):
    def __init__(self, name, parent_dir, size):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

class Directory(object):
    def __init__(self, name, parent_dir):
        self.name = name
        self.size = 0
        self.parent_dir = parent_dir
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class FsCtx(object):
    def __init__(self):
        self.root = Directory('/', None)
        self.cwd = None

def is_cmd(line):
    return line.startswith('$')

def cmd_is_ls(cmd):
    return cmd[0] == 'ls'

def cmd_is_cd(cmd):
    return cmd[0] == 'cd'

def do_cd(arg, ctx):
    if arg == '/':
        ctx.cwd = ctx.root
    if arg == '..':
        ctx.cwd = ctx.cwd.parent_dir
    else:
        for child in ctx.cwd.children:
            if child.name == arg:
                ctx.cwd = child

def parse_ls_output_entry(entry, ctx):
    dir_entry = entry.split(' ')
    if dir_entry[0] == 'dir':
        new_dir = Directory(dir_entry[1], ctx.cwd)
        ctx.cwd.add_child(new_dir)
    else:
        new_file = File(dir_entry[1], ctx.cwd, int(dir_entry[0]))
        ctx.cwd.add_child(new_file)

def do_ls(output, ctx):
    for entry in output:
        parse_ls_output_entry(entry, ctx)

def do_cmd(cmd, output, ctx):

    if cmd[0] == 'ls':
        do_ls(output, ctx)
    elif cmd[0] == 'cd':
        do_cd(cmd[1], ctx)
    else:
        # should not have reached here
        assert False

def build_fs_tree(terminal_out, ctx):
    gathering_output = False
    output = []
    for line in terminal_out:

        if is_cmd(line):
            if gathering_output:
                gathering_output = False
                do_cmd(cmd, output, ctx)

            cmd = line.split(' ')[1:]
            if cmd_is_cd(cmd):
                do_cmd(cmd, output, ctx)
            elif cmd_is_ls(cmd):
                gathering_output = True
                output = []
                pass
            else:
                # should not have reached here
                assert False
        else:
            output.append(line)

    # last cmd
    do_cmd(cmd, output, ctx)

def compute_sizes(node):
    if isinstance(node, Directory):
        for child in node.children:
            compute_sizes(child)
            node.size += child.size

def sum_dir_sizes(node):
    acc = 0

    if isinstance(node, Directory):
        for child in node.children:
            acc += sum_dir_sizes(child)

        if node.size <= 100000:
            acc += node.size

    return acc

def free_space(node, ctx):
    min_dir_size_to_delete = None
    dir_to_delete = None


    if isinstance(node, Directory):
        for child in node.children:
            (min_size, dir_node) = free_space(child, ctx)
            if min_size is not None:
                if min_dir_size_to_delete is None or min_size < min_dir_size_to_delete:

                    min_dir_size_to_delete = min_size
                    dir_to_delete = dir_node

        if 70000000 - ctx.root.size + node.size >= 30000000:
            if min_dir_size_to_delete is None or node.size < min_dir_size_to_delete:
                min_dir_size_to_delete = node.size
                dir_to_delete = node

    return (min_dir_size_to_delete, dir_to_delete)


def main():
    pb_input = parse_input(read_input(sys.argv[1]))

    ctx = FsCtx()

    build_fs_tree(pb_input, ctx)
    compute_sizes(ctx.root)
    print(sum_dir_sizes(ctx.root))
    print(free_space(ctx.root, ctx)[1].size)


if __name__ == "__main__":
    main()
