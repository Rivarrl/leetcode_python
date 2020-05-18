# -*- coding: utf-8 -*-
# ======================================
# @File    : 483.py
# @Time    : 2020/5/17 1:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [483. 最小好进制](https://leetcode-cn.com/problems/smallest-good-base/)
    """
    @timeit
    def smallestGoodBase(self, n: str) -> str:
        # 借鉴zero大佬的题解(https://leetcode-cn.com/problems/smallest-good-base/solution/shu-xue-fang-fa-fen-xi-dai-ma-by-zerotrac/)
        s = int(n)
        res = s - 1
        for i in range(59, 1, -1):
            k = int(s ** (1.0/i))
            if k > 1:
                tot = m = 1
                for _ in range(i):
                    m *= k
                    tot += m
                if tot == s:
                    res = k
                    break
        return str(res)


if __name__ == '__main__':
    a = Solution()
    a.smallestGoodBase("13")
    a.smallestGoodBase("4681")
    a.smallestGoodBase("1000000000000000000")