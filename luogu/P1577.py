# -*- coding: utf-8 -*-
# ======================================
# @File    : P1577.py
# @Time    : 2019/11/8 17:42
# @Author  : Rivarrl
# ======================================
import sys

# P1557. 切绳子

def p1557(N, K, arr):
    def judge(x):
        if x * K > SUM: return False
        piece = 0
        for e in arr:
            piece += e // x
        if piece < K:
            return False
        return True

    lo, hi = 0, MAX
    while lo < hi:
        mid = lo + (hi + 1 - lo) // 2
        if judge(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo / 100


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    N, K = map(int, line1.split(' '))
    arr = [0] * N
    MAX, SUM = -1, 0
    for i in range(N):
        arr[i] = int(float(input()) * 100)
        SUM += arr[i]
        if arr[i] > MAX:
            MAX = arr[i]
    res = p1557(N, K, arr)
    print("%.2f"%res)