# -*- coding: utf-8 -*-
# ======================================
# @File    : 918.py
# @Time    : 2019/11/22 0:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [918. 环形子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-circular-subarray/)
    """
    @timeit
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        思路：复制出来一个数组A贴在后面
        """
        def f(B):
            res = cur = 0
            for i, x in enumerate(B):
                cur = max(cur + x, x)
                res = max(cur, res)
            return res
        am = max(A)
        if am < 0: return am
        r1 = f(A)
        r2 = sum(A) + f([-e for e in A])
        return (r1, r2)[r1 < r2]

if __name__ == '__main__':
    a = Solution()
    a.maxSubarraySumCircular([5,-3,5])