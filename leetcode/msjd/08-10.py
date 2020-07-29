# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-10.py
# @Time    : 2020/7/29 23:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.10. 颜色填充](https://leetcode-cn.com/problems/color-fill-lcci/)
    """
    @timeit
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        image[sr][sc] = newColor
        q = deque()
        q.append((sr, sc))
        dxy = ((0, 1), (0, -1), (-1, 0), (1, 0))
        n, m = len(image), len(image[0])
        while q:
            r, c = q.pop()
            for dx, dy in dxy:
                x, y = r + dx, c + dy
                if 0 <= x < n and 0 <= y < m and image[x][y] == oldColor:
                    image[x][y] = newColor
                    q.appendleft((x, y))
        return image


if __name__ == '__main__':
    a = Solution()
    a.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2)