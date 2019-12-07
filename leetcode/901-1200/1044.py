# -*- coding: utf-8 -*-
# ======================================
# @File    : 1044.py
# @Time    : 2019/12/2 9:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1044. 最长重复子串](https://leetcode-cn.com/problems/longest-duplicate-substring/)
    """
    @timeit
    def longestDupSubstring(self, S: str) -> str:
        """
        二分查找 + Rabin-Karp
        """
        def search(x):
            # rabin-karp算法，找到重复的返回第一次重复的起始下标>0, 否则返回0
            if x == 0: return 0
            h = 0
            for i in range(x):
                h = (h * a + ns[i]) % mod
            # 26^x
            seen = {h}
            digit = pow(a, x-1, mod)
            for i in range(1, n-x+1):
                h = ((h - ns[i-1] * digit) * a + ns[i+x-1]) % mod
                if h in seen:
                    return i
                seen.add(h)
            return 0
        n = len(S)
        lo, hi = 0, n
        ns = [ord(c) - ord('a') for c in S]
        a = 26
        mod = 2 ** 32
        res = ""
        while lo < hi:
            mid = (lo + hi) >> 1
            r = search(mid)
            if r:
                res = S[r:r+mid]
                lo = mid + 1
            else:
                hi = mid
        return res


if __name__ == '__main__':
    a = Solution()
    a.longestDupSubstring("banana")
    a.longestDupSubstring("abcd")
