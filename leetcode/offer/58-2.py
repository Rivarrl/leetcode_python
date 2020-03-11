# -*- coding: utf-8 -*-
# ======================================
# @File    : 58-2.py
# @Time    : 2020/3/12 0:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# [面试题58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

class Solution:
    @timeit
    def reverseLeftWords(self, s: str, n: int) -> str:
        m = len(s)
        res = ""
        for i in range(n, m + n):
            res += s[i % m]
        return res

if __name__ == '__main__':
    a = Solution()
    a.reverseLeftWords(s = "abcdefg", n = 2)
    a.reverseLeftWords(s = "lrloseumgh", n = 6)
