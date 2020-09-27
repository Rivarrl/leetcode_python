# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-22.py
# @Time    : 2020/9/9 23:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.22. 单词转换](https://leetcode-cn.com/problems/word-transformer-lcci/)
    """
    @timeit
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        from collections import defaultdict, deque
        if not endWord in wordList: return []
        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                k = word[:i] + "*" + word[i+1:]
                g[k].append(word)
        beginq = deque()
        endq = deque()
        beginq.append([beginWord, 1])
        endq.append([endWord, 1])
        beginmemo = {beginWord:[beginWord]}
        endmemo = {endWord:[endWord]}
        qs = [beginq, endq]
        memos = [beginmemo, endmemo]
        q, cur, ops, sw = beginq, beginmemo, endmemo, 0
        while q:
            s = q[0][1]
            while q and s == q[0][1]:
                word, _ = q.popleft()
                for i in range(len(word)):
                    k = word[:i] + "*" + word[i+1:]
                    for nw in g[k]:
                        if nw in ops:
                            return ops[nw] + cur[word][::-1] if sw else cur[word] + ops[nw][::-1]
                        if nw in cur: continue
                        cur[nw] = cur[word] + [nw]
                        q.append([nw, s+1])
            sw ^= 1
            q, cur, ops = qs[sw], memos[sw], memos[sw ^ 1]
        return []


if __name__ == '__main__':
    a = Solution()
    a.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"])
    a.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log"])