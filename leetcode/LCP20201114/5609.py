# -*- coding: utf-8 -*-
# ======================================
# @File    : 5609.py
# @Time    : 2020/12/12 22:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [5609. 统计一致字符串的数目]()
    """
    @timeit
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            x = set(word)
            if x.intersection(allowed) == x:
                res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
    a.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
    a.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])