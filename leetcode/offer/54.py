# -*- coding: utf-8 -*-
# ======================================
# @File    : 54.py
# @Time    : 2020/4/30 20:50
# @Author  : Rivarrl
# ======================================
# [面试题54. 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(p):
            nonlocal x, res
            if p.right:
                dfs(p.right)
            x += 1
            if x == k:
                res = p.val
            if p.left:
                dfs(p.left)
        x = res = 0
        dfs(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,1,4,null,2])
    a.kthLargest(x, 1)
    x = construct_tree_node([5,3,6,2,4,null,null,1])
    a.kthLargest(x, 3)