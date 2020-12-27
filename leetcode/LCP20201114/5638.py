# -*- coding: utf-8 -*-
# ======================================
# @File    : 5638.py
# @Time    : 2020/12/27 12:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5638. 吃苹果的最大数目]()
    """
    @timeit
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        from collections import defaultdict
        n = len(apples)
        d = defaultdict(int)
        for i in range(n):
            j = i + days[i]
            if j != i:


if __name__ == '__main__':
    a = Solution()
    a.eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2])
    a.eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])