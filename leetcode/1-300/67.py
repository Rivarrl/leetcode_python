# -*- coding: utf-8 -*-
# ======================================
# @File    : 67.py
# @Time    : 2020/6/23 9:39 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
    """
    @timeit
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        if n < m:
            a, b, n, m = b, a, m, n
        p = 0
        res = ""
        k = 0
        while k < m:
            i, j = n - 1 - k, m - 1 - k
            x = int(a[i]) + int(b[j]) + p
            c = x % 2
            res = str(c) + res
            p = x >> 1
            k += 1
        while k < n:
            i = n - 1 - k
            if p == 0:
                res = a[:i + 1] + res
                break
            x = int(a[i]) + p
            c = x % 2
            res = str(c) + res
            p = x >> 1
            k += 1
        if p: res = '1' + res
        return res


if __name__ == '__main__':
    a = Solution()
    a.addBinary(a="11", b="1")
    a.addBinary(a="1010", b="1011")
