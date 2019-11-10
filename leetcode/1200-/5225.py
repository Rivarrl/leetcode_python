# -*- coding: utf-8 -*-
# ======================================
# @File    : 5225.py
# @Time    : 2019/11/10 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    @timeit
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        """
        [5255. 奇数值单元格的数目](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix/)
        思路：按照indices给的顺序对应加就行了，最后计算奇数个数
        """
        arr = [[0] * m for _ in range(n)]
        for x, y in indices:
            for i in range(m):
                arr[x][i] += 1
            for j in range(n):
                arr[j][y] += 1
        return sum(sum(1 if e & 1 else 0 for e in a) for a in arr)

if __name__ == '__main__':
    sol = Solution()
    res = sol.oddCells(2,3,[[0,1], [1,1]])
    print(res)