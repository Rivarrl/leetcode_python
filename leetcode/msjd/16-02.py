# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-02.py
# @Time    : 2020/11/5 6:16 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class WordsFrequency:
    """
    [面试题 16.02. 单词频率](https://leetcode-cn.com/problems/words-frequency-lcci/)
    """
    def __init__(self, book: List[str]):
        self.d = {}
        for t in book:
            self.d[t] = self.d.get(t, 0) + 1

    def get(self, word: str) -> int:
        return self.d.get(word, 0)

if __name__ == '__main__':
    a = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    a.get("you")
    a.get("have")
    a.get("an")
    a.get("apple")
    a.get("pen")