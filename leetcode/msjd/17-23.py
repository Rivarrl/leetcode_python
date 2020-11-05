# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-23.py
# @Time    : 2020/11/5 8:16 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.23. 最大黑方阵](https://leetcode-cn.com/problems/max-black-square-lcci/)
    """
    @timeit
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        import heapq
        n = len(matrix)
        pre = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                pre[i+1][j+1] += pre[i+1][j] + matrix[i][j]
        for j in range(1, n+1):
            for i in range(1, n+1):
                pre[i][j] += pre[i-1][j]
        q = [[-n, 0, 0]]
        seen = set()
        res = []
        matrix_pretty_print(pre)
        while q:
            rs, r, c = heapq.heappop(q)
            s = -rs
            x, y = r + s, c + s
            print(r, c, s, x, y, pre[r][c], pre[x][y], pre[x][c], pre[r][y],
                  pre[r][c] + pre[x][y] - pre[x][c] - pre[r][y])
            if pre[r][c] + pre[x][y] - pre[x][c] - pre[r][y] == 0:
                # if res and res[-1] > s: break
                if not res or res[0] > r or (res[0] == r and res[1] > c):
                    res = [r, c, s]
            else:
                for i, j in ((r, c), (r, c+1), (r+1, c), (r+1, c+1)):
                    if s - 1 > 0 and (i, j, s-1) not in seen:
                        seen.add((i,j,s-1))
                        q.append([1-s,i,j])
        return res

if __name__ == '__main__':
    a = Solution()
    # a.findSquare([[1,0,1],
    #               [0,0,1],
    #               [0,0,1]])
    # a.findSquare([[0,1,1],
    #               [1,0,1],
    #               [1,1,0]])
    a.findSquare([[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                  [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]])