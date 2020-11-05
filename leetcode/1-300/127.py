# -*- coding: utf-8 -*-
# ======================================
# @File    : 127.py
# @Time    : 2020/11/5 9:48 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        def visit(stk, vis, vis_other):
            word, step = stk.pop()
            for i in range(l):
                c = word[:i] + '*' + word[i + 1:]
                for e in d[c]:
                    if e in vis_other:
                        return step + vis_other[e]
                    if not e in vis:
                        vis[e] = step + 1
                        stk.insert(0, (e, step+1))

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        d = defaultdict(list)
        l = len(beginWord)
        for w in wordList:
            for i in range(l):
                d[w[:i] + '*' + w[i+1:]].append(w)
        stk_start = [(beginWord, 1)]
        stk_end = [(endWord, 1)]
        vis_start = {beginWord: 1}
        vis_end = {endWord: 1}
        while stk_start and stk_end:
            res = visit(stk_start, vis_start, vis_end)
            if res: return res
            res = visit(stk_end, vis_end, vis_start)
            if res: return res
        return 0