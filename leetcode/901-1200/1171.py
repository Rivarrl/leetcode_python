# -*- coding: utf-8 -*-
# ======================================
# @File    : 1171.py
# @Time    : 2019/12/7 15:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1171. 从链表中删去总和值为零的连续节点](https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
    """
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """
        思路:前缀和判重，配合栈弹出字典用
        """
        pre = {}
        p = ListNode(0)
        p.next = head
        pre[0] = p
        stk = [0]
        s = 0
        while head:
            s += head.val
            if s in pre:
                pre[s].next = head.next
                while stk[-1] != s:
                    pre.pop(stk.pop())
            else:
                pre[s] = head
                stk.append(s)
            head = head.next
        return p.next

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1,3,2,-3,-2,5,5,-5,1])
    r = a.removeZeroSumSublists(x)
    print_list_node(r)
