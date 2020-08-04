# -*- coding: utf-8 -*-
# ======================================
# @File    : 1461.py
# @Time    : 2020/6/1 20:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1461. 检查一个字符串是否包含所有长度为 K 的二进制子串](https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)
    """
    @timeit
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        for i in range(len(s) - k + 1):
            d.add(s[i:i+k])
        return len(d) == 2 ** k

if __name__ == '__main__':
    a = Solution()
    a.hasAllCodes(s = "00110110", k = 2)
    a.hasAllCodes(s = "00110", k = 2)
    a.hasAllCodes(s = "0110", k = 1)
    a.hasAllCodes(s = "0110", k = 2)
    a.hasAllCodes(s = "0000000001011100", k = 4)