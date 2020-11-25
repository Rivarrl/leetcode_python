# -*- coding: utf-8 -*-
# ======================================
# @File    : 164.py
# @Time    : 2020/11/26 0:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [164. 最大间距](https://leetcode-cn.com/problems/maximum-gap/)
    """
    @timeit
    def maximumGap(self, nums: List[int]) -> int:
        # 基数排序
        if len(nums) < 2: return 0
        max_num = max(nums)
        _MAX_DIGIT = 1
        while max_num >= 10:
            max_num //= 10
            _MAX_DIGIT += 1
        n = len(nums)
        digit = 1
        pos = [0] * 10
        for i in range(_MAX_DIGIT):
            for j in range(10):
                pos[j] = 0
            tmp = [x for x in nums]
            for x in tmp:
                k = (x // digit) % 10
                pos[k] += 1
            for j in range(1, 10):
                pos[j] += pos[j - 1]
            for i in range(n - 1, -1, -1):
                base = tmp[i]
                k = (base // digit) % 10
                nums[pos[k] - 1] = base
                pos[k] -= 1
            digit *= 10
        res = 0
        for i in range(1, len(nums)):
            res = max(nums[i] - nums[i-1], res)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maximumGap([3,6,9,1])
    a.maximumGap([10])
    a.maximumGap([1,10000000])