# -*- coding: utf-8 -*-
# ======================================
# @File    : test.py
# @Time    : 2020/5/11 2:51
# @Author  : Rivarrl
# ======================================
# FFTFTFTTTFFTFFTTFFFF


def f(s, k):
    n = len(s)
    res = 0
    def calc(s):
        res = 0
        for x in s:
            if x == 'F': res += 1
            else: res *= -1
        return abs(res)
    def dfs(s, j, k):
        nonlocal res
        if k == 0:
            res = max(res, calc(s))
            return
        for i in range(j+1, n):
            dfs(s[:i]+'FT'[s[i] == 'F']+s[i+1:], i, k-1)
    dfs(s, -1, k)
    return res

if __name__ == '__main__':
    s = "FFTFTFTTTFFTFFTTFFFF"
    k = 3
    res = f(s, k)
    print(res)