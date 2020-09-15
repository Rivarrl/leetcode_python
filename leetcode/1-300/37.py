# -*- coding: utf-8 -*-
# ======================================
# @File    : 37.py
# @Time    : 2020/9/15 10:02 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)
    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        def reconstruct_sets(sets, board, row, col, blk):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        sets[i][j] = set.intersection(row[i], col[j], blk[i // 3 * 3 + j // 3])

        nm = [str(x) for x in range(1, 10)]
        col = [set(nm) for _ in range(9)]
        row = [set(nm) for _ in range(9)]
        blk = [set(nm) for _ in range(9)]
        cnt = 81
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cnt -= 1
                    row[i].discard(board[i][j])
                    col[j].discard(board[i][j])
                    blk[i // 3 * 3 + j // 3].discard(board[i][j])
        sets = [[set() for _ in range(9)] for _ in range(9)]
        reconstruct_sets(sets, board, row, col, blk)
        last = cnt + 1
        while last > cnt:
            last = cnt
            for i in range(9):
                for j in range(9):
                    if board[i][j] == "." and len(sets[i][j]) == 1:
                        board[i][j] = sets[i][j].pop()
                        row[i].discard(board[i][j])
                        col[j].discard(board[i][j])
                        blk[i // 3 * 3 + j // 3].discard(board[i][j])
                        reconstruct_sets(sets, board, row, col, blk)
                        cnt -= 1
                        # matrix_pretty_print(board)
                        # print()

        def backtrack(row, col, blk, sets, i, j, board):
            while board[i][j] != ".":
                j += 1
                if j >= 9:
                    j = 0
                    i += 1
                if i >= 9:
                    return True
            if len(sets[i][j]) == 0: return False
            for x in sets[i][j]:
                board[i][j] = x
                row[i].discard(board[i][j])
                col[j].discard(board[i][j])
                blk[i // 3 * 3 + j // 3].discard(board[i][j])
                reconstruct_sets(sets, board, row, col, blk)
                if backtrack(row, col, blk, sets, i, j, board):
                    return True
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    blk[i // 3 * 3 + j // 3].add(board[i][j])
                    reconstruct_sets(sets, board, row, col, blk)
                    board[i][j] = '.'
        backtrack(row, col, blk, sets, 0, 0, board)
        # matrix_pretty_print(board)

if __name__ == '__main__':
    a = Solution()
    sudoku = [[".",".","9","7","4","8",".",".","."],
              ["7",".",".",".",".",".",".",".","."],
              [".","2",".","1",".","9",".",".","."],
              [".",".","7",".",".",".","2","4","."],
              [".","6","4",".","1",".","5","9","."],
              [".","9","8",".",".",".","3",".","."],
              [".",".",".","8",".","3",".","2","."],
              [".",".",".",".",".",".",".",".","6"],
              [".",".",".","2","7","5","9",".","."]]
    a.solveSudoku(sudoku)