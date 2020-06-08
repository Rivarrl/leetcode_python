# -*- coding: utf-8 -*-
# ======================================
# @File    : 126.py
# @Time    : 2020/6/7 12:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)
    """
    @timeit
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 搞一个字典，将abc分别存为*bc,a*c和ab*
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        d = defaultdict(list)
        l = len(beginWord)
        for w in wordList:
            for i in range(l):
                d[w[:i] + '*' + w[i+1:]].append(w)
        stk_start = {beginWord: [[beginWord]]}
        stk_end = {endWord: [[endWord]]}
        dis = 2
        vis = set()
        res = []
        while stk_start:
            if len(stk_end) < len(stk_start):
                stk_end, stk_start = stk_start, stk_end
            tmp = {}
            while stk_start:
                word, paths = stk_start.popitem()
                vis.add(word)
                for i in range(l):
                    c = word[:i] + '*' + word[i+1:]
                    for e in d[c]:
                        if e in stk_end:
                            if paths[0][0] == beginWord: # forward
                                res.extend(head + tail[::-1] for head in paths for tail in stk_end[e])
                            else: # backward
                                res.extend(head + tail[::-1] for tail in paths for head in stk_end[e])
                        if not e in vis:
                            tmp[e] = tmp.get(e, []) + [path + [e] for path in paths]
            dis += 1
            if res and dis > len(res[0]): break
            stk_start = tmp
        return res

if __name__ == '__main__':
    a = Solution()
    a.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    # a.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])