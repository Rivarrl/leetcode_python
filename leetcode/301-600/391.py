# -*- coding: utf-8 -*-
# ======================================
# @File    : 391.py
# @Time    : 2020/7/29 10:44 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [391. 完美矩形](https://leetcode-cn.com/problems/perfect-rectangle/)
    """
    @timeit
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 完美矩形的特点：所有矩形面积和=完美矩形面积，所有矩形边缘相接，所以除了整体矩形的四个边界点(1次)外的所有小矩形边界点均出现偶数次
        W = S = 0x3f3f3f3f
        E = N = -0x3f3f3f3f
        ss = 0
        d = set()
        for w, s, e, n in rectangles:
            W = min(W, w)
            S = min(S, s)
            E = max(E, e)
            N = max(N, n)
            ss += (e - w) * (n - s)
            for x in (w, e):
                for y in (s, n):
                    if (x, y) in d:
                        d.remove((x, y))
                    else:
                        d.add((x, y))
        return {(W, S), (W, N), (E, S), (E, N)} == d and ss == (E - W) * (N - S)


if __name__ == '__main__':
    a = Solution()
    a.isRectangleCover([[0,0,4,1],
                        [7,0,8,2],
                        [6,2,8,3],
                        [5,1,6,3],
                        [4,0,5,1],
                        [6,0,7,2],
                        [4,2,5,3],
                        [2,1,4,3],
                        [0,1,2,2],
                        [0,2,2,3],
                        [4,1,5,2],
                        [5,0,6,1]])
    # a.isRectangleCover(rectangles = [[1,1,3,3],
    #                                  [3,1,4,2],
    #                                  [3,2,4,4],
    #                                  [1,3,2,4],
    #                                  [2,3,3,4]])
    # a.isRectangleCover(rectangles = [[1,1,2,3],
    #                                  [1,3,2,4],
    #                                  [3,1,4,2],
    #                                  [3,2,4,4]])
    # a.isRectangleCover(rectangles = [[1,1,3,3],
    #                                  [3,1,4,2],
    #                                  [1,3,2,4],
    #                                  [3,2,4,4]])
    # a.isRectangleCover(rectangles = [[1,1,3,3],
    #                                  [3,1,4,2],
    #                                  [1,3,2,4],
    #                                  [2,2,4,4]])