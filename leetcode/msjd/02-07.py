# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-07.py
# @Time    : 2020/11/13 1:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.07. 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/)
    """
    @timeit
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p