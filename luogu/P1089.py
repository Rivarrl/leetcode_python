# -*- coding: utf-8 -*-
# ======================================
# @File    : P1089.py
# @Time    : 2019/12/18 23:14
# @Author  : Rivarrl
# ======================================
import sys

def solve():
    cur = mom = 0
    for i in range(12):
        cost = int(sys.stdin.readline().strip())
        cur += 300 - cost
        if cur < 0: return ~i
        if cur >= 100:
            mom += cur - cur % 100
            cur %= 100
    return int(mom * 1.2) + cur

if __name__ == '__main__':
    print(solve())