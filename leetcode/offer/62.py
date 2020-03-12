# -*- coding: utf-8 -*-
# ======================================
# @File    : 62.py
# @Time    : 2020/3/12 23:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
# [面试题62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

class Solution:
    @timeit
    def lastRemaining(self, n: int, m: int) -> int:
        arr = [i for i in range(n)]
        k = 0
        while len(arr) > 1:
            k = (k + m - 1) % len(arr)
            arr.pop(k)
        return arr[0]

if __name__ == '__main__':
    a = Solution()
    a.lastRemaining(5, 3)
    a.lastRemaining(10, 17)
    a.lastRemaining(10**5, 10**6)