# -*- coding: utf-8 -*-
# ======================================
# @File    : 11.py
# @Time    : 2020/4/21 14:26
# @Author  : Rivarrl
# ======================================
# [面试题11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        lo, hi = 0, n-1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if numbers[mi] == numbers[hi]:
                hi -= 1
            elif numbers[mi] < numbers[hi]:
                hi = mi
            else:
                lo = mi + 1
        return numbers[lo]


if __name__ == '__main__':
    a = Solution()
    a.minArray([3,4,5,1,2])
    a.minArray([2,2,2,0,1])
    a.minArray([1,3,3])