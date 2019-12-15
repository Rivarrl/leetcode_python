# -*- coding: utf-8 -*-
# ======================================
# @File    : 5285.py
# @Time    : 2019/12/15 11:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5285. 元素和小于等于阈值的正方形的最大边长](https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
    """
    @timeit
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i+1][j] + pre[i][j+1] - pre[i][j] + mat[i][j]
        a = min(n, m)
        def judge(k):
            for i in range(k, n+1):
                for j in range(k, m+1):
                    if pre[i][j] - pre[i-k][j] - pre[i][j-k] + pre[i-k][j-k] <= threshold:
                        return True
            return False
        lo, hi = 0, a
        while lo < hi:
            k = (lo + hi + 1) >> 1
            if judge(k):
                lo = k
            else:
                hi = k - 1
        return lo

if __name__ == '__main__':
    a = Solution()
    a.maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4)
    a.maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1)
    a.maxSideLength(mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6)
    a.maxSideLength(mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184)
