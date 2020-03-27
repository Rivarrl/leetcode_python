# -*- coding: utf-8 -*-
# ======================================
# @File    : 820.py
# @Time    : 2020/3/28 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [820. 单词的压缩编码](https://leetcode-cn.com/problems/short-encoding-of-words/submissions/)
    """
    @timeit
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 排除后缀
        s = set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in s:
                    s.remove(word[i:])
        return len(s) + sum(len(e) for e in s)

    @timeit
    def minimumLengthEncoding2(self, words: List[str]) -> int:
        # 字典树原理
        trie = {}
        res = 0
        for word in words:
            d = trie
            for c in word[::-1]:
                if '#' in d:
                    res -= d['#']
                    d.pop('#')
                if not c in d:
                    d[c] = {}
                d = d[c]
            if not d:
                d['#'] = len(word) + 1
                res += d['#']
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumLengthEncoding(words = ["time", "me", "bell"])
    a.minimumLengthEncoding2(words = ["time", "me", "bell"])