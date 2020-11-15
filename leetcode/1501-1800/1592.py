# -*- coding: utf-8 -*-
# ======================================
# @File    : 1592.py
# @Time    : 2020/11/14 21:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1592. 重新排列单词间的空格](https://leetcode-cn.com/problems/rearrange-spaces-between-words/)
    """
    @timeit
    def reorderSpaces(self, text: str) -> str:
        word = [s.strip() for s in text.split(' ') if s]
        n = len(word)
        x = text.count(' ')
        if n == 1: return word[0] + ' ' * x
        return (' ' * (x // (n - 1))).join(word) + ' ' * (x % (n-1))

if __name__ == '__main__':
    a = Solution()
    a.reorderSpaces(text = "  this   is  a sentence ")
    a.reorderSpaces(text = " practice   makes   perfect")
    a.reorderSpaces(text = "hello   world")
    a.reorderSpaces(text = "  walks  udp package   into  bar a")
    a.reorderSpaces(text = "a")