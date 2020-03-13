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
        # 模拟
        # 时间O(N^2),空间O(N)
        arr = [i for i in range(n)]
        k = 0
        while len(arr) > 1:
            k = (k + m - 1) % len(arr)
            arr.pop(k)
        return arr[0]

    @timeit
    def lastRemaining2(self, n: int, m: int) -> int:
        # 约瑟夫环问题，公式f(n) = (f(n-1)+m) % n
        # 时间O(N), 空间O(1)
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res


if __name__ == '__main__':
    a = Solution()
    a.lastRemaining2(5, 3)
    a.lastRemaining2(10, 17)
    a.lastRemaining2(10**5, 10**6)