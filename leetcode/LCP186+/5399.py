# -*- coding: utf-8 -*-
# ======================================
# @File    : 5399.py
# @Time    : 2020/5/16 22:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5399. 数位成本和为目标值的最大数字](https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target)
    """
    @timeit
    def largestNumber(self, cost: List[int], target: int) -> str:
        f = [-1] * (target + 1)
        g = [0] * (target + 1)
        f[0] = 0
        for i in range(len(cost)):
            c = cost[i]
            for j in range(c, target+1):
                if f[j - c] != -1 and f[j - c] + 1 >= f[j]:
                    f[j] = f[j - c] + 1
                    g[j] = i
        if f[-1] == -1: return "0"
        res = ''
        i = target
        while i > 0:
            res += chr(ord('1') + g[i])
            i -= cost[g[i]]
        res = ''.join(sorted(res, reverse=True))
        return res

if __name__ == '__main__':
    a = Solution()
    a.largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9)
    a.largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12)
    a.largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5)
    a.largestNumber(cost = [6,10,15,40,40,40,40,40,40], target = 47)