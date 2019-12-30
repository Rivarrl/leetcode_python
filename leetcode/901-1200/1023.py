# -*- coding: utf-8 -*-
# ======================================
# @File    : 1023.py
# @Time    : 2019/12/29 17:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Tree:
    def __init__(self, c='', num=-1):
        self.c = c
        self.id = num
        self.children = {}


class Solution:
    """
    [1023. 驼峰式匹配](https://leetcode-cn.com/problems/camelcase-matching/)
    """
    @timeit
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 字典树
        trie = Tree()
        for i, query in enumerate(queries):
            d = trie
            for c in query:
                if not c in d.children:
                    d.children[c] = Tree(c)
                d = d.children[c]
            d.id = i
        res = [False] * len(queries)
        def dfs(d, i=0):
            if d.id != -1 and i == len(pattern):
                res[d.id] = True
            for k, v in d.children.items():
                if k.islower(): dfs(v, i)
            if i < len(pattern) and pattern[i] in d.children:
                dfs(d.children[pattern[i]], i+1)
        dfs(trie)
        return res


    @timeit
    def camelMatch2(self, queries: List[str], pattern: str) -> List[bool]:
        def helper(word):
            i = 0
            for c in word:
                if i == len(pattern):
                    if c.isupper(): return False
                elif c == pattern[i]:
                    i += 1
                elif c.isupper(): return False
            return i == len(pattern)
        return list(map(helper, queries))


if __name__ == '__main__':
    a = Solution()
    # a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
    # a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa")
    a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")
    # a.camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP")
    # a.camelMatch2(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
    # a.camelMatch2(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa")
    a.camelMatch2(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")
    # a.camelMatch2(["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP")
