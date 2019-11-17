# -*- coding: utf-8 -*-
# ======================================
# @File    : 5109.py
# @Time    : 2019/11/16 22:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5109. 最小公共区域
    给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。
    很自然地，如果区域 X 包含区域 Y ，那么区域 X  比区域 Y 大。
    给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。
    如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。
    数据同样保证最小公共区域一定存在。
    输入：
    regions = [["Earth","North America","South America"],
    ["North America","United States","Canada"],
    ["United States","New York","Boston"],
    ["Canada","Ontario","Quebec"],
    ["South America","Brazil"]],
    region1 = "Quebec",
    region2 = "New York"
    输出："North America"
    提示：
    2 <= regions.length <= 10^4
    region1 != region2
    所有字符串只包含英文字母和空格，且最多只有 20 个字母。
    """
    @timeit
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        d = {}
        for r in regions:
            if r[0] not in d:
                d[r[0]] = Tree(r[0])
            for c in r[1:]:
                if not c in d:
                    d[c] = Tree(c)
                    d[c].fa = d[r[0]]
                d[r[0]].children.append(d[c])
        root = d[regions[0][0]]
        while root.fa != None:
            root = root.fa
        def dfs(p, lv):
            p.lv = lv
            if not p.children: return
            for c in p.children:
                dfs(c, lv+1)
        dfs(root, 1)
        t1, t2 = d[region1], d[region2]
        if t1.lv > t2.lv:
            t1, t2 = t2, t1
        while t2.lv > t1.lv:
            t2 = t2.fa
        while t2.val != t1.val:
            t1, t2 = t1.fa, t2.fa
        return t1.val

class Tree:
    def __init__(self, val):
        self.val = val
        self.fa = None
        self.lv = 0
        self.children = []

if __name__ == '__main__':
    a = Solution()
    # a.findSmallestRegion(regions = [["Earth","North America","South America"],
    #                     ["North America","United States","Canada"],
    #                     ["United States","New York","Boston"],
    #                     ["Canada","Ontario","Quebec"],
    #                     ["South America","Brazil"]],
    #                     region1 = "Quebec",
    #                     region2 = "New York")
    # a.findSmallestRegion([["Earth", "North America","South America"],
    #                       ["North America","United States","Canada"],
    #                       ["United States","New York","Boston"],
    #                       ["Canada","Ontario","Quebec"],
    #                       ["South America","Brazil"]],
    #                      "Canada","South America")
    a.findSmallestRegion([["Earth","North America","South America"],
                          ["North America","United States","Canada"],
                          ["United States","New York","Boston"],
                          ["Canada","Ontario","Quebec"],
                          ["South America","Brazil"]],
                        "Canada",
                        "Quebec")