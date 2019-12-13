# -*- coding: utf-8 -*-
# ======================================
# @File    : 909.py
# @Time    : 2019/12/13 18:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [909. 蛇梯棋](https://leetcode-cn.com/problems/snakes-and-ladders/)
    """
    @timeit
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        思路：bfs可做
        """
        n = len(board)
        vis = [0] * (n * n)
        stk = [(0, 0)]
        vis[0] = 1
        def step_to(s):
            ni = s // n
            nj = s % n
            j = n - 1 - nj if ni & 1 else nj
            i = n - 1 - ni
            return s if board[i][j] == -1 else board[i][j] - 1

        while stk:
            s, step = stk.pop()
            if s == n * n - 1: return step
            for p in range(1, 7):
                if s + p >= n * n: break
                to = step_to(s + p)
                if not vis[to]:
                    vis[to] = 1
                    stk.insert(0, (to, step+1))
        return -1


if __name__ == '__main__':
    a = Solution()
    a.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,35,-1,-1,13,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,15,-1,-1,-1,-1]])
