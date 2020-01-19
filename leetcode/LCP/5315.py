# -*- coding: utf-8 -*-
# ======================================
# @File    : 5315.py
# @Time    : 2020/1/19 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maximum69Number (self, num: int) -> int:
        sn = list(str(num))
        for i in range(len(sn)):
            if sn[i] == '6':
                sn[i] = '9'
                break
        return int(''.join(sn))


if __name__ == '__main__':
    a = Solution()
    a.maximum69Number(9669)
    a.maximum69Number(9996)
    a.maximum69Number(9999)