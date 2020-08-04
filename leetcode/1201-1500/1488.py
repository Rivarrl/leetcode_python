# -*- coding: utf-8 -*-
# ======================================
# @File    : 1488.py
# @Time    : 2020/6/28 2:12 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1488. 避免洪水泛滥](https://leetcode-cn.com/problems/avoid-flood-in-the-city/)
    """
    @timeit
    def avoidFlood(self, rains: List[int]) -> List[int]:
        import bisect
        d = {}
        stk = []
        res = [1] * len(rains)
        for i, x in enumerate(rains):
            if x == 0:
                stk.append(i)
            else:
                if x in d:
                    if not stk or stk[-1] < d[x]: return []
                    j = bisect.bisect_left(stk, d[x])
                    res[stk[j]] = x
                    stk.pop(j)
                d[x] = i
                res[i] = -1
        return res

if __name__ == '__main__':
    a = Solution()
    a.avoidFlood(rains = [1,2,3,4])
    a.avoidFlood(rains = [1,2,0,0,2,1])
    a.avoidFlood(rains = [1,2,0,1,2])
    a.avoidFlood(rains = [69,0,0,0,69])
    a.avoidFlood(rains = [10,20,20])
    a.avoidFlood([0,1,1])
    a.avoidFlood([1,0,2,3,0,1,2])