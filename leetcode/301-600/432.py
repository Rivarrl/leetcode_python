# -*- coding: utf-8 -*-
# ======================================
# @File    : 432.py
# @Time    : 2020/11/24 9:44 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

inf = 0x3f3f3f3f3f

class RowNode:
    """
    1 <-> 2 <-> 3
    |
    v
    key1 <-> key2 <-> ...
    """
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.next = nxt
        head = Node('', val)
        tail = Node('', val)
        head.next, tail.pre = tail, head
        self.child = head

class Node:
    """
    key1 <-> key2 <-> ...
    """
    def __init__(self, key, val, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = nxt

class AllOne:
    """
    [432. 全 O(1) 的数据结构](https://leetcode-cn.com/problems/all-oone-data-structure/)
    """
    def __init__(self):
        self.d_key = {}
        head = RowNode(0)
        tail = RowNode(inf)
        head.next, tail.pre = tail, head
        self.head, self.tail = head, tail
        self.d_val = {0:head, inf:tail}

    def del_col_node(self, cur):
        # 删除child中的节点，会造成连锁反应删除row节点
        dv = self.d_val
        pre, nxt = cur.pre, cur.next
        if pre.key == '' and nxt.key == '':
            row = dv[pre.val]
            self.del_node(row)
            del dv[pre.val]
        else:
            self.del_node(cur)

    def add_col_node(self, val, cur, offset):
        # 添加child中的节点
        dv = self.d_val
        if val not in dv:
            row = RowNode(val)
            dv[val] = row
            self.add_node(dv[val + offset], row)
        row = dv[val]
        self.add_node(row.child, cur)

    def del_node(self, cur):
        pre, nxt = cur.pre, cur.next
        pre.next, nxt.pre = nxt, pre
        cur.next, cur.pre = None, None

    def add_node(self, pre, cur):
        nxt = pre.next
        pre.next, nxt.pre = cur, cur
        cur.next, cur.pre = nxt, pre

    def inc(self, key: str) -> None:
        dk, dv = self.d_key, self.d_val
        if key not in dk:
            cur = Node(key, 0)
            dk[key] = cur
        else:
            cur = dk[key]
            self.del_col_node(cur)
        cur.val += 1
        val = cur.val
        self.add_col_node(val, cur, -1)

    def dec(self, key: str) -> None:
        dk, dv = self.d_key, self.d_val
        if key not in dk: return
        cur = dk[key]
        self.del_col_node(cur)
        if cur.val == 1:
            del dk[key]
        else:
            cur.val -= 1
            val = cur.val
            self.add_col_node(val, cur, 1)

    def getMaxKey(self) -> str:
        if self.head.next != self.tail:
            return self.tail.pre.child.next.key
        return ""

    def getMinKey(self) -> str:
        if self.head.next != self.tail:
            return self.head.next.child.next.key
        return ""


if __name__ == '__main__':
    a = AllOne()
    x = ["inc", "inc", "inc", "inc", "inc", "inc", "getMaxKey", "inc", "dec", "getMaxKey", "dec", "inc",
     "getMaxKey", "inc", "inc", "dec", "dec", "dec", "dec", "getMaxKey", "inc", "inc", "inc", "inc", "inc", "inc",
     "getMaxKey", "getMinKey"]
    y = [["hello"], ["world"], ["leet"], ["code"], ["DS"], ["leet"], [], ["DS"], ["leet"], [], ["DS"], ["hello"], [],
     ["hello"], ["hello"], ["world"], ["leet"], ["code"], ["DS"], [], ["new"], ["new"], ["new"], ["new"], ["new"],
     ["new"], [], []]
    tot = 0
    for i, j in zip(x, y):
        print(tot)
        if i == "inc":
            a.inc(j[0])
        elif i == "dec":
            a.dec(j[0])
        elif i == "getMaxKey":
            print(a.getMaxKey())
        else:
            print(a.getMinKey())
        p = a.head
        # while p:
        #     print(p.val, end=" ")
        #     p = p.next
        # print()
        tot += 1