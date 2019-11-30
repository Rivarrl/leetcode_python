# -*- coding: utf-8 -*-
# ======================================
# @File    : 5136.py
# @Time    : 2019/11/30 23:28
# @Author  : Rivarrl
# ======================================


# """
# 5136. 矩形内船只的数目
# 二分，二维的二分，分四个格子，注意边界不能重叠
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       pass

class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def dfs(bottomLeft, topRight):
            if not sea.hasShips(topRight, bottomLeft): return 0
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y: return 1
            lox, loy, hix, hiy = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
            mid_x = lox + hix >> 1
            mid_y = loy + hiy >> 1
            if topRight.x == bottomLeft.x:
                return dfs(bottomLeft, Point(mid_x, mid_y)) + dfs(Point(mid_x, mid_y+1), topRight)
            elif topRight.y == bottomLeft.y:
                return dfs(bottomLeft, Point(mid_x, mid_y)) + dfs(Point(mid_x+1, mid_y), topRight)
            else:
                return dfs(bottomLeft, Point(mid_x, mid_y)) + dfs(Point(mid_x+1, loy), Point(hix, mid_y)) + dfs(Point(lox, mid_y+1), Point(mid_x, hiy)) + dfs(Point(mid_x+1, mid_y+1), topRight)
        return dfs(topRight, bottomLeft)
