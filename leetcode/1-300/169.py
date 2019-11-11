# -*- coding: utf-8 -*-
# ======================================
# @File    : 169.py
# @Time    : 2019/11/11 11:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def majorityElement(self, nums: List[int]) -> int:
        """
        [169. 求众数](https://leetcode-cn.com/problems/majority-element/)
        思路：Boyer-Moore投票法
        把众数记为 +1 ，把其他数记为 -1 ，将它们全部加起来，显然和大于 0 ，从结果可以看出众数比其他数多。
        原理就是抵消前面的众数和非众数前缀数组，然后从后缀数组中继续找寻众数
        Q: 摩尔投票法为什么可行？
        A: 因为题目明确告诉我们nums中一定存在这个大于len(nums)//2的众数，这是投票法正确的前提
        """
        ctr = 0
        base = None
        for e in nums:
            if ctr == 0:
                base = e
            if e == base:
                ctr += 1
            else:
                ctr -= 1
        return base


if __name__ == '__main__':
    a = Solution()
    a.majorityElement([2,2,1,1,1,2,2])