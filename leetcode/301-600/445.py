# -*- coding: utf-8 -*-
# ======================================
# @File    : 445.py
# @Time    : 2020/4/14 0:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        stk1 = [p]
        while p and p.next:
            p = p.next
            stk1.append(p)
        p = l2
        stk2 = [p]
        while p and p.next:
            p = p.next
            stk2.append(p)
        if len(stk1) < len(stk2):
            stk1, stk2 = stk2, stk1
        i = z = 0
        while stk2:
            x = stk1[len(stk1) - 1 - i]
            y = stk2.pop()
            x.val, z = (x.val + y.val + z) % 10, (x.val + y.val + z) // 10
            i += 1
        while i < len(stk1) and z:
            x = stk1[len(stk1) - 1 - i]
            x.val, z = (x.val + z) % 10, (x.val + z) // 10
            i += 1
        if z:
            head = ListNode(1)
            head.next = stk1[0]
        else:
            head = stk1[0]
        return head


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([7,2,4,3])
    y = construct_list_node([5,6,4])
    a.addTwoNumbers(x, y)