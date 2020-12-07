# -*- coding: utf-8 -*-
# ======================================
# @File    : 861.py
# @Time    : 2020/12/7 10:07 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [861. 翻转矩阵后的得分](https://leetcode-cn.com/problems/score-after-flipping-matrix/)
    """
    @timeit
    def matrixScore(self, A: List[List[int]]) -> int:
        # 先横排，首位都变成1，再竖排，翻转0比1多的列
        n, m = len(A), len(A[0])
        res = n * (1 << (m-1))
        for j in range(1,m):
            cur = 0
            for i in range(n):
                if A[i][0] == 0:
                    cur += A[i][j] ^ 1
                else:
                    cur += A[i][j]
            cur = max(cur, n - cur)
            res += (cur << (m-j-1))
        return res

if __name__ == '__main__':
    a = Solution()
    a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])