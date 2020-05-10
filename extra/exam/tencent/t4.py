# -*- coding: utf-8 -*-
# ======================================
# @File    : t4.py
# @Time    : 2020/5/10 20:35
# @Author  : Rivarrl
# ======================================

def f(n, board):
    mi = min(board)
    res = mi
    for i in range(n):
        if board[i] >= n:
            res += 1
    return min(n, res)

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input().strip().split(' ')))
    res = f(n, board)
    print(res)

"""
5
2 2 1 2 2
"""