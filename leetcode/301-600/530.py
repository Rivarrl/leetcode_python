# -*- coding: utf-8 -*-
# ======================================
# @File    : 530.py
# @Time    : 2020/10/12 9:55 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [530. 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)
    """
    @timeit
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = 0x3f3f3f3f
        last = -1
        def f(p):
            if not p: return
            nonlocal res, last
            f(p.left)
            if last != -1 and p.val - last < res:
                res = p.val - last
            last = p.val
            f(p.right)
            return
        f(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,null,3,null,null,2])
    a.getMinimumDifference(x)
    x = construct_tree_node([5,4,7])
    a.getMinimumDifference(x)