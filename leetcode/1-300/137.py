# -*- coding: utf-8 -*-
# ======================================
# @File    : 137.py
# @Time    : 2020/5/1 18:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)
    """
    @timeit
    def singleNumber(self, nums: List[int]) -> int:
        # 状态转移
        one = two = 0
        for x in nums:
            one = one ^ x & ~two
            two = two ^ x & ~one
        return one

    @timeit
    def singleNumber2(self, nums: List[int]) -> int:
        # 按位寻找
        res = 0
        for i in range(32):
            mask = 1 << i
            c = 0
            for x in nums:
                if mask & x:
                    c += 1
            if c % 3 == 1:
                res |= mask
        return res if res < (1 << 31) else res - (1<<32)

if __name__ == '__main__':
    a = Solution()
    a.singleNumber2([2,2,3,2])
    a.singleNumber2([0,1,0,1,0,1,99])
    a.singleNumber2([-2,-2,1,1,-3,1,-3,-3,-4,-2])