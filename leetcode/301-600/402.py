# -*- coding: utf-8 -*-
# ======================================
# @File    : 402.py
# @Time    : 2020/11/15 0:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [402. 移掉K位数字](https://leetcode-cn.com/problems/remove-k-digits/)
    """
    @timeit
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return "0"
        stk = ["0"]
        i = 0
        while i < len(num):
            while stk and stk[-1] > num[i] and k > 0:
                stk.pop()
                k -= 1
            stk.append(num[i])
            i += 1
        while k > 0:
            stk.pop()
            k -= 1
        i = 0
        while i < len(stk) - 1:
            if stk[i] != '0':
                break
            i += 1
        return str(int("".join(stk[i:])))

if __name__ == '__main__':
    a = Solution()
    a.removeKdigits(num = "1432219", k = 3)
    a.removeKdigits(num = "10200", k = 1)
    a.removeKdigits(num = "10", k = 2)