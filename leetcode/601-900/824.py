# -*- coding: utf-8 -*-
# ======================================
# @File    : 824.py
# @Time    : 2019/12/23 20:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [824. 山羊拉丁文](https://leetcode-cn.com/problems/goat-latin/submissions/)
    """
    @timeit
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, word in enumerate(S.split(' ')):
            x = word[1:] + word[0] if word[0].lower() not in {'a', 'e', 'i', 'o', 'u'} else word
            res.append(x + 'ma' + 'a' * (i+1))
        return ' '.join(res)


if __name__ == '__main__':
    a = Solution()
    a.toGoatLatin("I speak Goat Latin")