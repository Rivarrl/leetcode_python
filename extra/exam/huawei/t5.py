# -*- coding: utf-8 -*-
# ======================================
# @File    : t5.py
# @Time    : 2020/5/22 19:44
# @Author  : Rivarrl
# ======================================

def gcd(x, y):
    if x == 0: return y
    return gcd(y%x, x)

def f(N, M):
    d = {e:e**2 for e in range(N, M+1)}
    res = []
    for c in range(N, M+1):
        a, b = N, c
        while a < b:
            if d[a] + d[b] > d[c]:
                b -= 1
            elif d[a] + d[b] < d[c]:
                a += 1
            else:
                if gcd(gcd(a, b), c) == 1: res.append((a, b, c))
                a += 1
                b -= 1
    return sorted(res)

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    res = f(N, M)
    if not res:
        print("NA")
    else:
        for a, b, c in res:
            print(a, b, c)
