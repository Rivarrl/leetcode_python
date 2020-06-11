# -*- coding: utf-8 -*-
# ======================================
# @File    : 15.py
# @Time    : 2020/6/12 0:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [15. 三数之和](https://leetcode-cn.com/problems/3sum/)
    """
    @timeit
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        nums = sorted(d.keys())
        n = len(nums)
        for i, x in enumerate(nums):
            if x < 0:
                # 分别求两个边界
                target = -x
                lo, hi = i + 1, n
                while lo < hi:
                    mi = lo + (hi - lo) // 2
                    if nums[mi] >= target - nums[-1]:
                        hi = mi
                    else:
                        lo = mi + 1
                left = lo
                hi = n
                while lo < hi:
                    mi = lo + (hi - lo) // 2
                    if nums[mi] <= target // 2:
                        lo = mi + 1
                    else:
                        hi = mi
                right = lo
                for j in nums[left:right]:
                    k = target - j
                    if k in d and k != j:
                        res.append([x, j, k])
            if d[x] > 1:
                if x == 0:
                    if d[x] >= 3:
                        res.append([0, 0, 0])
                elif -2*x in d:
                    if x > 0:
                        res.append([-2*x, x, x])
                    else:
                        res.append([x, x, -2*x])
        return res

if __name__ == '__main__':
    a = Solution()
    # a.threeSum([-1,0,1,2,-1,-4])
    a.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5])
