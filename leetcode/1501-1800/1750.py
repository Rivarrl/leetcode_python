# -*- coding: utf-8 -*-
# ======================================
# @File    : 1750.py
# @Time    : 2021/2/17 19:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1750. 删除字符串两端相同字符后的最短长度](https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends/)
    """
    @timeit
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l < r and s[l] == s[r]:
            x = s[l]
            while l < r and s[l] == x:
                l += 1
            while l <= r and s[r] == x:
                r -= 1
        return r - l + 1

if __name__ == '__main__':
    a = Solution()
    a.minimumLength(s = "ca")
    a.minimumLength(s = "cabaabac")
    a.minimumLength(s = "aabccabba")
    a.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb")