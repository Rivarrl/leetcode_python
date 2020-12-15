# -*- coding: utf-8 -*-
# ======================================
# @File    : 1653.py
# @Time    : 2020/11/14 22:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1653. 使字符串平衡的最少删除次数](https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced/)
    """
    @timeit
    def minimumDeletions(self, s: str) -> int:
        # 贪心，如果当前片段有连续n个b后面接连续m个a，删除数量较小的一边
        # 所以统计b的数量，遇到a之后n--
        res = ctr = 0
        for c in s:
            if c == 'b':
                ctr += 1
            else:
                if ctr > 0:
                    ctr -= 1
                    res += 1
        return res

    @timeit
    def minimumDeletions2(self, s: str) -> int:
        # 前缀和统计需要删多少b，后缀和统计需要删多少a
        n = len(s)
        a, b = [0], [0]
        for i in range(n):
            a.append(a[-1] + int(s[i] == 'b'))
            b.append(b[-1] + int(s[n-1-i] == 'a'))
        res = n
        for x, y in zip(a, reversed(b)):
            res = min(res, x+y)
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumDeletions2(s = "aababbab")
    a.minimumDeletions2(s = "bbaaaaabb")
    a.minimumDeletions2("baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb")