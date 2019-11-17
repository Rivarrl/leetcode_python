# -*- coding: utf-8 -*-
# ======================================
# @File    : 5264.py
# @Time    : 2019/11/17 10:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.d = set()
        self.recover(root, 0)

    def recover(self, p, val):
        p.val = val
        self.d.add(val)
        if p.left:
            self.recover(p.left, val * 2 + 1)
        if p.right:
            self.recover(p.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.d

