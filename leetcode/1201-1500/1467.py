# -*- coding: utf-8 -*-
# ======================================
# @File    : 1467.py
# @Time    : 2020/6/1 18:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1467. 两个盒子中球的颜色数相同的概率](https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
    """
    @timeit
    def getProbability(self, balls: List[int]) -> float:
        from math import factorial
        n, m = sum(balls), len(balls)
        total = factorial(n) // (factorial(n//2) ** 2)
        res = 0
        fac = [factorial(i) for i in range(7)]
        def comb(n, m):
            return fac[n] // (fac[m] * fac[n - m])
        def f(i, n1, n2, c1, c2, j=1):
            # 拿到第i个颜色球时，盒1有n1个球，盒2有n2个球，盒1颜色数c1，盒2颜色数c2, 当前情况有j种取法
            nonlocal res
            if n1 > n // 2 or (i - n1) > n // 2: return
            if i == m:
                if n1 == n2 and c1 == c2:
                    res += j
                return
            x = balls[i]
            for k in range(x+1):
                f(i+1, n1+k, n2+(x-k), c1+(k!=0), c2+(k!=x), j*comb(x, k))
        f(0,0,0,0,0)
        return res / total

if __name__ == '__main__':
    a = Solution()
    a.getProbability([1,1])
    a.getProbability([2,1,1])
    a.getProbability([1,2,1,2])
    a.getProbability([3,2,1])
    a.getProbability([6,6,6,6,6,6])