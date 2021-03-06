# -*- coding: utf-8 -*-
# ======================================
# @File    : 101.py
# @Time    : 2020/5/7 15:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)
    """
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
