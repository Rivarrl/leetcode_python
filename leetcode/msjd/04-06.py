# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-06.py
# @Time    : 2020/12/14 23:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.06. 后继者](https://leetcode-cn.com/problems/successor-lcci/)
    """
    @timeit
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        def f(root):
            if not root or not p: return None
            if root.val <= p.val: return f(root.right)
            if root.val > p.val: return f(root.left) or root
        return f(root)