# -*- coding: utf-8 -*-
# ======================================
# @File    : 5322.py
# @Time    : 2020/1/26 11:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1335. 工作计划的最低难度](https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule/)
    """
    @timeit
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        from functools import lru_cache
        n = len(jobDifficulty)
        if n < d: return -1
        @lru_cache(None)
        def dfs(i, j):
            p = d - j
            if p == 0: return max(jobDifficulty[i:]) if jobDifficulty[i:] else inf
            if i == n: return 0
            res = inf
            m = 0
            for k in range(i, n - p):
                m = max(m, jobDifficulty[k])
                res = min(res, m + dfs(k+1, j+1))
            return res
        inf = 0x3f3f3f3f
        return dfs(0, 1)


if __name__ == '__main__':
    a = Solution()
    a.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2)
    a.minDifficulty(jobDifficulty = [9,9,9], d = 4)
    a.minDifficulty(jobDifficulty = [1,1,1], d = 3)
    a.minDifficulty(jobDifficulty = [7,1,7,1,7,1], d = 3)
    a.minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6)