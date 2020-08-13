# -*- coding: utf-8 -*-
# ======================================
# @File    : 43.py
# @Time    : 2020/8/13 0:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)
    """
    @timeit
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        arr = [0] * (n1+n2)
        for i in range(n1-1, -1, -1):
            x = ord(num1[i]) - ord('0')
            for j in range(n2-1, -1, -1):
                y = ord(num2[j]) - ord('0')
                arr[i+j] += (x * y) % 10
                arr[i+j-1] += (x * y) // 10 + arr[i+j] // 10
                arr[i+j] %= 10
        if arr[-1] > 0:
            arr = [arr[-1]] + arr[:-1]
        else:
            arr = arr[:-1]
        while len(arr) > 1 and arr[0] == 0:
            arr.pop(0)
        return ''.join(chr(e+ord('0')) for e in arr)

if __name__ == '__main__':
    a = Solution()
    a.multiply("2", "3")
    a.multiply("123", "456")
    a.multiply("99", "999")
    a.multiply("0", "9999")
