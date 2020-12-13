# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-04.py
# @Time    : 2020/12/12 0:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.04. 分割链表](https://leetcode-cn.com/problems/partition-list-lcci/)
    """
    @timeit
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 迭代器模拟快排partition
        def f(head):
            if head and head.next:
                yield from f(head.next)
            yield head

        daeh = f(head)
        p, q = head, next(daeh)
        while p != q:
            while p != q and p.val < x:
                p = p.next
            while p != q and q.val >= x:
                q = next(daeh)
            if p != q:
                p.val, q.val = q.val, p.val
        return head


    @timeit
    def partition2(self, head: ListNode, x: int) -> ListNode:
        # 快慢指针模拟快排partition
        slow = fast = head
        while fast:
            if fast.val < x:
                slow.val, fast.val = fast.val, slow.val
                slow = slow.next
            fast = fast.next
        return head

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([3,5,8,5,10,2,1])
    a.partition2(x, 5)
    x = construct_list_node([1,4,3,2,5,2])
    a.partition2(x, 3)