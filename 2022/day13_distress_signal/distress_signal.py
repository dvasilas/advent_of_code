#!/usr/bin/python3

import sys

def read_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    return [line.strip() for line in lines]

class Node(object):
    pass

class IntNode(Node):
    def __init__(self, val):
        self.value = val

class ListNode(Node):
    def __init__(self):
        self.l = []

    def __eq__(self, other):
        return cmp_list(self, other) == 1
    def __lt__(self, other):
        return cmp_list(self, other) == 0

def isInt(c):
    try:
        _ = int(c)
        return True
    except ValueError:
        return False

def cmp_list(l1, l2):
    max_len = max(len(l1.l), len(l2.l))

    for i in range(max_len):
        if i == len(l2.l) and i < len(l1.l):
            return 2
        elif i == len(l1.l) and i < len(l2.l):
            return 0
        elif i == len(l1.l) and i == len(l2.l):
            return 1
        elif isinstance(l1.l[i], IntNode) and isinstance(l2.l[i], IntNode):
            if l1.l[i].value < l2.l[i].value:
                return 0
            elif l1.l[i].value > l2.l[i].value:
                return 2
            elif l1.l[i].value == l2.l[i].value:
                continue
        elif isinstance(l1.l[i], ListNode) and isinstance(l2.l[i], ListNode):
            res =  cmp_list(l1.l[i], l2.l[i])
            if res == 1:
                continue
            else:
                return res
        else:
            lnode = ListNode()
            if isinstance(l1.l[i], IntNode):
                lnode.l.append(l1.l[i])
                res = cmp_list(lnode, l2.l[i])
                if res != 1:
                    return res

            if isinstance(l2.l[i], IntNode):
                lnode.l.append(l2.l[i])
                res = cmp_list(l1.l[i], lnode)
                if res != 1:
                    return res

    return 1

def parse_list(line, stack):
    head = None
    acc_str = ""
    for i, c in enumerate(line):
        if c == '[':
            if head is not None:
                stack.append(head)
            node = ListNode()
            head = node
        elif c == ']':
            if acc_str != "":
                node = IntNode(int(acc_str))
                acc_str = ""
                head.l.append(node)
            if len(stack) > 0:
                complete_list = head
                head = stack.pop()
                head.l.append(complete_list)
        elif c == ',':
            if acc_str != "":
                node = IntNode(int(acc_str))
                head.l.append(node)
                acc_str = ""
        elif isInt(c):
            acc_str += c
        else:
            assert False

    return head

def print_list(l):
    print("[", end = '')
    for elem in l.l:
        if isinstance(elem, IntNode):
            print(elem.value, end = '')
        elif isinstance(elem, ListNode):
            print_list(elem)
        else:
            assert False
        print(",", end = '')
    print("]", end = '')


def main():
    pb_input = parse_input(read_input(sys.argv[1]))

    l1 = None
    l2 = None
    acc = 0
    pair_idx = 1
    lists = []
    for line in pb_input:
        stack = []
        if len(line)>1:
            head = parse_list(line, stack)
            if l1 is None:
                l1 = head
                lists.append(l1)
            elif l2 is None:
                l2 = head
                lists.append(l2)

        if l1 is not None and l2 is not None:
            if l1 < l2:
                acc += pair_idx

            pair_idx += 1
            l1 = None
            l2 = None
    print(acc)

    node_key_2 = ListNode()
    node1 = ListNode()
    node_key_2.l.append(node1)
    node1.l.append(IntNode(2))
    lists.append(node_key_2)

    node_key_6 = ListNode()
    node1 = ListNode()
    node_key_6.l.append(node1)
    node1.l.append(IntNode(6))
    lists.append(node_key_6)

    lists = sorted(lists)
    idx_key_2 = None
    idx_key_6 = None
    for i, l in enumerate(lists):
        if (l == node_key_2):
            idx_key_2 = i
        if (l == node_key_6):
            idx_key_6 = i

    print((idx_key_2+1)*(idx_key_6+1))


if __name__ == "__main__":
    main()
