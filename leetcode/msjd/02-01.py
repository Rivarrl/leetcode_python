# -*- coding: utf-8 -*-
# ======================================
# @File    : 02-01.py
# @Time    : 2020/6/26 0:51
# @Author  : Rivarrl
# ======================================
# [面试题 02.01. 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head: return head
        d = set()
        arr = []
        while head:
            if head.val not in d:
                d.add(head.val)
                arr.append(head)
            head = head.next
        res = p = arr[0]
        for x in arr[1:]:
            p.next = x
            p = p.next
        p.next = None
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1, 2, 3, 3, 2, 1])
    a.removeDuplicateNodes(x)
    # x = construct_list_node([1,1,1,1,2])
    # a.removeDuplicateNodes(x)