# -*- coding: utf-8 -*-
# ======================================
# @File    : simple6.py
# @Time    : 2019/10/8 10:05
# @Author  : Rivarrl
# ======================================

def numPrimeArrangements(n):
    """
    1175. 质数排列
    请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
    让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
    由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
    示例 1：
    输入：n = 5
    输出：12
    解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
    示例 2：
    输入：n = 100
    输出：682289015
    提示：
    1 <= n <= 100
    :param n: int
    :return: int
    """
    def f(x):
        ans = 1
        for i in range(1, x+1):
            ans = (ans * i) % mod
        return ans
    prime = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
    mod = 10**9 + 7
    p = 0
    for i in range(1, n+1):
        if i in prime:
            p += 1
    return (f(n - p) * f(p)) % mod


def robotSim(commands, obstacles):
    """
    874. 模拟行走机器人
    机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
    -2：向左转 90 度
    -1：向右转 90 度
    1 <= x <= 9：向前移动 x 个单位长度
    在网格上有一些格子被视为障碍物。
    第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
    如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
    返回从原点到机器人的最大欧式距离的平方。
    示例 1：
    输入: commands = [4,-1,3], obstacles = []
    输出: 25
    解释: 机器人将会到达 (3, 4)
    示例 2：
    输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    输出: 65
    解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
    提示：
    0 <= commands.length <= 10000
    0 <= obstacles.length <= 10000
    -30000 <= obstacle[i][0] <= 30000
    -30000 <= obstacle[i][1] <= 30000
    答案保证小于 2 ^ 31
    :param commands: List[int]
    :param obstacles: List[List[int]]
    :return: int
    """
    from collections import defaultdict
    def turn(s, c):
        if s == -1:
            if c[0] != 0:
                c[0] *= -1
        else:
            if c[1] != 0:
                c[1] *= -1
        c[0], c[1] = c[1], c[0]

    n = [0, 0]
    d = [0, 1]
    ans = 0
    od = defaultdict(list)
    odr = defaultdict(list)
    for o in obstacles:
        od[o[0]].append(o[1])
        odr[o[1]].append(o[0])
    for c in commands:
        if c in {-1, -2}:
            turn(c, d)
        elif 1 <= c <= 9:
            if d[0] == 0:
                # 上下
                dst = n[1] + d[1] * c
                if od[n[0]]:
                    for e in od[n[0]]:
                        if d[1] == 1:
                            # 上
                            if e > n[1]:
                                dst = min(e-1, dst)
                        else:
                            # 下
                            if e < n[1]:
                                dst = max(e+1, dst)
                n[1] = dst
            else:
                # 左右
                dst = n[0] + d[0] * c
                if odr[n[1]]:
                    for e in odr[n[1]]:
                        if d[0] == 1:
                            # 右
                            if e > n[0]:
                                dst = min(e-1, dst)
                        else:
                            # 左
                            if e < n[0]:
                                dst = max(e+1, dst)
                n[0] = dst
            ans = max(n[0] ** 2 + n[1] ** 2, ans)
    return ans


def uniqueOccurrences(arr):
    """
    1207. 独一无二的出现次数
    给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
    示例 1：
    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
    示例 2：
    输入：arr = [1,2]
    输出：false
    示例 3：
    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true
    提示：
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
    :param arr: List[int]
    :return: bool
    """
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    return len(d.values()) == len(set(d.values()))


def powerfulIntegers(x, y, bound):
    """
    970. 强整数
    给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
    返回值小于或等于 bound 的所有强整数组成的列表。
    你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
    示例 1：
    输入：x = 2, y = 3, bound = 10
    输出：[2,3,4,5,7,9,10]
    解释：
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2
    示例 2：
    输入：x = 3, y = 5, bound = 15
    输出：[2,4,6,8,10,14]
    提示：
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
    :param x: int
    :param y: int
    :param bound: int
    :return: List[int]
    """
    i = 0
    res = []
    while y ** i <= bound:
        j = 0
        while x ** j + y ** i <= bound:
            res.append(x**j + y**i)
            if x == 1:
                break
            j += 1
        if y == 1:
            break
        i += 1
    return list(set(res))


if __name__ == '__main__':
    x = [26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]
    uniqueOccurrences(x)
    # a = [-2,-1,8,9,6]
    # b = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
    # robotSim(a, b)
    # x = numPrimeArrangements(5)
    # print(x)
    pass