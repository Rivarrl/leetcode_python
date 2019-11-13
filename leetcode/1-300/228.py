# -*- coding: utf-8 -*-
# ======================================
# @File    : 228.py
# @Time    : 2019/11/13 10:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [228. 汇总区间](https://leetcode-cn.com/problems/summary-ranges/)
    """

    @timeit
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        思路：遍历
        """
        n = len(nums)
        res = []
        i = 0
        while i < n:
            flag = False
            res.append(str(nums[i]))
            j = i + 1
            if j < n and nums[j] - 1 == nums[i]:
                flag = True
                res[-1] += "->"
            while j < n and nums[j] - 1 == nums[j-1]:
                j += 1
            if flag:
                res[-1] += str(nums[j-1])
            i = j
        return res


if __name__ == '__main__':
    a = Solution()
    a.summaryRanges([0,2,3,4,6,8])

