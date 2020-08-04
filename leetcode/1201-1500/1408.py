# -*- coding: utf-8 -*-
# ======================================
# @File    : 1408.py
# @Time    : 2020/4/20 20:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1408. 数组中的字符串匹配](https://leetcode-cn.com/problems/string-matching-in-an-array/)
    """
    @timeit
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x), reverse=True)
        d = set()
        res = []
        for word in words:
            for pre in d:
                if word in pre:
                    res.append(word)
                    break
            d.add(word)
        return res

if __name__ == '__main__':
    a = Solution()
    a.stringMatching(words = ["mass","as","hero","superhero"])
    a.stringMatching(words = ["leetcode","et","code"])
    a.stringMatching(words = ["blue","green","bu"])