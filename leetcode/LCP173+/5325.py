# -*- coding: utf-8 -*-
# ======================================
# @File    : 5325.py
# @Time    : 2020/2/23 12:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5325. 包含所有三种字符的子字符串数目](https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters/)
    """
    @timeit
    def numberOfSubstrings(self, s: str) -> int:
        rec = [-1] * 3
        n = len(s)
        l = r = res = 0
        while r < n:
            rec[ord(s[r]) - ord('a')] = r
            if not -1 in rec:
                k = min(rec)
                rec[ord(s[k]) - ord('a')] = -1
                pre = k - l + 1
                suf = n - r
                res += pre * suf
                l = k + 1
            r += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.numberOfSubstrings("abcabc")
    a.numberOfSubstrings("aaacb")
    a.numberOfSubstrings("abc")
    a.numberOfSubstrings("bcabac")