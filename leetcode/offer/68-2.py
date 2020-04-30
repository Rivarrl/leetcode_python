# -*- coding: utf-8 -*-
# ======================================
# @File    : 68-2.py
# @Time    : 2020/4/30 21:00
# @Author  : Rivarrl
# ======================================
# [面试题68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(c):
            if not c: return
            if c in (p, q): return c
            left, right = dfs(c.left), dfs(c.right)
            if left and right: return c
            if left: return left
            if right: return right
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,5,1,6,2,0,8,null,null,7,4])
    p = x.left
    q = x.right
    a.lowestCommonAncestor(x, p, q)
    q = p.right.right
    a.lowestCommonAncestor(x, p, q)