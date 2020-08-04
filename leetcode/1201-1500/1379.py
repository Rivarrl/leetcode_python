# -*- coding: utf-8 -*-
# ======================================
# @File    : 1379.py
# @Time    : 2020/4/20 21:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1379. 找出克隆二叉树中的相同节点](https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
    """
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(o, c, t):
            if t is o: return c
            res = None
            if o.left:
                res = helper(o.left, c.left, t)
            if res: return res
            if o.right:
                res = helper(o.right, c.right, t)
            return res
        return helper(original, cloned, target)

if __name__ == '__main__':
    a = Solution()