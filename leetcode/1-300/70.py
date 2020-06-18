# -*- coding: utf-8 -*-
# ======================================
# @File    : 70.py
# @Time    : 2020/6/13 0:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
    """
    @timeit
    def climbStairs(self, n: int) -> int:
        res = one = two = 1
        for _ in range(2, n+1):
            res = one + two
            one = two
            two = res
        return res

if __name__ == '__main__':
    a = Solution()
    a.climbStairs(2)
    a.climbStairs(3)