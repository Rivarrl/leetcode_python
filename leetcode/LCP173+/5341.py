# -*- coding: utf-8 -*-
# ======================================
# @File    : 5341.py
# @Time    : 2020/2/16 10:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class ProductOfNumbers:
    """
    [5341. 最后 K 个数的乘积](https://leetcode-cn.com/problems/product-of-the-last-k-numbers/)
    """
    def __init__(self):
        self.pre = [1]
        self.rec = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.rec = len(self.pre) - 1
            k = 1
        else:
            k = num
        self.pre.append(self.pre[-1] * k)

    @timeit
    def getProduct(self, k: int) -> int:
        n = len(self.pre) - 1
        if k >= n - self.rec: return 0
        return self.pre[-1] // self.pre[n-k]

if __name__ == '__main__':
    a = ProductOfNumbers()
    a.add(3)
    a.add(0)
    a.add(2)
    a.add(5)
    a.add(4)
    a.getProduct(2)
    a.getProduct(3)
    a.getProduct(4)
    a.add(8)
    a.getProduct(2)
