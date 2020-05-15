# -*- coding: utf-8 -*-
# ======================================
# @File    : 25.py
# @Time    : 2020/5/16 0:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)
    """
    @timeit
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        dummy = last = ListNode(-1)
        p = head
        while n > 0:
            if n < k:
                last.next = p
                break
            q = p
            for _ in range(k-1):
                t = p.next
                p.next = t.next
                t.next = q
                q = t
            last.next = q
            last = p
            p = p.next
            n -= k
        return dummy.next


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.reverseKGroup(x, 3)