# -*- coding: utf-8 -*-
# ======================================
# @File    : 7.py
# @Time    : 2019/11/10 20:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def reverse(self, x: int) -> int:
        """
        [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)
        思路：强转str（误），记录符号位，除余加入队列，队列先进先出，从队列弹出再变反转数
        """
        if x < 0:
            x = -x
            flag = -1
        else:
            flag = 1
        stk = []
        while x > 0:
            stk.append(x % 10)
            x //= 10
        res = 0
        while stk:
            res = res * 10 + stk.pop(0)
        res *= flag
        return res if -2 ** 31 <= res < 2 ** 31 else 0


if __name__ == '__main__':
    sol = Solution()
    sol.reverse(-123)