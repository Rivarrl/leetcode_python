# -*- coding: utf-8 -*-
# ======================================
# @File    : 1010.py
# @Time    : 2019/12/24 23:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1010. 总持续时间可被 60 整除的歌曲](https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
    """
    @timeit
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        res = 0
        for t in time:
            xt = t % 60
            res += d[(60 - xt) % 60]
            d[xt] += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.numPairsDivisibleBy60([30,20,150,100,40])
    a.numPairsDivisibleBy60([60,60,60])
    a.numPairsDivisibleBy60([15,63,451,213,37,209,343,319])