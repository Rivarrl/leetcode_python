# -*- coding: utf-8 -*-
# ======================================
# @File    : 236.py
# @Time    : 2019/11/17 10:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路：最近公共祖先（LCA）问题，
        """
