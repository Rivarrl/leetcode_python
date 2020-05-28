# -*- coding: utf-8 -*-
# ======================================
# @File    : 1451.py
# @Time    : 2020/5/26 19:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1451. 重新排列句子中的单词]()
    """
    @timeit
    def arrangeWords(self, text: str) -> str:
        line = text.split(' ')
        line[0] = line[0][0].lower() + line[0][1:]
        d = {}
        for word in line:
            n = len(word)
            d[n] = d.get(n, []) + [word]
        res = []
        for k in sorted(d.keys()):
            for v in d[k]:
                res.append(v)
        res = ' '.join(res)
        return res[0].upper() + res[1:]


if __name__ == '__main__':
    a = Solution()
    a.arrangeWords(text = "Leetcode is cool")
    a.arrangeWords(text = "Keep calm and code on")
    a.arrangeWords(text = "To be or not to be")