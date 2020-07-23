# -*- coding: utf-8 -*-
# ======================================
# @File    : 5435.py
# @Time    : 2020/6/27 22:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5435. 并行课程 II](https://leetcode-cn.com/problems/parallel-courses-ii/)
    """
    @timeit
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 状态压缩dp，枚举全集 py会超时
        def count1(x):
            res = 0
            while x > 0:
                x &= (x - 1)
                res += 1
            return res
        pre = [0] * n
        for u, v in dependencies:
            pre[v-1] |= (1 << (u-1))
        mpre = [0] * (1 << n)
        valid = [0] * (1 << n)
        for mask in range(1 << n):
            if count1(mask) > k: continue
            for i in range(n):
                if mask & (1 << i):
                    mpre[mask] |= pre[i]
            valid[mask] = int(mpre[mask] & mask == 0)
        inf = 0x3f3f3f3f
        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            subset = mask
            while subset > 0:
                if valid[subset] and mask & mpre[subset] == mpre[subset]:
                    dp[mask] = min(dp[mask], dp[mask ^ subset] + 1)
                subset = (subset - 1) & mask
        return dp[-1]

    @timeit
    def minNumberOfSemesters2(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 状态压缩dp，dfs剪枝
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, num, k, s, mask):
            if num - i < k: return
            if k == 0:
                if dp[mask] == -1 or dp[mask] > s:
                    dp[mask] = s
            else:
                dfs(i + 1, num, k - 1, s, mask | (1 << lesson[i]))
                dfs(i + 1, num, k, s, mask)

        dp = [-1] * (1 << n)
        dp[0] = 0
        pre = [0] * n
        for u, v in dependencies:
            pre[v-1] |= 1 << (u - 1)
        for i in range(1 << n):
            if dp[i] == -1: continue
            lesson = []
            for j in range(n):
                # 已经修过 or j的前置课程包含i集合中的课，互相引用
                if i & (1 << j) or pre[j] & i != pre[j]: continue
                lesson.append(j)
            ll = len(lesson)
            dfs(0, ll, min(ll, k), dp[i] + 1, i)
        return dp[-1]


if __name__ == '__main__':
    a = Solution()
    # a.minNumberOfSemesters(n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2)
    # a.minNumberOfSemesters(n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2)
    # a.minNumberOfSemesters(n = 11, dependencies = [], k = 2)
    # a.minNumberOfSemesters(n = 5, dependencies = [[3,1]], k = 4)
    # a.minNumberOfSemesters(n = 4, dependencies = [[2,1], [2,4]], k=2)
    # a.minNumberOfSemesters(n = 4, dependencies = [[1,2], [4,2]], k=1)
    a.minNumberOfSemesters2(n = 8, dependencies = [[1,6],[2,7],[8,7],[2,5],[3,4]], k = 3)