# -*- coding: utf-8 -*-
# ======================================
# @File    : 5137.py
# @Time    : 2019/12/28 23:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5153. 层数最深叶子节点的和](https://leetcode-cn.com/contest/biweekly-contest-16/problems/deepest-leaves-sum/)
    """
    @timeit
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1,0] for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = 1
        dxy = [[1,0], [0,1], [1,1]]
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(n):
                if i == j == n - 1 or board[i][j] == 'X' or dp[i][j][0] < 0: continue
                c = 0 if i == j == 0 else int(board[i][j])
                dp[i][j][0] += c
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if x < n and y < n and board[x][y] != 'X':
                        if dp[x][y][0] < dp[i][j][0]:
                            dp[x][y][0], dp[x][y][1] = dp[i][j][0], dp[i][j][1]
                        elif dp[x][y][0] == dp[i][j][0]:
                            dp[x][y][1] += dp[i][j][1]
                        dp[x][y][1] %= mod
        return dp[-1][-1] if dp[-1][-1][0] != -1 else [0, 0]


if __name__ == '__main__':
    a = Solution()
    a.pathsWithMaxScore(board = ["E23", "2X2", "12S"])
    a.pathsWithMaxScore(board = ["E12", "1X1", "21S"])
    a.pathsWithMaxScore(board = ["E11", "XXX", "11S"])