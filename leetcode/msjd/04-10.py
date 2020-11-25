# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-10.py
# @Time    : 2020/11/25 8:59 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.10. 检查子树](https://leetcode-cn.com/problems/check-subtree-lcci/)
    """
    @timeit
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def eq(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2 or t1.val != t2.val: return False
            return eq(t1.left, t2.left) and eq(t1.right, t2.right)
        def is_child(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return eq(t1, t2) or is_child(t1.left, t2) or is_child(t1.right, t2)
        return is_child(t1, t2)

if __name__ == '__main__':
    a = Solution()
    t1, t2 = construct_tree_node([1,2,3]), construct_tree_node([2])
    a.checkSubTree(t1, t2)
    t1, t2 = construct_tree_node([1,null,2,4]), construct_tree_node([3,2])
    a.checkSubTree(t1, t2)