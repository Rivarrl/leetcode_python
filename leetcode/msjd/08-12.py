# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-12.py
# @Time    : 2020/12/18 22:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.12. 八皇后](https://leetcode-cn.com/problems/eight-queens-lcci/)
    """
    @timeit
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def f(row, s, c, d1, d2):
            if row == n:
                res.append([''.join(e) for e in s])
                return
            for col in range(n):
                if c[col] or d1[col + n-1-row] or d2[col + row]: continue
                s[row][col] = "Q"
                c[col] = True
                d1[col + n-1-row] = True
                d2[col + row] = True
                f(row+1, s, c, d1, d2)
                s[row][col] = "."
                c[col] = False
                d1[col + n-1-row] = False
                d2[col + row] = False
        f(0, [['.'] * n for _ in range(n)], [False] * n, [False] * (2*n), [False] * (2*n))
        return res

if __name__ == '__main__':
    a = Solution()
    a.solveNQueens(4)