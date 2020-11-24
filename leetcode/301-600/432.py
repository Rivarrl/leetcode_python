# -*- coding: utf-8 -*-
# ======================================
# @File    : 432.py
# @Time    : 2020/11/24 9:44 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

inf = 0x3f3f3f3f3f

class Row:
    """
    1 <-> 2 <-> 3
    |
    v
    key1 <-> key2 <-> ...
    """
    def __init__(self, val, size=0, pre=None, nxt=None):
        self.val = val
        self.size = size
        self.pre = pre
        self.next = nxt
        head = Node('', val)
        tail = Node('', val)
        head.next, tail.pre = tail, head
        self.head, self.tail = head, tail

class Node:
    """
    key1 <-> key2 <-> ...
    """
    def __init__(self, key, pre=None, nxt=None):
        self.key = key
        self.pre = pre
        self.next = nxt

class AllOne:
    """
    [432. 全 O(1) 的数据结构](https://leetcode-cn.com/problems/all-oone-data-structure/)
    """
    def __init__(self):
        self.d_key = {}
        head = Row(0, size=inf)
        tail = Row(inf, size=inf)
        head.next, tail.pre = tail, head
        self.head, self.tail = head, tail
        self.d_row = {0:head, inf:tail}
        self.row_count = 0

    def inc(self, key: str) -> None:
        dk, dr = self.d_key, self.d_row
        del_flag = False
        if key not in dk:
            dk[key] = [Node(key), 0]
        else:
            del_flag = True
        node, val = dk[key]
        row = dr[val]
        if del_flag:
            row, _ = self.del_node(row, node)
        nxt_val = val + 1
        if nxt_val not in dr:
            dr[nxt_val] = nxt_row = Row(nxt_val)
            p, q = row, row.next
            p.next, q.pre, nxt_row.next, nxt_row.pre = nxt_row, nxt_row, q, p
            self.row_count += 1
        self.add_node(dr[nxt_val], node)
        dk[key][1] += 1


    def dec(self, key: str) -> None:
        dk, dr = self.d_key, self.d_row
        if key not in dk: return
        node, val = dk[key]
        dk[key][1] -= 1
        row = dr[val]
        _, row = self.del_node(row, node)
        pre_val = dk[key][1]
        if pre_val > 0:
            if pre_val not in dr:
                dr[pre_val] = pre_row = Row(pre_val)
                p, q = row.pre, row
                p.next, q.pre, pre_row.next, pre_row.pre = pre_row, pre_row, q, p
                self.row_count += 1
            self.add_node(dr[pre_val], node)
        else:
            dk.pop(key)

    def getMaxKey(self) -> str:
        if self.row_count == 0: return ""
        return self.tail.pre.tail.pre.key

    def getMinKey(self) -> str:
        if self.row_count == 0: return ""
        return self.head.next.head.next.key

    def del_node(self, row, node):
        p, q = node.pre, node.next
        p.next, q.pre, node.pre, node.next = q, p, None, None
        row.size -= 1
        if row.size == 0:
            self.d_row.pop(row.val)
            p, q = row.pre, row.next
            p.next, q.pre, row.pre, row.next = q, p, None, None
            self.row_count -= 1
            return p, q
        return row, row

    def add_node(self, row, node):
        p, q = row.head, row.head.next
        p.next, q.pre, node.pre, node.next = node, node, p, q
        row.size += 1


if __name__ == '__main__':
    a = AllOne()
    x = ["inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMaxKey", "getMinKey"]
    y = [["a"], ["b"], ["b"], ["b"], ["b"], ["b"], ["b"], [], []]
    tot = 0
    for i, j in zip(x, y):
        print(tot, i, j)
        if i == "inc":
            a.inc(j[0])
        elif i == "dec":
            a.dec(j[0])
        elif i == "getMaxKey":
            print(a.getMaxKey())
        else:
            print(a.getMinKey())
        tot += 1