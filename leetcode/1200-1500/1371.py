# -*- coding: utf-8 -*-
# ======================================
# @File    : 1371.py
# @Time    : 2020/5/20 0:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1371. 每个元音包含偶数次的最长子字符串](https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)
    """
    @timeit
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {0:-1}
        res = f = 0
        for i in range(n):
            if s[i] == 'a':
                f ^= 1
            elif s[i] == 'e':
                f ^= (1 << 1)
            elif s[i] == 'i':
                f ^= (1 << 2)
            elif s[i] == 'o':
                f ^= (1 << 3)
            elif s[i] == 'u':
                f ^= (1 << 4)
            if f in d:
                res = max(res, i - d[f])
            else:
                d[f] = i
        return res


if __name__ == '__main__':
    a = Solution()
    a.findTheLongestSubstring(s = "eleetminicoworoep")
    a.findTheLongestSubstring(s = "leetcodeisgreat")
    a.findTheLongestSubstring(s = "bcbcbc")