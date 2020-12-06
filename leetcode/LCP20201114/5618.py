# -*- coding: utf-8 -*-
# ======================================
# @File    : 5618.py
# @Time    : 2020/12/6 10:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5618. K 和数对的最大数目]()
    """
    @timeit
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = {}
        res = 0
        for x in nums:
            if d.get(x, 0) > 0:
                res += 1
                d[x] -= 1
            else:
                d[k-x] = d.get(k-x, 0) + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxOperations(nums = [1,2,3,4], k = 5)
    a.maxOperations(nums = [3,1,3,4,3], k = 6)