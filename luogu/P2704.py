# -*- coding: utf-8 -*-
# ======================================
# @File    : P2704.py
# @Time    : 2020/2/9 14:21
# @Author  : Rivarrl
# ======================================
import sys
# P2704 [NOI2001]炮兵阵地
# 状态压缩dp
# 状态与上两行的相关
# 将摆放士兵状态设为1，否则为0
# 两行相与不是0时存在互相攻击的炮兵
# dp[i][j][k]表示第i行状态为j，第i-1行状态为k时的最大炮兵数

def solve(arr, n, m):
    # sta保存状态，count保存该状态号对应状态的炮兵数(1的个数)
    sta, count = [0] * 70, [0] * 70
    length = 0
    # 1024^2*100枚举范围过大，需要预处理，枚举行内符合条件的状态保存到sta中
    for i in range(1 << m):
        if (i & (i << 1)) or (i & (i << 2)): continue
        sta[length] = k = i
        while k > 0:
            count[length] += k & 1
            k >>= 1
        length += 1
    dp = [[[0] * length for _ in range(length)] for _ in range(n)]
    # 初始化dp[0][i][0]
    for i in range(length):
        # 不能把炮兵放在山上
        if sta[i] & arr[0]: continue
        dp[0][i][0] = count[i]
    # 初始化dp[1][i][j]
    for i in range(length):
        if sta[i] & arr[1]: continue
        for j in range(length):
            if sta[j] & arr[0]: continue
            if sta[i] & sta[j]: continue
            dp[1][i][j] = max(dp[1][i][j], dp[0][j][0] + count[i])
    for row in range(2, n):
        # 枚举当前第row行状态
        for i in range(length):
            if sta[i] & arr[row]: continue
            # 枚举row-1行的状态
            for j in range(length):
                # 不能把炮兵放在山上
                if sta[j] & arr[row-1]: continue
                # 不能和row行的打起来
                if sta[i] & sta[j]: continue
                # 枚举row-2行的状态
                for k in range(length):
                    # 不能把炮兵放在山上
                    if sta[k] & arr[row-2]: continue
                    # 不能打架
                    if (sta[i] & sta[k]) or (sta[j] & sta[k]): continue
                    # 将row-1行合理的布阵结果dp[row-1][j][k]加上第row行的布阵数
                    dp[row][i][j] = max(dp[row][i][j], dp[row-1][j][k] + count[i])
    res = 0
    for i in range(length):
        for j in range(length):
            res = max(res, dp[n-1][i][j])
    return res

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    n, m = map(int, line1.split(' '))
    arr = [0] * n
    for i in range(n):
        line = sys.stdin.readline().strip()
        for j in range(m):
            # 山地用1，平地用0
            # 有山的位置不可以摆放炮兵，等价于摆放过炮兵的状态1
            if line[j] == 'H':
                arr[i] |= 1 << j
    res = solve(arr, n, m)
    print(res)