# -*- coding: utf-8 -*-
# ======================================
# @File    : 335.py
# @Time    : 2019/12/19 1:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [335. 路径交叉](https://leetcode-cn.com/problems/self-crossing/)
    """
    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        数学题：记录东南西北方向最外圈的值
        """
        n = len(x)
        if n < 4: return True
        N, W, S, E = x[:4]

        i = 4
        while i < n:




if __name__ == '__main__':
    a = Solution()
    a.isSelfCrossing([2,1,1,2])
    a.isSelfCrossing([1,2,3,4])
    a.isSelfCrossing([1,1,1,1])