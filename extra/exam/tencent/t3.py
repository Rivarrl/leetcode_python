# -*- coding: utf-8 -*-
# ======================================
# @File    : t3.py
# @Time    : 2020/5/10 20:26
# @Author  : Rivarrl
# ======================================

def f(n, arr):
    arr.sort()
    res = [0] * n
    idx = [0, n-1]
    i, j = 0, 1
    for x in arr:
        res[idx[i]] = x
        idx[i] += j
        j *= -1
        i ^= 1
    return " ".join(map(str, res))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    res = f(n, arr)
    print(res)

"""
2 
10 20

5
3 5 8 2 6
"""