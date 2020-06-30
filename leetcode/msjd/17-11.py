# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-11.py
# @Time    : 2020/6/30 21:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.11. 单词距离](https://leetcode-cn.com/problems/find-closest-lcci/)
    """
    @timeit
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = -1
        res = len(words) + 1
        for i, x in enumerate(words):
            if x == word1:
                i1 = i
            elif x == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1-i2))
        return res


if __name__ == '__main__':
    a = Solution()
    a.findClosest(words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student")