# -*- coding: utf-8 -*-
# ======================================
# @File    : 25.py
# @Time    : 2020/5/7 19:19
# @Author  : Rivarrl
# ======================================
# [面试题25. 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)
from algorithm_utils import *
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = p = ListNode(0)
        while l1 or l2:
            if not l1: c, l2 = l2, l2.next
            elif not l2: c, l1 = l1, l1.next
            elif l1.val < l2.val: c, l1 = l1, l1.next
            else: c, l2 = l2, l2.next
            p.next = c
            p = p.next
        return res.next

if __name__ == '__main__':
    a = Solution()
    x, y = construct_list_node([1,2,4]), construct_list_node([1,3,4])
    a.mergeTwoLists(x, y)
