# -*- coding: utf-8 -*-
# ======================================
# @File    : 1759
# @Time    : 2021/3/5 13:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1759. 统计同构子字符串的数目](https://leetcode-cn.com/problems/count-number-of-homogenous-substrings/)
    """
    @timeit
    def countHomogenous(self, s: str) -> int:
        l = r = 0
        n = len(s)
        res = 0
        while r < n:
            while r + 1 < n and s[r] == s[r+1]:
                r += 1
            x = r - l + 1
            res += (1 + x) * x // 2
            r += 1
            l = r
        return res % (10 ** 9 + 7)

if __name__ == '__main__':
    a = Solution()
    a.countHomogenous(s = "abbcccaa")
    a.countHomogenous(s = "xy")
    a.countHomogenous(s = "zzzzz")