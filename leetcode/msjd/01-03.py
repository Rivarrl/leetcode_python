# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-03.py
# @Time    : 2020/5/9 23:09
# @Author  : Rivarrl
# ======================================
# [面试题 01.03. URL化](https://leetcode-cn.com/problems/string-to-url-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def replaceSpaces(self, S: str, length: int) -> str:
        s = [c for c in S]
        n = len(s)
        i, j = length - 1, n - 1
        while i >= 0 and j >= 0:
            if s[i] == ' ':
                s[j] = '0'
                s[j-1] = '2'
                s[j-2] = '%'
                j -= 2
            else:
                s[j] = s[i]
            i -= 1
            j -= 1
        return ''.join(s[j+1:])

if __name__ == '__main__':
    a = Solution()
    a.replaceSpaces("Mr John Smith    ", 13)
    a.replaceSpaces("               ", 5)
    a.replaceSpaces("ds sdfs afs sdfa dfssf asdf             ", 27)