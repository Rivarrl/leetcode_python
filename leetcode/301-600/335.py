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
    @timeit
    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        分三类：2112，21311，213222
        """
        n = len(x)
        if n >= 4:
            for i in range(3, n):
                if x[i] >= x[i-2] and x[i-1] <= x[i-3]: return True
                if i > 3 and x[i] >= x[i-2] - x[i-4] and x[i-1] == x[i-3]: return True
                if i > 4 and x[i-2] > x[i-4] and x[i-2] >= x[i] >= x[i-2] - x[i-4] and x[i-3] >= x[i-1] >= x[i-3] - x[i-5]: return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.isSelfCrossing([2,1,1,2])
    a.isSelfCrossing([1,2,3,4])
    a.isSelfCrossing([1,1,1,1])