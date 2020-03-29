# -*- coding: utf-8 -*-
# ======================================
# @File    : mst1.py
# @Time    : 2020/3/27 0:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

"""
ms 2020面试题
士兵排阵
给定所有士兵战力值列表arr和队伍数n
要求同一队的士兵战力值各不相同，求满足条件的各队最高与最低战力差的和的最小值。
"""

@timeit
def t(arr, n):
    d = {}
    for e in arr:
        d[e] = d.get(e, 0) + 1
    m = len(arr)//n
    st = sorted(list(set(arr)))
    res = 0
    for j in range(n):
        s = set()
        i = 0
        for e in st:
            if d[e] == n - j:
                i += 1
                d[e] -= 1
                s.add(e)
            elif d[e] > n - j:
                return -1
        for e in st:
            if i >= m:
                break
            if not e in s and d[e] > 0:
                i += 1
                s.add(e)
                d[e] -= 1
        res += max(s) - min(s)
    return res

if __name__ == '__main__':
    t([1,1],1)
    t([5,5,10,10,4,8,3,6,4,8,3,6], 3)
    t([1,2,3,4,5,5,6,6,10,9,8,7], 3)