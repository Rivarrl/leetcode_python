# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-05.py
# @Time    : 2020/11/25 8:48 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.05. 链表求和](https://leetcode-cn.com/problems/sum-lists-lcci/)
    """
    @timeit
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        p = res = ListNode(0)
        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            c, p.val = divmod(a + b + c, 10)
            if not l1 and not l2:
                if c == 1:
                    p.next = ListNode(1)
                break
            p.next = ListNode(0)
            p = p.next
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([7,1,6])
    y = construct_list_node([5,9,3])
    a.addTwoNumbers(x, y)