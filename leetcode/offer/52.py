# -*- coding: utf-8 -*-
# ======================================
# @File    : 52.py
# @Time    : 2020/4/28 23:02
# @Author  : Rivarrl
# ======================================
# [面试题52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        p, q = headA, headB
        ctr = 0
        while p != q and ctr < 4:
            if p.next:
                p = p.next
            else:
                p = headB
                ctr += 1
            if q.next:
                q = q.next
            else:
                q = headA
                ctr += 1
        return None if ctr == 4 else p

if __name__ == '__main__':
    a = Solution()
    A = construct_list_node([4,1])
    B = construct_list_node([5,0,1])
    C = construct_list_node([8,4,5])
    p = A
    while p.next:
        p = p.next
    p.next = C
    p = B
    while p.next:
        p = p.next
    p.next = C
    a.getIntersectionNode(A, B)
    A = construct_list_node([2,6,4])
    B = construct_list_node([1,5])
    a.getIntersectionNode(A, B)