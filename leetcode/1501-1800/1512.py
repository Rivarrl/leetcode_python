# -*- coding: utf-8 -*-
# ======================================
# @File    : 1512.py
# @Time    : 2021/1/7 23:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1512. 好数对的数目](https://leetcode-cn.com/problems/number-of-good-pairs/)
    """
    @timeit
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        ctr = Counter(nums)
        res = 0
        for k in ctr:
            v = ctr[k]
            res += (v-1)*v//2
        return res

if __name__ == '__main__':
    a = Solution()
    a.numIdenticalPairs(nums = [1,2,3,1,1,3])
    a.numIdenticalPairs(nums = [1,1,1,1])
    a.numIdenticalPairs(nums = [1,2,3])