# -*- coding: utf-8 -*-
# ======================================
# @File    : 1207.py
# @Time    : 2020/10/28 0:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1207. 独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences/)
    """
    @timeit
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return len(d.values()) == len(set(d.values()))

if __name__ == '__main__':
    a = Solution()
    a.uniqueOccurrences(arr = [1,2,2,1,1,3])
    a.uniqueOccurrences(arr = [1,2])
    a.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])