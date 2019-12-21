# -*- coding: utf-8 -*-
# ======================================
# @File    : 717.py
# @Time    : 2019/12/21 22:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [717. 1比特与2比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/)
    """
    @timeit
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        # 总是0结尾
        if n == 1: return True
        if bits[-2] == 0: return True
        if n > 2:
            j = n - 2
            while bits[j] == 1: j -= 1
            return (n - 2 - j) % 2 == 0
        return False

if __name__ == '__main__':
    a = Solution()
    a.isOneBitCharacter([1,0,0])
    a.isOneBitCharacter([1,1,1,0])