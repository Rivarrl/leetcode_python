# -*- coding: utf-8 -*-
# ======================================
# @File    : 765.py
# @Time    : 2021/2/14 12:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [765. 情侣牵手](https://leetcode-cn.com/problems/couples-holding-hands/)
    """
    @timeit
    def minSwapsCouples(self, row: List[int]) -> int:
        res = 0
        n = len(row)
        for i in range(0, n, 2):
            j = i + 1
            while row[i] ^ row[j] != 1:
                j += 1
            if j != i + 1:
                row[i+1], row[j] = row[j], row[i+1]
                res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.minSwapsCouples([0,2,1,3])
    a.minSwapsCouples([3,2,0,1])