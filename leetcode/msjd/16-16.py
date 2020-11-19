# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-16.py
# @Time    : 2020/11/19 9:36 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.16. 部分排序](https://leetcode-cn.com/problems/sub-sort-lcci/)
    """
    @timeit
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        l = r = -1
        inf = 0x3f3f3f3f
        t = -inf
        for i in range(n):
            if array[i] >= t:
                t = array[i]
            else:
                r = i
        for j in range(n-1, -1, -1):
            if array[j] <= t:
                t = array[j]
            else:
                l = j
        return [l, r]


if __name__ == '__main__':
    a = Solution()
    a.subSort([1,2,4,7,10,11,7,12,6,7,16,18,19])
    a.subSort([1,2,3,3,3,4,5,6])