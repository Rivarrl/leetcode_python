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


if __name__ == '__main__':
    a = Solution(2, [])
    a.pick()