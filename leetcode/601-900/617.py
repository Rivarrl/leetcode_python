# -*- coding: utf-8 -*-
# ======================================
# @File    : 617.py
# @Time    : 2020/9/23 0:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)
    """
    @timeit
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def f(t1, t2):
            if t1 and t2:
                t1.val += t2.val
                t1.left = f(t1.left, t2.left)
                t1.right = f(t1.right, t2.right)
            return t1 or t2
        return f(t1, t2)

if __name__ == '__main__':
    a = Solution()
    t1 = construct_tree_node([1,3,2,5])
    t2 = construct_tree_node([2,1,3,null,4,null,7])
    a.mergeTrees(t1, t2)