# -*- coding: utf-8 -*-
# ======================================
# @File    : 46.py
# @Time    : 2020/5/2 14:06
# @Author  : Rivarrl
# ======================================
# [面试题46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def translateNum(self, num: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def helper(s):
            if len(s) == 1: return 1
            if len(s) == 2: return 2 if 0 < int(s[0]) <= 2 and int(s[:2]) < 26 else 1
            res = helper(s[1:])
            if 0 < int(s[0]) <= 2 and int(s[:2]) < 26:
                res += helper(s[2:])
            return res
        return helper(str(num))

    @timeit
    def translateNum2(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1]
            if 10 <= int(s[i-2:i]) < 26:
                dp[i] += dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    a = Solution()
    a.translateNum2(12258)
    a.translateNum2(25)
