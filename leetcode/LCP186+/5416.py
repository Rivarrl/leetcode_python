# -*- coding: utf-8 -*-
# ======================================
# @File    : 5416.py
# @Time    : 2020/5/24 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5416. 检查单词是否为句中其他单词的前缀]()
    """
    @timeit
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(' ')):
            if word.startswith(searchWord):
                return i + 1
        return -1

if __name__ == '__main__':
    a = Solution()
    a.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")
    a.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro")
    a.isPrefixOfWord(sentence = "i am tired", searchWord = "you")
    a.isPrefixOfWord(sentence = "i use triple pillow", searchWord = "pill")
    a.isPrefixOfWord(sentence = "hello from the other side", searchWord = "they")