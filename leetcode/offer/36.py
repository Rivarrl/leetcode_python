# -*- coding: utf-8 -*-
# ======================================
# @File    : 36.py
# @Time    : 2020/5/6 20:54
# @Author  : Rivarrl
# ======================================
# [面试题36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/comments/)
from algorithm_utils import *

class Solution:
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        if not root: return root
        stk = []
        last = head = tail = None
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            tail = root
            if last:
                last.right = root
                root.left = last
            else:
                head = root
            last = root
            root = root.right
        head.left, tail.right = tail, head
        return head

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,5,1,3])
    a.treeToDoublyList(x)
