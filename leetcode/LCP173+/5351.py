# -*- coding: utf-8 -*-
# ======================================
# @File    : 5351.py
# @Time    : 2020/3/21 23:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Solution:
    """
    [5351. 3n 块披萨](https://leetcode-cn.com/problems/pizza-with-3n-slices/)
    """
    @timeit
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        dp = [[0] * (n//3+1) for _ in range(n)]
        dp2 = [[0] * (n//3+1) for _ in range(n)]
        res = 0
        for i in range(n-1):
            for j in range(n//3):
                dp[i][j+1] = max(slices[i], dp[i-1][j+1], dp[i][j+1])
                if i > 1:
                    dp[i][j+1] = max(dp[i-2][j] + slices[i], dp[i][j+1])
            res = max(res, dp[i][n//3])
        for i in range(1, n):
            for j in range(n//3):
                dp2[i][j+1] = max(slices[i], dp2[i-1][j+1], dp2[i][j+1])
                if i > 1:
                    dp2[i][j+1] = max(dp2[i-2][j] + slices[i], dp2[i][j+1])
            res = max(res, dp2[i][n//3])
        return res

    @timeit
    def maxSizeSlices2(self, slices: List[int]) -> int:
        from functools import lru_cache
        n = len(slices)
        @lru_cache(None)
        def f(i, j, last):
            if j == 0 or i >= n - last: return 0
            return max(f(i + 2, j - 1, last) + slices[i], f(i + 1, j, last))
        return max(f(2, n//3-1, 1) + slices[0], f(1, n//3, 0))



if __name__ == '__main__':
    a = Solution()
    a.maxSizeSlices([1,2,3,4,5,6])
    a.maxSizeSlices([8,9,8,6,1,1])
    a.maxSizeSlices([4,1,2,5,8,3,1,9,7])
    a.maxSizeSlices([3,1,2])
    a.maxSizeSlices([9,5,1,7,8,4,4,5,5,8,7,7])

    a.maxSizeSlices2([1,2,3,4,5,6])
    a.maxSizeSlices2([8,9,8,6,1,1])
    a.maxSizeSlices2([4,1,2,5,8,3,1,9,7])
    a.maxSizeSlices2([3,1,2])
    a.maxSizeSlices2([9,5,1,7,8,4,4,5,5,8,7,7])
