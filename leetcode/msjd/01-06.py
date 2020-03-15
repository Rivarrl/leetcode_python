# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-06.py
# @Time    : 2020/3/16 0:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def compressString(self, S: str) -> str:
        n = len(S)
        i = 0
        res = ''
        while i < n:
            j = i
            while j < n - 1 and S[j] == S[j+1]:
                j += 1
            res += S[i] + '%d'%(j+1-i)
            i = j + 1
        return res if len(res) < n else S

if __name__ == '__main__':
    a = Solution()
    a.compressString("aabcccccaaa")
    a.compressString("abbccd")