# -*- coding: utf-8 -*-
# ======================================
# @File    : 61.py
# @Time    : 2020/3/11 23:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
# [面试题61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

class Solution:
    @timeit
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < 5 and nums[i] == 0:
            i += 1
        cnt = i
        for j in range(i, 4):
            x = nums[j+1] - nums[j] - 1
            if x < 0: return False
            cnt -= x
        return cnt >= 0


if __name__ == '__main__':
    a = Solution()
    a.isStraight([1,2,3,4,5])
    a.isStraight([0,0,1,2,5])
    a.isStraight([0,0,2,2,5])