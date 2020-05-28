# -*- coding: utf-8 -*-
# ======================================
# @File    : t3.py
# @Time    : 2020/5/28 19:24
# @Author  : Rivarrl
# ======================================
import sys

# 给定一个字符串s，你可以通过在字符串前面添加字符将其转化为回文串，找到并返回可以用这种方式转换的最短回文串

def f(x):
    n = len(x)
    if x == x[::-1]: return x
    pre = ''
    for i in range(n-1, -1, -1):
        pre += x[i]
        tmp = pre + x
        if tmp == tmp[::-1]:
            return tmp

if __name__ == '__main__':
    for line in sys.stdin:
        x = line.strip()
        res = f(x)
        print(res)