# -*- coding: utf-8 -*-
# ======================================
# @File    : 1131.py
# @Time    : 2019/12/18 0:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1131. 绝对值表达式的最大值](https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/)
    """
    @timeit
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        把绝对值号打开计算, arr1[i] - arr1[j] + arr2[i] - arr2[j] + i - j
        """
        A, B, C, D = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)


if __name__ == '__main__':
    a = Solution()
    a.maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6])
    a.maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4])