# -*- coding: utf-8 -*-
# ======================================
# @File    : 226.py
# @Time    : 2020/5/7 15:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
    """
    @timeit
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        stk = [root]
        while stk:
            p = stk.pop()
            if p.left: stk.append(p.left)
            if p.right: stk.append(p.right)
            p.left, p.right = p.right, p.left
        return root

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,7,1,3,6,9])
    a.invertTree(x)