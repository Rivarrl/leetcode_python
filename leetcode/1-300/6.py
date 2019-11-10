# -*- coding: utf-8 -*-
# ======================================
# @File    : 6.py
# @Time    : 2019/11/10 17:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def convert(self, s: str, numRows: int) -> str:
        """
        [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)
        思路：一个索引i走到numRows-1或0时改变方向
        """
        if numRows == 1: return s
        res = [list() for _ in range(numRows)]
        i, j = 0, -1
        for c in s:
            res[i].append(c)
            if i == 0 or i == numRows - 1:
                j *= -1
            i += j
        return ''.join(list(map(lambda x:''.join(x), res)))

    @timeit
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        n = len(s)
        for i in range(numRows):
            j = 2 * (numRows - i) - 2
            k = 2 * i
            x = 1
            t = i
            if j == 0 or k == 0 or k == j:
                d = max(j, k)
                while t < n:
                    res += s[t]
                    t += d
            else:
                while t < n:
                    res += s[t]
                    t = t + j if x else t + k
                    x ^= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.convert("LEETCODEISHIRING", 3)
    sol.convert2("LEETCODEISHIRING", 3)