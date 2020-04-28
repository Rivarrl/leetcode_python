# -*- coding: utf-8 -*-
# ======================================
# @File    : 39.py
# @Time    : 2020/4/28 22:49
# @Author  : Rivarrl
# ======================================
# [面试题39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def majorityElement(self, nums: List[int]) -> int:
        base = nums[0]
        ctr = 0
        for e in nums:
            if e == base:
                ctr += 1
            else:
                ctr -= 1
                if ctr < 0:
                    base = e
                    ctr = 1
        return base


if __name__ == '__main__':
    a = Solution()
    a.majorityElement([1,2,3,2,2,2,5,4,2])