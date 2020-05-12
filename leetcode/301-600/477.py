# -*- coding: utf-8 -*-
# ======================================
# @File    : 477.py
# @Time    : 2020/5/12 22:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [477. 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance/)
    """
    @timeit
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ma = max(nums)
        m = 0
        while ma:
            m += 1
            ma >>= 1
        res = 0
        for i in range(m):
            cnt = 0
            for j in nums:
                cnt += (j >> i) & 1
            res += (n - cnt) * cnt
        return res

if __name__ == '__main__':
    a = Solution()
    a.totalHammingDistance([4,14,2])