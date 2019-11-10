# -*- coding: utf-8 -*-
# ======================================
# @File    : 5256.py
# @Time    : 2019/11/10 10:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        5256. 重构 2 行二进制矩阵
        """
        n = len(colsum)
        if n == 0 or sum(colsum) != upper + lower: return []
        res = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
                lower -= 1
                upper -= 1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        if upper > 0 or lower > 0: return []
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.reconstructMatrix(upper = 9, lower = 2, colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2])