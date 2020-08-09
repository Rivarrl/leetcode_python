# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-01.py
# @Time    : 2020/8/9 1:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.01. 插入](https://leetcode-cn.com/problems/insert-into-bits-lcci/)
    """
    @timeit
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        # 先清扫插入区域：置0，再插入：或
        N &= ~(((1 << j-i+1) - 1) << i)
        return N | (M << i)

if __name__ == '__main__':
    a = Solution()
    a.insertBits(1<<10, (1<<4)|3, 2, 6)
    a.insertBits(0, 31, 0, 4)