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
        direction = [0, 1, 2, 3]
        cur = [0, 0, 0]
        for _ in range(K):

        res = [[''] * (u-d+1) for _ in range(l, r+1)]
        for i in range(l, r+1):
            for j in range(d, u+1):
                if cur
                color = 'X' if rec.get((i, j), 0) == 1 else '_'


if __name__ == '__main__':
    a = Solution()
    a.printKMoves(0)
    a.printKMoves(2)
    a.printKMoves(5)