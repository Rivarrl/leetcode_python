# -*- coding: utf-8 -*-
# ======================================
# @File    : 5353.py
# @Time    : 2020/3/8 10:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1375. 灯泡开关 III](https://leetcode-cn.com/problems/bulb-switcher-iii/)
    """
    @timeit
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        n = len(light)
        q = 0
        for i in range(n):
            q = max(q, light[i])
            if q == i + 1:
                res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.numTimesAllBlue([2,1,3,5,4])
    a.numTimesAllBlue([3,2,4,1,5])
    a.numTimesAllBlue([4,1,2,3])
    a.numTimesAllBlue([2,1,4,3,6,5])
    a.numTimesAllBlue([1,2,3,4,5,6])