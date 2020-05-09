# -*- coding: utf-8 -*-
# ======================================
# @File    : 529.py
# @Time    : 2020/5/9 12:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [529. 扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)
    """
    @timeit
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        from collections import deque
        i, j = click
        n, m = len(board), len(board[0])
        def count_mine(i, j):
            ctr = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0: continue
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and board[x][y] == 'M': ctr += 1
            return ctr

        if board[i][j] == 'M': board[i][j] = 'X'
        elif board[i][j] == 'E':
            ctr = count_mine(i, j)
            if ctr > 0: board[i][j] = str(ctr)
            else:
                board[i][j] = 'B'
                stk = deque()
                stk.append((i, j))
                vis = [[False] * m for _ in range(n)]
                vis[i][j] = True
                while stk:
                    i, j = stk.popleft()
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx == 0 and dy == 0: continue
                            x, y = i + dx, j + dy
                            if 0 <= x < n and 0 <= y < m and not vis[x][y] and board[x][y] == 'E':
                                vis[x][y] = True
                                ctr = count_mine(x, y)
                                if ctr > 0:
                                    board[x][y] = str(ctr)
                                else:
                                    board[x][y] = 'B'
                                    stk.append((x, y))
        return board


if __name__ == '__main__':
    a = Solution()
    # a.updateBoard([['E', 'E', 'E', 'E', 'E'],
    #              ['E', 'E', 'M', 'E', 'E'],
    #              ['E', 'E', 'E', 'E', 'E'],
    #              ['E', 'E', 'E', 'E', 'E']], [3,0])
    # a.updateBoard([['B', '1', 'E', '1', 'B'],
    #              ['B', '1', 'M', '1', 'B'],
    #              ['B', '1', '1', '1', 'B'],
    #              ['B', 'B', 'B', 'B', 'B']], [1,2])
    # a.updateBoard([["E","E","E","E","E","E","E","E"],
    #                ["E","E","E","E","E","E","E","M"],
    #                ["E","E","M","E","E","E","E","E"],
    #                ["M","E","E","E","E","E","E","E"],
    #                ["E","E","E","E","E","E","E","E"],
    #                ["E","E","E","E","E","E","E","E"],
    #                ["E","E","E","E","E","E","E","E"],
    #                ["E","E","M","M","E","E","E","E"]],[0,0])
    a.updateBoard([["E","M","M","2","B","B","B","B"],
                   ["E","E","M","2","B","B","B","B"],
                   ["E","E","2","1","B","B","B","B"],
                   ["E","M","1","B","B","B","B","B"],
                   ["1","2","2","1","B","B","B","B"],
                   ["B","1","M","1","B","B","B","B"],
                   ["B","1","1","1","B","B","B","B"],
                   ["B","B","B","B","B","B","B","B"]],[0,0])