# -*- coding: utf-8 -*-
# ======================================
# @File    : 648.py
# @Time    : 2020/12/18 10:20 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, key):
        self.key = key
        self.end = 0
        self.children = dict()

class Solution:
    """
    [648. 单词替换](https://leetcode-cn.com/problems/replace-words/)
    """
    @timeit
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x:len(x))
        trie = Node("*")
        for word in dictionary:
            p = trie
            for c in word:
                if c not in p.children:
                    x = Node(c)
                    p.children[c] = x
                p = p.children[c]
                if p.end == 1: break
            p.end = 1
        arr = sentence.split(' ')
        res = []
        for word in arr:
            p = trie
            i, n = 0, len(word)
            while i < n:
                if word[i] not in p.children:
                    break
                else:
                    p = p.children[word[i]]
                i += 1
            if p.end:
                res.append(word[:i])
            else:
                res.append(word)
        return ' '.join(res)


if __name__ == '__main__':
    a = Solution()
    a.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
    a.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs")
    a.replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
    a.replaceWords(dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery")
    a.replaceWords(dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted")