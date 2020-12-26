# -*- coding: utf-8 -*-
# ======================================
# @File    : 85.py
# @Time    : 2020/12/26 10:09 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)
    """
    @timeit
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        arr = [int(''.join(row), base=2) for row in matrix]
        n = len(arr)
        res = 0
        for i in range(n):
            j, c = i, arr[i]
            while j < n:
                c &= arr[j]
                if not c: break
                w, c2 = 0, c
                while c2:
                    w += 1
                    c2 = c2 & (c2 >> 1)
                res = max(res, w * (j-i+1))
                j += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    a.maximalRectangle(matrix = [])
    a.maximalRectangle(matrix = [["0"]])
    a.maximalRectangle(matrix = [["1"]])
    a.maximalRectangle(matrix = [["0","0"]])