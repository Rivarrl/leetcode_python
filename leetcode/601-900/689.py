# -*- coding: utf-8 -*-
# ======================================
# @File    : 689.py
# @Time    : 2020/12/23 10:01 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [689. 三个无重叠子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
    """
    @timeit
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp1, dp2, dp3 = [0] * n, [0] * n, [0] * n
        mx1 = mx2 = mx3 = cur = 0
        for i in range(n):
            cur += nums[i]
            if i >= k: cur -= nums[i-k]
            if i >= k - 1:
                mx1 = max(mx1, cur)
                dp1[i] = mx1
                if i >= 2 * k - 1:
                    mx2 = max(mx2, cur + dp1[i - k])
                    dp2[i] = mx2
                    if i >= 3 * k - 1:
                        mx3 = max(mx3, cur + dp2[i - k])
                        dp3[i] = mx3
        res = [0] * 3
        mx3 = max(dp3)
        res[2] = dp3.index(mx3)
        mx2 = max(dp2[:res[2] - k + 1])
        res[1] = dp2.index(mx2)
        mx1 = max(dp1[:res[1] - k + 1])
        res[0] = dp1.index(mx1)
        return [i+1-k for i in res]

if __name__ == '__main__':
    a = Solution()
    # a.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
    a.maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3], 1)