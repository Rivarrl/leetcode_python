# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/5/28 19:05
# @Author  : Rivarrl
# ======================================
import sys

# 一只松鼠一次可以跳上1级台阶，也可以跳上2级，求该松鼠跳上一个n级台阶总共有多少种跳法。
# dp

def f(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

if __name__ == '__main__':
    for line in sys.stdin:
        x = int(line.strip())
        res = f(x)
        print(res)