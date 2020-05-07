# -*- coding: utf-8 -*-
# ======================================
# @File    : 572.py
# @Time    : 2020/5/7 0:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [572. 另一个树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree/)
    """
    @timeit
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def f(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and f(s.left, t.left) and f(s.right, t.right)
        def g(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return f(s, t) or g(s.left, t) or g(s.right, t)
        return g(s, t)

if __name__ == '__main__':
    a = Solution()
    s = construct_tree_node([3,4,5,1,2])
    t = construct_tree_node([4,1,2])
    a.isSubtree(s, t)
    s = construct_tree_node([3,4,5,1,2,null,null,null,0])
    a.isSubtree(s, t)