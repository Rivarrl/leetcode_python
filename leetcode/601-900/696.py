# -*- coding: utf-8 -*-
# ======================================
# @File    : 696.py
# @Time    : 2020/8/10 0:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [696. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings/)
    """
    @timeit
    def countBinarySubstrings(self, s: str) -> int:
        cur, last, res = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                last, cur = cur, 1
            if cur <= last: res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.countBinarySubstrings("00110011")
    a.countBinarySubstrings("10101")