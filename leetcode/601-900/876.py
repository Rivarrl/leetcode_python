# -*- coding: utf-8 -*-
# ======================================
# @File    : 876.py
# @Time    : 2020/3/23 9:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/)
    """
    @timeit
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast else slow


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.middleNode(x)
    x = construct_list_node([1,2,3,4,5,6])
    a.middleNode(x)