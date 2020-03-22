# -*- coding: utf-8 -*-
# ======================================
# @File    : 5179.py
# @Time    : 2020/3/15 10:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1382. 将二叉搜索树变平衡](https://leetcode-cn.com/problems/balance-a-binary-search-tree/)
    """
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(p):
            if not p: return
            dfs(p.left)
            res.append(p)
            dfs(p.right)
        def dfs1(arr):
            if len(arr) == 0: return
            lo, hi = 0, len(arr)-1
            mid = lo + hi >> 1
            p = arr[mid]
            p.left = dfs1(arr[:mid])
            p.right = dfs1(arr[mid+1:])
            return p
        res = []
        dfs(root)
        return dfs1(res)


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,null,2,null,null,null,3,null,null,null,null,null,null,null,4])
    res = a.balanceBST(x)
    tree_node_print(res)