# -*- coding: utf-8 -*-
# ======================================
# @File    : 840.py
# @Time    : 2019/12/9 22:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [840. 矩阵中的幻方](https://leetcode-cn.com/problems/magic-squares-in-grid/)
    """
    @timeit
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        思路: n*m中3*3的个数是固定值, grid总长并不大, 可以穷举
        """
        n, m = len(grid), len(grid[0])
        if min(n, m) < 3: return 0
        def valid(arr, i, j):
            vis = [0] * 10
            r = arr[i-1][j-1] + arr[i][j] + arr[i+1][j+1]
            if r != arr[i+1][j-1] + arr[i][j] + arr[i-1][j+1]: return False
            for k in range(-1, 2):
                r1 = r2 = 0
                for t in range(-1, 2):
                    if not 1 <= arr[i+k][j+t] <= 9 or vis[arr[i+k][j+t]]: return False
                    vis[arr[i+k][j+t]] = 1
                    r2 += arr[i+k][j+t]
                    r1 += arr[i+t][j+k]
                if r1 != r or r2 != r: return False
            return True

        res = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if valid(grid, i, j):
                    res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    # a.numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])
    # a.numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]])
    a.numMagicSquaresInside([[10,3,5],[1,6,11],[7,9,2]])
