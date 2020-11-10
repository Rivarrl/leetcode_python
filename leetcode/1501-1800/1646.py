# -*- coding: utf-8 -*-
# ======================================
# @File    : 1646.py
# @Time    : 2020/11/10 1:03 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1646. 获取生成数组中的最大值]()
    """
    @timeit
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        num = [0] * (n+1)
        num[1] = 1
        for i in range(2, n+1):
            if i & 1:
                num[i] = num[i//2] + num[i//2 + 1]
            else:
                num[i] = num[i//2]
        return max(num)

if __name__ == '__main__':
    a = Solution()
    a.getMaximumGenerated(n = 7)
    a.getMaximumGenerated(n = 2)
    a.getMaximumGenerated(n = 3)
