# -*- coding: utf-8 -*-
# ======================================
# @File    : 710.py
# @Time    : 2020/12/29 10:13 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

import random
class Solution:
    """
    [710. 黑名单中的随机数](https://leetcode-cn.com/problems/random-pick-with-blacklist/)
    """
    def __init__(self, N: int, blacklist: List[int]):
        # 黑名单的编号小于白名单数的部分b 与白名单编号大于白名单数 w，做一一映射
        self.d = {}
        n = len(blacklist)
        sb = set(blacklist)
        k = N - n
        arr = [i for i in range(k, N) if i not in sb]
        i = 0
        for x in blacklist:
            if x < k:
                self.d[x] = arr[i]
                i += 1
        self.k = k

    def pick(self) -> int:
        x = random.randint(0, self.k - 1)
        return self.d.get(x, x)

class Solution2:
    """
    [710. 黑名单中的随机数](https://leetcode-cn.com/problems/random-pick-with-blacklist/)
    """
    def __init__(self, N: int, blacklist: List[int]):
        # 二分查找，通过在白名单数中随机值x，根据黑名单反推出白名单的第x个值具体是什么
        n = len(blacklist)
        self.k = N - n
        self.b = blacklist

    def pick(self) -> int:
        x = random.randint(0, self.k - 1)
        b = self.b
        if not b or b[0] > x: return x
        # 查找出比白名单中第x个值小的黑名单值的个数
        lo, hi = 0, len(b) - 1
        while lo < hi:
            mi = lo + hi + 1 >> 1
            if b[mi] - mi <= x:
                lo = mi
            else:
                hi = mi - 1
        return lo + x + 1

if __name__ == '__main__':
    a = Solution(2, [])
    a.pick()