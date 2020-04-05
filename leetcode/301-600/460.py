# -*- coding: utf-8 -*-
# ======================================
# @File    : 460.py
# @Time    : 2020/4/5 13:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import defaultdict

class Node:
    # 双向链表节点
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 0
        self.pre = None
        self.next = None

    def append(self, node):
        node.pre, node.next = self, self.next
        self.next.pre = node
        self.next = node


def linked_list():
    # 双向链表, python 元组比类快
    """
    初始化头尾两个空节点，方便操作
    依题意，双向链表需要从头插入和从尾删除两种操作
    """
    dummy_head = Node(-1, -1)
    dummy_tail = Node(-1, -1)
    dummy_head.next = dummy_tail
    dummy_tail.pre = dummy_head
    return (dummy_head, dummy_tail)


class LFUCache:
    """
    [460. LFU缓存](https://leetcode-cn.com/problems/lfu-cache/)
    使用map key_d存储缓存信息，freq_d存储访问频率，也可以用列表，不过用map更节省空间
    双向链表保存相同访问频率的最近一次访问的顺序，头节点为最近访问，尾节点为最远访问
    所以每次添加从头添加，而删除从尾删除
    get时把key的freq先从freq_d中去除，再+1再插入freq_d[freq+1]中
    """
    def __init__(self, capacity: int):
        self.key_d = {}
        self.freq_d = defaultdict(linked_list)
        self.size = 0
        self.cap = capacity
        self.min_freq = 0

    @timeit
    def get(self, key: int) -> int:
        if not key in self.key_d: return -1
        self.increase(self.key_d[key])
        return self.key_d[key].val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if key in self.key_d:
            node = self.key_d[key]
            node.val = value
        else:
            node = Node(key, value)
            self.key_d[key] = node
            self.size += 1
        if self.size > self.cap:
            # 超载了，需要删掉最少最远访问节点
            rm = self.delete(self.freq_d[self.min_freq][1].pre)
            self.key_d.pop(rm)
            self.size -= 1
        self.increase(node)

    def delete(self, node):
        if node.pre:
            node.pre.next = node.next
            node.next.pre = node.pre
            # 空的时候清空
            if node.pre is self.freq_d[node.freq][0] and node.next is self.freq_d[node.freq][1]:
                self.freq_d.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freq_d[node.freq][0].append(node)
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq - 1:
            head, tail = self.freq_d[node.freq - 1]
            if head.next is tail:
                self.min_freq = node.freq


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.get(3)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
