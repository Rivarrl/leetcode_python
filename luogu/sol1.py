# -*- coding: utf-8 -*-
# ======================================
# @File    : sol1.py
# @Time    : 2019/11/7 23:47
# @Author  : Rivarrl
# ======================================

import sys

# P2678. 跳石头
def p2678(L, N, M, arr):
    arr = [0] + arr + [L]
    def judge(x):
        last = removes = 0
        for i in range(1, N+2):
            if arr[i] - last < x:
                removes += 1
            else:
                last = arr[i]
        # 如果当前的步长需要移除的石头数超出了预算返回false
        if removes > M:
            return False
        return True

    lo, hi = 1, L
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if judge(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    L, N, M = map(int, line1.split(' '))
    arr = [0] * N
    for i in range(N):
        arr[i] = int(input())
    res = p2678(L, N, M, arr)
    print(res)