# -*- coding: utf-8 -*-
# ======================================
# @File    : 964.py
# @Time    : 2020/6/24 4:31 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [964. 表示数字的最少运算符](https://leetcode-cn.com/problems/least-operators-to-express-number/)
    """
    @timeit
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from math import log
        from functools import lru_cache
        @lru_cache(None)
        def f(cur):
            # 避免多加一个+号，返回-1
            if cur == 0:
                return -1
            if cur < x:
                # 不足x的部分，比较两种操作
                # 1，cur = cur * (x/x) = x/x+x/x+...+x/x (cur个/和cur-1个+)
                # 2，cur = x - (x-cur) * (x/x) = x-x/x-x/x-...-x/x (x-cur个-和/)
                return min(cur * 2 - 1, (x - cur) * 2)
            # x的n次幂有n-1个*
            n = int(log(cur, x))
            c = x ** n
            # 计算剩余部分的运算符数
            res = f(cur - c) + n
            if c * x < 2 * cur:
                res = min(res, f(c * x - cur) + 1 + n)
            # 答案为n-1 + 1 + res = n + res，注意res如果是0不用算加号
            return res
        return f(target)

if __name__ == '__main__':
    a = Solution()
    a.leastOpsExpressTarget(3,19)
    a.leastOpsExpressTarget(5,501)
    a.leastOpsExpressTarget(100, 100000000)
    a.leastOpsExpressTarget(2, 125046)