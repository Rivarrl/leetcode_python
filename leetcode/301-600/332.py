# -*- coding: utf-8 -*-
# ======================================
# @File    : 332.py
# @Time    : 2019/12/17 0:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [332. 重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/)
    JFK开始的一条最长路径
    """
    @timeit
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        n = len(tickets)
        tickets.sort()
        graph = defaultdict(list)
        vis = defaultdict(int)
        for fr, to in tickets:
            graph[fr].append(to)
            vis[(fr, to)] += 1
        def dfs(fr, n):
            if n == 0: return [fr]
            for to in graph[fr]:
                if vis[(fr, to)] > 0:
                    vis[(fr, to)] -= 1
                    suf = dfs(to, n - 1)
                    if suf: return [fr] + suf
                    vis[(fr, to)] += 1
        return dfs("JFK", n)


    @timeit
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        """
        Hierholzer算法求欧拉迹
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        res = []
        def dfs(fr):
            while graph[fr]:
                dfs(graph[fr].pop())
            res.append(fr)
        dfs("JFK")
        return res[::-1]


if __name__ == '__main__':
    a = Solution()
    a.findItinerary2([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    a.findItinerary2([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    a.findItinerary2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    a.findItinerary2([["EZE","AXA"],["TIA","ANU"],
                     ["ANU","JFK"],["JFK","ANU"],
                     ["ANU","EZE"],["TIA","ANU"],
                     ["AXA","TIA"],["TIA","JFK"],
                     ["ANU","TIA"],["JFK","TIA"]])