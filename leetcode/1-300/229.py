# -*- coding: utf-8 -*-
# ======================================
# @File    : 229.py
# @Time    : 2019/11/11 10:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        [229. 求众数 II](https://leetcode-cn.com/problems/majority-element-ii/)
        思路：摩尔投票法变种，区别是本题定义众数是个数大于len(nums)//3的数，至多可以有两个众数，用两个变量来存储这两个众数并计数
        """
        a1, a2 = None, None
        c1, c2 = 0, 0
        gap = len(nums) // 3
        for e in nums:
            if c1 == 0 and e != a2: a1, c1 = e, 1
            elif c2 == 0 and e != a1: a2, c2 = e, 1
            elif e == a1: c1 += 1
            elif e == a2: c2 += 1
            else:
                if a1: c1 -= 1
                if a2: c2 -= 1
        res = []
        if c1 > 0 and nums.count(a1) > gap:
            res.append(a1)
        if c2 > 0 and nums.count(a2) > gap:
            res.append(a2)
        return res


if __name__ == '__main__':
    a = Solution()
    a.majorityElement([3,2,3])
    a.majorityElement([-1,1,1,1,2,1])
    a.majorityElement([1,2,2,3,2,1,1,3])

