# -*- coding: utf-8 -*-
# ======================================
# @File    : 735.py
# @Time    : 2020/12/27 23:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [735. 行星碰撞](https://leetcode-cn.com/problems/asteroid-collision/)
    """
    @timeit
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        res = []
        for e in asteroids:
            if e > 0:
                stk.append(e)
            else:
                while stk and stk[-1] < (-e):
                    stk.pop()
                if stk:
                    if stk[-1] == -e:
                        stk.pop()
                        continue
                else:
                    res.append(e)
        return res + stk

if __name__ == '__main__':
    a = Solution()
    a.asteroidCollision(asteroids = [5, 10, -5])
    a.asteroidCollision(asteroids = [8, -8])
    a.asteroidCollision(asteroids = [10, 2, -5])
    a.asteroidCollision(asteroids = [-2, -1, 1, 2])