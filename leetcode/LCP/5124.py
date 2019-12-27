# -*- coding: utf-8 -*-
# ======================================
# @File    : 5124.py
# @Time    : 2019/12/15 10:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5124. 顺次数](https://leetcode-cn.com/problems/sequential-digits/)
    """
    @timeit
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sl = str(low)
        sh = str(high)
        ld = len(sl)
        hd = len(sh)
        l0 = int(sl[0])
        if 10 - l0 < ld: ld += 1
        res = []
        for d in range(ld, hd+1):
            for i in range(10-d):
                t = int(''.join([str(j+1+i) for j in range(d)]))
                if t < low: continue
                elif t > high: break
                else:
                    res.append(t)
        return res


if __name__ == '__main__':
    a = Solution()
    a.sequentialDigits(100, 300)
    a.sequentialDigits(1000, 13000)
