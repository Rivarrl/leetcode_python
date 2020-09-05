# -*- coding: utf-8 -*-
# ======================================
# @File    : 60.py
# @Time    : 2020/9/5 16:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [60. 第k个排列](https://leetcode-cn.com/problems/permutation-sequence/)
    """
    @timeit
    def getPermutation(self, n: int, k: int) -> str:
        tot = 1
        for i in range(1, n+1):
            tot *= i
        mask = 0
        t = n
        k -= 1
        res = ""
        while t > 0:
            a = (tot // t)
            j = 0
            for i in range(n):
                if mask & (1 << i): continue
                if j == k // a:
                    mask |= (1 << i)
                    res += str(i+1)
                    break
                j += 1
            k %= a
            tot //= t
            t -= 1
        return res



if __name__ == '__main__':
    a = Solution()
    a.getPermutation(n = 3, k = 3)
    a.getPermutation(n = 4, k = 9)
