# -*- coding: utf-8 -*-
# ======================================
# @File    : 1496.py
# @Time    : 2020/7/17 5:21 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1496. 判断路径是否相交](https://leetcode-cn.com/problems/path-crossing/)
    """
    @timeit
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        direction = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E": (0, 1)}
        st = (0, 0)
        s.add(st)
        for c in path:
            st = (st[0] + direction[c][0], st[1] + direction[c][1])
            if st in s:
                return True
            s.add(st)
        return False


if __name__ == '__main__':
    a = Solution()
    a.isPathCrossing("NES")
    a.isPathCrossing("NESWW")