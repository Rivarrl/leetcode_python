# -*- coding: utf-8 -*-
# ======================================
# @File    : 108.py
# @Time    : 2020/7/3 6:18 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)
    """
    @timeit
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def f(lo, hi):
            if lo > hi: return None
            mi = lo + (hi - lo) // 2
            root = TreeNode(nums[mi])
            root.left = f(lo, mi-1)
            root.right = f(mi+1, hi)
            return root
        return f(0, len(nums)-1)

if __name__ == '__main__':
    a = Solution()
    a.sortedArrayToBST([-10,-3,0,5,9])