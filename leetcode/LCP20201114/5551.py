# -*- coding: utf-8 -*-
# ======================================
# @File    : 5551.py
# @Time    : 2020/11/14 22:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5551. 使字符串平衡的最少删除次数]
    """
    @timeit
    def minimumDeletions(self, s: str) -> int:
        d = [[] for _ in range(2)]
        n = len(s)
        for i in range(n):
            j = 0 if s[i] == 'a' else 1
            d[j] += [i]
        d[1] = d[1][::-1]
        res = 0
        while d[0] and d[1] and d[0][-1] > d[1][-1]:
            if n - 1 - d[0][-1] > d[1][-1]:
                d[1].pop()
            else:
                d[0].pop()
            res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.minimumDeletions(s = "aababbab")
    a.minimumDeletions(s = "bbaaaaabb")
    a.minimumDeletions("baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb")