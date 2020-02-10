# -*- coding: utf-8 -*-
# ======================================
# @File    : 6.py
# @Time    : 2020/2/10 18:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [100264. 分苹果](https://leetcode-cn.com/contest/sf-2020/problems/how-many-apples-lc/)
    # 主要思路是推导公式
    # 推出通项公式
    # F[i] + n - k = ((n-k)/n)^i * (F[0] + n - k)
    # 然后利用最后一次(第n次)分苹果的结果还可以再分，得到第n+1次分得的结果的公式为F[n+1] = (1/n) * (F[n] - k)
    # 把前面的通项公式代入得到F[n+1] + 1 = (1/n) * ((n-k)/n)^n * (F[0] + n - k)
    # F[n+1]为整数的情况下使得F[0]最小
    # 也就是F[0]与其系数互为倒数的最小数，取最大公约数可得
    # F[0]_min = n * (n/gcd(n, n-k))^n - (n-k)
    """
    def findNum(self, n: int, k: int) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x%y)
        mod = 10 ** 9 + 7
        res = n
        base = n // gcd(n, n - k)
        for i in range(n):
            res *= base
            res %= mod
        res -= (n - k)
        return (res + mod) % mod

if __name__ == '__main__':
    a = Solution()
    a.findNum(2, 1)
    a.findNum(3, 1)
    a.findNum(4, 2)