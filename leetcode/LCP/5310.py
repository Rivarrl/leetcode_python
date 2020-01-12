# -*- coding: utf-8 -*-
# ======================================
# @File    : 5310
# @Time    : 2020/1/12 14:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5310. 二指输入的的最小距离]()
    """
    @timeit
    def minimumDistance(self, word: str) -> int:
        from functools import lru_cache
        def score(x, y):
            if x == '': return 0
            w1, w2 = ord(x) - ord('A'), ord(y) - ord('A')
            return abs(w1 % 6 - w2 % 6) + abs(w1 // 6 - w2 // 6)
        @lru_cache(None)
        def dfs(x, y, k):
            if k == len(word):
                return 0
            if x == '': return dfs(word[k], y, k+1)
            return min(score(y, word[k]) + dfs(x, word[k], k+1), score(x, word[k]) + dfs(word[k], y, k+1))
        return dfs('', '', 0)

    @timeit
    def minimumDistance2(self, word: str) -> int:
        inf = 0x3f3f3f3f
        n = len(word)
        dp = [[[inf] * (n+1) for _ in range(26)] for _ in range(26)]
        dist = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(26):
                dp[i][j][0] = 0
                dist[i][j] = abs(i % 6 - j % 6) + abs(i // 6 - j // 6)
        for k in range(n):
            x = ord(word[k]) - ord('A')
            for i in range(26):
                for j in range(26):
                    dp[i][x][k+1] = min(dp[i][x][k+1], dp[i][j][k] + dist[x][j])
                    dp[x][j][k+1] = min(dp[x][j][k+1], dp[i][j][k] + dist[i][x])
        res = inf
        for i in range(26):
            for j in range(26):
                res = min(res, dp[i][j][n])
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumDistance(word = "CAKE")
    a.minimumDistance(word = "HAPPY")
    a.minimumDistance(word = "NEW")
    a.minimumDistance(word = "YEAR")