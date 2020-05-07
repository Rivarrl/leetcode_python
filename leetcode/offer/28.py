# -*- coding: utf-8 -*-
# ======================================
# @File    : 28.py
# @Time    : 2020/5/7 15:43
# @Author  : Rivarrl
# ======================================
# [面试题28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root, root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,2,3,4,4,3])
    a.isSymmetric(x)
    x = construct_tree_node([1,2,2,null,3,null,3])
    a.isSymmetric(x)
