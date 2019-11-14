# -*- coding: utf-8 -*-
# ======================================
# @File    : 397.py
# @Time    : 2019/11/14 11:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [397. 整数替换](https://leetcode-cn.com/problems/integer-replacement/)
    """
    @timeit
    def integerReplacement(self, n: int) -> int:
        """
        思路1：记忆化搜索
        """
        def f(x):
            if x == 1: return 0
            if x in memo: return memo[x]
            res = 1 + min(f(x-1), f(x+1)) if x & 1 else 1 + f(x//2)
            memo[x] = res
            return res
        memo = {}
        return f(n)


    @timeit
    def integerReplacement2(self, n: int) -> int:
        """
        思路2：贪心，偶数不用说，只有一种操作
        奇数的时候，选择连续1的个数2以上的时候+1，也就是xxxx11的时候选择+1
        因为100000这种情况是贪心最想要的，而想要做出这种数，需要在11111时+1
        3是个特例，+1和-1后产生相同的1的个数，但是-1距离1更近，需要进行特判
        """
        res = 0
        while n > 1:
            if n & 1:
                if n == 3:
                    n -= 1
                else:
                    if (n & 2):
                        n += 1
                    else:
                        n -= 1
            else:
                n >>= 1
            res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    # a.integerReplacement(65535)
    a.integerReplacement2(763)

