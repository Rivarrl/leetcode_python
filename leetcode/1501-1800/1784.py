# -*- coding: utf-8 -*-
# ======================================
# @File    : 1784
# @Time    : 2021/3/8 12:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1784. 检查二进制字符串字段](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)
    """
    @timeit
    def checkOnesSegment(self, s: str) -> bool:
        s = s.rstrip("0")
        return len(s) == s.count("1")


if __name__ == '__main__':
    a = Solution()
    a.checkOnesSegment(s = "1001")
    a.checkOnesSegment(s = "110")