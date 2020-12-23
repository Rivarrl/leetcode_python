# -*- coding: utf-8 -*-
# ======================================
# @File    : 688.py
# @Time    : 2020/12/23 1:07 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [688. “马”在棋盘上的概率](https://leetcode-cn.com/problems/knight-probability-in-chessboard/)
    """
    @timeit
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        from functools import lru_cache
        @lru_cache(None)
        def f(k, x, y):
            if k == 0: return 1
            res = 0
            for tx, ty in ((x-2, y-1), (x+2, y-1), (x-2, y+1), (x+2, y+1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)):
                if 0 <= tx < N and 0 <= ty < N:
                    res += f(k-1, tx, ty) / 8
            return res
        return f(K, r, c)

if __name__ == '__main__':
    a = Solution()
    a.knightProbability(3, 2, 0, 0)
    a.knightProbability(3, 3, 0, 0)
