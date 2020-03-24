# -*- coding: utf-8 -*-
# ======================================
# @File    : 55-2.py
# @Time    : 2020/3/24 14:29
# @Author  : Rivarrl
# ======================================
# [面试题55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(p):
            nonlocal res
            if not p: return 0
            left, right = dfs(p.left), dfs(p.right)
            if abs(left - right) > 1:
                res = False
            return max(left, right) + 1
        res = True
        dfs(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.isBalanced(x)
    x = construct_tree_node([1,2,2,3,3,null,null,4,4,null,null,null,null,null,null])
    a.isBalanced(x)