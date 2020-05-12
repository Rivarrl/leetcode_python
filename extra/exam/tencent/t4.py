# -*- coding: utf-8 -*-
# ======================================
# @File    : t4.py
# @Time    : 2020/5/10 20:35
# @Author  : Rivarrl
# ======================================
def f(n, board):
    def dfs(l, r, x=0):
        if l > r: return 0
        if l == r: return board[l]
        res = mi = min(board[l:r+1]) - x
        i = l
        for j in range(l, r+1):
            if board[j] - x == mi:
                res += dfs(i, j-1, mi)
                i = j + 1
        res += dfs(i, r, mi)
        return min(res, r - l + 1)
    return dfs(0, n-1)

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input().strip().split(' ')))
    res = f(n, board)
    print(res)

"""
5
2 2 1 2 2
"""