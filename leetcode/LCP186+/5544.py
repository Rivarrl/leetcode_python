# -*- coding: utf-8 -*-
# ======================================
# @File    : 5544.py
# @Time    : 2020/10/18 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5544. 执行操作后字典序最小的字符串]()
    """
    @timeit
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        p = list(set((i*a)%10 for i in range(10)))
        def cmp(a, b):
            n = len(a)
            for i in range(n):
                if ord(a[i]) > ord(b[i]):
                    return b
                elif ord(a[i]) < ord(b[i]):
                    return a
            return a
        def f(s):
            res = g(s)
            for e in p:
                cur = g(''.join([str((int(c) + e) % 10) for c in s]))
                res = cmp(cur, res)
            return res
        def g(s):
            r = 0
            for i in range(9):
                j = s.find(str(i))
                if j != -1:
                    r = j
                    break
            return s[r:] + s[:r]
        def q(s1, s2):
            res = ''
            i = j = 0
            while i < len(s1) or j < len(s2):
                if i == len(s1):
                    res += s2[j]
                    j += 1
                elif j == len(s2):
                    res += s1[i]
                    i += 1
                else:
                    res += s1[i] + s2[j]
                    i += 1
                    j += 1
            return res
        if b & 1:
            t1 = f(s[::2])
            t2 = f(s[1::2])
            x = q(t1, t2)
            res = g(x)
        else:
            t = f(s[1::2])
            x, y = g(s[::2]), g(t)
            res = q(x, y)
        return res

if __name__ == '__main__':
    a = Solution()
    a.findLexSmallestString(s = "5525", a = 9, b = 2)
    a.findLexSmallestString(s = "74", a = 5, b = 1)
    a.findLexSmallestString(s = "0011", a = 4, b = 2)
    a.findLexSmallestString(s = "43987654", a = 7, b = 3)