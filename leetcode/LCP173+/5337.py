# -*- coding: utf-8 -*-
# ======================================
# @File    : 5337.py
# @Time    : 2020/3/7 22:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def findTheLongestSubstring(self, s: str) -> int:
        pre = [0]
        au = 'aeiou'
        for c in s:
            t = 0 if not c in au else 1 << (au.index(c) + 1)
            pre += [pre[-1] ^ t]
        d = {}
        dr = {}
        for i in range(len(pre)):
            dr[pre[i]] = i
            d[pre[i]] = i if not pre[i] in d else d[pre[i]]
        res = 0
        for k in d:
            res = max(res, dr[k] - d[k])
        return res


if __name__ == '__main__':
    a = Solution()
    a.findTheLongestSubstring("eleetminicoworoep")
    a.findTheLongestSubstring("leetcodeisgreat")
    a.findTheLongestSubstring("bcbcbc")
