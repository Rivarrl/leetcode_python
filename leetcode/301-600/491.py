# -*- coding: utf-8 -*-
# ======================================
# @File    : 491.py
# @Time    : 2020/8/25 0:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [491. 递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)
    """
    @timeit
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(1 << n):
            cur = -100
            cnt, p = 0, 1
            for j in range(n):
                if i & (1 << j) == 0: continue
                if nums[j] >= cur:
                    cur = nums[j]
                else:
                    p = 0
                    break
                cnt += 1
            if cnt > 1 and p:
                res.add(tuple(nums[j] for j in range(n) if i & (1 << j)))
        return list([list(e) for e in res])

if __name__ == '__main__':
    a = Solution()
    a.findSubsequences([4,6,7,7])