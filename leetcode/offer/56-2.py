# -*- coding: utf-8 -*-
# ======================================
# @File    : 56-2.py
# @Time    : 2020/4/30 23:38
# @Author  : Rivarrl
# ======================================
# [面试题56 - II. 数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def singleNumber(self, nums: List[int]) -> int:
        # 状态机
        one = two = 0
        for x in nums:
            one = one ^ x & ~two
            two = two ^ x & ~one
        return one

if __name__ == '__main__':
    a = Solution()
    a.singleNumber(nums = [3,4,3,3])
    a.singleNumber(nums = [9,1,7,9,7,9,7])