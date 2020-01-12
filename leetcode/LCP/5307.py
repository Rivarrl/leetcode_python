# -*- coding: utf-8 -*-
# ======================================
# @File    : 5307
# @Time    : 2020/1/12 13:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5307. 将整数转换为两个无零整数的和]()
    """
    @timeit
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' in str(i) or '0' in str(n-i):
                continue
            return [i, n-i]


if __name__ == '__main__':
    a = Solution()
    a.getNoZeroIntegers(2)
    a.getNoZeroIntegers(11)
    a.getNoZeroIntegers(10000)
    a.getNoZeroIntegers(69)
    a.getNoZeroIntegers(1010)