# -*- coding: utf-8 -*-
# ======================================
# @File    : km.py
# @Time    : 2019/11/29 14:13
# @Author  : Rivarrl
# ======================================

# KM算法
# 模板题 HDU-2255
# https://vjudge.net/problem/HDU-2255
# 根据二分图的图解，点集x在左边，y在右边，为x分配其最高的边权作为期望值，y期望值初始为0
# KM算法中，可将没有连接的两个点xi, yj认为它们有一条期望为0的边，即最差情况选择这条边
# 然后一边进行匈牙利算法，一边更新两侧期望值，直到找到完全匹配

# 匈牙利算法 + slack
def dfs(x):
    vx[x] = 1
    for y in range(n):
        if vy[y]: continue
        dist = ex[x] + ey[y]
        if dist == edges[x][y]:
            # 符合匹配要求的时候才修改vis值
            vy[y] = 1
            if connect[y] == -1 or dfs(connect[y]):
                connect[y] = x
                return 1
        else:
            # slack的作用是记录当当前权值匹配失败时，所有xi需要降低至少多少权值才可以去找下一个选择yj
            slack[y] = min(slack[y], dist - edges[x][y])
    return 0

def km():
    # 给x集合赋初始期望值
    for i in range(n):
        ex[i] = max(edges[i][j] for j in range(n))
    for x in range(n):
        # 重置松弛数组
        for e in range(n): slack[e] = inf
        while True:
            # vis数组配套dfs用，每次dfs前都需要重新初始化
            for e in range(n): vx[e] = vy[e] = 0
            # 直接匹配成功就跳出
            if dfs(x): break
            # 否则降低期望为最小可降低的期望值
            d = inf
            for y in range(n):
                # 从没有访问过的y中选择降权的目标
                if not vy[y]: d = min(d, slack[y])
            # 对刚刚dfs中访问过的x/y进行对应的更新
            for z in range(n):
                # 对被访问过的x来说，需要减去这个期望值
                if vx[z]: ex[z] -= d
                # 对被访问过的y来说，需要加上这个期望值来维持整体平衡
                if vy[z]: ey[z] += d
                # 对未被访问过的y来说，需要让松弛数组减去这个期望值
                # 因为x的期望值-d而y的未变，所以它们的距离-d，其中会有至少1个slack[z]减到0
                else: slack[z] -= d
    return sum(edges[connect[y]][y] for y in range(n))

if __name__ == '__main__':
    maxn = 302
    inf = 0x3f3f3f3f
    # 权值关系
    edges = [[0] * maxn for _ in range(maxn)]
    # x/y集合的期望值
    ex, ey = [0] * maxn, [0] * maxn
    # x/y集合的vis数组
    vx, vy = [0] * maxn, [0] * maxn
    # 匹配数组
    connect = [-1] * maxn
    # 松弛数组，用来记录x可参与竞争还需多少期望值
    # 由于程序这里要取最小，初始值设为无穷大
    slack = [inf] * maxn
    # 假装输入
    n = 5
    # 答案：29
    matrix = [[3, 4, 6, 4, 9],
              [6, 4, 5, 3, 8],
              [7, 5, 3, 4, 2],
              [6, 3, 2, 2, 5],
              [8, 4, 5, 4, 7]]
    for i in range(n):
        for j in range(n):
            edges[i][j] = matrix[i][j]
    res = km()
    print(res)