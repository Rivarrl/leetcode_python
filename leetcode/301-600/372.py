# -*- coding: utf-8 -*-
# ======================================
# @File    : 372.py
# @Time    : 2020/4/21 19:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [372. 超级次方](https://leetcode-cn.com/problems/super-pow/)
    """
    @timeit
    def superPow(self, a: int, b: List[int]) -> int:
        # 快速幂
        def pow(a, b):
            if b == 0: return 1
            a %= 1337
            res = 1
            while b:
                if b & 1:
                    res *= a
                    res %= 1337
                a *= a
                b >>= 1
            return res
        n = len(b)
        if n == 0: return 1
        res = 1
        c = b.pop()
        res *= pow(a, c)
        res *= pow(self.superPow(a, b), 10)
        res %= 1337
        return res

if __name__ == '__main__':
    a = Solution()
    a.superPow(a = 2, b = [3])
    a.superPow(a = 2, b = [1,0])