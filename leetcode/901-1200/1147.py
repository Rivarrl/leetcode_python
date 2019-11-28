# -*- coding: utf-8 -*-
# ======================================
# @File    : 1147.py
# @Time    : 2019/11/28 23:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1147. 段式回文](https://leetcode-cn.com/problems/longest-chunked-palindrome-decomposition/)
    """
    @timeit
    def longestDecomposition(self, text: str) -> int:
        """
        思路：双指针向中间逼近，贪心算法
        """
        n = len(text)
        r = 0
        res = 0
        for i in range(n):
            mi = n - 1 - i
            if mi <= i:
                if r > 0 or mi == i: res += 1
                break
            if text[i-r:i+1] == text[mi:mi+r+1]:
                res += 2
                r = 0
            else:
                r += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")
    a.longestDecomposition("merchant")
    a.longestDecomposition("antaprezatepzapreanta")
    a.longestDecomposition("aaa")