# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-04.py
# @Time    : 2020/8/8 23:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.04. 检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci/)
    """
    @timeit
    def isBalanced(self, root: TreeNode) -> bool:
        def f(p):
            if not p: return 0, True
            left, right = f(p.left), f(p.right)
            return max(left[0], right[0]) + 1, left[1] and right[1] and (abs(left[0]-right[0]) <= 1)
        return f(root)[1]

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.isBalanced(x)
    x = construct_tree_node([1,2,2,3,3,null,null,4,4])
    a.isBalanced(x)