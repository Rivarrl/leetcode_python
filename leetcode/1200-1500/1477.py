# -*- coding: utf-8 -*-
# ======================================
# @File    : 1477.py
# @Time    : 2020/6/28 5:39 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1477. 找两个和为目标值且不重叠的子数组](https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)
    """
    @timeit
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        d = {0:-1}
        n = len(arr)
        c = 0
        res = n + 1
        dp = [n+1] * n
        for i in range(n):
            c += arr[i]
            if i > 0: dp[i] = dp[i-1]
            if c - target in d:
                j = d[c-target]
                if j != -1:
                    res = min(res, dp[j] + i - j)
                dp[i] = min(dp[i], i - j)
            d[c] = i
        return res if res < n + 1 else -1

if __name__ == '__main__':
    a = Solution()
    a.minSumOfLengths(arr = [3,2,2,4,3], target = 3)
    a.minSumOfLengths(arr = [7,3,4,7], target = 7)
    a.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6)
    a.minSumOfLengths(arr = [5,5,4,4,5], target = 3)
    a.minSumOfLengths(arr = [3,1,1,1,5,1,2,1], target = 3)