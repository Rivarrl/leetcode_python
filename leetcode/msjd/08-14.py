# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-14.py
# @Time    : 2020/12/19 0:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.14. 布尔运算](https://leetcode-cn.com/problems/boolean-evaluation-lcci/)
    """
    @timeit
    def countEval(self, s: str, result: int) -> int:
        res = 0
        n = len(s)
        def f(i, s):
            if i == n:


        f(0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.countEval(s = "1^0|0|1", result = 0)
    a.countEval(s = "0&0&0&1^1|0", result = 1)