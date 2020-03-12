# -*- coding: utf-8 -*-
# ======================================
# @File    : 55-1.py
# @Time    : 2020/3/13 0:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# [面试题55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)
class Solution:
    @timeit
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(p):
            if not p: return 0
            return max(dfs(p.left), dfs(p.right)) + 1
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.maxDepth(x)
