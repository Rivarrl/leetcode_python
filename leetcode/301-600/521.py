# -*- coding: utf-8 -*-
# ======================================
# @File    : 521.py
# @Time    : 2020/5/9 18:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [521. 最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/)
    """
    @timeit
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1

if __name__ == '__main__':
    a = Solution()
    a.findLUSlength("aba", "cdc")
    a.findLUSlength(a = "aaa", b = "bbb")
    a.findLUSlength(a = "aaa", b = "aaa")