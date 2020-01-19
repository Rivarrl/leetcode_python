# -*- coding: utf-8 -*-
# ======================================
# @File    : 5316.py
# @Time    : 2020/1/19 10:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def printVertically(self, s: str) -> List[str]:
        sp = s.split(' ')
        n = max([len(a) for a in sp])
        res = [''] * n
        for i in range(n):
            for j in range(len(sp)):
                if i < len(sp[j]):
                    res[i] += sp[j][i]
                else:
                    res[i] += ' '
        return [e.rstrip() for e in res]


if __name__ == '__main__':
    a = Solution()
    a.printVertically("HOW ARE YOU")
    a.printVertically("TO BE OR NOT TO BE")
    a.printVertically("CONTEST IS COMING")