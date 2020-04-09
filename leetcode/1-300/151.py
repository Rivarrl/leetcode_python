# -*- coding: utf-8 -*-
# ======================================
# @File    : 151.py
# @Time    : 2020/4/10 0:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def reverseWords(self, s: str) -> str:
        n = len(s)
        tmp = ''
        f = 1
        st = [0]
        for i in range(n):
            if s[i] == ' ':
                if f:
                    continue
                else:
                    f = 1
                    st += [len(tmp) + 1]
            else:
                f = 0
            tmp += s[i]
        if not tmp: return ""
        if tmp[-1] == ' ':
            tmp = tmp[:-1]
            st = st[:-1]
        lst = len(tmp)
        res = ''
        for i in range(len(st)-1, -1, -1):
            for j in range(st[i], lst):
                res += tmp[j]
            if i > 0: res += ' '
            lst = st[i] - 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.reverseWords("the sky is blue")
    a.reverseWords("  hello world!  ")
    a.reverseWords("a good   example")
