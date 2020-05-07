# -*- coding: utf-8 -*-
# ======================================
# @File    : 26.py
# @Time    : 2020/5/7 16:00
# @Author  : Rivarrl
# ======================================
# [面试题26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def f(p, q):
            if not q: return True
            if not p: return False
            return p.val == q.val and f(p.left, q.left) and f(p.right, q.right)
        def g(p, q):
            if not p or not q: return False
            return f(p, q) or g(p.left, B) or g(p.right, B)
        return g(A, B)


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3])
    y = construct_tree_node([3,1])
    a.isSubStructure(x, y)
    x = construct_tree_node([3,4,5,1,2])
    y = construct_tree_node([4,1])
    a.isSubStructure(x, y)