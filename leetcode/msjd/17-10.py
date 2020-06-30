# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-10.py
# @Time    : 2020/6/30 21:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.10. 主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci)
    """
    @timeit
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        if not nums: return -1
        base = nums[0]
        ctr = 1
        for x in nums[1:]:
            if ctr == 0:
                base = x
            if x == base:
                ctr += 1
            else:
                ctr -= 1
        return base if nums.count(base) > len(nums) // 2 else -1

if __name__ == '__main__':
    a = Solution()
    a.majorityElement([1,2,5,9,5,9,5,5,5])
    a.majorityElement([3,2])
    a.majorityElement([2,2,1,1,1,2,2])
    a.majorityElement([6,5,5])