# -*- coding: utf-8 -*-
# ======================================
# @File    : 5546.py
# @Time    : 2020/10/25 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        last = 0
        for i, k in enumerate(keysPressed):
            d[k] = max(d[k], releaseTimes[i] - last)
            last = releaseTimes[i]
        m = max(d.values())
        for i in range(25, -1, -1):
            k = chr(ord('a') + i)
            if k in d and d[k] == m:
                return k
        return ''

if __name__ == '__main__':
    a = Solution()
    a.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")
    a.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda")
