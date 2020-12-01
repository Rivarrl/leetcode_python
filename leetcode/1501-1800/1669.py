# -*- coding: utf-8 -*-
# ======================================
# @File    : 1669.py
# @Time    : 2020/12/2 0:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [1669. 合并两个链表]()
    """
    @timeit
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tot = 0
        p = list1
        while tot + 1 < a:
            tot += 1
            p = p.next
        t, p.next = p.next, list2
        while p.next:
            p = p.next
        while tot < b:
            tot += 1
            t = t.next
        p.next = t
        return list1


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([0, 1, 2, 3, 4, 5])
    y = construct_list_node([1000000, 1000001, 1000002])
    a.mergeInBetween(x, 3, 4, y)
    x = construct_list_node([0, 1, 2, 3, 4, 5, 6])
    y = construct_list_node([1000000, 1000001, 1000002,1000003,1000004])
    a.mergeInBetween(x, 2, 5, y)