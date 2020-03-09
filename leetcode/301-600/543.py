# -*- coding: utf-8 -*-
# ======================================
# @File    : 543.py
# @Time    : 2020/3/10 0:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/)
    """
    @timeit
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(p):
            if not p: return 0, 0, 0
            if not p.left and not p.right: return 0, 0, 0
            a, b, c = 0, 0, 0
            if p.left:
                ll, lr, lm = dfs(p.left)
                a = max(ll, lr) + 1
                c = max(c, lm)
            if p.right:
                rl, rr, rm = dfs(p.right)
                b = max(rl, rr) + 1
                c = max(c, rm)
            return a, b, max(a + b, c)
        return dfs(root)[-1]


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,5,null,null])
    a.diameterOfBinaryTree(x)