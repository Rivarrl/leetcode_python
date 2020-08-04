# -*- coding: utf-8 -*-
# ======================================
# @File    : 1534.py
# @Time    : 2020/8/3 9:43 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1534. 统计好三元组](https://leetcode-cn.com/problems/count-good-triplets/)
    """
    @timeit
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)
        for i in range(n-2):
            for j in range(i+1, n-1):
                if abs(arr[i] - arr[j]) > a: continue
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c: continue
                    res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)
    a.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)
