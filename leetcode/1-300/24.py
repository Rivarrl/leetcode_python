# -*- coding: utf-8 -*-
# ======================================
# @File    : 24.py
# @Time    : 1/30/20 11:05 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        t = p
        while p and p.next and p.next.next:
            q = p.next
            x = q.next
            q.next = x.next
            x.next = q
            p.next = x
            p = p.next.next
        return t.next

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    r = a.swapPairs(x)
    list_node_print(r)