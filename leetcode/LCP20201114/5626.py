# -*- coding: utf-8 -*-
# ======================================
# @File    : 5626.py
# @Time    : 2020/12/13 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5626. 十-二进制数的最少数目]()
    """
    @timeit
    def minPartitions(self, n: str) -> int:
        return max([int(e) for e in n])

if __name__ == '__main__':
    a = Solution()
    a.minPartitions(n = "32")
    a.minPartitions(n = "82734")
    a.minPartitions(n = "27346209830709182346")