# -*- coding: utf-8 -*-
# ======================================
# @File    : 1641.py
# @Time    : 2020/11/14 21:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1641. 统计字典序元音字符串的数目](https://leetcode-cn.com/problems/count-sorted-vowel-strings/)
    """
    @timeit
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(1, n):
            e += a
            i += e
            o += i
            u += o
        return a + e + i + o + u



if __name__ == '__main__':
    a = Solution()
    a.countVowelStrings(1)
    a.countVowelStrings(2)
    a.countVowelStrings(33)