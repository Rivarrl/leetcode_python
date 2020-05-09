# -*- coding: utf-8 -*-
# ======================================
# @File    : 517.py
# @Time    : 2020/5/9 22:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [517. 超级洗衣机](https://leetcode-cn.com/problems/super-washing-machines/)
    """
    @timeit
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n != 0: return -1
        avg = total // n
        for i in range(n):
            machines[i] -= avg
        res = s = mx = 0
        for x in machines:
            s += x
            mx = max(mx, abs(s))
            res = max(res, mx, x)
        return res

if __name__ == '__main__':
    a = Solution()
    a.findMinMoves([1,0,5])
    a.findMinMoves([0,3,0])
    a.findMinMoves([0,2,0])
    a.findMinMoves([9,1,8,8,9])