# -*- coding: utf-8 -*-
# ======================================
# @File    : 404.py
# @Time    : 2020/9/19 0:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [404. 左叶子之和](https://leetcode-cn.com/problems/sum-of-left-leaves/)
    """
    @timeit
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, isl):
            if root:
                if not root.left and not root.right and isl:
                    ans[-1] += root.val
                if root.left:
                    helper(root.left, True)
                if root.right:
                    helper(root.right, False)
        ans = [0]
        helper(root, False)
        return ans[-1]

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.sumOfLeftLeaves(x)