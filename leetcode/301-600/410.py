# -*- coding: utf-8 -*-
# ======================================
# @File    : 410.py
# @Time    : 2019/11/27 23:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)
    """
    @timeit
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        思路：二分查找，最大值最小化
        """
        def judge(x):
            line = c = 0
            for i in nums:
                if c + i > x:
                    line += 1
                    c = 0
                if line == m: return False
                c += i
            return True
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) >> 1
            if judge(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi


if __name__ == '__main__':
    a = Solution()
    a.splitArray([7,2,5,10,8], 2)