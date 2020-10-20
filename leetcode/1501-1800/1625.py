# -*- coding: utf-8 -*-
# ======================================
# @File    : 1625.py
# @Time    : 2020/10/20 12:57 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1625. 执行操作后字典序最小的字符串](https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/)
    """
    @timeit
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        def cmp(x, y):
            for a, b in zip(x, y):
                if ord(a) > ord(b):
                    return y
                elif ord(a) < ord(b):
                    return x
            return x
        ss = s + s
        n = len(s)
        step = gcd(n, b)
        res = '9' * n
        for i in range(0, n, step):
            sub = ss[i:i+n]
            for j in range(10):
                th = 0 if step % 2 == 0 else 9
                for k in range(th+1):
                    q = ''
                    for t in range(n):
                        if t & 1:
                            q += chr(ord('0') + (ord(sub[t]) - ord('0') + a*j) % 10)
                        else:
                            q += chr(ord('0') + (ord(sub[t]) - ord('0') + a*k) % 10)
                    res = cmp(res, q)
        return ''.join(res)

if __name__ == '__main__':
    a = Solution()
    a.findLexSmallestString(s = "5525", a = 9, b = 2)
    a.findLexSmallestString(s = "74", a = 5, b = 1)
    a.findLexSmallestString(s = "0011", a = 4, b = 2)
    a.findLexSmallestString(s = "43987654", a = 7, b = 3)
