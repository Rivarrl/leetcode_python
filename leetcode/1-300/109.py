# -*- coding: utf-8 -*-
# ======================================
# @File    : 109.py
# @Time    : 2020/8/18 12:56 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)
    """
    @timeit
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        pre, slow, fast = None, head, head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        t = slow.next
        if not pre:
            left = None
        else:
            pre.next = None
            left = self.sortedListToBST(head)
        right = self.sortedListToBST(t)
        root = TreeNode(slow.val)
        root.left = left
        root.right = right
        return root

if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([-10, -3, 0, 5, 9, 6])
    a.sortedListToBST(x)