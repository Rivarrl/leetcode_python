# -*- coding: utf-8 -*-
# ======================================
# @File    : 1723.py
# @Time    : 2021/1/10 19:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1723. 完成所有工作的最短时间](https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/)
    """
    @timeit
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort()
        inf = 0x3f3f3f3f
        n = len(jobs)
        tot = [0] * (1 << n)
        for i in range(1, 1 << n):
            for j in range(n):
                if (i & (1 << j)) == 0: continue
                tot[i] = tot[i ^ (1 << j)] + jobs[j]
                break

        def f(x):
            dp = [inf] * (1 << n)
            dp[0] = 0
            for i in range(1, 1 << n):
                j = i
                while j:
                    if tot[j] <= x:
                        dp[i] = min(dp[i], dp[i ^ j] + 1)
                    j = (j - 1) & i
            return dp[-1] <= k

        lo, hi = max(jobs), sum(jobs)
        while lo < hi:
            mi = lo + hi >> 1
            if f(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo

if __name__ == '__main__':
    a = Solution()
    # a.minimumTimeRequired(jobs = [3,2,3], k = 3)
    a.minimumTimeRequired(jobs = [1,2,4,7,8], k = 2)