# -*- coding: utf-8 -*-
# ======================================
# @File    : 1160.py
# @Time    : 2020/3/17 0:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1160. 拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/)
    """
    @timeit
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for c in chars:
            d[c] = d.get(c, 0) + 1
        res = 0
        for word in words:
            tmp = {}
            for c in word:
                tmp[c] = tmp.get(c, 0) + 1
                if tmp[c] > d.get(c, 0):
                    break
            else:
                res += len(word)
        return res

if __name__ == '__main__':
    a = Solution()
    a.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach")
    a.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")