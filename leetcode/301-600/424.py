# -*- coding: utf-8 -*-
# ======================================
# @File    : 424.py
# @Time    : 2020/7/29 3:21 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [424. 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement/)
    """
    @timeit
    def characterReplacement(self, s: str, k: int) -> int:
        # 滑窗
        n = len(s)
        if k >= n: return n
        res = cur = k
        left, right = 0, k - 1
        d = {}
        for i in range(k):
            d[s[i]] = d.get(s[i], 0) + 1
        while right < n:

            right += 1


if __name__ == '__main__':
    a = Solution()
    a.characterReplacement(s = "ABAB", k = 2)
    a.characterReplacement(s = "AABABBA", k = 1)