# -*- coding: utf-8 -*-
# ======================================
# @File    : 5637.py
# @Time    : 2020/12/27 12:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5637. 判断字符串的两半是否相似]()
    """
    @timeit
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = b = 0
        d = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            if i < n // 2:
                a += int(s[i].lower() in d)
            else:
                b += int(s[i].lower() in d)
        return a == b

if __name__ == '__main__':
    a = Solution()
    a.halvesAreAlike(s = "book")
    a.halvesAreAlike(s = "textbook")
    a.halvesAreAlike(s = "MerryChristmas")
    a.halvesAreAlike(s = "AbCdEfGh")