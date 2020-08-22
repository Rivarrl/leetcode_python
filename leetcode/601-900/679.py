# -*- coding: utf-8 -*-
# ======================================
# @File    : 679.py
# @Time    : 2020/8/22 23:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [679. 24 点游戏](https://leetcode-cn.com/problems/24-game/)
    """
    @timeit
    def judgePoint24(self, nums: List[int]) -> bool:
        def f(a, b=False, c=False, d=False):
            if c == False:
                return abs(a+b-24) < 0.001 or abs(a-b-24) < 0.001 or abs(a*b-24) < 0.001 or abs(b-a-24) < 0.001 or (False if b==0 else abs(a/b-24) < 0.001) or (False if a==0 else abs(b/a-24) < 0.001)
            elif d == False:
                return f(a+b, c) or f(a-b, c) or f(b-a, c) or f(a*b, c) or (False if b==0 else f(a/b, c)) or (False if a==0 else f(b/a, c)) \
                    or f(b+c, a) or f(b-c, a) or f(c-b, a) or f(b*c, a) or (False if c==0 else f(b/c, a)) or (False if b==0 else f(c/b, a)) \
                    or f(a+c, b) or f(a-c, b) or f(c-a, b) or f(a*c, b) or (False if c==0 else f(a/c, b)) or (False if a==0 else f(c/a, b))
            else:
                return f(a+b, c, d) or f(a-b, c, d) or f(b-a, c, d) or f(a*b, c, d) or (False if b==0 else f(a/b, c, d)) or (False if a==0 else f(b/a, c, d)) \
                    or f(b+c, a, d) or f(b-c, a, d) or f(c-b, a, d) or f(b*c, a, d) or (False if c==0 else f(b/c, a, d)) or (False if b==0 else f(c/b, a, d)) \
                    or f(a+c, b, d) or f(a-c, b, d) or f(c-a, b, d) or f(a*c, b, d) or (False if c==0 else f(a/c, b, d)) or (False if a==0 else f(c/a, b, d)) \
                    or f(a+d, b, c) or f(a-d, b, c) or f(d-a, b, c) or f(a*d, b, c) or (False if d==0 else f(a/d, b, c)) or (False if a==0 else f(d/a, b, c)) \
                    or f(b+d, a, c) or f(b-d, a, c) or f(d-b, a, c) or f(b*d, a, c) or (False if d==0 else f(b/d, a, c)) or (False if b==0 else f(d/b, a, c)) \
                    or f(c+d, a, b) or f(c-d, a, b) or f(d-c, a, b) or f(c*d, a, b) or (False if d==0 else f(c/d, a, b)) or (False if c==0 else f(d/c, a, b))
        return f(*nums)

if __name__ == '__main__':
    a = Solution()
    a.judgePoint24([4, 1, 8, 7])
    a.judgePoint24([1, 2, 1, 2])