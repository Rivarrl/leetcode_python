# -*- coding: utf-8 -*-
# ======================================
# @File    : 5547.py
# @Time    : 2020/10/25 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def f(x):
            a = x[1] - x[0]
            for i in range(2, len(x)):
                if x[i] - x[i-1] != a: return False
            return True
        res = []
        for i, j in zip(l, r):
            res.append(f(sorted(nums[i:j+1])))
        return res

if __name__ == '__main__':
    a = Solution()
    a.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
    a.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])
