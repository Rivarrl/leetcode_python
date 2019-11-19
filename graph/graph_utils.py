# -*- coding: utf-8 -*-
# ======================================
# @File    : graph_utils.py
# @Time    : 2019/11/18 23:02
# @Author  : Rivarrl
# ======================================
from collections import defaultdict

# positive infinite weight
inf_w = (1 << 31) - 1

def build_graph(n, connections, direction=1, tp=1):
    # tp 1：dict伪邻接表，2：邻接表，3：邻接矩阵，4：链式前向星
    return {
            1: _fake_linked_list(n, connections, direction),
            2: _linked_list(n, connections, direction),
            3: _matrix(n, connections, direction),
            4: _forward_star_list(n, connections, direction)
            }[tp]


def _fake_linked_list(n, connections, direction=1):
    # 构图，伪邻接表
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        if direction == 0:
            graph[b].append(a)
    return graph


class Node:
    def __init__(self, idx, weight = 1, next = None):
        self.idx = idx
        self.weight = weight
        self.next = next

def _linked_list(n, connections, direction = 1):
    # direction 有向无向 0 无向，1 有向
    # weights 点权 None 无权，list(int) 带权
    def build_connections(a, b, c=None):
        p = arr[a]
        while p.next:
            p = p.next
        p.next = Node(b)
        if c: p.weight = c

    arr = [None] * n
    for i in range(n):
        arr[i] = Node(i)
    w = len(connections[0]) == 3
    for i in range(len(connections)):
        a, b = connections[i][0], connections[i][1]
        c = connections[i][2] if w else None
        build_connections(a, b, c)
        if direction == 0:
            build_connections(b, a, c)
    return arr


def _matrix(n, connections, direction=1):
    # direction 有向无向 0 无向，1 有向
    # weights 点权 None 无权，list(int) 带权
    w = len(connections[0]) == 3
    if w:
        arr = [[inf_w] * n for _ in range(n)]
        for a, b, c in connections:
            arr[a][b] = c
            if direction == 0:
                arr[b][a] = c
    else:
        arr = [[0] * n for _ in range(n)]
        for a, b in connections:
            arr[a][b] = 1
            if direction == 0:
                arr[b][a] = 1
    return arr

class StarNode:
    def __init__(self, to=0, w=0, nxt=0):
        self.to = to
        self.w = w
        self.next = nxt

def _forward_star_list(n, connections, direction=1):
    # direction 有向无向 0 无向，1 有向
    # weights 点权 None 无权，list(int) 带权
    ne = len(connections)
    head = [-1] * n
    arr = [StarNode() for _ in range(ne + 1)]
    w = len(connections[0]) == 3
    for i in range(ne):
        a, b = connections[i][0], connections[i][1]
        arr[i].to = b
        if w: arr[i].w = connections[i][2]
        arr[i].next = head[a]
        head[a] = i
    if direction == 0:
        arr += [StarNode() for _ in range(ne + 1)]
        for i in range(ne):
            j = i + ne
            a, b = connections[i][0], connections[i][1]
            arr[j].to = a
            if w: arr[j].w = connections[i][2]
            arr[j].next = head[b]
            head[b] = j
    return head, arr


def reverse_graph(graph: dict) -> dict:
    # 伪邻接表翻转
    r_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            # 因为构造graph用的邻接表是假的，reverse相当于将链表倒置，所以用后进先出模拟链表倒置
            r_graph[v].insert(0, u)
    return r_graph


if __name__ == '__main__':
    # 链式前向星的图遍历
    a = build_graph(10, [[0,1],[1,2],[2,3],[2,4],[4,3],[4,5],[5,2],[4,6],[6,7],[7,1],[7,8],[8,9]], tp=4)
    head, arr = a
    for i in range(10):
        j = head[i]
        while j != -1:
            print("%d -> %d" % (i, arr[j].to))
            j = arr[j].next

