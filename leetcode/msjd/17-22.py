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
        from collections import defaultdict
        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                k = word[:i] + "*" + word[i+1:]
                g[k].append(word)


if __name__ == '__main__':
    a = Solution()
    a.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"])
    a.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log"])