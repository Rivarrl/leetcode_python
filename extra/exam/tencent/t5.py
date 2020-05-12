# -*- coding: utf-8 -*-
# ======================================
# @File    : t5.py
# @Time    : 2020/5/10 20:59
# @Author  : Rivarrl
# ======================================

def f(s, k):
    """
    dp[i][j][0] 前i次操作修改j次得到的正向最远距离
    dp[i][j][1] 前i次操作修改j次得到的负向最远距离
    # 分两种情况，s[i]是T或F，每个情况又分为修改和没改两种
    # 对正向取最大，负向取最小，最后取abs最大的
    if s[i] == 'T':
        dp[i][j][0] = max(dp[i-1][j-1][0] + 1, -dp[i-1][j][1])
        dp[i][j][1] = min(dp[i-1][j-1][1] + 1, -dp[i-1][j][0])
    if s[i] == 'F':
        dp[i][j][0] = max(-dp[i-1][j-1][1], dp[i-1][j][0] + 1)
        dp[i][j][1] = min(-dp[i-1][j-1][0], dp[i-1][j][1] + 1)
    """
    n = len(s)
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
    c = 0
    for i in range(n):
        if s[i] == 'T':
            c *= -1
        else:
            c += 1
        dp[i + 1][0][0] = dp[i + 1][0][1] = c
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] == 'T':
                dp[i][j][0] = max(dp[i - 1][j - 1][0] + 1, -dp[i - 1][j][1])
                dp[i][j][1] = min(dp[i - 1][j - 1][1] + 1, -dp[i - 1][j][0])
            if s[i - 1] == 'F':
                dp[i][j][0] = max(-dp[i - 1][j - 1][1], dp[i - 1][j][0] + 1)
                dp[i][j][1] = min(-dp[i - 1][j - 1][0], dp[i - 1][j][1] + 1)
    return max(dp[-1][-1][0], -dp[-1][-1][1])


if __name__ == '__main__':
    # s = input()
    # k = int(input())
    s = "FFTFTFTTTFFTFFTTFFFF"
    k = 3
    res = f(s, k)
    print(res)

"""
FFTFTFTTTFFTFFTTFFFF
3
9
"""
