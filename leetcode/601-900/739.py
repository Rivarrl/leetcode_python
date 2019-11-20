# -*- coding: utf-8 -*-
# ======================================
# @File    : 739.py
# @Time    : 2019/11/21 0:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/)
    """
    @timeit
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        思路：单调栈，维护一个单调递减的栈即可
        """
        stk = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            while stk and T[stk[-1]] < t:
                j = stk.pop()
                res[j] = i - j
            stk.append(i)
        return res

if __name__ == '__main__':
    a = Solution()
    a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    # [1, 1, 4, 2, 1, 1, 0, 0]