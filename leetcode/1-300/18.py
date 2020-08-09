# -*- coding: utf-8 -*-
# ======================================
# @File    : 18.py
# @Time    : 2020/8/8 23:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [18. 四数之和](https://leetcode-cn.com/problems/4sum/)
    """
    @timeit
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def check(rs):
            xd = {}
            for r in rs:
                if not r in xd:
                    xd[r] = 0
                xd[r] += 1
                if xd[r] > c[r]:
                    return False
            return True
        d = {}
        c = {}
        m = []
        res = []
        l = len(nums)
        if l < 4: return res
        for i in range(l):
            if not nums[i] in c:
                c[nums[i]] = 0
            c[nums[i]] += 1
        if target == 0 and 0 in c and c[0] >= 4:
            res.append([0,0,0,0])
        for i in range(l):
            for j in range(i + 1, l):
                s = nums[i] + nums[j]
                sr = sorted([nums[i], nums[j]])
                if not s in d:
                    d[s] = [sr]
                    m.append(s)
                else:
                    if not sr in d[s]:
                        d[s].append(sr)
        lm = len(m)
        m.sort()
        i, j = 0, lm - 1
        while i <= j:
            if m[i] + m[j] == target:
                if i == j:
                    li = len(d[m[i]])
                    for ii in range(li):
                        for jj in range(ii, li):
                            [xi, yi], [xj, yj] = d[m[i]][ii], d[m[i]][jj]
                            rs = sorted([xi, yi, xj, yj])
                            if not rs in res and check(rs):
                                res.append(rs)
                else:
                    for xi, yi in d[m[i]]:
                        for xj, yj in d[m[j]]:
                            rs = sorted([xi, yi, xj, yj])
                            if not rs in res and check(rs):
                                res.append(rs)
                i += 1
                j -= 1
            elif m[i] + m[j] > target:
                j -= 1
            else:
                i += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.fourSum([1, 0, -1, 0, -2, 2], 0)