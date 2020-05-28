# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-15.py
# @Time    : 2020/5/27 18:30
# @Author  : Rivarrl
# ======================================
# [面试题 17.15. 最长单词](https://leetcode-cn.com/problems/longest-word-lcci/)
from algorithm_utils import *

class Trie:
    def __init__(self, s):
        self.s = s
        self.is_tail = False
        self.children = dict()

class Solution:
    @timeit
    def longestWord(self, words: List[str]) -> str:
        root = Trie('')
        for word in words:
            p = root
            for c in word:
                if not c in p.children:
                    p.children[c] = Trie(c)
                p = p.children[c]
            p.is_tail = True
        words.sort(key=lambda x:(-len(x), x))
        def ok(word, d=0):
            if len(word) == 0: return d > 1
            p = root
            for i, c in enumerate(word):
                if not c in p.children: return False
                if p.children[c].is_tail and ok(word[i+1:], d+1): return True
                p = p.children[c]
            return False
        for word in words:
            if ok(word): return word
        return ""


if __name__ == '__main__':
    a = Solution()
    # a.longestWord(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"])
    # a.longestWord(["ttaaaa","pp","tpa","kpaqkt","tktpqq","aqppatp"])
    a.longestWord(["llllcccl","clclll","ccc","llccllccl","lcclccclcl","c"])