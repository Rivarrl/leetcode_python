# -*- coding: utf-8 -*-
# ======================================
# @File    : 1502
# @Time    : 2021/2/23 18:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1502. 判断能否形成等差数列](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence/)
    """
    @timeit
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        i, x = 1, arr[1] - arr[0]
        while i < n - 1 and arr[i+1] - arr[i] == x:
            i += 1
        return i == n - 1

if __name__ == '__main__':
    a = Solution()
    a.canMakeArithmeticProgression(arr = [3,5,1])
    a.canMakeArithmeticProgression(arr = [1,2,4])