# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-04.py
# @Time    : 2020/10/13 23:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.04. 下一个数](https://leetcode-cn.com/problems/closed-number-lcci/)
    """
    @timeit
    def findClosedNumbers(self, num: int) -> List[int]:
        def f(x):
            r = 0
            while x:
                x &= (x - 1)
                r += 1
            return r
        c = f(num)
        x, y = num + 1, num - 1
        while x < (1 << 31) and f(x) != c:
            x += 1
        while y >= 0 and f(y) != c:
            y -= 1
        if x == (1 << 31): x = -1
        return [x, y]

if __name__ == '__main__':
    a = Solution()
    a.findClosedNumbers(2)
    a.findClosedNumbers(1)
    a.findClosedNumbers(14)