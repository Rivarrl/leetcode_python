# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-06.py
# @Time    : 2020/11/13 1:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.06. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci/)
    """
    @timeit
    def isPalindrome(self, head: ListNode) -> bool:
        p = head
        res = True
        def f(q):
            if not q: return
            f(q.next)
            nonlocal res, p
            if p.val != q.val:
                res = False
            p = p.next
        f(head)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2])
    a.isPalindrome(x)
    x = construct_list_node([1,2,2,1])
    a.isPalindrome(x)