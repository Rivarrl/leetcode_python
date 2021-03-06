# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-08.py
# @Time    : 2020/11/30 23:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.08. 有重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-ii-lcci/)
    """
    @timeit
    def permutation(self, S: str) -> List[str]:
        def f(i):
            if i == n - 1: return [S[i]]
            res = []
            for x in f(i+1):
                for j in range(len(x)+1):
                    res.append(x[:j] + S[i] + x[j:])
            return list(set(res))
        n = len(S)
        return f(0)

if __name__ == '__main__':
    a = Solution()
    a.permutation(S = "qqe")
    a.permutation(S = "ab")