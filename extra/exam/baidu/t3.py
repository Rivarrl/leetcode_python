# -*- coding: utf-8 -*-
# ======================================
# @File    : t3.py
# @Time    : 2020/3/14 20:04
# @Author  : Rivarrl
# ======================================
# t3 牛牛和牛妹在树上染色，牛牛黑色，牛妹白色，牛牛从1开始，牛妹从n开始，谁不能继续染色了谁输，打印胜者
# 输入：T 用例轮数，n树节点，n-1行边的表示
# 输出：胜者
"""
输入：
2
7
1 2
1 3
1 4
2 7
4 6
5 7
4
1 4
2 3
2 4
输出：
niuniu
niumei
"""

import sys
from collections import deque, defaultdict
def solve():
    T = int(sys.stdin.readline().strip())
    def ok(arr):
        for e in arr:
            if e == 0: return False
        return True
    res = []
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        graph = defaultdict(list)
        for i in range(n-1):
            u, v = map(int, sys.stdin.readline().strip().split())
            graph[u].append(v)
            graph[v].append(u)
        nnstk, nmstk = deque(), deque()
        nnstk.append(1)
        nmstk.append(n)
        vis = [0] * (n+1)
        vis[0] = vis[1] = vis[n] = 1
        c = 0
        while not ok(vis):
            if c & 1:
                stk = nmstk
            else:
                stk = nnstk
            while stk:
                u = stk.popleft()
                flag = 0
                for v in graph[u]:
                    if vis[v] == 0:
                        vis[v] = 1
                        stk.append(v)
                        flag = 1
                if flag: break
            else:
                break
            c += 1
        res.append('niuniu' if c & 1 else 'niumei')
    return res

if __name__ == '__main__':
    res = solve()
    for r in res:
        print(r)
