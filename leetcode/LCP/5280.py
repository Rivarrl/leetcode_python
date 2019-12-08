# -*- coding: utf-8 -*-
# ======================================
# @File    : 5280.py
# @Time    : 2019/12/8 10:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    5280. 用户分组
    """
    @timeit
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        arr = [(groupSizes[i], i) for i in range(n)]
        arr.sort()
        res = [[]]
        for j in range(n):
            gi, i = arr[j]
            res[-1].append(i)
            if j == n - 1: break
            if len(res[-1]) == gi: res.append([])
        return res


if __name__ == '__main__':
    a = Solution()
    a.groupThePeople([3,3,3,3,3,1,3])
    a.groupThePeople([2,1,3,3,3,2])