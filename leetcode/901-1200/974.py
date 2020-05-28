# -*- coding: utf-8 -*-
# ======================================
# @File    : 974.py
# @Time    : 2020/5/27 16:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [974. 和可被 K 整除的子数组](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)
    """
    @timeit
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {0:1}
        n = len(A)
        res = s = 0
        for i in range(n):
            s = (s + A[i]) % K
            if s in d:
                res += d[s]
            d[s] = d.get(s, 0) + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.subarraysDivByK([4,5,0,-2,-3,1], 5)