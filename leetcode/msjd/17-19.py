# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-19.py
# @Time    : 2020/6/6 8:34
# @Author  : Rivarrl
# ======================================
# [面试题 17.19. 消失的两个数字](https://leetcode-cn.com/problems/missing-two-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums = [0] + nums + [-1, -1]
        for i in range(1, len(nums)):
            while nums[i] != -1 and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == -1:
                res.append(i)
            if len(res) == 2:
                break
        return res

if __name__ == '__main__':
    a = Solution()
    a.missingTwo([1])
    a.missingTwo([2,3])