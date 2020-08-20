# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-02.py
# @Time    : 2020/8/17 19:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.02. 最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci/)
    """
    @timeit
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def f(i, j):
            if i > j: return
            if i == j: return TreeNode(nums[i])
            k = i + j >> 1
            root = TreeNode(nums[k])
            root.left = f(i, k-1)
            root.right = f(k+1, j)
            return root
        return f(0, len(nums)-1)


if __name__ == '__main__':
    a = Solution()
    a.sortedArrayToBST([-10,-3,0,5,9])