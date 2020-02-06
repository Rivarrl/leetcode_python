# -*- coding: utf-8 -*-
# ======================================
# @File    : 5330.py
# @Time    : 2020/2/2 10:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1339. 分裂二叉树的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree/)
    """
    @timeit
    def maxProduct(self, root: TreeNode) -> int:
        arr = []
        def dfs(p):
            if not p: return 0
            ret = p.val + dfs(p.left) + dfs(p.right)
            arr.append(ret)
            return ret
        dfs(root)
        n = len(arr)
        mod = 10 ** 9 + 7
        res = 0
        for i in range(n-1):
            res = max(res, arr[i] * (arr[-1] - arr[i]))
        return res % mod

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,3,9,10,7,8,6,5,4,11,1])
    a.maxProduct(x)
