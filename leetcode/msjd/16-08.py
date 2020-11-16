# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-08.py
# @Time    : 2020/9/25 12:49 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.08. 整数的英语表示](https://leetcode-cn.com/problems/english-int-lcci/)
    """
    @timeit
    def numberToWords(self, num: int) -> str:
        ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000]
        ss = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
              "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty",
              "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred", "Thousand", "Million", "Billion"]
        k = 90
        def f(num):
            if num == 0:
                return 'Zero'
            i = len(ns) - 1
            while i > 0 and ns[i] > num:
                i -= 1
            n, s = ns[i], ss[i]
            pre = f(num // n) + ' ' if n > k else ''
            suf = ' ' + f(num % n) if num % n else ''
            return pre + s + suf
        return f(num)

if __name__ == '__main__':
    a = Solution()
    a.numberToWords(123)
    a.numberToWords(12345)
    a.numberToWords(1234567)
    a.numberToWords(1234567891)
