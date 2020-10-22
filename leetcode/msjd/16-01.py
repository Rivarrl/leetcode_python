# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-01.py
# @Time    : 2020/10/22 3:28 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.01. 交换数字](https://leetcode-cn.com/problems/swap-numbers-lcci/)
    """
    @timeit
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers

if __name__ == '__main__':
    a = Solution()
    a.swapNumbers([1, 2])