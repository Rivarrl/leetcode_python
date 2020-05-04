# -*- coding: utf-8 -*-
# ======================================
# @File    : 5387.py
# @Time    : 2020/5/2 22:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numberWays(self, hats: List[List[int]]) -> int:
        # 人选帽子，O(2^40)超时
        from functools import lru_cache
        mod = 10 ** 9 + 7
        n = len(hats)
        @lru_cache(None)
        def dfs(i, s):
            if i == n: return 1
            res = 0
            for h in hats[i]:
                if s & (1 << h) == 0:
                    res += dfs(i+1, s | (1 << h))
                    res %= mod
            return res
        return dfs(0, 0)

    @timeit
    def numberWays2(self, hats: List[List[int]]) -> int:
        # 帽子选人，O(2^10)
        from functools import lru_cache
        mod = 10 ** 9 + 7
        n, tot = len(hats), 0
        hs = {}
        for i in range(n):
            for j in hats[i]:
                if not j in hs:
                    hs[j] = tot
                    tot += 1
        d = {}
        for i in range(n):
            for k in hats[i]:
                x = hs[k]
                d[x] = d.get(x, set()) | {i,}
        @lru_cache(None)
        def dfs(j, s):
            if j == tot:
                # 所有人都有帽子return 1
                return 1 if bin(s).count('1') == n else 0
            # 扔掉帽子j
            res = dfs(j+1, s)
            # 尝试把帽子j依次分配给能分配的所有人
            for i in d[j]:
                if s & (1 << i) == 0:
                    res += dfs(j+1, s | (1 << i))
                    res %= mod
            return res
        return dfs(0, 0)


    @timeit
    def numberWays22(self, hats: List[List[int]]) -> int:
        # 帽子选人，非递归写法
        n = len(hats)
        mod = 10 ** 9 + 7
        m = 1 << n
        dp = [[0] * m for _ in range(41)]
        valid = [[False] * n for _ in range(41)]
        for j in range(n):
            for i in hats[j]:
                valid[i][j] = True
        dp[0][0] = 1
        for h in range(1, 41):
            for s in range(m):
                dp[h][s] = (dp[h][s] + dp[h-1][s]) % mod
                for i in range(n):
                    if (s >> i) & 1 and valid[h][i]:
                        dp[h][s] = (dp[h][s] + dp[h-1][s ^ (1<<i)]) % mod
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    a.numberWays([[3,4],[4,5],[5]])
    a.numberWays([[3,5,1],[3,5]])
    a.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    a.numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]])