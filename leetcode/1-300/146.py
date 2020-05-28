# -*- coding: utf-8 -*-
# ======================================
# @File    : 146.py
# @Time    : 2020/5/25 20:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Node:
    def __init__(self, key, val, pre=None, nx=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = nx

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head, self.tail = Node(float('inf'),float('inf')), Node(float('inf'),float('inf'))
        self.head.next, self.tail.pre = self.tail, self.head

    def get(self, key: int) -> int:
        if not key in self.d: return -1
        p = self.d[key]
        p.pre.next, p.next.pre = p.next, p.pre
        q = self.head.next
        q.pre, p.next = p, q
        self.head.next, p.pre = p, self.head
        return p.val

    def put(self, key: int, value: int) -> None:
        p = Node(key, value)
        q = self.head.next
        q.pre, p.next = p, q
        self.head.next, p.pre = p, self.head
        if key in self.d:
            t = self.d[key]
            t.pre.next, t.next.pre = t.next, t.pre
        else:
            self.cap -= 1
        self.d[key] = p
        if self.cap < 0:
            p = self.tail.pre
            p.pre.next, p.next.pre = p.next, p.pre
            self.d.pop(p.key)
            self.cap += 1

if __name__ == '__main__':
    a = LRUCache(2)
    a.put(1, 1)
    a.put(2, 2)
    a.get(1)
    a.put(3, 3)
    a.get(2)
    a.put(4, 4)
    a.get(1)
    a.get(3)
    a.get(4)