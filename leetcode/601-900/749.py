# -*- coding: utf-8 -*-
# ======================================
# @File    : 749.py
# @Time    : 2020/12/29 23:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [749. 隔离病毒](https://leetcode-cn.com/problems/contain-virus/)
    """
    @timeit
    def containVirus(self, grid: List[List[int]]) -> int:


if __name__ == '__main__':
    a = Solution()
    a.containVirus(grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]])
    a.containVirus(grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]])
    a.containVirus(grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]])