# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-05.py
# @Time    : 2020/12/13 21:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.05. 合法二叉搜索树](https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/)
    """
    @timeit
    def isValidBST(self, root: TreeNode) -> bool:
        inf = float('inf')
        def f(p, lo=-inf, hi=inf):
            if not p: return True
            return lo < p.val < hi and f(p.left, lo, p.val) and f(p.right, p.val, hi)
        return f(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,1,3])
    a.isValidBST(x)
    x = construct_tree_node([5,1,4,null,null,3,6])
    a.isValidBST(x)
    x = construct_tree_node([10,5,15,null,null,6,20])
    a.isValidBST(x)