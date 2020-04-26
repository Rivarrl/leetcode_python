# -*- coding: utf-8 -*-
# ======================================
# @File    : 5392.py
# @Time    : 2020/4/26 15:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5392. 分割字符串的最大得分](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/)
    """
    @timeit
    def maxScore(self, s: str) -> int:
        n = len(s)
        left, right = [0], [0]
        for i in range(n):
            left += [left[-1]]
            if s[i] == '0': left[-1] += 1
            right = [right[0]] + right
            j = n - 1 - i
            if s[j] == '1': right[0] += 1
        res = 0
        for i in range(1, n):
            c = left[i] + right[i]
            if c > res:
                res = c
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxScore("011101")
    a.maxScore("00111")
    a.maxScore("1111")
    a.maxScore("00")