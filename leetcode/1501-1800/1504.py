# -*- coding: utf-8 -*-
# ======================================
# @File    : 1504.py
# @Time    : 2020/12/22 0:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1504. 统计全 1 子矩形](https://leetcode-cn.com/problems/count-submatrices-with-all-ones/)
    """
    @timeit
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0] for _ in range(n)]
        

if __name__ == '__main__':
    a = Solution()
    a.numSubmat(mat = [[1,0,1],
            [1,1,0],
            [1,1,0]])
    a.numSubmat(mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]])
    a.numSubmat(mat = [[1,1,1,1,1,1]])
    a.numSubmat(mat = [[1,0,1],[0,1,0],[1,0,1]])