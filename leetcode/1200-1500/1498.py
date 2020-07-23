# -*- coding: utf-8 -*-
# ======================================
# @File    : 1498.py
# @Time    : 2020/7/21 12:54 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1498. 满足条件的子序列数目](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)
    """
    @timeit
    def numSubseq(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        nums = [0] + sorted(d.keys())
        n = len(nums)
        dx = {0:0}
        tot = 0
        for x in nums:
            tot += d[x]
            dx[x] = tot
        res = 0
        mod = 10 ** 9 + 7
        lo, hi = 1, n - 1
        while lo <= hi:
            if nums[lo] + nums[hi] <= target:
                x = dx[nums[hi]] - dx[nums[lo - 1]] - 1
                for i in range(d[nums[lo]]):
                    res = (res + (1 << x - i)) % mod
                lo += 1
            else:
                hi -= 1
        return res

if __name__ == '__main__':
    a = Solution()
    # 4
    a.numSubseq(nums = [3,5,6,7], target = 9)
    # 6
    a.numSubseq(nums = [3,3,6,8], target = 10)
    # 61
    a.numSubseq(nums = [2,3,3,4,6,7], target = 12)
    # 127
    a.numSubseq(nums = [5,2,4,1,7,6,8], target = 16)
    # 15
    a.numSubseq([1,1,1,2],5)