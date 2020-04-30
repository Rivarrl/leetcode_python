# -*- coding: utf-8 -*-
# ======================================
# @File    : 66.py
# @Time    : 2020/4/30 21:47
# @Author  : Rivarrl
# ======================================
# [面试题66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1]
        for i, x in enumerate(a):
            res += [res[-1] * x]
        r = 1
        for i in range(len(a)-1, -1, -1):
            x = a[i]
            res[i] *= r
            r *= x
        return res[:-1]

if __name__ == '__main__':
    a = Solution()
    a.constructArr([1,2,3,4,5])