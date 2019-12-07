# -*- coding: utf-8 -*-
# ======================================
# @File    : 910.py
# @Time    : 2019/12/4 16:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [910. 最小差值 II](https://leetcode-cn.com/problems/smallest-range-ii/)
    """
    @timeit
    def smallestRangeII(self, A: List[int], K: int) -> int:
        """
        思路：贪心算法,排序之后每次只需要考虑4个位置, 即A[0]+K, A[i]-K, A[-1]-K, A[i-1]+K, 最大值和最小值一定会在它们之间产生.
        """
        hi, lo = max(A), min(A)
        if K == 0: return hi - lo
        n = len(A)
        if n < 2: return 0
        A.sort()
        res = A[-1] - A[0]
        for i in range(1, n):
            lo = min(A[0] + K, A[i] - K)
            hi = max(A[i-1] + K, A[-1] - K)
            res = min(res, hi - lo)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.smallestRangeII([0, 10], 2)
    # a.smallestRangeII([1,3,6], 3)
    # a.smallestRangeII([0, 2, 9, 100], 100)
    a.smallestRangeII([7,8,8,5,2], 4)