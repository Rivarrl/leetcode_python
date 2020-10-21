# -*- coding: utf-8 -*-
# ======================================
# @File    : 5545.py
# @Time    : 2020/10/18 11:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        from collections import defaultdict
        import bisect
        d = defaultdict(list)
        n = len(scores)
        for i in range(n):
            d[ages[i]].append(scores[i])
        for k, v in d.items(): v.sort()
        arr = sorted(d.keys())
        def f(j):
            if j == 0: return {d[arr[j]][i]: sum(d[arr[j]][:i+1]) for i in range(len(d[arr[j]]))}
            else:
                kd = f(j-1)
                a = sorted(kd.keys())
                res = {}
                tmp = {}
                cur = 0
                print(a)
                for i in range(len(d[arr[j]])-1, -1, -1):
                    t = d[arr[j]][i]
                    k = bisect.bisect_right(a, t) - 1
                    tmp[t] = k
                    cur += t
                    res[t] = max(cur + kd[a[tmp[]]], t + kd[a[k]])
                return res
        print(f())

if __name__ == '__main__':
    a = Solution()
    # a.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5])
    # a.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1])
    # a.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1])
    # a.bestTeamScore([1,1,1,1,1,1,1,1,1,1], [811,364,124,873,790,656,581,446,885,134])
    # a.bestTeamScore([9,2,8,8,2], [4,1,3,3,5])
    a.bestTeamScore([1,3,7,3,2,4,10,7,5], [4,5,2,1,1,2,4,1,4])