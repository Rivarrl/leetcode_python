# -*- coding: utf-8 -*-
# ======================================
# @File    : 45.py
# @Time    : 2020/5/4 17:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def jump(self, nums: List[int]) -> int:
        # O(n^2)选择下一次可跳的最远的
        i = step = 0
        n = len(nums)
        while i < n - 1:
            m = k = 0
            for j in range(1, nums[i]+1):
                if i + j >= n - 1:
                    k = n - 1
                    break
                if j + nums[i+j] >= m:
                    m = j + nums[i+j]
                    k = i + j
            step += 1
            i = k
        return step

    @timeit
    def jump2(self, nums: List[int]) -> int:
        # O(n)本次跳的最远右边界到达之前更新下一次的右边界
        if len(nums) == 1: return 0
        step, j, right = 0, 0, nums[0]
        for i in range(len(nums)):
            right = max(i + nums[i], right)
            if right >= len(nums) - 1: return step + 1
            if i == j:
                step += 1
                j = right
            print(j, right)
        return step

if __name__ == '__main__':
    a = Solution()
    a.jump2([2,3,1,1,4])
    # a.jump2([2,3,1])