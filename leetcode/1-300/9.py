# -*- coding: utf-8 -*-
# ======================================
# @File    : 9.py
# @Time    : 2019/11/10 21:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isPalindrome(self, x: int) -> bool:
        """
        [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)
        思路：首先负数不是回文数，将正数的每一位按位取到一个数组中，双指针去找符合不符合回文结构
        """
        if x < 0: return False
        if x < 10: return True
        rec = []
        while x > 0:
            rec.append(x % 10)
            x //= 10
        i, j = 0, len(rec) - 1
        while i < j:
            if rec[i] != rec[j]: return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    sol.isPalindrome(121)
    sol.isPalindrome(-121)
    sol.isPalindrome(10)