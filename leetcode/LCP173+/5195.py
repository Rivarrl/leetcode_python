# -*- coding: utf-8 -*-
# ======================================
# @File    : 5195.py
# @Time    : 2020/4/5 10:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5195. 最长快乐字符串](https://leetcode-cn.com/problems/longest-happy-string/)
    """
    @timeit
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        while a > 0 or b > 0 or c > 0:
            m = max(a, b, c)
            ll = len(res)
            if not res:
                if m == a:
                    t = 2 if a >= 2 and a > b + c else min(a, 1)
                    a -= t
                    res += 'a' * t
                elif m == b:
                    t = 2 if b >= 2 and b > a + c else min(b, 1)
                    b -= t
                    res += 'b' * t
                else:
                    t = 2 if c >= 2 and c > a + b else min(c, 1)
                    c -= t
                    res += 'c' * t
            elif res[-1] == 'a':
                m = max(b, c)
                if m == b:
                    t = 2 if b >= 2 and b > a + c else min(b, 1)
                    b -= t
                    res += 'b' * t
                else:
                    t = 2 if c >= 2 and c > a + b else min(c, 1)
                    c -= t
                    res += 'c' * t
            elif res[-1] == 'b':
                m = max(a, c)
                if m == c:
                    t = 2 if c >= 2 and c > a + b else min(c, 1)
                    c -= t
                    res += 'c' * t
                else:
                    t = 2 if a >= 2 and a > b + c else min(a, 1)
                    a -= t
                    res += 'a' * t
            else:
                m = max(a, b)
                if m == b:
                    t = 2 if b >= 2 and b > a + c else min(b, 1)
                    b -= t
                    res += 'b' * t
                else:
                    t = 2 if a >= 2 and a > b + c else min(a, 1)
                    a -= t
                    res += 'a' * t
            if len(res) == ll:
                break
        return res

    @timeit
    def longestDiverseString2(self, a: int, b: int, c: int) -> str:
        # a > b > c
        def dfs(a, b, c, sa, sb, sc):
            if a < b:
                return dfs(b,a,c,sb,sa,sc)
            if a < c:
                return dfs(c,b,a,sc,sb,sa)
            if b < c:
                return dfs(a,c,b,sa,sc,sb)
            ta = min(a, 2)
            if b == 0:
                return sa * ta
            tb = 1 if a - ta >= b else 0
            return sa*ta+sb*tb+dfs(a-ta,b-tb,c,sa,sb,sc)
        return dfs(a, b, c, 'a', 'b', 'c')


if __name__ == '__main__':
    a = Solution()
    a.longestDiverseString2(a = 1, b = 1, c = 7)
    a.longestDiverseString2(a = 2, b = 2, c = 1)
    a.longestDiverseString2(a = 7, b = 1, c = 0)
    a.longestDiverseString2(a = 0, b = 8, c = 11)