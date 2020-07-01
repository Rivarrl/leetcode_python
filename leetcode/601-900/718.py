# -*- coding: utf-8 -*-
# ======================================
# @File    : 718.py
# @Time    : 2020/7/1 22:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [718. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)
    """
    @timeit
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m+1) for _ in range(n+1)]
        res = 0
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                    res = max(dp[i+1][j+1], res)
        return res

    @timeit
    def findLength2(self, A: List[int], B: List[int]) -> int:
        # 滑动窗口
        def f(i, j, n):
            res = ctr = 0
            for k in range(n):
                if A[i+k] == B[j+k]:
                    ctr += 1
                    res = max(res, ctr)
                else:
                    ctr = 0
            return res
        res = 0
        for i in range(len(A)):
            res = max(res, f(i, 0, min(len(A)-i, len(B))))
        for j in range(len(B)):
            res = max(res, f(0, j, min(len(B)-j, len(A))))
        return res

    @timeit
    def findLength3(self, A: List[int], B: List[int]) -> int:
        # 二分答案，judge函数判别答案为x时是否满足条件

if __name__ == '__main__':
    a = Solution()
    a.findLength2([1,2,3,2,1], [3,2,1,4,7])
    a.findLength2([0,1,1,1,1], [1,0,1,0,1])