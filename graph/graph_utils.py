# -*- coding: utf-8 -*-
# ======================================
# @File    : graph_utils.py
# @Time    : 2019/11/18 23:02
# @Author  : Rivarrl
# ======================================
from collections import defaultdict

def build_graph(connections):
    # 构图，邻接表
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
    return graph

def reverse_graph(graph):
    r_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            # 因为构造graph用的邻接表是假的，reverse相当于将链表倒置，所以用后进先出模拟链表倒置
            r_graph[v].insert(0, u)
    return r_graph