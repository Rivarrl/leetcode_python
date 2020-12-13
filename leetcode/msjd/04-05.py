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
        def f(p):
            if not p: return True
            if p.left

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,1,3])
    a.isValidBST(x)
    x = construct_tree_node([5,1,4,null,null,3,6])
    a.isValidBST(x)