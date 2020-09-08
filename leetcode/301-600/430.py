# -*- coding: utf-8 -*-
# ======================================
# @File    : 430.py
# @Time    : 2020/9/8 1:31 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    """
    [430. 扁平化多级双向链表](https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/)
    """
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p:
            if p.child:
                tmp = p.next
                nxt = self.flatten(p.child)
                p.next, nxt.prev = nxt, p
                p.child = None
                while p and p.next:
                    p = p.next
                if tmp: p.next, tmp.prev = tmp, p
            p = p.next
        return head

if __name__ == '__main__':
    a = Solution()
