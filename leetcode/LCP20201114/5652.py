# -*- coding: utf-8 -*-
# ======================================
# @File    : 5652.py
# @Time    : 2021/1/10 17:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5652. 交换链表中的节点]()
    """
    @timeit
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 1
        q1 = q2 = None
        while p:
            if n == k:
                q1 = p
            n += 1
            p = p.next
        p = head
        i = 1
        while p:
            if i == n - k:
                q2 = p
            i += 1
            p = p.next
        if q1.val != q2.val:
            q1.val, q2.val = q2.val, q1.val
        return head

if __name__ == '__main__':
    a = Solution()
    head = [1, 2, 3, 4, 5]
    a.swapNodes(construct_list_node(head), 2)
    head = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
    a.swapNodes(construct_list_node(head), 5)
    head = [1]
    a.swapNodes(construct_list_node(head), 1)
    head = [1, 2]
    a.swapNodes(construct_list_node(head), 1)
    head = [1, 2, 3]
    a.swapNodes(construct_list_node(head), 2)