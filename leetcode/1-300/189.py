# -*- coding: utf-8 -*-
# ======================================
# @File    : 189.py
# @Time    : 2021/1/8 10:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(x, y):
            if x == 0: return y
            return gcd(y % x, x)
        n = len(nums)
        m = gcd(n, k)
        for i in range(m):
            j = (i + k) % n
            if j == i: continue
            tmp, nums[j] = nums[j], nums[i]
            while j != i:
                t = (j + k) % n
                tmp, nums[t] = nums[t], tmp
                j = t

if __name__ == '__main__':
    a = Solution()
    a.rotate([1,2,3,4,5,6,7], 3)
    a.rotate([-1,-100,3,99], 2)