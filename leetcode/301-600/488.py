# -*- coding: utf-8 -*-
# ======================================
# @File    : 488.py
# @Time    : 2020/12/23 5:08 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [488. 祖玛游戏](https://leetcode-cn.com/problems/zuma-game/)
    """
    @timeit
    def findMinStep(self, board: str, hand: str) -> int:
        from functools import lru_cache
        import re
        hand = ''.join(sorted([e for e in hand]))
        N, M = len(board), len(hand)
        res = M + 1
        def deal(x):
            while re.findall("(W{3,}|R{3,}|B{3,}|G{3,}|Y{3,})", x):
                x = re.sub("(W{3,}|R{3,}|B{3,}|G{3,}|Y{3,})", "", x)
            return x
        @lru_cache(None)
        def f(t, h):
            n, m = len(t), len(h)
            if not t:
                nonlocal res
                res = min(res, M - m)
                return
            if not h: return
            for j in range(m):
                if j > 0 and h[j] == h[j - 1]: continue
                nh = h[:j] + h[j + 1:]
                f(deal(h[j] + t), nh)
                for i in range(1, n):
                    x = t[:i] + h[j] + t[i:]
                    f(deal(x), nh)
                f(deal(t + h[j]), nh)
        f(board, hand)
        return -1 if res > M else res

if __name__ == '__main__':
    a = Solution()
    a.findMinStep(board = "WRRBBW", hand = "RB")
    a.findMinStep(board = "WWRRBBWW", hand = "WRBRW")
    a.findMinStep(board = "G", hand = "GGGGG")
    a.findMinStep(board = "RBYYBBRRB", hand = "YRBGB")
    a.findMinStep("RRYGGYYRRYGGYYRR", "GGBBB")