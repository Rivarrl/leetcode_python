# -*- coding: utf-8 -*-
# ======================================
# @File    : 1411.py
# @Time    : 2020/6/5 22:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1411. 给 N x 3 网格图涂色的方案数](https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/)
    """
    @timeit
    def numOfWays(self, n: int) -> int:
        aba = abc = 6
        mod = 10 ** 9 + 7
        for i in range(1, n):
            aba, abc = abc*2 + aba*3, aba*2 + abc*2
        return (aba + abc) % mod

if __name__ == '__main__':
    a = Solution()
    a.numOfWays(1)
    a.numOfWays(2)
    a.numOfWays(3)
    a.numOfWays(7)
    a.numOfWays(5000)