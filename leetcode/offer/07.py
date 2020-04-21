# -*- coding: utf-8 -*-
# ======================================
# @File    : 07.py
# @Time    : 2020/4/21 13:14
# @Author  : Rivarrl
# ======================================
# [面试题07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre, ino):
            if not pre: return None
            cur = TreeNode(pre[0])
            i = ino.index(pre[0])
            cur.left = helper(pre[1:i+1], ino[:i])
            cur.right = helper(pre[i+1:], ino[i+1:])
            return cur
        return helper(preorder, inorder)

if __name__ == '__main__':
    a = Solution()
    a.buildTree([3,9,20,15,7], [9,3,15,20,7])
    a.buildTree([1,2], [2,1])
    a.buildTree([], [])
    a.buildTree([1,2], [1,2])
    a.buildTree([1,2,3],[3,2,1])