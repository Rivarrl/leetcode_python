# -*- coding: utf-8 -*-
# ======================================
# @File    : 212.py
# @Time    : 2019/11/18 13:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
    """
    @timeit
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        思路：回溯算法
        """
        n = len(board)
        nw = len(words)
        if n == 0 or nw == 0: return []
        m = len(board[0])
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def dfs(i, j, word, vis, d):
            if "$" in d and d["$"] == True:
                res.append(word + board[i][j])
                d['$'] = False
            vis[i] |= (1 << j)
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and vis[x] & (1 << y) == 0 and board[x][y] in d:
                    dfs(x, y, word + board[i][j], vis, d[board[x][y]])
            vis[i] &= ~(1 << j)

        def reset(arr):
            for i in range(len(arr)):
                arr[i] = 0
        res = []
        vis = [0] * n
        d = {}
        for k in range(nw):
            p = d
            for a in words[k]:
                if not a in p:
                    p[a] = {}
                p = p[a]
            p['$'] = True
        for i in range(n):
            for j in range(m):
                if board[i][j] in d:
                    reset(vis)
                    dfs(i, j, "", vis, d[board[i][j]])
        return res


if __name__ == '__main__':
    a = Solution()
    a.findWords(words = ["oath","pea","eat","rain"],
                board = [
                          ['o','a','a','n'],
                          ['e','t','a','e'],
                          ['i','h','k','r'],
                          ['i','f','l','v']
                        ])
    a.findWords(board = [
                            ["a","b","c"],
                            ["a","e","d"],
                            ["a","f","g"]
                        ],
                words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"])
