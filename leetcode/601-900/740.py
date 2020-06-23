# -*- coding: utf-8 -*-
# ======================================
# @File    : 740.py
# @Time    : 2020/6/23 1:50 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [740. 删除与获得点数](https://leetcode-cn.com/problems/delete-and-earn/)
    """
    @timeit
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import defaultdict
        if not nums: return 0
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        dp = [0] * (max(d) + 1)
        res = 0
        for i in range(1, max(d)+1):
            c = i * d[i]
            if i >= 3:
                dp[i] = max(dp[i-2], dp[i-3]) + c
            elif i == 2:
                dp[i] = dp[i-2] + c
            else:
                dp[i] = c
            res = max(res, dp[i])
        return res

if __name__ == '__main__':
    a = Solution()
    a.deleteAndEarn(nums=[3, 4, 2])
    a.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4])
