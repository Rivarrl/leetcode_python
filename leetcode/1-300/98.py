# -*- coding: utf-8 -*-
# ======================================
# @File    : 98.py
# @Time    : 2020/5/5 0:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stk = []
        last = -(1<<32)
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if root.val <= last: return False
            last = root.val
            root = root.right
        return True

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([-2147483648])
    a.isValidBST(x)
    # x = construct_tree_node([5,1,4,null,null,3,6])
    # a.isValidBST(x)
    # x = construct_tree_node([10,5,15,null,null,6,20])
    # a.isValidBST(x)