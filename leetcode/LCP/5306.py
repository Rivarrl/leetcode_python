# -*- coding: utf-8 -*-
# ======================================
# @File    : 5306
# @Time    : 2020/1/5 15:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5306. 让字符串成为回文串的最少插入次数
    """
    @timeit
    def minInsertions(self, s: str) -> int:
        def dfs(i, j):
            if i >= j: return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == s[j]:
                dp[(i, j)] = dfs(i+1, j-1)
            else:
                dp[(i, j)] = min(dfs(i+1, j), dfs(i, j-1)) + 1
            return dp[(i, j)]
        n = len(s)
        dp = {}
        return dfs(0, n-1)


if __name__ == '__main__':
    a = Solution()
    a.minInsertions("leetcode")
    a.minInsertions("mbadm")
    a.minInsertions("g")