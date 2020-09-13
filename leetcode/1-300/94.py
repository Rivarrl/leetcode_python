# -*- coding: utf-8 -*-
# ======================================
# @File    : 94.py
# @Time    : 2020/9/14 0:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
    """
    @timeit
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            stk, p = [], root
            while stk or p:
                if p:
                    stk.append(p)
                    p = p.left
                else:
                    p = stk.pop()
                    res.append(p.val)
                    p = p.right
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,null,2,3])
    a.inorderTraversal(x)