# -*- coding: utf-8 -*-
# ======================================
# @File    : 5276.py
# @Time    : 2019/11/9 16:30
# @Author  : Rivarrl
# ======================================

from algorithm_utils import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
        思路：题出绕了，其实是想降低难度，反向表示可以使得l1和l2的个位对齐，方便顺序求和
        """
        res = p = ListNode(0)
        plus1 = 0
        while l1 or l2:
            if not l1:
                c = l2.val + plus1
                plus1, r = c // 10, c % 10
                l2 = l2.next
            elif not l2:
                c = l1.val + plus1
                plus1, r = c // 10, c % 10
                l1 = l1.next
            else:
                c = l1.val + l2.val + plus1
                plus1, r = c // 10, c % 10
                l1, l2 = l1.next, l2.next
            p.next = ListNode(r)
            p = p.next
        if plus1 == 1:
            p.next = ListNode(1)
        return res.next


if __name__ == '__main__':
    l1, l2 = construct_list_node([9,8,7]), construct_list_node([1,1,2])
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    list_node_print(res)