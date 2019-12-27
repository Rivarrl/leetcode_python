# -*- coding: utf-8 -*-
# ======================================
# @File    : P1089.py
# @Time    : 2019/12/18 23:14
# @Author  : Rivarrl
# ======================================
import sys

def solve():
    jinjin = mom = 0
    for i in range(12):
        cost = int(sys.stdin.readline().strip())
        jinjin += 300 - cost
        if jinjin < 0: return ~i
        if jinjin >= 100:
            mom += jinjin - jinjin % 100
            jinjin %= 100
    return int(mom * 1.2) + jinjin

if __name__ == '__main__':
    print(solve())