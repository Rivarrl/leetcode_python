# -*- coding: utf-8 -*-
# ======================================
# @File    : 5360.py
# @Time    : 2020/4/4 22:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5360. 统计最大组的数目]()
    """
    @timeit
    def countLargestGroup(self, n: int) -> int:
        d = {}
        def f(x):
            return sum([int(e) for e in str(x)])
        for i in range(1, n+1):
            x = f(i)
            d[x] = d.get(x, 0) + 1
        m = max(d.values())
        res = 0
        for k, v in d.items():
            if v == m:
                res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.countLargestGroup(13)
    a.countLargestGroup(2)
    a.countLargestGroup(15)
    a.countLargestGroup(24)