# -*- coding: utf-8 -*-
# ======================================
# @File    : 110.py
# @Time    : 2020/8/17 16:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)
    """
    @timeit
    def isBalanced(self, root: TreeNode) -> bool:
        def f(p):
            if not p: return True, 0
            left = f(p.left)
            right = f(p.right)
            return left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1
        return f(root)[0]


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.isBalanced(x)
    x = construct_tree_node([1,2,2,3,3,null,null,4,4])
    a.isBalanced(x)