# -*- coding: utf-8 -*-
# ======================================
# @File    : 1542.py
# @Time    : 2020/9/15 1:39 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1542. 找出最长的超赞子字符串]()
    """
    @timeit
    def longestAwesome(self, s: str) -> int:
        def valid(a):
            return sum([e%2 for e in a]) <= 1
        n = len(s)
        left = r1 = r2 = 0
        a = [0] * 10
        while r2 < n:
            x = ord(s[right]) - ord('0')
            a[x] += 1
            right += 1
            while not valid(a) and right < n:
                x = ord(s[right]) - ord('0')
                y = ord(s[left]) - ord('0')
                a[x] += 1
                a[y] -= 1
                left += 1
                right += 1
        return right - left + 1


if __name__ == '__main__':
    a = Solution()
    a.longestAwesome(s = "3242415")
    a.longestAwesome(s = "12345678")
    a.longestAwesome(s = "213123")
    a.longestAwesome(s = "00")