# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-08.py
# @Time    : 2020/12/12 20:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.08. 环路检测](https://leetcode-cn.com/problems/linked-list-cycle-lcci/)
    """
    @timeit
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                    head = head.next
                    slow = slow.next
                return head


if __name__ == '__main__':
    a = Solution()
    xx = [ListNode(i) for i in [3, 2, 0, 4]]
    for i in range(3):
        xx[i].next = xx[i+1]
    xx[-1].next = xx[1]
    a.detectCycle(xx[0])
    x = ListNode(1)
    y = ListNode(2)
    x.next = y
    y.next = x
    a.detectCycle(x)
    x = construct_list_node([1])
    a.detectCycle(x)