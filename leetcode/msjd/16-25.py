# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-25.py
# @Time    : 2020/11/17 12:47 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    """
    [面试题 16.25. LRU缓存](https://leetcode-cn.com/problems/lru-cache-lcci/)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None,-1)
        self.tail = Node(None,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.rec = {}

    @timeit
    def get(self, key: int) -> int:
        if key not in self.rec: return -1
        node = self.rec[key]
        self.delete(node)
        self.appendHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.rec:
            node = Node(key, value)
            self.appendHead(node)
            self.rec[key] = node
            self.capacity -= 1
        else:
            old_node = self.rec[key]
            self.delete(old_node)
            node = Node(key, value)
            self.appendHead(node)
            self.rec[key] = node
        if self.capacity < 0:
            tail = self.deleteTail()
            self.rec.pop(tail.key)
            self.capacity += 1

    def delete(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next
        node.pre = node.next = None
        return node

    def appendHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def deleteTail(self):
        return self.delete(self.tail.pre)

if __name__ == '__main__':
    a = LRUCache(2)
    a.put(2, 1)
    a.put(1, 1)
    a.put(2, 3)
    a.put(4, 1)
    a.get(1)
    a.get(2)