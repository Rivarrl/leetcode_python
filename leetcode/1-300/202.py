# -*- coding: utf-8 -*-
# ======================================
# @File    : 202.py
# @Time    : 2020/4/30 14:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [202. 快乐数](https://leetcode-cn.com/problems/happy-number/)
    """
    @timeit
    def isHappy(self, n: int) -> bool:
        def f(x):
            res = 0
            while x > 0:
                res += (x % 10) ** 2
                x //= 10
            return res
        slow = f(n)
        fast = f(slow)
        while slow != fast:
            slow = f(slow)
            fast = f(f(fast))
        return 1 in (slow, fast)

if __name__ == '__main__':
    a = Solution()
    a.isHappy(19)
    a.isHappy(18)