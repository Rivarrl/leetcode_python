# -*- coding: utf-8 -*-
# ======================================
# @File    : 5610.py
# @Time    : 2020/12/12 22:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5610. 有序数组中差绝对值之和]()
    """
    @timeit
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        tot = 0
        s = sum(nums)
        for i, x in enumerate(nums):
            res[i] = i * x - tot + s - tot - (n - i) * x
            tot += x
        return res


if __name__ == '__main__':
    a = Solution()
    a.getSumAbsoluteDifferences(nums = [2,3,5])
    a.getSumAbsoluteDifferences(nums = [1,4,6,8,10])