# -*- coding: utf-8 -*-
# ======================================
# @File    : 112.py
# @Time    : 2020/7/7 9:48 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)
    """
    @timeit
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def f(p, s):
            s += p.val
            if not p.left and not p.right:
                return s == sum
            res = False
            if p.left:
                res = f(p.left, s) or res
            if res: return True
            if p.right:
                res = f(p.right, s) or res
            return res
        return False if not root else f(root, 0)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,4,8,11,null,13,4,7,2,null,null,null,null,null,1])
    a.hasPathSum(x, 22)