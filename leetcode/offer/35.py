# -*- coding: utf-8 -*-
# ======================================
# @File    : 35.py
# @Time    : 2020/5/6 21:18
# @Author  : Rivarrl
# ======================================
# [面试题35. 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)
from algorithm_utils import *

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    @timeit
    def copyRandomList(self, head: 'Node') -> 'Node':
        # hash
        d = {}
        p = head
        while p:
            x = Node(p.val)
            d[p] = x
            p = p.next
        p = head
        res = q = Node(-1)
        while p:
            v = d[p]
            q.next = v
            if p.random: q.next.random = d[p.random]
            p, q = p.next, q.next
        return res.next

    @timeit
    def copyRandomList2(self, head: 'Node') -> 'Node':
        # 原地
        # 分3步，先在每个节点后面复制一个不带random指针的节点；然后把random指针接好，最后把原来的链表拆掉
        if not head: return head
        p = head
        while p:
            q = p.next
            p.next = Node(p.val)
            p.next.next = q
            p = q
        p = head
        while p and p.next:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        res = p = head.next
        while p and p.next:
            p.next = p.next.next
            p = p.next
        return res

if __name__ == '__main__':
    a = Solution()
    arr = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(4):
        arr[i].next = arr[i+1]
    arr[1].random = arr[0]
    arr[2].random = arr[4]
    arr[3].random = arr[2]
    arr[4].random = arr[0]
    a.copyRandomList2(arr[0])
