# -*- coding: utf-8 -*-
# ======================================
# @File    : 16.py
# @Time    : 2020/6/24 1:29 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)
    """
    @timeit
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res, m = 0, 0x3f3f3f3f
        for i in range(n):
            a = nums[i]
            j, k = i+1, n-1
            while j < k:
                b, c = nums[j], nums[k]
                d = a + b + c
                if d < target:
                    j += 1
                elif d > target:
                    k -= 1
                else:
                    return target
                if abs(d - target) < m:
                    m = abs(d - target)
                    res = d
        return res

if __name__ == '__main__':
    a = Solution()
    a.threeSumClosest([-1,2,1,4], 1)
