# -*- coding: utf-8 -*-
# ======================================
# @File    : 5384.py
# @Time    : 2020/5/2 22:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5384. 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/)
    """
    @timeit
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        n = len(candies)
        res = [False] * n
        for i in range(n):
            res[i] = candies[i] + extraCandies >= mx
        return res

if __name__ == '__main__':
    a = Solution()
    a.kidsWithCandies([2,3,5,1,3],3)
    a.kidsWithCandies([4,2,1,1,2],1)
    a.kidsWithCandies([12,1,12],10)