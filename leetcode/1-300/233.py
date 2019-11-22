# -*- coding: utf-8 -*-
# ======================================
# @File    : 233.py
# @Time    : 2019/11/23 0:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [233. 数字 1 的个数](https://leetcode-cn.com/problems/number-of-digit-one/)
    """
    @timeit
    def countDigitOne(self, n: int) -> int:
        """
        思路：找规律，按位数找
        0-9只有1个1（个位） 1
        10-99有10-19 十位10个 + 11,21,31,...,91 个位9*1=9个 20
        100-999有100-199百位100个，x10-x19再加十位9*10=90个，xx1再加个位90个
        到此找到规律
        如果把个位十位加在一起
        n=999时的答案应是百位100 + 十位(10+90)=100 + 个位(1+9+90)=100 = 300
        所以计算n可以只计算n的位数部分，假设n有x位，那么首先得到(x-1)*10**(x-2)个1
        """
        cnt, i = 0, 1
        while i <= n:
            cnt += n // (i * 10) * i + min(max(n % (i * 10) - i + 1, 0), i)
            i *= 10
        return cnt


if __name__ == '__main__':
    a = Solution()
    # a.countDigitOne(20)
    a.countDigitOne(110)
