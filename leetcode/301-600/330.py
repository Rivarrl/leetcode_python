# -*- coding: utf-8 -*-
# ======================================
# @File    : 330.py
# @Time    : 2019/12/19 1:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [330. 按要求补齐数组](https://leetcode-cn.com/problems/patching-array/)
    """
    @timeit
    def minPatches(self, nums: List[int], n: int) -> int:
        # 贪心算法
        # miss表示可以组成的区间为[1,miss)，miss刚好不能被组成
        ctr = i = 0
        miss = 1
        while miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                ctr += 1
        return ctr

if __name__ == '__main__':
    a = Solution()
    a.minPatches(nums = [1,3], n = 6)
    a.minPatches(nums = [1,5,10], n = 20)
    a.minPatches(nums = [1,2,2], n = 5)
    a.minPatches([], 8)