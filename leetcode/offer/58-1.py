# -*- coding: utf-8 -*-
# ======================================
# @File    : 58-1.py
# @Time    : 2020/4/30 21:31
# @Author  : Rivarrl
# ======================================
# [面试题58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)

if __name__ == '__main__':
    a = Solution()
    a.reverseWords("the sky is blue")
    a.reverseWords("  hello world!  ")
    a.reverseWords("a good   example")