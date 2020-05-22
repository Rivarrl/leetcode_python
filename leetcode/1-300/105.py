# -*- coding: utf-8 -*-
# ======================================
# @File    : 105.py
# @Time    : 2020/5/22 17:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
    """
    @timeit
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def f(a, b):
            if not a: return
            p = a[0]
            head = TreeNode(p)
            i = b.index(p)
            if i > 0:
                head.left = f(a[1:i+1], b[:i])
            head.right = f(a[i+1:], b[i+1:])
            return head
        return f(preorder, inorder)

if __name__ == '__main__':
    a = Solution()
    a.buildTree([3,9,20,15,7], [9,3,15,20,7])