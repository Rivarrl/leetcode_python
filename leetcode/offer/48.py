# -*- coding: utf-8 -*-
# ======================================
# @File    : 48.py
# @Time    : 2020/5/2 13:37
# @Author  : Rivarrl
# ======================================
# [面试题48. 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = j = 0
        for i, x in enumerate(s):
            if x in d:
                j = max(j, d[x])
            res = max(res, i - j + 1)
            d[x] = i + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.lengthOfLongestSubstring("abcabcbb")
    a.lengthOfLongestSubstring("bbbbb")
    a.lengthOfLongestSubstring("pwwkew")