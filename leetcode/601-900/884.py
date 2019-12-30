# -*- coding: utf-8 -*-
# ======================================
# @File    : 884.py
# @Time    : 2019/12/30 23:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [884. 两句话中的不常见单词](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/)
    """
    @timeit
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = {}
        for e in A.split(' ') + B.split(' '):
            d[e] = d.get(e, 0) + 1
        return [e for e in d if d[e] == 1]


if __name__ == '__main__':
    a = Solution()
    a.uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour")
    a.uncommonFromSentences(A = "apple apple", B = "banana")