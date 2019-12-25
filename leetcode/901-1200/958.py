# -*- coding: utf-8 -*-
# ======================================
# @File    : 958.py
# @Time    : 2019/12/26 0:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [958. 二叉树的完全性检验](https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/)
    """
    @timeit
    def isCompleteTree(self, root: TreeNode) -> bool:
        stk = [root]
        stop = False
        while stk:
            stk1 = []
            while stk:
                p = stk.pop(0)
                if not p: stop = True
                else:
                    if stop: return False
                    stk1.append(p.left)
                    stk1.append(p.right)
            stk = stk1[:]
        return True


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,5,6])
    a.isCompleteTree(x)
    x = construct_tree_node([1,2,3,4,5,null,7])
    a.isCompleteTree(x)
    x = construct_tree_node([1,2,3,5,null,7,8])
    a.isCompleteTree(x)
    x = construct_tree_node([1,2,3,4,5])
    a.isCompleteTree(x)
    x = construct_tree_node([1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15])
    a.isCompleteTree(x)