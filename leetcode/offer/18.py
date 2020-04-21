# -*- coding: utf-8 -*-
# ======================================
# @File    : 18.py
# @Time    : 2020/4/21 16:47
# @Author  : Rivarrl
# ======================================
# [面试题18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p = head
        if p and p.val == val: return head.next
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
                break
            p = p.next
        return head


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([4,5,1,9])
    a.deleteNode(x, 5)
    x = construct_list_node([4,5,1,9])
    a.deleteNode(x, 1)
    x = construct_list_node([-3,5,-99])
    a.deleteNode(x, -3)