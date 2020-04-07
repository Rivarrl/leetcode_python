# -*- coding: utf-8 -*-
# ======================================
# @File    : 13.py
# @Time    : 2020/4/8 0:45
# @Author  : Rivarrl
# ======================================
# [面试题13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def movingCount(self, m: int, n: int, k: int) -> int:
        from collections import deque
        stk = deque()
        stk.append((0, 0))
        vis = [[0] * n for _ in range(m)]
        vis[0][0] = 1
        res = 0
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def f(x):
            r = 0
            while x > 0:
                r += x % 10
                x //= 10
            return r
        def ok(x, y):
            if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                if f(x) + f(y) <= k:
                    return 1
            return 0
        while stk:
            i, j = stk.popleft()
            res += 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if ok(x, y):
                    vis[x][y] = 1
                    stk.append((x, y))
        return res


if __name__ == '__main__':
    a = Solution()
    a.movingCount(2,3,1)
    a.movingCount(3,1,0)
    a.movingCount(11,8,16)
    a.movingCount(16,8,4)
