# -*- coding: utf-8 -*-
# ======================================
# @File    : 328.py
# @Time    : 2020/11/13 0:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [328. 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/)
    """
    @timeit
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1, p2, p3 = head, head.next, head.next
        while p1.next and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        p1.next = p3
        return head

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.oddEvenList()
    x = construct_list_node([2,1,3,5,6,4,7])
    a.oddEvenList()