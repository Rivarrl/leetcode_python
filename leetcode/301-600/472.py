# -*- coding: utf-8 -*-
# ======================================
# @File    : 472.py
# @Time    : 2020/12/1 1:04 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [472. 连接词](https://leetcode-cn.com/problems/concatenated-words/)
    """
    @timeit
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # trie
        trie = {}
        res = []
        for word in words:
            d = trie
            for i, x in enumerate(word):
                d[x] = d.get(x, [{}, 0])
                if i == len(word) - 1:
                    d[x][1] = 1
                d = d[x][0]
        def f(word, depth=0):
            d = trie
            for i, x in enumerate(word):
                if x not in d: break
                if d[x][1] == 1:
                    if i == len(word) - 1:
                        return depth > 0
                    if f(word[i+1:], depth+1):
                        return True
                d = d[x][0]
            return False
        for word in words:
            if f(word):
                res.append(word)
        return res


    @timeit
    def findAllConcatenatedWordsInADict2(self, words: List[str]) -> List[str]:
        # hash存短串
        words.sort(key=len)
        m = max(1, len(words[0]))
        prev = set()
        res = []
        def f(word):
            if word in prev: return True
            for i in range(m, len(word) - m + 1):
                if word[:i] in prev and f(word[i:]):
                    return True
            return False
        for word in words:
            if f(word):
                res.append(word)
            prev.add(word)
        return res

if __name__ == '__main__':
    a = Solution()
    a.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])