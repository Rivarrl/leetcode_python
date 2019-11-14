# -*- coding: utf-8 -*-
# ======================================
# @File    : 868.py
# @Time    : 2019/11/15 0:38
# @Author  : Rivarrl
# ======================================

class Solution:
    """
    [868. 二进制间距](https://leetcode-cn.com/problems/binary-gap/)
    """
    def binaryGap(self, N: int) -> int:
        """
        思路：用右移
        """
        while N & 1 == 0:
            N >>= 1
        N >>= 1
        res, ctr = 0, 1
        while N:
            if N & 1:
                res = max(res, ctr)
                ctr = 1
            else:
                ctr += 1
            N >>= 1
        return res

if __name__ == '__main__':
    a = Solution()
    s = a.binaryGap(22)
    print(s)
    s = a.binaryGap(5)
    print(s)
    s = a.binaryGap(6)
    print(s)
    s = a.binaryGap(8)
    print(s)
