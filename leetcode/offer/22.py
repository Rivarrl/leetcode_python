# -*- coding: utf-8 -*-
# ======================================
# @File    : 22.py
# @Time    : 2020/5/7 19:21
# @Author  : Rivarrl
# ======================================
# [面试题22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        p = head
        for _ in range(n - k):
            p = p.next
        return p


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.getKthFromEnd(x, 2)