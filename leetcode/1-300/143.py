# -*- coding: utf-8 -*-
# ======================================
# @File    : 143.py
# @Time    : 2020/10/20 12:46 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [143. 重排链表](https://leetcode-cn.com/problems/reorder-list/)
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        stk = []
        tail = slow.next
        slow.next = None
        while tail:
            stk.append(tail)
            tail = tail.next
        p = head
        while stk:
            t = p.next
            cur = stk.pop()
            p.next = cur
            p.next.next = t
            p = p.next.next


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4])
    a.reorderList(x)
    list_node_print(x)
    x = construct_list_node([1,2,3,4,5])
    a.reorderList(x)
    list_node_print(x)
