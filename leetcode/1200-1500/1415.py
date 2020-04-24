# -*- coding: utf-8 -*-
# ======================================
# @File    : 1415.py
# @Time    : 2020/4/24 13:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1415. 长度为 n 的开心字符串中字典序第 k 小的字符串](https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
    """
    @timeit
    def getHappyString(self, n: int, k: int) -> str:
        f = "12" * (n // 2 + n % 2)
        f = [int(f[i]) for i in range(n)]
        def ok(f):
            for i in range(n):
                if (i > 0 and f[i-1] == f[i]) or (i < n-1 and f[i+1] == f[i]):
                    return 0
            return 1
        def plus(f):
            for i in range(n-1, -1, -1):
                f[i] += 1
                if f[i] == 4:
                    if i == 0: return 0
                    f[i] = 1
                else:
                    break
        p = 0
        for _ in range(1, k):
            x = plus(f)
            if x == 0: return ""
            while not ok(f):
                x = plus(f)
                if x == 0: return ""
        return "" if p == -1 else "".join([" abc"[i] for i in f])

    @timeit
    def getHappyString2(self, n: int, k: int) -> str:
        m = 3 * (2 ** (n-1))
        if k > m: return ""
        d = {'a':['b', 'c'], 'b':['a', 'c'], 'c':['a', 'b']}
        res = ''
        k -= 1
        if k < m // 3:
            res += 'a'
        elif m // 3 <= k < m * 2 // 3:
            res += 'b'
            k -= m//3
        else:
            res += 'c'
            k -= m*2//3
        m //= 3
        for i in range(n-1):
            if k < m // 2:
                res += d[res[-1]][0]
            else:
                res += d[res[-1]][1]
                k -= m // 2
            m //= 2
        return res

if __name__ == '__main__':
    a = Solution()
    # a.getHappyString2(n = 1, k = 3)
    # a.getHappyString2(n = 1, k = 4)
    # a.getHappyString2(n = 3, k = 9)
    # a.getHappyString2(n=2, k=7)
    a.getHappyString2(n=10, k=100)
    # a.getHappyString2(1,1)
    # a.getHappyString2(4, 85)