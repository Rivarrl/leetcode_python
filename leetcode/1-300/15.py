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
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n-2):
            if a > 0 and nums[a] == nums[a-1]: continue
            b, c = a + 1, n - 1
            while b < c:
                if nums[a] + nums[b] + nums[c] > 0:
                    while b < c and nums[c] == nums[c-1]:
                        c -= 1
                    c -= 1
                elif nums[a] + nums[b] + nums[c] < 0:
                    while b < c and nums[b] == nums[b+1]:
                        b += 1
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    while b < c and nums[c] == nums[c-1]:
                        c -= 1
                    c -= 1
                    while b < c and nums[b] == nums[b+1]:
                        b += 1
                    b += 1
        return res

    @timeit
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        nums = sorted(d.keys())
        n = len(nums)
        for i, a in enumerate(nums):
            if a < 0:
                # 分别求两个边界
                target = -a
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
                for b in nums[left:right]:
                    c = target - b
                    if c in d and c != b:
                        res.append([a, b, c])
            if d[a] > 1:
                if a == 0:
                    if d[a] >= 3:
                        res.append([0, 0, 0])
                elif -2*a in d:
                    if a > 0:
                        res.append([-2*a, a, a])
                    else:
                        res.append([a, a, -2*a])
        return res

if __name__ == '__main__':
    a = Solution()
    a.threeSum([-1,0,1,2,-1,-4])
    # a.threeSum2([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5])
