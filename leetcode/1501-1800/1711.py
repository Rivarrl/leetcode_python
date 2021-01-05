# -*- coding: utf-8 -*-
# ======================================
# @File    : 1711.py
# @Time    : 2021/1/5 10:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1711. 大餐计数](https://leetcode-cn.com/problems/count-good-meals/)
    """
    @timeit
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        res = 0
        mod = 10 ** 9 + 7
        for x in deliciousness:
            for i in range(22):
                res += d[(1 << i) - x]
            d[x] += 1
        return res % mod

if __name__ == '__main__':
    a = Solution()
    a.countPairs(deliciousness = [1,3,5,7,9])
    a.countPairs(deliciousness = [1,1,1,3,3,3,7])