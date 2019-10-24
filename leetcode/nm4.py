# -*- coding: utf-8 -*-
# ======================================
# @File    : nm4.py
# @Time    : 2019/10/24 16:32
# @Author  : Rivarrl
# ======================================
from typing import List

from algorithm_utils import *

def numRollsToTarget(d: int, f: int, target: int) -> int:
    """
    1155. 掷骰子的N种方法
    这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
    我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
    如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。
    示例 1：
    输入：d = 1, f = 6, target = 3
    输出：1
    示例 2：
    输入：d = 2, f = 6, target = 7
    输出：6
    示例 3：
    输入：d = 2, f = 5, target = 10
    输出：1
    示例 4：
    输入：d = 1, f = 2, target = 3
    输出：0
    示例 5：
    输入：d = 30, f = 30, target = 500
    输出：222616187
    提示：
    1 <= d, f <= 30
    1 <= target <= 1000
    """
    if d * f < target: return 0
    mod = 10 ** 9 + 7
    dp = [[0] * (max(f, target)+1) for _ in range(d+1)]
    for i in range(1, f+1):
        dp[1][i] = 1
    for i in range(1, d):
        for j in range(i, target):
            for k in range(1, f+1):
                if j + k <= target:
                    dp[i+1][j+k] += dp[i][j]
    return dp[d][target] % mod


def dieSimulator(n: int, rollMax: List[int]) -> int:
    """
    1223. 掷骰子模拟
    有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
    不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
    现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
    假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
    示例 1：
    输入：n = 2, rollMax = [1,1,2,2,2,3]
    输出：34
    解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
    示例 2：
    输入：n = 2, rollMax = [1,1,1,1,1,1]
    输出：30
    示例 3：
    输入：n = 3, rollMax = [1,1,1,2,2,3]
    输出：181
    提示：
    1 <= n <= 5000
    rollMax.length == 6
    1 <= rollMax[i] <= 15
    """
    dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
    mod = 10 ** 9 + 7
    for j in range(6):
        dp[1][j][0] = dp[1][j][1] = 1
    for i in range(2, n+1):
        for j in range(6):
            g = min(i, rollMax[j])
            dp[i][j][1] = sum(dp[i-1][x][0] for x in range(6) if x != j) % mod
            for k in range(2, g+1):
                dp[i][j][k] = dp[i-1][j][k-1]
            dp[i][j][0] = sum(dp[i][j][x] for x in range(1, g+1)) % mod
    res = sum(dp[n][j][0] for j in range(6))
    print(res)
    return res % mod


if __name__ == '__main__':
    dieSimulator(3, [1,1,1,2,2,3])
    # x = numRollsToTarget(30,30,500)
    # print(x)
    pass