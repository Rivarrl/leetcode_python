# -*- coding: utf-8 -*-
# ======================================
# @File    : 211.py
# @Time    : 2019/11/12 9:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class WordDictionary:
    """
    [211. 添加与搜索单词 - 数据结构设计](https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/)
    思路：字典树，用字典实现
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p = self.d
        for c in word:
            p.setdefault(c, {})
            p = p[c]
        p['FIN'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, 0, self.d)

    def _search(self, word, i, p):
        if i == len(word):
            return 'FIN' in p
        if word[i] in p:
            return self._search(word, i+1, p[word[i]])
        elif word[i] == '.':
            for e in p:
                if e == 'FIN': continue
                if self._search(word, i+1, p[e]):
                    return True
        return False

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("a")
    param_2 = obj.search("a.")
    print(param_2)
