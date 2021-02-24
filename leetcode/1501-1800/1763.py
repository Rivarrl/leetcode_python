# -*- coding: utf-8 -*-
# ======================================
# @File    : 1763
# @Time    : 2021/2/24 13:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1763. 最长的美好子字符串](https://leetcode-cn.com/problems/longest-nice-substring/)
    """
    @timeit
    def longestNiceSubstring(self, s: str) -> str:
        from collections import defaultdict
        n = len(s)
        def ok(s):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            x = ord('A')
            for i in range(26):
                y, z = chr(x+i), chr(x+i+32)
                if min(d[y], d[z]) == 0 and max(d[y], d[z]) > 0:
                    return False
            return True
        res = ''
        for i in range(n):
            for j in range(n-1, i, -1):
                cur_len = j - i + 1
                if cur_len <= len(res): break
                if ok(s[i:j+1]):
                    res = s[i:j+1]
                    break
        return res

if __name__ == '__main__':
    a = Solution()
    a.longestNiceSubstring(s = "YazaAay")
    a.longestNiceSubstring(s = "Bb")
    a.longestNiceSubstring(s = "c")
    a.longestNiceSubstring(s = "dDzeE")
    a.longestNiceSubstring("jcJ")
    a.longestNiceSubstring("cChH")