# -*- coding: utf-8 -*-
# ======================================
# @File    : 1758
# @Time    : 2021/2/24 15:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1758. 生成交替二进制字符串的最少操作数](https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string/)
    """
    @timeit
    def minOperations(self, s: str) -> int:
        cnt1 = cnt2 = 0
        x1, x2 = "0", "1"
        for c in s:
            if c != x1:
                cnt1 += 1
            if c != x2:
                cnt2 += 1
            x1, x2 = x2, x1
        return min(cnt1, cnt2)

if __name__ == '__main__':
    a = Solution()
    a.minOperations(s = "0100")
    a.minOperations(s = "10")
    a.minOperations(s = "1111")