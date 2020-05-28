# -*- coding: utf-8 -*-
# ======================================
# @File    : 5385.py
# @Time    : 2020/5/2 22:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1432. 改变一个整数能得到的最大差值](https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer/)
    """
    @timeit
    def maxDiff(self, num: int) -> int:
        x = y = z = str(num)
        for i in range(len(z)):
            if int(z[i]) < 9:
                x = x.replace(z[i], '9')
                break
        if int(z[0]) > 1: y = y.replace(z[0], '1')
        else:
            for i in range(1, len(z)):
                if z[i] != z[0] and int(z[i]) > 0:
                    y = y.replace(z[i], '0')
                    break
        return int(x) - int(y)

if __name__ == '__main__':
    a = Solution()
    a.maxDiff(555)
    a.maxDiff(9)
    a.maxDiff(123456)
    a.maxDiff(10000)
    a.maxDiff(9288)
    a.maxDiff(1101057)