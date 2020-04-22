# -*- coding: utf-8 -*-
# ======================================
# @File    : 733.py
# @Time    : 2020/4/22 23:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        if n == 0: return image
        m = len(image[0])
        stk = [(sr, sc)]
        o = image[sr][sc]
        if newColor == o: return image
        image[sr][sc] = newColor
        while stk:
            i, j = stk.pop(0)
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and image[x][y] == o:
                    image[x][y] = newColor
                    stk.append((x, y))
        return image


if __name__ == '__main__':
    a = Solution()
    a.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2)