# -*- coding: utf-8 -*-
# ======================================
# @File    : 56-1.py
# @Time    : 2020/4/28 2:07
# @Author  : Rivarrl
# ======================================
# [面试题56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        for e in nums:
            ret ^= e
        low = ret & (-ret)
        res = [0, 0]
        for e in nums:
            if e & low == 0:
                res[0] ^= e
            else:
                res[1] ^= e
        return res

if __name__ == '__main__':
    a = Solution()
    a.singleNumbers([4,1,4,6])
    a.singleNumbers([1,2,10,4,1,4,3,3])