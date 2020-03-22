# -*- coding: utf-8 -*-
# ======================================
# @File    : 1094.py
# @Time    : 2020/03/07 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1370. 上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string/)
    """
    @timeit
    def sortString(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        res = ""
        alp = "abcdefghijklmnopqrstuvwxyz"
        while not all(d[e] == 0 for e in d):
            l = 0
            for e in alp:
                if e in d and d[e] > 0 and ord(e) > l:
                    l = ord(e)
                    res += e
                    d[e] -= 1
            l = 200
            for e in alp[::-1]:
                if e in d and d[e] > 0 and ord(e) < l:
                    l = ord(e)
                    res += e
                    d[e] -= 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.sortString("aaaabbbbcccc")
    a.sortString("rat")
    a.sortString("leetcode")
    a.sortString("ggggggg")
    a.sortString("spo")
