# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/5/28 19:12
# @Author  : Rivarrl
# ======================================
import sys
# 输入一个数组，至多可以修改数组中的一个元素，检查是否可以将这个数组变成非递减数组。

def f(arr):
    n = len(arr)
    rv = 0
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            rv += 1
        if rv == 2: return False
    return True

if __name__ == '__main__':
    for line in sys.stdin:
        arr = list(map(int, line.split()))
        res = f(arr)
        print(["false", "true"][res])