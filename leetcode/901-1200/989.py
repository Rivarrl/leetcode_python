# -*- coding: utf-8 -*-
# ======================================
# @File    : 989.py
# @Time    : 2019/12/13 23:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution(object):
    """
    [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
    """
    @timeit
    def addToArrayForm(self, A, K):
        plus = 0
        n = len(A)
        digit = 0
        while K // (10 ** digit) > 0:
            digit += 1
        if n < digit:
            A = [0] * (digit - n) + A
            n = digit
        for j in range(n):
            i = n - 1 - j
            if j < digit:
                k = (K // (10 ** j)) % 10
                A[i] = A[i] + plus + k
            elif plus == 1:
                A[i] += plus
            else: break
            if A[i] >= 10:
                A[i] -= 10
                plus = 1
            else:
                plus = 0
        if plus == 1: A.insert(0, 1)
        return A


    @timeit
    def addToArrayForm2(self, A, K):
        """
        官方的优秀题解：由于K最大是10000，可以模拟进位，先把K加到A的个位上，把个位加上，剩下的加到十位，。。。
        """
        A[-1] += K
        for i in range(len(A)-1, -1, -1):
            K = A[i] // 10
            A[i] %= 10
            if i: A[i-1] += K
        if K: A = [int(e) for e in str(K)] + A
        return A


if __name__ == '__main__':
    a = Solution()
    a.addToArrayForm2(A = [1,2,0,0], K = 34)
    a.addToArrayForm2(A = [0], K = 34)
    a.addToArrayForm2([9,9,9,9,9,9,9,9], 1)
