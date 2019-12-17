# -*- coding: utf-8 -*-
# ======================================
# @File    : 393.py
# @Time    : 2019/12/17 12:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [393. UTF-8 编码验证](https://leetcode-cn.com/problems/utf-8-validation/)
    """
    @timeit
    def validUtf8(self, data: List[int]) -> bool:
        if not data: return False
        case1 = 1 << 7
        case2 = case1 | (case1 >> 1) | (case1 >> 2)
        case3 = case2 | (case1 >> 3)
        case4 = case3 | (case1 >> 4)
        n = len(data)
        i = 0
        f = lambda x: x & case1 and not x & (case1 >> 1)
        while i < n:
            if 0 <= data[i] < case1:
                pass
            elif case1 <= data[i] < case2:
                if i + 1 >= n or not f(data[i+1]): return False
                i += 1
            elif case2 <= data[i] < case3:
                if i + 2 >= n: return False
                for _ in range(2):
                    i += 1
                    if not f(data[i]): return False
            elif case3 <= data[i] < case4:
                if i + 3 >= n: return False
                for _ in range(3):
                    i += 1
                    if not f(data[i]): return False
            else: return False
            i += 1
        return True


if __name__ == '__main__':
    a = Solution()
    a.validUtf8([197, 130, 1])
    a.validUtf8([235, 140, 4])