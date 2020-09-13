# -*- coding: utf-8 -*-
# ======================================
# @File    : 79.py
# @Time    : 2020/9/13 2:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)
    """
    @timeit
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
        n, m = len(board), len(board[0])
        def f(i, j, k):
            if k == len(word) - 1: return True
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and seen[x][y] == 0 and board[x][y] == word[k+1]:
                    seen[x][y] = 1
                    if f(x, y, k+1): return True
                    seen[x][y] = 0
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    seen = [[0] * m for _ in range(n)]
                    seen[i][j] = 1
                    if f(i, j, 0): return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.exist([['A','B','C','E'], ['S','F','C','S'],['A','D','E','E']], "ABCCED")
    a.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE")
    a.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCB")
    a.exist([["a","a"]], "aaa")
    a.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")