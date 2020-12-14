# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-02.py
# @Time    : 2020/12/15 0:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.02. 二进制数转字符串](https://leetcode-cn.com/problems/bianry-number-to-string-lcci/)
    """
    @timeit
    def printBin(self, num: float) -> str:
        import math
        res = ['0.']
        for i in range(32):
            if num == 0:
                return ''.join(res)
            num *= 2
            p = math.floor(num)
            res.append(str(p))
            num -= p
        return 'ERROR'


if __name__ == '__main__':
    a = Solution()
    a.printBin(0.625)
    a.printBin(0.1)