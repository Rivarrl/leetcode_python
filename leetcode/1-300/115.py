# -*- coding: utf-8 -*-
# ======================================
# @File    : 115.py
# @Time    : 2019/11/11 13:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import defaultdict

class Solution:

    @timeit
    def numDistinct(self, s: str, t: str) -> int:
        """
        [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)
        思路：动态规划，对每个与s[i]相同的字符t[j]对应的dp[j]进行更新，如果j=0，t[j] += 1，其他情况，t[j] += t[j-1]
        """
        if len(s) == 0 or len(t) == 0 or len(s) < len(t): return 0
        n = len(t)
        d = defaultdict(list)
        for i in range(n-1, -1, -1):
            d[t[i]].append(i)
        dp = [0] * n
        for c in s:
            if not c in d:
                continue
            for idx in d[c]:
                dp[idx] += (dp[idx - 1] if idx > 0 else 1)
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.numDistinct("ababaabba", "aabba")