# -*- coding: utf-8 -*-
# ======================================
# @File    : 60.py
# @Time    : 2020/3/12 23:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# [面试题60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

class Solution:
    @timeit
    def twoSum(self, n: int) -> List[float]:
        dp = {}
        for i in range(1, 7):
            dp[i] = 1
        for i in range(1, n):
            tmp = {}
            for x in dp:
                for j in range(1, 7):
                    tmp[x+j] = tmp.get(x+j, 0) + dp[x]
            dp = tmp
        return [x / 6 ** n for x in dp.values()]

if __name__ == '__main__':
    a = Solution()
    a.twoSum(1)
    a.twoSum(2)