# -*- coding: utf-8 -*-
# ======================================
# @File    : 5134.py
# @Time    : 2019/12/28 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5134. 将每个元素替换为右侧最大元素](https://leetcode-cn.com/contest/biweekly-contest-16/problems/replace-elements-with-greatest-element-on-right-side/)
    """
    @timeit
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        m = arr[-1]
        for i in range(n-2, -1, -1):
            res[i] = m
            if arr[i] > m: m = arr[i]
        return res



if __name__ == '__main__':
    a = Solution()
    a.replaceElements([17,18,5,4,6,1])