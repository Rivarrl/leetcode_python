# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-03.py
# @Time    : 2020/8/17 19:11
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.03. 翻转数位](https://leetcode-cn.com/problems/reverse-bits-lcci/)
    """
    @timeit
    def reverseBits(self, num: int) -> int:
        pre = cur = 0
        res = 1
        for i in range(32):
            if num & (1 << i):
                cur += 1
            else:
                res = max(res, pre + cur)
                pre, cur = cur + 1, 0
        res = max(res, cur+pre)
        return res

if __name__ == '__main__':
    a = Solution()
    a.reverseBits(1775)
    a.reverseBits(7)
    a.reverseBits(2147483646)