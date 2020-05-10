# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/5/7 20:23
# @Author  : Rivarrl
# ======================================

matrix = [['0','1','C','H','A'],
          ['9','E','7','B','I'],
          ['K','D','4','8','J'],
          ['6','5','F','G','O'],
          ['L','N','M','2','3']]
def f(s):
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    def dfs(i, j, k=1):
        if k == len(s): return True
        for dx, dy in dxy:
            x, y = i + dx, j + dy
            if 0 <= x < 5 and 0 <= y < 5 and not vis[x][y] and matrix[x][y] == s[k]:
                vis[x][y] = True
                if dfs(x, y, k+1): return True
                vis[x][y] = False
        return False

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == s[0]:
                vis = [[False]*5 for _ in range(5)]
                vis[i][j] = True
                if dfs(i, j): return 1
    return 0

x = input().strip()
while x:
    res = f(x)
    print(['N', 'Y'][res])
    x = input().strip()
