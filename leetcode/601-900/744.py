# -*- coding: utf-8 -*-
# ======================================
# @File    : 744.py
# @Time    : 2019/11/21 0:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [744. 寻找比目标字母大的最小字母](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)
    """
    @timeit
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        思路：有序数组，找目标值的位置，用二分查找
        """
        n = len(letters)
        l, r = 0, n - 1
        tc = ord(target)
        if tc >= ord(letters[-1]): return letters[0]
        while l < r:
            mid = r + l >> 1
            mc = ord(letters[mid])
            if mc <= tc:
                l = mid + 1
            else:
                r = mid
        return letters[r]

if __name__ == '__main__':
    a = Solution()
    a.nextGreatestLetter(["c", "f", "j"], "a")
    a.nextGreatestLetter(["c", "f", "j"], "d")
    a.nextGreatestLetter(["c", "f", "j"], "f")
    a.nextGreatestLetter(["c", "f", "j"], "g")
    a.nextGreatestLetter(["c", "f", "j"], "k")