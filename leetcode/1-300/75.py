# -*- coding: utf-8 -*-
# ======================================
# @File    : 75.py
# @Time    : 2020/10/7 17:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, l, r = 0, 0, n - 1
        while i < n:
            while l < r and nums[l] == 0: l += 1
            while l < r and nums[r] == 2: r -= 1
            if l == r: break
            if i < r and nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            if i > l and nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            i += 1


if __name__ == '__main__':
    a = Solution()
    x = [2,0,2,1,1,0]
    a.sortColors(x)
    # print(x)
    x = [0,1,0]
    a.sortColors(x)
    print(x)