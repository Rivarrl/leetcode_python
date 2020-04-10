# -*- coding: utf-8 -*-
# ======================================
# @File    : 887.py
# @Time    : 2020/4/11 0:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[i][j] 表示第i个抛鸡蛋可以确定的j层需要花费的最小移动次数
        # dp[i][j] = min(max(dp[i-1][k-1], dp[i][j-k]) for k in range(j)) + 1
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if j == 0: return 0
            if i == 1: return j
            # 二分查找两个候选答案
            lo, hi = 1, j
            while lo + 1 < hi:
                mid = lo + (hi - lo) // 2
                x1, x2 = dp(i-1, mid-1), dp(i, j-mid)
                if x1 == x2:
                    lo = hi = mid
                elif x1 > x2:
                    hi = mid
                else:
                    lo = mid
            return min(max(dp(i-1, k-1), dp(i, j-k)) for k in (lo, hi)) + 1
        return dp(K, N)

    @timeit
    def superEggDrop2(self, K: int, N: int) -> int:
        # 逆向思维，dp[i][j]表示i个鸡蛋操作j次能达到的最大楼层数，找出最小满足dp[i][j]>=N的j
        # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + 1
        # 操作数不会超过N
        dp = [[0] * (N+1) for _ in range(K+1)]
        j = 0
        while dp[K][j] < N:
            j += 1
            for i in range(1, K+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + 1
        return j

    @timeit
    def superEggDrop3(self, K: int, N: int) -> int:
        # minmax问题，用二分查找答案
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans
        lo, hi = 1, N
        while lo < hi:
            mid = lo + hi >> 1
            if f(mid) < N:
                lo = mid + 1
            else:
                hi = mid
        return lo


    @timeit
    def superEggDrop4(self, K: int, N: int) -> int:
        # 官方题解知识点：决策单调性
        # 个人理解，做法简单来说就是随着K值的不断增加，最后答案确定f(K,N)
        # 这样做是因为每次固定了K值，那么dp的前半部分dp(k-1,x-1)与n值无关，后半部分dp(k,n-x)随n的增加而单调递增
        # 故整体值随n是单调递增的
        dp = list(range(N+1))
        dp2 = [0] * (N+1)
        for k in range(2, K+1):
            x = 1
            for n in range(1, N+1):
                while x < n and max(dp[x-1], dp2[n-x]) >= max(dp[x], dp2[n-x-1]):
                    x += 1
                dp2[n] = max(dp[x-1], dp2[n-x]) + 1
            dp = dp2[:]
        return dp[-1]



if __name__ == '__main__':
    a = Solution()
    a.superEggDrop2(K = 1, N = 2)
    a.superEggDrop2(K = 2, N = 6)
    a.superEggDrop2(2, 7)
    a.superEggDrop2(K = 3, N = 14)
    a.superEggDrop2(100,10000)