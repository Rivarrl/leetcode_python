# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-02.py
# @Time    : 2020/11/13 1:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 02.02. 返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/)
    """
    @timeit
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        i = n - k
        p = head
        for _ in range(i):
            p = p.next
        return p.val

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,2,3,4,5])
    a.kthToLast(x, 2)