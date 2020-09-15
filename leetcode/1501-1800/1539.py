# -*- coding: utf-8 -*-
# ======================================
# @File    : 1539.py
# @Time    : 2020/9/15 12:44 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1539. 第 k 个缺失的正整数]()
    """
    @timeit
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        p = 0
        for i in range(n):
            if i == 0:
                p += arr[i] - 1
            else:
                p += arr[i] - 1 - arr[i-1]
            if p >= k:
                return arr[i] - 1 - (p-k)
        return arr[-1] + k - p

if __name__ == '__main__':
    a = Solution()
    a.findKthPositive(arr = [2,3,4,7,11], k = 5)
    a.findKthPositive(arr = [1,2,3,4], k = 2)