# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/5/10 20:01
# @Author  : Rivarrl
# ======================================

def f(n, x):
    if n < 11: return 0
    i = x.find('8')
    return i >= 0 and n - i >= 11

if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        n = int(input())
        x = input()
        res = f(n, x)
        print(["NO", "YES"][res])
