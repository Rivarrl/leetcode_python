# -*- coding: utf-8 -*-
# ======================================
# @File    : 5178.py
# @Time    : 2020/3/22 10:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5178. 四因数](https://leetcode-cn.com/problems/four-divisors/)
    """
    @timeit
    def sumFourDivisors(self, nums: List[int]) -> int:
        def f(x):
            ctr = res = 0
            if x == 0 or int(x ** 0.5) == x ** 0.5: return 0
            for i in range(1, int(x**0.5)+1):
                j = x//i
                if j == x / i:
                    ctr += 2
                    res += i + j
                if ctr > 4:
                    return 0
            return 0 if ctr != 4 else res

        res = 0
        for x in nums:
            res += f(x)
        return res



if __name__ == '__main__':
    a = Solution()
    a.sumFourDivisors([21,4,7])