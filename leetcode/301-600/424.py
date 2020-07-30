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
        # window = max_count + k
        n = len(s)
        if k >= n: return n
        d = [0] * 26
        A = ord('A')
        left = res = max_count = 0
        for right in range(n):
            d[ord(s[right]) - A] += 1
            max_count = max(max_count, d[ord(s[right]) - A])
            if right - left + 1 > max_count + k:
                d[ord(s[left]) - A] -= 1
                left += 1
            res = max(res, max_count + k)
        return min(n, res)


if __name__ == '__main__':
    a = Solution()
    a.characterReplacement(s = "ABAB", k = 2)
    a.characterReplacement(s = "AABABBA", k = 1)
    a.characterReplacement(s = "AAAA", k = 2)