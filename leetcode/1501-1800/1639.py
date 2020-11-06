# -*- coding: utf-8 -*-
# ======================================
# @File    : 1639.py
# @Time    : 2020/11/6 1:23 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1639. 通过给定词典构造目标字符串的方案数]()
    """
    @timeit
    def numWays(self, words: List[str], target: str) -> int:
        from collections import defaultdict
        need = set(e for e in target)
        mod = 10 ** 9 + 7
        n = len(words)
        m = len(words[0])
        q = len(target)
        count = [defaultdict(int) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                if words[i][j] in need:
                    count[j][words[i][j]] += 1
        dp = [[0] * q for _ in range(m)]
        dp[0][0] = count[0][target[0]]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + count[j][target[0]]
            for k in range(1, q):
                dp[j][k] = dp[j-1][k-1] * count[j][target[k]] + dp[j-1][k]
        return dp[-1][-1] % mod

if __name__ == '__main__':
    a = Solution()
    a.numWays(words = ["acca","bbbb","caca"], target = "aba")
    a.numWays(words = ["abba","baab"], target = "bab")
    a.numWays(words = ["abcd"], target = "abcd")
    a.numWays(words = ["abab","baba","abba","baab"], target = "abba")