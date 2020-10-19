# -*- coding: utf-8 -*-
# ======================================
# @File    : 1621.py
# @Time    : 2020/10/19 12:59 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1621. 大小为 K 的不重叠线段的数目](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)
    """
    @timeit
    def numberOfSets(self, n: int, k: int) -> int:
        """
                    不取          取长1             取长2
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-2][j-1] + .. + dp[j][j-1]
                     dp[i-1][j] = dp[i-2][j] + dp[i-2][j-1] + .. + dp[j][j-1]
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j] - dp[i-2][j]
                 = 2*dp[i-1][j] + dp[i-1][j-1] - dp[i-2][j]
        """
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1): dp[i][0] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                if j > i - 1: break
                dp[i][j] = 2*dp[i-1][j] + dp[i-1][j-1] - dp[i-2][j]
        return dp[n][k] % (10 ** 9 + 7)

    @timeit
    def numberOfSets2(self, n: int, k: int) -> int:
        # 组合数
        import math
        return math.comb(n+k-1, k*2) % (10 ** 9 + 7)


if __name__ == '__main__':
    a = Solution()
    a.numberOfSets(4, 2)
    a.numberOfSets(3, 1)
    a.numberOfSets(30, 7)
    a.numberOfSets(5, 3)
    a.numberOfSets(3, 2)
    a.numberOfSets2(4, 2)