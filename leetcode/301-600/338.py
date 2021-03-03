# -*- coding: utf-8 -*-
# ======================================
# @File    : 338.py
# @Time    : 2021/3/3 20:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [338. 比特位计数](https://leetcode-cn.com/problems/counting-bits/)
    """
    @timeit
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i & (i-1)] + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.countBits(2)
    a.countBits(5)