# -*- coding: utf-8 -*-
# ======================================
# @File    : 363.py
# @Time    : 2020/5/8 18:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [363. 矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/)
    """
    @timeit
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        n, m = len(matrix), len(matrix[0])
        pre = [[0] * (m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                pre[i][j] = pre[i][j-1] + matrix[i][j-1]
        res = -(1 << 32)
        for l in range(m):
            for r in range(l+1, m+1):
                tmp, cur = [0], 0
                for i in range(n):
                    cur += pre[i][r] - pre[i][l]
                    j = bisect.bisect_left(tmp, cur - k)
                    if j < len(tmp): res = max(res, cur - tmp[j])
                    bisect.insort(tmp, cur)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2)