# -*- coding: utf-8 -*-
# ======================================
# @File    : 5623.py
# @Time    : 2020/12/26 22:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5623. 修改后的最大二进制字符串]()
    """
    @timeit
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        x = binary.count('0')
        if x > 1:
            j = binary.find('0')
            k = j + x - 1
            return ''.join(['1' if i != k else '0' for i in range(n)])
        return binary

if __name__ == '__main__':
    a = Solution()
    a.maximumBinaryString(binary = "000110")
    a.maximumBinaryString(binary = "01")
    a.maximumBinaryString("01111001100000110010")