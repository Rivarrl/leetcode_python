# -*- coding: utf-8 -*-
# ======================================
# @File    : 12.py
# @Time    : 2020/4/21 14:32
# @Author  : Rivarrl
# ======================================
# [面试题12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def dfs(i, j, s=0):
            if s == len(word) - 1: return True
            vis[i][j] = 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and vis[x][y] == 0 and board[x][y] == word[s+1]:
                    if dfs(x, y, s+1): return True
            vis[i][j] = 0
            return False

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    vis = [[0] * m for _ in range(n)]
                    if dfs(i, j): return True
        return False


if __name__ == '__main__':
    a = Solution()
    # a.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
    a.exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS")
    # a.exist(board = [["a","b"],["c","d"]], word = "abcd")
    # a.exist([['a','a']], "aaa")