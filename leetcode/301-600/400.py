# -*- coding: utf-8 -*-
# ======================================
# @File    : 400.py
# @Time    : 2020/5/6 18:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [400. 第N个数字](https://leetcode-cn.com/problems/nth-digit/)
    """
    @timeit
    def findNthDigit(self, n: int) -> int:
        arr = [0]
        i = 0
        while arr[-1] < (1 << 31):
            arr.append(arr[-1] + 9 * (i+1) * 10 ** i)
            i += 1
        j = len(arr) - 1
        while n > 0:
            if n > arr[j]:
                n -= arr[j]
                break
            j -= 1
        x = (10 ** j) + (n - 1) // (j + 1)
        return int(str(x)[(n-1)%(j+1)])


if __name__ == '__main__':
    a = Solution()
    a.findNthDigit(3)
    a.findNthDigit(11)
    a.findNthDigit(10)