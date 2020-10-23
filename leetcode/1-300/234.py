# -*- coding: utf-8 -*-
# ======================================
# @File    : 234.py
# @Time    : 2020/10/23 12:54 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)
    """
    @timeit
    def isPalindrome(self, head: ListNode) -> bool:
        q = head
        def f(p):
            nonlocal q
            if not p or not p.next: return True
            res = f(p.next)
            q = q.next
            return res and p.val == q.val
        return f(head)

    @timeit
    def isPalindrome2(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next if fast else slow
        p = mid
        while p and p.next:
            tmp = p.next
            p.next = tmp.next
            tmp.next = mid
            mid = tmp
        while head and mid:
            if head.val != mid.val: return False
            head = head.next
            mid = mid.next
        return True

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2])
    a.isPalindrome(x)
    x = construct_list_node([1,2,2,1])
    a.isPalindrome(x)