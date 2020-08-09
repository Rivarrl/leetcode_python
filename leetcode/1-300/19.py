# -*- coding: utf-8 -*-
# ======================================
# @File    : 19.py
# @Time    : 2020/8/8 23:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [19. 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)
    """
    cur = 0
    @timeit
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            head.next = self.removeNthFromEnd(head.next, n)
            self.cur += 1
            if n == self.cur:
                return head.next
        return head


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.removeNthFromEnd(x, 2)
    x = construct_list_node([1])
    a.removeNthFromEnd(x, 1)