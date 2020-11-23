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
        for step in range(K):
            i, j, k = cur
            color = rec[(i, j)]
            rec[(i, j)] = 1 - color
            if color == 0:
                k = (k + 1) % 4
            else:
                k = (k + 3) % 4
            dx, dy = dxy[k]
            i += dx
            j += dy
            cur = [i, j, k]
            rec[(i, j)] = rec.get((i, j), 0)
            l, r, d, u = min(l, j), max(r, j), min(d, i), max(u, i)
        res = [['_' for _ in range(l, r+1)] for _ in range(d, u+1)]
        for di in range(u - d + 1):
            for dj in range(r - l + 1):
                i, j = di + d, dj + l
                if i == cur[0] and j == cur[1]:
                    res[di][dj] = direction[cur[-1]]
                else:
                    res[di][dj] = 'X' if rec.get((i, j), 0) == 1 else '_'
        return [''.join(e) for e in res[::-1]]

if __name__ == '__main__':
    a = Solution()
    a.printKMoves(0)
    a.printKMoves(1)
    a.printKMoves(2)
    a.printKMoves(5)