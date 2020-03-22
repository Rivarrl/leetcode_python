# -*- coding: utf-8 -*-
# ======================================
# @File    : 5338.py
# @Time    : 2020/3/7 22:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1372. 二叉树中的最长交错路径](https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/)
    """
    @timeit
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(p):
            if not p.left and not p.right: return 0, 0, 0
            ra = rb = rc = 0
            if p.left:
                a, b, c = dfs(p.left)
                ra = max(ra, b + 1)
                rc = max(rc, c)
            if p.right:
                a, b, c = dfs(p.right)
                rb = max(rb, a + 1)
                rc = max(rc, c)
            return ra, rb, max(ra, rb, rc)
        return dfs(root)[2]

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,1,1,null,1,null,null,null,null,1,1,null,null,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,null,null])
    a.longestZigZag(x)
