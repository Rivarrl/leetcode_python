# -*- coding: utf-8 -*-
# ======================================
# @File    : hwm2.py
# @Time    : 2020/3/31 9:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

@timeit
def solve(a, b):
    n,m = len(a), len(b)
    i = j = 0
    res = []
    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
    return res

if __name__ == '__main__':
    solve([1,2,5,7,11,15], [3,4,9,11,13,19,23])