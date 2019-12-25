# -*- coding: utf-8 -*-
# ======================================
# @File    : 1016.py
# @Time    : 2019/12/25 13:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1016. 子串能表示从 1 到 N 数字的二进制串](https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n/)
    表示N>>1 ~ N之间的数就可以
    """
    @timeit
    def queryString(self, S: str, N: int) -> bool:
        for n in range(max(1, N >> 1), N+1):
            if S.find(bin(n)[2:]) < 0: return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.queryString(S = "0110", N = 3)
    a.queryString(S = "0110", N = 4)
