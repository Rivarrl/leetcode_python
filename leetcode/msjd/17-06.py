# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-06.py
# @Time    : 2020/6/30 21:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.06. 2出现的次数](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/)
    """
    @timeit
    def numberOf2sInRange(self, n: int) -> int:
        # 数位dp，按每一位递推，所有判断情况如下：
        # dp[02] = dp[2]
        # dp[123] = dp[23] + dp[99]
        # dp[233] = dp[33] + dp[99] * 2 + 33
        # dp[543] = dp[43] + dp[99] * 5 + 100
        # dp[i][0]记录答案，dp[i][1]记录对应位的dp[9..9]值
        import math
        digit = int(math.log10(n)) + 1
        dp = [[0, 0] for _ in range(digit+1)]
        dp[1][0] = 1 if n % 10 >= 2 else 0
        dp[1][1] = 1
        for i in range(2, digit+1):
            k = n // (10 ** (i-1)) % 10
            dp[i][0] = k * dp[i-1][1] + dp[i-1][0]
            if k == 2:
                dp[i][0] += n % (10 ** (i-1)) + 1
            elif k > 2:
                dp[i][0] += 10 ** (i-1)
            dp[i][1] = 10 * dp[i-1][1] + 10 ** (i-1)
        return dp[digit][0]


if __name__ == '__main__':
    a = Solution()
    a.numberOf2sInRange(25)