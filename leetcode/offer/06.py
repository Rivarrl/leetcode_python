# -*- coding: utf-8 -*-
# ======================================
# @File    : 06.py
# @Time    : 2020/4/21 13:11
# @Author  : Rivarrl
# ======================================
# [面试题06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def reversePrint(self, head: ListNode) -> List[int]:
        def dfs(p):
            if not p: return []
            return dfs(p.next) + [p.val]
        return dfs(head)


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,3,2])
    a.reversePrint(x)