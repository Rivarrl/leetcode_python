# -*- coding: utf-8 -*-
# ======================================
# @File    : 1497.py
# @Time    : 2020/7/20 9:50 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1497. 检查数组对是否可以被 k 整除](https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/)
    """
    @timeit
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        n = len(arr)
        for i in range(n):
            d[arr[i] % k] = d.get(arr[i] % k, 0) + 1
        if d.get(0, 0) & 1: return False
        for i in range(1, k//2 + 1):
            if d.get(i, 0) != d.get(k-i, 0):
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)
    a.canArrange(arr = [1,2,3,4,5,6], k = 7)
    a.canArrange(arr = [1,2,3,4,5,6], k = 10)
    a.canArrange(arr = [-10,10], k = 2)
    a.canArrange(arr = [-1,1,-2,2,-3,3,-4,4], k = 3)