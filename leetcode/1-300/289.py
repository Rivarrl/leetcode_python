# -*- coding: utf-8 -*-
# ======================================
# @File    : 289.py
# @Time    : 2019/11/25 10:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [289. 生命游戏](https://leetcode-cn.com/problems/game-of-life/)
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        思路：原地操作，把活变死的赋值为2，死变活的赋值为-1，再遍历改回来
        """
        n = len(board)
        if n == 0: return
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                ctr = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == y == 0: continue
                        if 0 <= i + x < n and 0 <= j + y < m and board[i+x][j+y] >= 1:
                            ctr += 1
                        if ctr > 3: break
                    if ctr > 3: break
                if board[i][j] == 1:
                    if ctr < 2 or ctr > 3:
                        board[i][j] = 2
                else:
                    if ctr == 3:
                        board[i][j] = -1
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1


    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        思路：还是原地修改，用两位的二进制，高低位分别表示修改后和修改前
        """
        n = len(board)
        if n == 0: return
        m = len(board[0])
        def count(i, j):
            ctr = 0
            for x, y in [(xi, yi) for xi in range(-1, 2) for yi in range(-1, 2) if not xi == yi == 0]:
                if 0 <= i + x < n and 0 <= j + y < m and board[i+x][j+y] & 1:
                    ctr += 1
                if ctr > 3:
                    break
            return ctr
        for i in range(n):
            for j in range(m):
                ctr = count(i, j)
                if board[i][j] & 1:
                    if ctr in (2, 3):
                        board[i][j] |= 2
                else:
                    if ctr == 3:
                        board[i][j] |= 2
        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1


if __name__ == '__main__':
    a = Solution()
    a.gameOfLife([[0,1,0],
                  [0,0,1],
                  [1,1,1],
                  [0,0,0]])