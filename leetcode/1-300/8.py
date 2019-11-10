# -*- coding: utf-8 -*-
# ======================================
# @File    : 8.py
# @Time    : 2019/11/10 20:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def myAtoi(self, str: str) -> int:
        """
        [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)
        思路：直接int(str)就行hh。。
        遍历字符串，匹配ASCII码值，考虑到可能会有多段数字子串，只将第一个落入0-9的部分留下，最后判断是否越界
        """
        def is_digit(x):
            return ord('0') <= ord(x) <= ord('9')
        n = len(str)
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        i = 0
        rec = 0
        while i < n and (str[i] == ' ' or str[i] == '0'):
            if str[i] == '0': rec += 1
            i += 1
        if i == n: return 0
        if i > 0 and str[i-1] == '0' and (not is_digit(str[i]) or str[i]==' '): return 0
        if i > 0 and str[i-1] == ' ' and rec > 0: return 0
        if str[i] == '-':
            flag = -1
            i += 1
        elif str[i] == '+':
            flag = 1
            i += 1
        elif is_digit(str[i]):
            flag = 1
        else:
            return 0
        while i < n and str[i] == '0':
            i += 1
        j = i
        while j < n and is_digit(str[j]):
            j += 1
        if j - i == 0: return 0
        if j - i > 10: return INT_MAX if flag == 1 else INT_MIN
        res = 0
        for k in range(i, j):
            digit = j - 1 - k
            c = ord(str[k]) - ord('0')
            res += c * (10 ** digit)
            if res > INT_MAX + 1:
                return INT_MAX if flag == 1 else INT_MIN
        if res >= INT_MAX + 1 and flag == -1:
            return INT_MIN
        if res >= INT_MAX and flag == 1:
            return INT_MAX
        return res * flag


if __name__ == '__main__':
    sol = Solution()
    sol.myAtoi("42")
    sol.myAtoi("    -42")
    sol.myAtoi("4193 with words")
    sol.myAtoi("words and 987")
    sol.myAtoi("-91283472332")
    sol.myAtoi("-0000000000001")
    sol.myAtoi("2147483648")
    sol.myAtoi("0-1")
    sol.myAtoi("0 123")
