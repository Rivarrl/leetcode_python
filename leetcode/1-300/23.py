# -*- coding: utf-8 -*-
# ======================================
# @File    : 23.py
# @Time    : 2020/4/26 13:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [23. 合并K个排序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)
    """
    @timeit
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        def __lt__(self, other):
            return self.val < other.val
        ListNode.__lt__ = __lt__
        q = []
        for p in lists:
            if not p: continue
            heapq.heappush(q, p)
        res = r = ListNode(0)
        while q:
            p = heapq.heappop(q)
            r.next = p
            r = r.next
            if p.next:
                heapq.heappush(q, p.next)
        return res.next

if __name__ == '__main__':
    a = Solution()
    x1 = construct_list_node([1,4,5])
    x2 = construct_list_node([1,3,4])
    x3 = construct_list_node([2,6])
    a.mergeKLists([x1, x2, x3])