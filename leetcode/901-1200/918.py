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
        思路：分类
        1：答案在数组中间，2：答案在两端
        1就是求一次最大子数组和，2等价于sum(A) - 最小子数组和，取反求最大然后加就可以
        两种情况取较大的返回
        特殊情况：最大值小于0，那么求得的1的结果是这个小于0的最大值，但2的结果肯定是大于0的最大值，会误判为情况2
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