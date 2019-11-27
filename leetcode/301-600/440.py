# -*- coding: utf-8 -*-
# ======================================
# @File    : 440.py
# @Time    : 2019/11/28 0:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys
sys.setrecursionlimit(10000)
class Solution:
    """
    [440. 字典序的第K小数字](https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/)
    """
    @timeit
    def findKthNumber(self, n: int, k: int) -> int:
        """
        思路：递归
        """
        stk = [1]
        while k > 0:
            k -= 1
            if stk[-1] * 10 <= n:
                stk += [stk[-1] * 10]
            else:
                x = stk.pop()
                if k < 10:
                    return x + k
                else:
                    k -= 10
        return stk[-1]

if __name__ == '__main__':
    a = Solution()
    a.findKthNumber(13, 2)
    a.findKthNumber(25, 12)
    a.findKthNumber(25000, 1521)