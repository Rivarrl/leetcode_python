# -*- coding: utf-8 -*-
# ======================================
# @File    : cpm.py
# @Time    : 2019/12/3 17:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# Concurrency Processing Management
# 优先级限制下的并行任务调度问题
# 思路：
# 将每个任务拆分为两个节点，任务i起始指向任务i结束，权值为任务i的执行从开始到结束所需时间。
# 任务之间按优先级高指向优先级低权值为0
# 再加上总体起始节点s和结束节点t，s指向所有任务i的起始节点，所有任务i的终止节点指向t
# 就构成了一个有向无环图（DAG），权值非负，问题转换成求DAG的最长路径，用acycliclp的拓扑图方法即可
maxn = 100
head = [-1] * maxn
to = [0] * maxn
weight = [0] * maxn
nxt = [0] * maxn
tot = 0
N = s = t = 0
inf_w = float('inf')
dist_to = [-inf_w] * maxn
edge_to = [-1] * maxn

def add_edge(u, v, w):
    global tot
    to[tot] = v
    weight[tot] = w
    nxt[tot] = head[u]
    head[u] = tot
    tot += 1

# 复习一遍拓扑图求最长路径，这次用链式前向星存图
def topological():
    degree_in = [0] * (t+1)
    for u in range(t+1):
        idx = head[u]
        while idx != -1:
            degree_in[to[idx]] += 1
            idx = nxt[idx]
    stk = [u for u in range(t+1) if degree_in[u] == 0]
    tpsort, i = [0] * (t+1), 0
    while stk:
        u = stk.pop()
        tpsort[i] = u
        i += 1
        idx = head[u]
        while idx != -1:
            v = to[idx]
            degree_in[v] -= 1
            if degree_in[v] == 0:
                stk.insert(0, v)
            idx = nxt[idx]
    return tpsort

def acyclic_lp():
    tpsort = topological()
    dist_to[s] = 0.0
    def relax(u):
        idx = head[u]
        while idx != -1:
            v, w = to[idx], weight[idx]
            if dist_to[v] < dist_to[u] + w:
                dist_to[v] = dist_to[u] + w
                edge_to[v] = idx
            idx = nxt[idx]
    for u in tpsort:
        relax(u)

def display():
    print("Start times:")
    for u in range(N):
        dis = dist_to[u]
        print("{:3d}:{:6.1f}".format(u, dis))
    print('Finish time: %5.1f' % dist_to[t])



if __name__ == '__main__':
    import re
    # 一共N个任务，编号0~N-1。
    # 第一行输入任务数N
    # 后面N行每一行依次输入第i个任务所需时间及优先于哪些任务id
    with open('./data/cpm.txt', 'r', encoding='utf-8') as f:
        N = int(f.readline().strip())
        s = 2 * N
        t = s + 1
        for i in range(N):
            line = f.readline().strip()
            a = re.split('\s+', line)
            duration = float(a[0])
            add_edge(i, i + N, duration)
            add_edge(s, i, 0.0)
            add_edge(i + N, t, 0.0)
            for e in list(map(int, a[1:])):
                add_edge(i+N, e, 0.0)
    acyclic_lp()
    display()