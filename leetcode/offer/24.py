# -*- coding: utf-8 -*-
# ======================================
# @File    : 24.py
# @Time    : 2020/5/7 19:20
# @Author  : Rivarrl
# ======================================
# [面试题24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)
from algorithm_utils import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = q = head
        while q and q.next:
            t = q.next
            q.next = t.next
            t.next = p
            p = t
        return p


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    r = a.reverseList(x)
    list_node_print(r)