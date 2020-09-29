# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-18.py
# @Time    : 2020/9/28 12:53 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.18. 最短超串](https://leetcode-cn.com/problems/shortest-supersequence-lcci/)
    """
    @timeit
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for x in small:
            d[x] += 1
        n = len(big)
        l = r = tot = 0
        seen = defaultdict(int)
        def hit(seen):
            return sum(v-seen[k] for k, v in d.items())
        res = [0, 0]
        while r < n:
            print(l, r, big[l:r+1])
            seen[r] += 1
            c = hit(seen)
            if c <= tot:
                seen[l] -= 1
                l += 1
            else:
                tot = c
                res = [l, r]
            r += 1
        return res

if __name__ == '__main__':
    a = Solution()
    big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    small = [1, 5, 9]
    a.shortestSeq(big, small)