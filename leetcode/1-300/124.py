# -*- coding: utf-8 -*-
# ======================================
# @File    : 124.py
# @Time    : 2020/6/21 14:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)
    """
    @timeit
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            p = MIN
            if root:
                p = root.val
                l = helper(root.left)
                r = helper(root.right)
                cur = max(p, p+l, p+r)
                self.ans = max(self.ans, cur, l, r, p+l+r)
                p = cur
            return p
        MIN = -2**31
        self.ans = MIN
        helper(root)
        return self.ans

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3])
    a.maxPathSum(x)
    x = construct_tree_node([-10,9,20,null,null,15,7])
    a.maxPathSum(x)