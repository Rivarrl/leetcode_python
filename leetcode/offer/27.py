# -*- coding: utf-8 -*-
# ======================================
# @File    : 27.py
# @Time    : 2020/5/7 15:53
# @Author  : Rivarrl
# ======================================
# [面试题27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(p):
            if not p: return None
            p.left, p.right = dfs(p.right), dfs(p.left)
            return p
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,7,1,3,6,9])
    a.mirrorTree(x)