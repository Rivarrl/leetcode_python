# -*- coding: utf-8 -*-
# ======================================
# @File    : 344
# @Time    : 2020/1/10 14:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string/)
    """
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            j = n-1-i
            s[i], s[j] = s[j], s[i]


if __name__ == '__main__':
    a = Solution()
    a.reverseString(["h","e","l","l","o"])
    a.reverseString(["H","a","n","n","a","h"])