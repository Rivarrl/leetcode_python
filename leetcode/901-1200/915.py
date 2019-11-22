# -*- coding: utf-8 -*-
# ======================================
# @File    : 915.py
# @Time    : 2019/11/22 0:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [915. 分割数组](https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals/)
    """
    @timeit
    def partitionDisjoint(self, A: List[int]) -> int:
        """
        思路：找到第一个max(left)<=min(right)位置
        """
        n = len(A)
        cmp = [0] * n
        m = 10**6 + 1
        for i in range(n-1, -1, -1):
            cmp[i] = m = min(m, A[i])
        m = -1
        for i, x in enumerate(A):
            m = max(m, x)
            if m <= cmp[i+1]: return i+1


    @timeit
    def partitionDisjoint2(self, A: List[int]) -> int:
        """
        思路：优化，保存一个左边最大值，后面的遍历过程中比这个值还小的，一定要被划分到left中，相等不用。
        """
        lm = m = A[0]
        res = 0
        for i in range(1, len(A)):
            m = max(m, A[i])
            if A[i] < lm:
                lm = m
                res = i
        return res + 1



if __name__ == '__main__':
    a = Solution()
    a.partitionDisjoint2([1,1])
    a.partitionDisjoint2([5,0,3,8,6])
    a.partitionDisjoint2([1,1,1,0,6,12])