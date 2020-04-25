# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/4/25 15:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))

if __name__ == '__main__':
    a = Solution()
    a.expectNumber([1,2,3])
    a.expectNumber([1,1])
    a.expectNumber([1,1,2])