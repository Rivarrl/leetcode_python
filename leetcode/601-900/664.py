# -*- coding: utf-8 -*-
# ======================================
# @File    : 664
# @Time    : 2020/1/9 11:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [664. 奇怪的打印机](https://leetcode-cn.com/problems/strange-printer/)
    """
    @timeit
    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j):
            if i > j: return 0
            while i < j and s[i] == s[i+1]:
                i += 1
            res = dfs(i+1, j) + 1
            for p in range(i+1, j+1):
                if s[p] == s[i]:
                    res = min(res, dfs(i+1, p-1) + dfs(p, j))
            return res
        return dfs(0, len(s) - 1)


if __name__ == '__main__':
    a = Solution()
    a.strangePrinter("aaabbb")
    a.strangePrinter("aba")