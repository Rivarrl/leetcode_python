# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-03.py
# @Time    : 2020/7/31 21:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.03. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)
    """
    @timeit
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i: return i
            i = max(nums[i], i+1)
        return -1

if __name__ == '__main__':
    a = Solution()
    a.findMagicIndex([0, 2, 3, 4, 5])
    a.findMagicIndex([1, 1, 1])