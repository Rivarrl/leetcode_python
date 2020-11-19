# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-22.py
# @Time    : 2020/11/18 1:02 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.22. 兰顿蚂蚁](https://leetcode-cn.com/problems/langtons-ant-lcci/)
    """
    @timeit
    def printKMoves(self, K: int) -> List[str]:
        rec = {(0, 0): 0}
        l = r = u = d = 0
        direction = ['R', 'D', 'L', 'U']
        dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        cur = [0, 0, 0]
        for _ in range(K):
            i, j, k = cur
            dx, dy = dxy[k]
            i += dx
            j += dy
            if rec.get((i, j), 0) == 0:
                k = (k + 1) % 4
            else:
                k = (k + 3) % 4
            rec[(i, j)] = 1 - rec.get((i, j), 0)
            cur = [i, j, k]
            l, r, d, u = min(l, i), max(r, i), min(d, j), max(u, j)
        print(l, r, d, u)
        res = [[''] * (u-d+1) for _ in range(l, r+1)]
        pos = tuple(cur[:2])
        for di in range(l, r+1):
            for dj in range(d, u+1):
                i, j = di - l, dj - d
                if i == cur[0] and j == cur[1]:
                    res[i][j] = direction[cur[-1]]
                else:
                    res[i][j] = 'X' if rec.get((i, j), 0) == 1 else '_'
        return [''.join(e) for e in res]

if __name__ == '__main__':
    a = Solution()
    a.printKMoves(0)
    a.printKMoves(1)
    a.printKMoves(2)
    a.printKMoves(5)