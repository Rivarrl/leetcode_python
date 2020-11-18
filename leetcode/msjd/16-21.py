# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-21.py
# @Time    : 2020/11/18 1:18 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.21. 交换和](https://leetcode-cn.com/problems/sum-swap-lcci/)
    """
    @timeit
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        s = sum(array1) - sum(array2)
        if s & 1 == 0:
            c = s // 2
            for x in set(array1):
                if x - c in set(array2):
                    return [x, x-c]
        return []

if __name__ == '__main__':
    a = Solution()
    a.findSwapValues(array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3])
    a.findSwapValues(array1 = [1, 2, 3], array2 = [4, 5, 6])