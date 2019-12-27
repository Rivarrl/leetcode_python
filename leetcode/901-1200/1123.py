# -*- coding: utf-8 -*-
# ======================================
# @File    : 1123.py
# @Time    : 2019/12/28 0:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1123. 最深叶节点的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/)
    """
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(p):
            if not p: return 0, None
            left, right = dfs(p.left), dfs(p.right)
            if left[0] > right[0]:
                c, x = left
            elif left[0] < right[0]:
                c, x = right
            else:
                c, x = left[0], p
            return c + 1, x
        return dfs(root)[1]


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3])
    a.lcaDeepestLeaves(x)
    x = construct_tree_node([1,2,3,4])
    a.lcaDeepestLeaves(x)
    x = construct_tree_node([1,2,3,4,5])
    a.lcaDeepestLeaves(x)
