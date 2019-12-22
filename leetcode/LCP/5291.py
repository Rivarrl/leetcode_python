# -*- coding: utf-8 -*-
# ======================================
# @File    : 5291.py
# @Time    : 2019/12/22 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5291. 统计位数为偶数的数字](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/)
    """
    @timeit
    def findNumbers(self, nums: List[int]) -> int:
        return len([e for e in nums if len(str(e)) % 2 == 0])

if __name__ == '__main__':
    a = Solution()
    a.findNumbers(nums = [12,345,2,6,7896])
    a.findNumbers([555,901,482,1771])