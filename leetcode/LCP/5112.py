# -*- coding: utf-8 -*-
# ======================================
# @File    : 5112.py
# @Time    : 2019/11/30 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5112. 十六进制魔术数字
    """
    @timeit
    def toHexspeak(self, num: str) -> str:
        d = {"A", "B", "C", "D", "E", "F", "1", "0"}
        oz = {"1":"I", "0":"O"}
        s = str(hex(int(num))[2:]).upper()
        for i in range(len(s)):
            if not s[i] in d:
                return "ERROR"
            if s[i] in oz:
                s = s[:i] + oz[s[i]] + s[i+1:]
        return s

if __name__ == '__main__':
    a = Solution()
    a.toHexspeak("257")
    a.toHexspeak("3")
