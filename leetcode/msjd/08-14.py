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
        from functools import lru_cache
        n = len(s)
        @lru_cache(None)
        def f(s):
            if not s: return 0


        return f(s)

if __name__ == '__main__':
    a = Solution()
    a.countEval(s = "1^0|0|1", result = 0)
    a.countEval(s = "0&0&0&1^1|0", result = 1)