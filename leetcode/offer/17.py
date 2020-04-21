# -*- coding: utf-8 -*-
# ======================================
# @File    : 17.py
# @Time    : 2020/4/21 16:41
# @Author  : Rivarrl
# ======================================
# [面试题17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def printNumbers(self, n: int) -> List[int]:
        x = 1
        res = []
        while x < 10 ** n:
            res.append(x)
            x += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.printNumbers(1)
    a.printNumbers(2)