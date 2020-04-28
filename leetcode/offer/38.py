# -*- coding: utf-8 -*-
# ======================================
# @File    : 38.py
# @Time    : 2020/4/28 22:45
# @Author  : Rivarrl
# ======================================
# [面试题38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def permutation(self, s: str) -> List[str]:
        def dfs(i):
            if i == n: return ['']
            res = set()
            for x in dfs(i+1):
                for j in range(len(x)+1):
                    res.add(x[:j] + s[i] + x[j:])
            return list(res)
        n = len(s)
        return dfs(0)


if __name__ == '__main__':
    a = Solution()
    a.permutation("abc")
    a.permutation("aac")